"""발행된 글의 반응 수집 — Bluesky는 무료 API로 가능, X는 읽기 제한으로 수동."""
from __future__ import annotations

import sys

import requests

from .config import Config
from .db import Store


def collect_metrics(store: Store, cfg: Config) -> list[dict]:
    """Bluesky 발행분의 좋아요/리포스트/답글 수를 가져옴."""
    rows = store.conn.execute(
        "SELECT remote_id, format FROM posts"
        " WHERE platform='bluesky' AND remote_id IS NOT NULL AND dry=0"
    ).fetchall()
    if not rows:
        return []
    uris = [r["remote_id"] for r in rows]
    out = []
    for i in range(0, len(uris), 25):  # getPosts는 25개씩
        batch = uris[i:i + 25]
        try:
            r = requests.get(
                "https://public.api.bsky.app/xrpc/app.bsky.feed.getPosts",
                params=[("uris", u) for u in batch], timeout=20)
            r.raise_for_status()
            for p in r.json().get("posts", []):
                fmt = next((x["format"] for x in rows
                            if x["remote_id"] == p["uri"]), "?")
                out.append({
                    "format": fmt,
                    "uri": p["uri"],
                    "likes": p.get("likeCount", 0),
                    "reposts": p.get("repostCount", 0),
                    "replies": p.get("replyCount", 0),
                })
        except Exception as exc:
            print(f"[warn] metrics 조회 실패: {exc}", file=sys.stderr)
    return out


def print_metrics(store: Store, cfg: Config) -> None:
    rows = collect_metrics(store, cfg)
    if not rows:
        print("수집된 반응 지표 없음 (Bluesky 발행분만 수집 가능)")
        return
    print(f"{'format':10} {'likes':>6} {'reposts':>7} {'replies':>7}  uri")
    for r in rows:
        print(f"{r['format']:10} {r['likes']:>6} {r['reposts']:>7}"
              f" {r['replies']:>7}  {r['uri'][:60]}")
    # 포맷별 평균
    agg: dict[str, list[int]] = {}
    for r in rows:
        agg.setdefault(r["format"], []).append(r["likes"])
    print("\n포맷별 평균 좋아요:")
    for fmt, likes in sorted(agg.items(),
                             key=lambda kv: -sum(kv[1]) / len(kv[1])):
        print(f"  {fmt:10} {sum(likes) / len(likes):.1f} ({len(likes)}건)")
