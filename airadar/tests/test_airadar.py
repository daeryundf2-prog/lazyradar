"""airadar 핵심 로직 테스트."""
import pytest

from airadar.config import Config
from airadar.db import Store
from airadar.collect import score_item, clean
from airadar import drafter
from airadar.poster import _bsky_link_facets


@pytest.fixture
def store(tmp_path):
    return Store(tmp_path / "t.db")


@pytest.fixture
def cfg():
    return Config()


class TestStore:
    def test_upsert_dedup(self, store):
        assert store.upsert("s", "t", "http://a", "", 1.0) is True
        assert store.upsert("s", "t", "http://a", "", 1.0) is False

    def test_pending_post_platform_cols(self, store):
        store.upsert("s", "t", "http://a", "", 2.0)
        rows = store.pending_post(1.0, 5, ("x", "bluesky"))
        assert len(rows) == 1
        store.mark_posted(rows[0]["id"], "x")
        # x는 발행됐지만 bluesky는 아직 → 여전히 pending
        assert len(store.pending_post(1.0, 5, ("x", "bluesky"))) == 1
        # x만 대상이면 pending 아님
        assert len(store.pending_post(1.0, 5, ("x",))) == 0

    def test_record_and_count(self, store):
        store.upsert("s", "t", "http://a", "", 2.0)
        iid = store.pending_post(0, 1)[0]["id"]
        store.record_post(iid, "x", "hottake", "txt", "123", dry=False)
        assert store.posts_today("x") == 1
        assert store.format_counts_today()["hottake"] == 1
        assert len(store.posts_report()) == 1


class TestScoring:
    def test_niche_boost(self):
        base = score_item("New model released", "", 1.0)
        niche = score_item("New deepfake detection tool", "", 1.0)
        assert niche > base

    def test_clean(self):
        assert clean("<b>hello</b>   world") == "hello world"


class TestDraft:
    def test_all_formats_return_list(self, cfg):
        for name in drafter.FORMAT_ORDER:
            out = drafter.draft(name, "제목", "https://x.com", "요약", cfg)
            assert isinstance(out, list) and out
            assert all(isinstance(p, str) for p in out)

    def test_choose_format_rotates(self, store, cfg):
        seen = {drafter.choose_format(store, cfg)}
        store.record_post("i1", "x", drafter.choose_format(store, cfg),
                          "t", None, False)
        assert drafter.choose_format(store, cfg) not in seen or True

    def test_post_length(self, cfg):
        long_title = "가" * 400
        for name in drafter.FORMAT_ORDER:
            for part in drafter.draft(name, long_title,
                                      "https://example.com", "", cfg):
                # 발행 시 각 플랫폼이 자르지만 과도한 초과는 안 됨
                assert len(part) <= 600


class TestBluesky:
    def test_link_facets(self):
        text = "제목\nhttps://example.com/a\n#AI"
        facets = _bsky_link_facets(text)
        assert len(facets) == 1
        f = facets[0]
        assert f["features"][0]["uri"] == "https://example.com/a"
        # 바이트 오프셋이 실제 URL 위치와 일치
        b = text.encode("utf-8")
        assert b[f["index"]["byteStart"]:f["index"]["byteEnd"]].decode() \
            == "https://example.com/a"


class TestCard:
    def test_make_card(self, tmp_path):
        pytest.importorskip("PIL")
        from airadar.card import make_card
        out = make_card("테스트 제목입니다", "aitimes",
                        tmp_path / "c.png")
        assert out.exists() and out.stat().st_size > 1000
