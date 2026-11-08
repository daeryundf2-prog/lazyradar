"""airadar 설정 로더 — config.yaml + 환경변수."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from dotenv import load_dotenv

DEFAULT_FEEDS = [
    # 이름, URL, 가중치 (니치 관련도)
    ("openai", "https://openai.com/news/rss.xml", 1.0),
    ("google-ai", "https://blog.google/technology/ai/rss/", 1.0),
    ("huggingface", "https://huggingface.co/blog/feed.xml", 1.0),
    ("verge-ai", "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml", 0.8),
    ("techcrunch-ai", "https://techcrunch.com/category/artificial-intelligence/feed/", 0.8),
    ("venturebeat-ai", "https://venturebeat.com/category/ai/feed/", 0.8),
    ("mit-tr-ai", "https://www.technologyreview.com/topic/artificial-intelligence/feed", 0.8),
    # arXiv는 평일에만 새 목록이 나옴 (주말엔 빈 피드가 정상)
    ("arxiv-cl", "https://rss.arxiv.org/rss/cs.CL", 0.6),
    ("arxiv-cv", "https://rss.arxiv.org/rss/cs.CV", 0.6),
    # 한국어 소스
    ("aitimes", "https://www.aitimes.com/rss/allArticle.xml", 1.0),
    ("tech42", "https://tech42.co.kr/feed/", 0.8),
    ("itdonga", "https://it.donga.com/feeds/rss/", 0.6),
    ("etnews", "https://rss.etnews.com/Section901.xml", 0.7),
]

HACKERNEWS_URL = (
    "https://hn.algolia.com/api/v1/search"
    "?query=AI&tags=story&numericFilters=points%3E150"
)

# 딥페이크/포렌식 니치 부스터 키워드
NICHE_KEYWORDS = [
    "deepfake", "deep fake", "synthetic media", "c2pa", "watermark",
    "provenance", "detection", "딥페이크", "합성", "생성형", "forensic",
    "ai-generated", "face swap", "voice clone",
]


@dataclass
class Config:
    feeds: list[tuple[str, str, float]] = field(default_factory=lambda: list(DEFAULT_FEEDS))
    hackernews: bool = True
    # 발행
    post_to_x: bool = False
    post_to_threads: bool = False
    post_to_bluesky: bool = False
    max_posts_per_run: int = 5
    x_daily_cap: int = 15  # X 무료 한도 ~17/일, 여유 두고 15
    post_to_mastodon: bool = False
    masto_instance: str = "https://mastodon.social"
    card_images: bool = True   # 포스트에 카드 이미지 첨부
    use_llm: bool = False      # API 키 있으면 hottake를 LLM 생성으로
    weekly_report_day: int = 6  # 0=월 … 6=일, run 시 해당 요일이면 주간 리포트 발송
    min_score_to_post: float = 1.0
    dry_run: bool = True
    hashtags: list[str] = field(default_factory=lambda: ["AI", "인공지능"])
    # 이메일
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 465
    smtp_user: str = ""
    email_to: str = ""
    email_subject_prefix: str = "[AI Radar]"
    max_items_in_digest: int = 30
    # 경로
    db_path: str = "airadar.db"

    @staticmethod
    def load(path: str | Path = "config.yaml") -> "Config":
        # .env를 환경변수로 로드 — 이미 설정된 실제 환경변수는 덮어쓰지 않음
        load_dotenv()
        cfg = Config()
        p = Path(path)
        if p.exists():
            data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
            for k, v in data.items():
                if k == "feeds":
                    cfg.feeds = [
                        (f["name"], f["url"], float(f.get("weight", 1.0)))
                        for f in v
                    ]
                elif hasattr(cfg, k):
                    try:
                        setattr(cfg, k, v)
                    except AttributeError:
                        # 읽기 전용 프로퍼티(예: smtp_password)는 무시
                        pass
        cfg.smtp_user = os.environ.get("AIRADAR_SMTP_USER", cfg.smtp_user)
        cfg.email_to = os.environ.get("AIRADAR_EMAIL_TO", cfg.email_to)
        if os.environ.get("AIRADAR_DRY_RUN") is not None:
            cfg.dry_run = os.environ["AIRADAR_DRY_RUN"].lower() in ("1", "true", "yes")
        return cfg

    @property
    def smtp_password(self) -> str:
        return os.environ.get("AIRADAR_SMTP_PASSWORD", "")

    @property
    def x_keys(self) -> dict:
        return {
            "api_key": os.environ.get("X_API_KEY", ""),
            "api_secret": os.environ.get("X_API_SECRET", ""),
            "access_token": os.environ.get("X_ACCESS_TOKEN", ""),
            "access_secret": os.environ.get("X_ACCESS_SECRET", ""),
        }

    @property
    def threads_token(self) -> str:
        return os.environ.get("THREADS_ACCESS_TOKEN", "")

    @property
    def threads_user_id(self) -> str:
        return os.environ.get("THREADS_USER_ID", "me")

    @property
    def bsky_handle(self) -> str:
        return os.environ.get("BSKY_HANDLE", "")

    @property
    def bsky_password(self) -> str:
        return os.environ.get("BSKY_APP_PASSWORD", "")

    @property
    def masto_token(self) -> str:
        return os.environ.get("MASTO_ACCESS_TOKEN", "")
