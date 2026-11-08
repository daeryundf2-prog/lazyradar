"""X + Threads 자동 포스팅 — 포맷 실험 지원."""
from __future__ import annotations

import sys
import time
from pathlib import Path

import requests

from .config import Config
from .db import Store, POST_COL
from . import drafter

THREADS_API = "https://graph.threads.net/v1.0"


def _post_x(parts: list[str], cfg: Config,
            card: Path | None = None) -> str | None:
    """parts가 여러 개면 스레드로 발행. 첫 트윗 id 반환."""
    keys = cfg.x_keys
    if not all(keys.values()):
        print("[warn] X API 키 미설정 — 건너뜀", file=sys.stderr)
        return None
    try:
        import tweepy
    except ImportError:
        print("[warn] tweepy 미설치 — pip install tweepy", file=sys.stderr)
        return None
    client = tweepy.Client(
        consumer_key=keys["api_key"], consumer_secret=keys["api_secret"],
        access_token=keys["access_token"],
        access_token_secret=keys["access_secret"],
    )
    media_ids = None
    if card and card.exists():
        auth = tweepy.OAuth1UserHandler(
            keys["api_key"], keys["api_secret"],
            keys["access_token"], keys["access_secret"])
        media = tweepy.API(auth).media_upload(str(card))
        media_ids = [media.media_id]
    first_id = reply_to = None
    for part in parts:
        r = client.create_tweet(
            text=part[:280], in_reply_to_tweet_id=reply_to,
            media_ids=media_ids if reply_to is None else None)
        reply_to = r.data["id"]
        first_id = first_id or reply_to
        time.sleep(1)
    return str(first_id) if first_id else None


def _post_threads(parts: list[str], cfg: Config,
                  card: Path | None = None) -> str | None:
    # 참고: Threads API는 로컬 이미지를 못 올림(공개 URL만 가능) — card 무시
    if not cfg.threads_token:
        print("[warn] Threads 토큰 미설정 — 건너뜀", file=sys.stderr)
        return None
    uid = cfg.threads_user_id
    reply_to = first_id = None
    for part in parts:
        data = {"media_type": "TEXT", "text": part[:490],
                "access_token": cfg.threads_token}
        if reply_to:
            data["reply_to_id"] = reply_to
        r = requests.post(f"{THREADS_API}/{uid}/threads",
                          data=data, timeout=20)
        r.raise_for_status()
        container = r.json()["id"]
        time.sleep(2)
        r = requests.post(
            f"{THREADS_API}/{uid}/threads_publish",
            data={"creation_id": container,
                  "access_token": cfg.threads_token},
            timeout=20)
        r.raise_for_status()
        media_id = r.json()["id"]
        reply_to = media_id
        first_id = first_id or media_id
        time.sleep(1)
    return str(first_id) if first_id else None


def _post_bluesky(parts: list[str], cfg: Config,
                  card: Path | None = None) -> str | None:
    """Bluesky AT Protocol — 앱 비밀번호로 세션 생성 후 발행."""
    if not cfg.bsky_handle or not cfg.bsky_password:
        print("[warn] Bluesky 계정 미설정 — 건너뜀", file=sys.stderr)
        return None
    s = requests.post(
        "https://bsky.social/xrpc/com.atproto.server.createSession",
        json={"identifier": cfg.bsky_handle,
              "password": cfg.bsky_password}, timeout=20)
    s.raise_for_status()
    sess = s.json()
    headers = {"Authorization": f"Bearer {sess['accessJwt']}"}

    blob = None
    if card and card.exists():
        up = requests.post(
            "https://bsky.social/xrpc/com.atproto.repo.uploadBlob",
            headers={**headers, "Content-Type": "image/png"},
            data=card.read_bytes(), timeout=30)
        up.raise_for_status()
        blob = up.json()["blob"]

    def _post_one(text: str, reply=None, embed=None) -> dict:
        record = {"$type": "app.bsky.feed.post", "text": text[:300],
                  "createdAt": time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                             time.gmtime()),
                  "facets": _bsky_link_facets(text[:300])}
        if reply:
            record["reply"] = reply
        if embed:
            record["embed"] = embed
        r = requests.post(
            "https://bsky.social/xrpc/com.atproto.repo.createRecord",
            headers=headers,
            json={"repo": sess["did"],
                  "collection": "app.bsky.feed.post",
                  "record": record}, timeout=20)
        r.raise_for_status()
        return r.json()

    first = None
    parent = None
    for i, part in enumerate(parts):
        reply = {"root": first, "parent": parent} if parent else None
        embed = ({"$type": "app.bsky.embed.images",
                  "images": [{"image": blob, "alt": part[:200]}]}
                 if blob and i == 0 else None)
        res = _post_one(part, reply, embed)
        node = {"uri": res["uri"], "cid": res["cid"]}
        first = first or node
        parent = node
        time.sleep(1)
    return first["uri"] if first else None


def _bsky_link_facets(text: str) -> list[dict]:
    """텍스트 안 URL을 클릭 가능한 링크 facet으로."""
    import re
    facets = []
    for m in re.finditer(r"https?://\S+", text):
        facets.append({
            "index": {"byteStart": len(text[:m.start()].encode("utf-8")),
                      "byteEnd": len(text[:m.end()].encode("utf-8"))},
            "features": [{"$type": "app.bsky.richtext.facet#link",
                          "uri": m.group(0)}],
        })
    return facets


def _post_mastodon(parts: list[str], cfg: Config,
                   card: Path | None = None) -> str | None:
    """Mastodon — /api/v1/statuses, 스레드는 in_reply_to로."""
    if not cfg.masto_token:
        print("[warn] Mastodon 토큰 미설정 — 건너뜀", file=sys.stderr)
        return None
    base = cfg.masto_instance.rstrip("/")
    headers = {"Authorization": f"Bearer {cfg.masto_token}"}
    media_ids = None
    if card and card.exists():
        m = requests.post(f"{base}/api/v2/media", headers=headers,
                          files={"file": card.open("rb")}, timeout=30)
        m.raise_for_status()
        media_ids = [m.json()["id"]]
    first_id = reply_to = None
    for i, part in enumerate(parts):
        data = {"status": part[:500]}
        if reply_to:
            data["in_reply_to_id"] = reply_to
        if media_ids and i == 0:
            data["media_ids[]"] = media_ids[0]
        r = requests.post(f"{base}/api/v1/statuses",
                          headers=headers, data=data, timeout=20)
        r.raise_for_status()
        reply_to = r.json()["id"]
        first_id = first_id or reply_to
        time.sleep(1)
    return str(first_id) if first_id else None


def autopost(store: Store, cfg: Config) -> int:
    """점수 상위 항목을 포맷 로테이션으로 발행. 건수 반환."""
    platforms = [
        ("x", cfg.post_to_x, _post_x),
        ("threads", cfg.post_to_threads, _post_threads),
        ("bluesky", cfg.post_to_bluesky, _post_bluesky),
        ("mastodon", cfg.post_to_mastodon, _post_mastodon),
    ]
    active = [p for p in platforms if p[1]]
    if not active:
        print("[info] 발행 플랫폼이 모두 비활성화 (config.yaml의 post_to_*)")
        return 0
    # X 무료 한도 보호
    if cfg.post_to_x and store.posts_today("x") >= cfg.x_daily_cap:
        print(f"[info] X 일일 한도({cfg.x_daily_cap}) 도달 — X 건너뜀")
        active = [p for p in active if p[0] != "x"]
        if not active:
            return 0
    rows = store.pending_post(
        cfg.min_score_to_post, cfg.max_posts_per_run,
        tuple(p[0] for p in active))
    if not rows:
        print("[info] 발행할 항목 없음")
        return 0
    posted = 0
    for r in rows:
        fmt = drafter.choose_format(store, cfg)
        parts = drafter.draft(fmt, r["title"], r["link"],
                              r["summary"] or "", cfg)
        card = None
        if cfg.card_images:
            try:
                from .card import make_card
                card = make_card(r["title"], r["source"])
            except Exception as exc:
                print(f"[warn] 카드 생성 실패: {exc}", file=sys.stderr)
        attempted = False
        for platform, _, fn in active:
            if r[POST_COL[platform]] is not None:
                continue
            text = "\n\n".join(parts)
            try:
                if cfg.dry_run:
                    print(f"[dry-run:{platform}:{fmt}] {text}\n---")
                else:
                    remote = fn(parts, cfg, card)
                    print(f"[ok:{platform}:{fmt}] {r['title'][:60]}")
                    store.mark_posted(r["id"], platform)
                    store.record_post(r["id"], platform, fmt, text,
                                      remote, dry=False)
                attempted = True
            except Exception as exc:
                print(f"[err:{platform}] {r['id']}: {exc}", file=sys.stderr)
        posted += 1 if attempted else 0
        if not cfg.dry_run:
            time.sleep(3)  # 레이트리밋 여유
    return posted
