"""회귀 테스트 — null rank 정렬 크래시 방지, search.py의 unavailable/archived 제외."""

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import generate_global_readme as gen  # noqa: E402
import search  # noqa: E402


def _write_data(tmp_path, items):
    data = tmp_path / "global_creations.json"
    data.write_text(json.dumps({"items": items}, ensure_ascii=False), encoding="utf-8")
    return data


# ── 국가 정렬 키 (generate_global_readme.py) ─────────────────────────

def test_country_sort_key_falls_back_past_null():
    # rank_country=None(unavailable/archived 등)이면 rank_global로, 둘 다 null이면 999
    assert gen.country_sort_key({"rank_country": None, "rank_global": 7}) == 7
    assert gen.country_sort_key({"rank_country": None, "rank_global": None}) == 999
    assert gen.country_sort_key({"rank_country": 2, "rank_global": 9}) == 2
    assert gen.country_sort_key({}) == 999


def test_country_sort_key_sorts_without_crash():
    items = [
        {"name": "both_null", "rank_country": None, "rank_global": None},
        {"name": "normal", "rank_country": 1, "rank_global": 3},
        {"name": "null_country", "rank_country": None, "rank_global": 5},
    ]
    ordered = [it["name"] for it in sorted(items, key=gen.country_sort_key)]
    assert ordered[0] == "normal" and ordered[1] == "null_country"
    assert ordered[-1] == "both_null"


def test_generator_survives_null_rank_items(tmp_path, monkeypatch):
    # 순위 필드가 명시적 null이어도 README 생성이 크래시 없이 끝나야 한다.
    data = _write_data(tmp_path, [{
        "name": "nullrank", "github": "https://github.com/o/nullrank",
        "country": "미국 (United States)", "country_code": "US",
        "author": "o", "model_affinity": "M",
        "stars": 1, "forks": 1, "score": 1.0, "status": "⚡ Active",
        "summary": "s", "use_case": "u",
        "rank_country": None, "rank_global": None,
    }])
    readme = tmp_path / "README.md"
    monkeypatch.setattr(gen, "DATA_PATH", str(data))
    monkeypatch.setattr(gen, "CANDIDATES_PATH", str(tmp_path / "none.json"))
    monkeypatch.setattr(gen, "README_PATH", str(readme))
    gen.main()
    md = readme.read_text(encoding="utf-8")
    assert "**nullrank**" in md and "**-**" in md


# ── search.py Top N / 검색 필터 ─────────────────────────────────────

def _search_items():
    return [
        {"name": "alive", "rank_global": 1, "rank_country": 1, "status": "⚡ Active",
         "country": "미국", "country_code": "US", "stars": 100, "forks": 10,
         "score": 1.0, "summary": "s", "use_case": "u",
         "github": "https://github.com/o/alive"},
        {"name": "gone404", "rank_global": None, "rank_country": None,
         "status": "unavailable", "country": "미국", "country_code": "US",
         "stars": 1, "forks": 0, "score": 0.0, "summary": "s", "use_case": "u",
         "github": "https://github.com/o/gone404"},
        {"name": "frozen", "rank_global": None, "rank_country": None,
         "archived": True, "status": "💤 Stable", "country": "미국",
         "country_code": "US", "stars": 1, "forks": 0, "score": 0.0,
         "summary": "s", "use_case": "u",
         "github": "https://github.com/o/frozen"},
        {"name": "unranked", "rank_global": None, "rank_country": None,
         "status": "⚡ Active", "country": "미국", "country_code": "US",
         "stars": 2, "forks": 0, "score": 0.5, "summary": "s", "use_case": "u",
         "github": "https://github.com/o/unranked"},
    ]


def test_top_n_skips_unavailable_and_archived(tmp_path, monkeypatch, capsys):
    data = _write_data(tmp_path, _search_items())
    monkeypatch.setattr(search, "DATA_PATH", str(data))
    monkeypatch.setattr(sys, "argv", ["search.py", "--top", "5"])
    search.main()
    out = capsys.readouterr().out
    assert "alive" in out and "unranked" in out
    assert "gone404" not in out and "frozen" not in out
    assert "#-" in out  # null rank는 #-로 표시 — 크래시 없음


def test_query_skips_unavailable_and_archived(tmp_path, monkeypatch, capsys):
    data = _write_data(tmp_path, _search_items())
    monkeypatch.setattr(search, "DATA_PATH", str(data))
    monkeypatch.setattr(sys, "argv", ["search.py", "--query", "s"])
    search.main()
    out = capsys.readouterr().out
    assert "alive" in out
    assert "gone404" not in out and "frozen" not in out


def test_fmt_rank_handles_null():
    assert search.fmt_rank(3) == "#03"
    assert search.fmt_rank(None) == "#-"
    assert search.fmt_rank("-") == "#-"
