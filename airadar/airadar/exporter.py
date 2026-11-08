"""수집 항목을 마크다운 파일로 저장 — digests/YYYY-MM-DD.md 에 누적."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from .config import Config
from .db import Store


def save_digest(store: Store, cfg: Config,
                out_dir: str = "digests") -> Path | None:
    rows = store.pending_export()
    if not rows:
        print("[info] 저장할 새 항목 없음")
        return None
    d = Path(out_dir)
    d.mkdir(exist_ok=True)
    path = d / f"{datetime.now():%Y-%m-%d}.md"
    lines = [
        f"## {datetime.now():%H:%M} 수집 — {len(rows)}건\n",
    ]
    for r in rows:
        niche = " ⭐" if r["score"] >= 1.5 else ""
        lines.append(f"- **[{r['source']}] {r['title']}**{niche}")
        lines.append(f"  - {r['link']}")
        if r["summary"]:
            lines.append(f"  - {r['summary'][:200]}")
    with path.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n\n")
    store.mark_exported([r["id"] for r in rows])
    print(f"[ok] {len(rows)}건 저장 → {path}")
    return path
