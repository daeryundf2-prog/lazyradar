"""SQLite 기반 수집/발행 상태 저장소."""
from __future__ import annotations

import hashlib
import sqlite3
import time
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS items (
    id TEXT PRIMARY KEY,
    source TEXT NOT NULL,
    title TEXT NOT NULL,
    link TEXT NOT NULL,
    summary TEXT,
    score REAL NOT NULL DEFAULT 0,
    collected_at INTEGER NOT NULL,
    emailed_at INTEGER,
    posted_x_at INTEGER,
    posted_threads_at INTEGER,
    posted_bluesky_at INTEGER,
    posted_mastodon_at INTEGER
);
CREATE INDEX IF NOT EXISTS idx_items_emailed ON items(emailed_at);

CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id TEXT NOT NULL,
    platform TEXT NOT NULL,
    format TEXT NOT NULL,
    text TEXT NOT NULL,
    remote_id TEXT,
    dry INTEGER NOT NULL DEFAULT 0,
    posted_at INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_posts_format ON posts(format);
"""


POST_COL = {"x": "posted_x_at", "threads": "posted_threads_at",
            "bluesky": "posted_bluesky_at", "mastodon": "posted_mastodon_at"}


class Store:
    def __init__(self, path: str | Path):
        self.conn = sqlite3.connect(str(path))
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)
        # 신규 플랫폼 컬럼 마이그레이션
        cols = {r[1] for r in self.conn.execute("PRAGMA table_info(items)")}
        for col in (*POST_COL.values(), "exported_at"):
            if col not in cols:
                self.conn.execute(f"ALTER TABLE items ADD COLUMN {col} INTEGER")
        self.conn.commit()

    @staticmethod
    def make_id(source: str, link: str) -> str:
        return hashlib.sha256(f"{source}|{link}".encode()).hexdigest()[:24]

    def upsert(self, source: str, title: str, link: str,
               summary: str, score: float) -> bool:
        """새 항목이면 True 반환."""
        item_id = self.make_id(source, link)
        cur = self.conn.execute(
            "INSERT OR IGNORE INTO items"
            " (id, source, title, link, summary, score, collected_at)"
            " VALUES (?,?,?,?,?,?,?)",
            (item_id, source, title, link, summary, score, int(time.time())),
        )
        self.conn.commit()
        return cur.rowcount > 0

    def pending_export(self, limit: int = 100) -> list[sqlite3.Row]:
        return self.conn.execute(
            "SELECT * FROM items WHERE exported_at IS NULL"
            " ORDER BY score DESC, collected_at DESC LIMIT ?",
            (limit,),
        ).fetchall()

    def mark_exported(self, ids: list[str]) -> None:
        now = int(time.time())
        self.conn.executemany(
            "UPDATE items SET exported_at=? WHERE id=?", [(now, i) for i in ids])
        self.conn.commit()

    def pending_email(self, limit: int = 30) -> list[sqlite3.Row]:
        return self.conn.execute(
            "SELECT * FROM items WHERE emailed_at IS NULL"
            " ORDER BY score DESC, collected_at DESC LIMIT ?",
            (limit,),
        ).fetchall()

    def pending_post(self, min_score: float, limit: int = 5,
                     platforms: tuple[str, ...] = ("x", "threads")
                     ) -> list[sqlite3.Row]:
        """지정 플랫폼 중 하나라도 미발행인 항목."""
        conds = " OR ".join(f"{POST_COL[p]} IS NULL" for p in platforms)
        return self.conn.execute(
            f"SELECT * FROM items WHERE ({conds}) AND score >= ?"
            " ORDER BY score DESC, collected_at DESC LIMIT ?",
            (min_score, limit),
        ).fetchall()

    def mark_emailed(self, ids: list[str]) -> None:
        now = int(time.time())
        self.conn.executemany(
            "UPDATE items SET emailed_at=? WHERE id=?", [(now, i) for i in ids])
        self.conn.commit()

    def mark_posted(self, item_id: str, platform: str) -> None:
        col = POST_COL[platform]
        self.conn.execute(
            f"UPDATE items SET {col}=? WHERE id=?", (int(time.time()), item_id))
        self.conn.commit()

    def record_post(self, item_id: str, platform: str, fmt: str,
                    text: str, remote_id: str | None, dry: bool) -> None:
        self.conn.execute(
            "INSERT INTO posts (item_id, platform, format, text, remote_id,"
            " dry, posted_at) VALUES (?,?,?,?,?,?,?)",
            (item_id, platform, fmt, text, remote_id, int(dry),
             int(time.time())))
        self.conn.commit()

    def format_counts_today(self) -> dict[str, int]:
        start = int(time.time()) - (int(time.time()) % 86400)
        rows = self.conn.execute(
            "SELECT format, COUNT(*) c FROM posts"
            " WHERE posted_at >= ? AND dry = 0 GROUP BY format",
            (start,)).fetchall()
        return {r["format"]: r["c"] for r in rows}

    def posts_today(self, platform: str) -> int:
        start = int(time.time()) - (int(time.time()) % 86400)
        r = self.conn.execute(
            "SELECT COUNT(*) c FROM posts"
            " WHERE platform=? AND posted_at>=? AND dry=0",
            (platform, start)).fetchone()
        return r["c"]

    def posts_report(self, days: int = 30) -> list[sqlite3.Row]:
        since = int(time.time()) - days * 86400
        return self.conn.execute(
            "SELECT p.platform, p.format, p.remote_id, p.dry,"
            " datetime(p.posted_at,'unixepoch','localtime') at,"
            " i.title FROM posts p JOIN items i ON i.id = p.item_id"
            " WHERE p.posted_at >= ? ORDER BY p.posted_at DESC",
            (since,)).fetchall()

    def stats(self) -> dict:
        r = self.conn.execute(
            "SELECT COUNT(*) total,"
            " SUM(emailed_at IS NOT NULL) emailed,"
            " SUM(posted_x_at IS NOT NULL) posted_x,"
            " SUM(posted_threads_at IS NOT NULL) posted_th FROM items"
        ).fetchone()
        return dict(r)
