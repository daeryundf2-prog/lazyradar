"""포스트 포맷 팩토리 — 같은 기사를 여러 스타일로 작성.

각 포맷 함수는 (title, link, summary, cfg) -> list[str] 를 반환.
원소가 여러 개면 스레드(X)로, Threads/단일 플랫폼에선 개행으로 합침.
"""
from __future__ import annotations

import itertools

from .config import Config


def _tags(cfg: Config) -> str:
    return " ".join(f"#{t.lstrip('#')}" for t in cfg.hashtags)


def fmt_headline(title, link, summary, cfg):
    """A. 헤드라인 봇 — 제목+링크만."""
    return [f"{title}\n{link}\n{_tags(cfg)}"]


def fmt_tldr(title, link, summary, cfg):
    """B. 한줄 요약 — 요약 앞부분 첨부."""
    s = summary.split(". ")[0][:120] if summary else ""
    body = f"{title}\n\n{s}" if s else title
    return [f"오늘의 AI 소식 📡\n{body}\n\n{link}\n{_tags(cfg)}"]


_OPINIONS = itertools.cycle([
    "이거 꽤 큰데요.",
    "체크해둘 만합니다.",
    "흥미로운 흐름입니다.",
    "딥페이크·합성미디어 쪽도 영향 있을 듯.",
    "이건 지켜봐야겠네요.",
])


def fmt_hottake(title, link, summary, cfg):
    """C. 한줄평형 — LLM 키 있으면 생성, 없으면 템플릿."""
    take = None
    if getattr(cfg, "use_llm", False):
        from .llm import commentary
        take = commentary(title, summary)
    take = take or next(_OPINIONS)
    return [f"{take}\n\n{title}\n{link}\n{_tags(cfg)}"]


def fmt_question(title, link, summary, cfg):
    """D. 질문형 — 참여 유도."""
    return [f"{title}\n\n이거 실제로 의미 있는 변화일까요?\n{link}\n{_tags(cfg)}"]


def fmt_bookmark(title, link, summary, cfg):
    """E. 북마크형 — 저장 유도."""
    return [f"📌 저장해두세요\n\n{title}\n{link}\n{_tags(cfg)}"]


def fmt_thread(title, link, summary, cfg):
    """F. 스레드형 — 훅/내용/링크 3파트 (X 스레드용)."""
    s = summary[:220] if summary else title
    return [
        f"AI 소식 하나 정리합니다 🧵\n\n{title}",
        f"{s}",
        f"원문: {link}\n{_tags(cfg)}",
    ]


FORMATS = {
    "headline": fmt_headline,
    "tldr": fmt_tldr,
    "hottake": fmt_hottake,
    "question": fmt_question,
    "bookmark": fmt_bookmark,
    "thread": fmt_thread,
}

FORMAT_ORDER = list(FORMATS)


def choose_format(store: Store, cfg: Config) -> str:
    """오늘 가장 적게 쓴 포맷을 골라 고르게 실험."""
    counts = store.format_counts_today()
    return min(FORMAT_ORDER, key=lambda f: counts.get(f, 0))


def draft(fmt: str, title: str, link: str, summary: str,
          cfg: Config) -> list[str]:
    return FORMATS[fmt](title, link, summary, cfg)


from .db import Store  # noqa: E402  (순환 import 회피용 하단 배치)
