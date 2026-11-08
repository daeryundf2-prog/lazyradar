"""이메일 다이제스트 발송."""
from __future__ import annotations

import smtplib
import sys
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

from .config import Config
from .db import Store


def build_digest_html(rows) -> str:
    items = []
    for r in rows:
        niche = " ⭐" if r["score"] >= 1.5 else ""
        items.append(
            f'<li style="margin-bottom:14px">'
            f'<a href="{r["link"]}"><b>{r["title"]}</b></a>{niche}'
            f'<br><span style="color:#666;font-size:0.9em">'
            f'{r["source"]} · score {r["score"]:.1f}</span>'
            f'<br><span style="font-size:0.9em">{r["summary"][:200]}</span>'
            f"</li>"
        )
    return (
        "<html><body style='font-family:sans-serif'>"
        f"<h2>AI Radar — {datetime.now():%Y-%m-%d %H:%M}</h2>"
        f"<p>새 항목 {len(rows)}건 (⭐ = 딥페이크/포렌식 니치 관련)</p>"
        f"<ol>{''.join(items)}</ol>"
        "</body></html>"
    )


def send_digest(store: Store, cfg: Config) -> int:
    rows = store.pending_email(cfg.max_items_in_digest)
    if not rows:
        print("[info] 이메일로 보낼 새 항목 없음")
        return 0
    if not cfg.smtp_user or not cfg.email_to:
        print("[warn] SMTP 미설정 — 본문을 stdout에 출력합니다")
        for r in rows:
            print(f"  - [{r['source']}] {r['title']}\n    {r['link']}")
        store.mark_emailed([r["id"] for r in rows])
        return len(rows)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"{cfg.email_subject_prefix} {len(rows)}건 — {datetime.now():%m/%d}"
    msg["From"] = formataddr(("AI Radar", cfg.smtp_user))
    msg["To"] = cfg.email_to
    msg.attach(MIMEText(build_digest_html(rows), "html", "utf-8"))

    if cfg.dry_run:
        print(f"[dry-run] 이메일 발송 생략 → {cfg.email_to} ({len(rows)}건)")
    else:
        with smtplib.SMTP_SSL(cfg.smtp_host, cfg.smtp_port) as s:
            s.login(cfg.smtp_user, cfg.smtp_password)
            s.send_message(msg)
        print(f"[ok] 이메일 발송 완료 → {cfg.email_to} ({len(rows)}건)", file=sys.stderr)
    store.mark_emailed([r["id"] for r in rows])
    return len(rows)


def send_weekly(store: Store, cfg: Config) -> bool:
    """주간 성과 리포트 — 포맷/플랫폼별 발행 집계 이메일."""
    rows = store.posts_report(days=7)
    stats = store.stats()
    by_fmt: dict[str, int] = {}
    by_plat: dict[str, int] = {}
    for r in rows:
        by_fmt[r["format"]] = by_fmt.get(r["format"], 0) + 1
        by_plat[r["platform"]] = by_plat.get(r["platform"], 0) + 1
    html = (
        "<html><body style='font-family:sans-serif'>"
        f"<h2>AI Radar 주간 리포트 — {datetime.now():%Y-%m-%d}</h2>"
        f"<h3>누적</h3><pre>{stats}</pre>"
        "<h3>이번 주 포맷별 발행</h3>"
        f"<pre>{by_fmt or '발행 없음'}</pre>"
        "<h3>이번 주 플랫폼별 발행</h3>"
        f"<pre>{by_plat or '발행 없음'}</pre>"
        "<p>각 포스트 반응(좋아요·조회수)은 앱에서 확인 후 "
        "포맷별로 대조하세요. 잘 되는 포맷만 남기면 됩니다.</p>"
        "</body></html>"
    )
    if not cfg.smtp_user or not cfg.email_to:
        print("[info] SMTP 미설정 — 주간 리포트 스킵")
        return False
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"{cfg.email_subject_prefix} 주간 리포트"
    msg["From"] = formataddr(("AI Radar", cfg.smtp_user))
    msg["To"] = cfg.email_to
    msg.attach(MIMEText(html, "html", "utf-8"))
    if cfg.dry_run:
        print("[dry-run] 주간 리포트 발송 생략")
    else:
        with smtplib.SMTP_SSL(cfg.smtp_host, cfg.smtp_port) as s:
            s.login(cfg.smtp_user, cfg.smtp_password)
            s.send_message(msg)
        print("[ok] 주간 리포트 발송 완료")
    return True
