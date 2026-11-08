"""선택적 LLM 한줄 해설 — API 키가 있을 때만 활성화.

지원: Anthropic (ANTHROPIC_API_KEY), OpenAI 호환 (OPENAI_API_KEY,
OPENAI_BASE_URL로 로컬/대체 엔드포인트도 가능).
"""
from __future__ import annotations

import os

import requests

PROMPT = (
    "다음 AI 뉴스 기사에 대해 한국어로 한 줄 해설을 써줘. "
    "딥페이크·AI 생성물 탐지·포렌식 관점을 우선시하고, "
    "관련 없으면 일반 AI 업계 관점으로. 40자 이내, '~음/~임' 종결, "
    "이모지·해시태그 금지.\n\n"
    "제목: {title}\n요약: {summary}"
)


def commentary(title: str, summary: str) -> str | None:
    """한줄 해설 생성. 실패/키 없으면 None."""
    prompt = PROMPT.format(title=title, summary=(summary or "")[:400])
    try:
        if os.environ.get("ANTHROPIC_API_KEY"):
            r = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": os.environ["ANTHROPIC_API_KEY"],
                    "anthropic-version": "2023-06-01",
                },
                json={"model": "claude-haiku-4-5-20251001",
                      "max_tokens": 120,
                      "messages": [{"role": "user", "content": prompt}]},
                timeout=30)
            r.raise_for_status()
            return r.json()["content"][0]["text"].strip()
        if os.environ.get("OPENAI_API_KEY"):
            base = os.environ.get("OPENAI_BASE_URL",
                                  "https://api.openai.com/v1")
            r = requests.post(
                f"{base}/chat/completions",
                headers={"Authorization":
                         f"Bearer {os.environ['OPENAI_API_KEY']}"},
                json={"model": os.environ.get("OPENAI_MODEL",
                                              "gpt-4o-mini"),
                      "max_tokens": 120,
                      "messages": [{"role": "user", "content": prompt}]},
                timeout=30)
            r.raise_for_status()
            return r.json()["choices"][0]["message"]["content"].strip()
    except Exception:
        return None
    return None
