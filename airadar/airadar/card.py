"""포스트 첨부용 브랜디드 카드 이미지 생성 (1200x630)."""
from __future__ import annotations

import math
import tempfile
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT_CANDIDATES = [
    "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/NanumGothic.ttf",
]


def _font(size: int) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def _wrap_by_px(draw, text: str, font, max_w: int, max_lines: int = 4):
    lines = []
    for para in text.split("\n"):
        buf = ""
        for ch in para:
            if draw.textlength(buf + ch, font=font) <= max_w:
                buf += ch
            else:
                lines.append(buf)
                buf = ch
        if buf:
            lines.append(buf)
    return lines[:max_lines] + (["…"] if len(lines) > max_lines else [])


def make_card(title: str, source: str, out: str | Path | None = None) -> Path:
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), "#0b1220")
    d = ImageDraw.Draw(img)

    # 레이더 장식 (우측)
    cx, cy = W - 220, H // 2
    for r in (60, 110, 160):
        d.ellipse([cx-r, cy-r, cx+r, cy+r], outline="#1e3a5f", width=3)
    for i in range(50):
        a = math.radians(-90 - i * 1.4)
        shade = max(0, 200 - i * 4)
        d.line([cx, cy, cx + 165*math.cos(a), cy + 165*math.sin(a)],
               fill=(20, shade, 160), width=2)
    d.ellipse([cx-170, cy-170, cx+170, cy+170], outline="#22d3ee", width=4)
    for (px, py, rr) in [(cx+70, cy-55, 8), (cx-45, cy+80, 5)]:
        d.ellipse([px-rr, py-rr, px+rr, py+rr], fill="#22d3ee")

    # 상단 배지
    badge_f = _font(30)
    d.rounded_rectangle([60, 60, 60 + d.textlength("AI RADAR", font=badge_f) + 36, 116],
                        radius=28, outline="#22d3ee", width=2)
    d.text((78, 74), "AI RADAR", font=badge_f, fill="#22d3ee")

    # 제목 (왼쪽 780px)
    title_f = _font(52)
    lines = _wrap_by_px(d, title, title_f, 780)
    y = 170
    for ln in lines:
        d.text((60, y), ln, font=title_f, fill="#e2e8f0")
        y += 68

    # 출처
    src_f = _font(32)
    d.text((60, H - 100), f"via {source}", font=src_f, fill="#64748b")

    # 하단 라인
    d.line([60, H - 40, W - 60, H - 40], fill="#1e3a5f", width=2)

    if out is None:
        out = Path(tempfile.mkdtemp()) / "card.png"
    img.save(str(out))
    return Path(out)
