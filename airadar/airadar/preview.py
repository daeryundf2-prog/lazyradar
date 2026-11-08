"""로컬 미리보기 — 오늘 발행될 글을 HTML로 확인."""
from __future__ import annotations

import base64
import webbrowser
from pathlib import Path

from . import drafter
from .card import make_card
from .config import Config
from .db import Store


def generate_preview(store: Store, cfg: Config, n: int = 5) -> Path:
    rows = store.pending_post(cfg.min_score_to_post, n)
    if not rows:
        rows = store.conn.execute(
            "SELECT * FROM items ORDER BY collected_at DESC LIMIT ?",
            (n,)).fetchall()
    blocks = []
    for r in rows:
        card_b64 = ""
        try:
            card_b64 = base64.b64encode(
                make_card(r["title"], r["source"]).read_bytes()
            ).decode()
        except Exception:
            pass
        fmts = []
        for name in drafter.FORMAT_ORDER:
            text = "\n\n".join(drafter.draft(
                name, r["title"], r["link"], r["summary"] or "", cfg))
            fmts.append(
                f"<div class='fmt'><div class='fmtname'>{name}</div>"
                f"<pre>{text}</pre></div>")
        blocks.append(
            f"<section><h3>{r['title']}</h3>"
            f"<div class='meta'>{r['source']} · score {r['score']:.1f} · "
            f"<a href='{r['link']}'>{r['link']}</a></div>"
            + (f"<img src='data:image/png;base64,{card_b64}'/>"
               if card_b64 else "")
            + f"<div class='grid'>{''.join(fmts)}</div></section>")
    html = f"""<!doctype html><meta charset=utf-8><title>airadar preview</title>
<style>
body{{background:#0b1220;color:#e2e8f0;font-family:sans-serif;margin:24px}}
section{{border:1px solid #1e3a5f;border-radius:12px;padding:20px;margin-bottom:28px}}
h3{{margin:0 0 6px}} .meta{{color:#64748b;font-size:.85em;margin-bottom:12px}}
a{{color:#22d3ee}} img{{max-width:480px;border-radius:8px;margin:8px 0}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.fmt{{background:#0f1a2e;border-radius:8px;padding:10px}}
.fmtname{{color:#22d3ee;font-weight:700;margin-bottom:6px}}
pre{{white-space:pre-wrap;font-family:inherit;font-size:.9em;margin:0}}
</style>
<h1>📡 airadar — 오늘 발행 예정 미리보기</h1>
{''.join(blocks)}"""
    out = Path("preview.html")
    out.write_text(html, encoding="utf-8")
    return out


def preview(store: Store, cfg: Config, n: int = 5,
            open_browser: bool = True) -> Path:
    out = generate_preview(store, cfg, n)
    print(f"[ok] 미리보기 생성 → {out.resolve()}")
    if open_browser:
        webbrowser.open(f"file://{out.resolve()}")
    return out
