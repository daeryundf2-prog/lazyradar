"""airadar CLI — collect / digest / post / run / status / formats / preview / weekly / ideas / metrics / report."""
from __future__ import annotations

import argparse
import sys
import time

from .collect import collect
from .config import Config
from .db import Store
from .mailer import send_digest, send_weekly
from .poster import autopost


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="airadar",
                                 description="AI 뉴스 수집 → 이메일 + 자동 포스팅")
    ap.add_argument("-c", "--config", default="config.yaml")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("collect", help="피드 수집만")
    sub.add_parser("save", help="수집 + 마크다운 파일 저장 (digests/)")
    sub.add_parser("digest", help="이메일 다이제스트 발송")
    sub.add_parser("post", help="자동 포스팅")
    sub.add_parser("run", help="collect + digest + post (+주간리포트)")
    sub.add_parser("status", help="DB 통계")
    p_fmt = sub.add_parser("formats", help="포맷별 미리보기")
    p_fmt.add_argument("-n", type=int, default=1, help="항목 수")
    p_prev = sub.add_parser("preview", help="발행 예정 HTML 미리보기")
    p_prev.add_argument("-n", type=int, default=5)
    p_prev.add_argument("--no-open", action="store_true")
    sub.add_parser("weekly", help="주간 성과 리포트 이메일")
    p_idea = sub.add_parser("ideas", help="뻘글/잡담 소재 뽑기")
    p_idea.add_argument("-n", type=int, default=3)
    sub.add_parser("metrics", help="발행 글 반응 수집 (Bluesky)")
    p_rep = sub.add_parser("report", help="포맷별 발행 로그")
    p_rep.add_argument("--days", type=int, default=30)
    args = ap.parse_args(argv)

    cfg = Config.load(args.config)
    store = Store(cfg.db_path)

    if args.cmd in ("collect", "save", "run"):
        n = collect(store, cfg)
        print(f"[ok] 새 항목 {n}건 수집")
    if args.cmd == "save":
        from .exporter import save_digest
        save_digest(store, cfg)
    if args.cmd == "run":
        from .exporter import save_digest
        save_digest(store, cfg)
    if args.cmd in ("digest", "run"):
        send_digest(store, cfg)
    if args.cmd in ("post", "run"):
        autopost(store, cfg)
    if args.cmd == "run" and time.localtime().tm_wday == cfg.weekly_report_day:
        send_weekly(store, cfg)
    if args.cmd == "status":
        print(store.stats())
    if args.cmd == "formats":
        from . import drafter
        rows = store.pending_post(0.0, args.n) or store.conn.execute(
            "SELECT * FROM items ORDER BY collected_at DESC LIMIT ?",
            (args.n,)).fetchall()
        for r in rows:
            print(f"=== {r['title'][:70]}")
            for name in drafter.FORMAT_ORDER:
                text = "\n\n".join(drafter.draft(
                    name, r["title"], r["link"], r["summary"] or "", cfg))
                print(f"  [{name}]\n  {text}\n")
    if args.cmd == "preview":
        from .preview import preview
        preview(store, cfg, args.n, open_browser=not args.no_open)
    if args.cmd == "weekly":
        send_weekly(store, cfg)
    if args.cmd == "ideas":
        from .topics import idea
        for line in idea(args.n):
            print(line)
    if args.cmd == "metrics":
        from .metrics import print_metrics
        print_metrics(store, cfg)
    if args.cmd == "report":
        rows = store.posts_report(args.days)
        if not rows:
            print("발행 로그 없음")
        for r in rows:
            flag = "(dry)" if r["dry"] else ""
            print(f"{r['at']} [{r['platform']}:{r['format']}]{flag}"
                  f" {r['title'][:60]} remote={r['remote_id']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
