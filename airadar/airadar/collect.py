"""RSS + HackerNews 수집기."""
from __future__ import annotations

import re
import sys
import time

import feedparser
import requests

from .config import Config, HACKERNEWS_URL, NICHE_KEYWORDS
from .db import Store

_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")


def clean(text: str, limit: int = 300) -> str:
    text = _TAG_RE.sub(" ", text or "")
    text = _WS_RE.sub(" ", text).strip()
    return text[:limit]


def score_item(title: str, summary: str, feed_weight: float) -> float:
    """피드 가중치 + 니치 키워드 부스터."""
    text = f"{title} {summary}".lower()
    boost = sum(0.5 for kw in NICHE_KEYWORDS if kw in text)
    return feed_weight + boost


def collect(store: Store, cfg: Config) -> int:
    """피드를 긁어 새 항목을 저장. 새로 들어온 건수 반환."""
    new_count = 0

    for name, url, weight in cfg.feeds:
        try:
            feed = feedparser.parse(url)
            for e in feed.entries[:40]:
                title = clean(getattr(e, "title", ""), 200)
                link = getattr(e, "link", "")
                summary = clean(getattr(e, "summary", ""))
                if not title or not link:
                    continue
                if store.upsert(name, title, link, summary,
                                score_item(title, summary, weight)):
                    new_count += 1
        except Exception as exc:  # 피드 하나 죽어도 계속
            print(f"[warn] feed {name} failed: {exc}", file=sys.stderr)
        time.sleep(0.3)

    if cfg.hackernews:
        try:
            r = requests.get(HACKERNEWS_URL, timeout=15)
            r.raise_for_status()
            for hit in r.json().get("hits", [])[:30]:
                title = clean(hit.get("title") or "", 200)
                link = hit.get("url") or (
                    f"https://news.ycombinator.com/item?id={hit['objectID']}")
                pts = hit.get("points") or 0
                score = 0.7 + min(pts, 500) / 1000.0
                score += sum(0.5 for kw in NICHE_KEYWORDS
                             if kw in title.lower())
                if title and store.upsert("hackernews", title, link,
                                          f"HN points: {pts}", score):
                    new_count += 1
        except Exception as exc:
            print(f"[warn] hackernews failed: {exc}", file=sys.stderr)

    return new_count
