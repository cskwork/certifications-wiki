"""Excalidraw JSON → SVG 순수 Python 변환기.

각 과목 폴더(`db/`, `nw/`, `os/`, `pg/`, `se/`) 아래의 `.excalidraw` 파일을 읽어
같은 이름의 `.svg` 파일을 옆에 저장한다. Quartz/GitHub Pages가 바로 렌더할 수 있는
정적 SVG이며, Obsidian 임베드도 `![[file.svg]]` 구문으로 동일하게 동작한다.

지원 요소: rectangle, ellipse, text (줄바꿈 포함), arrow, line.
한글은 Pretendard → system-ui 순 폴백으로 렌더.

실행: `python3 export_svg.py`
"""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_ROOT = ROOT / "content"
SUBJECTS = ["db", "nw", "os", "pg", "se"]

PAD = 40  # SVG viewBox padding
FONT_STACK = (
    "Pretendard, 'Apple SD Gothic Neo', 'Noto Sans KR', "
    "-apple-system, BlinkMacSystemFont, system-ui, sans-serif"
)


def _bbox(elements: list[dict]) -> tuple[float, float, float, float]:
    xs_min, ys_min = float("inf"), float("inf")
    xs_max, ys_max = float("-inf"), float("-inf")
    for el in elements:
        if el.get("isDeleted"):
            continue
        x, y = el["x"], el["y"]
        w, h = el.get("width", 0), el.get("height", 0)
        if el["type"] in ("arrow", "line"):
            # points are relative to (x, y)
            pts = el.get("points") or [[0, 0], [w, h]]
            for px, py in pts:
                xs_min = min(xs_min, x + px)
                ys_min = min(ys_min, y + py)
                xs_max = max(xs_max, x + px)
                ys_max = max(ys_max, y + py)
        else:
            xs_min = min(xs_min, x)
            ys_min = min(ys_min, y)
            xs_max = max(xs_max, x + w)
            ys_max = max(ys_max, y + h)
    if xs_min == float("inf"):
        return 0.0, 0.0, 800.0, 600.0
    return xs_min - PAD, ys_min - PAD, xs_max - xs_min + 2 * PAD, ys_max - ys_min + 2 * PAD


def _color(val: str | None, fallback: str = "none") -> str:
    if not val or val == "transparent":
        return fallback
    return val


def _render_rect(el: dict) -> str:
    rx = 10 if el.get("roundness") else 0
    fill = _color(el.get("backgroundColor"), "none")
    stroke = _color(el.get("strokeColor"), "#1e1e1e")
    sw = el.get("strokeWidth", 2)
    return (
        f'<rect x="{el["x"]:.1f}" y="{el["y"]:.1f}" '
        f'width="{el["width"]:.1f}" height="{el["height"]:.1f}" '
        f'rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    )


def _render_ellipse(el: dict) -> str:
    cx = el["x"] + el["width"] / 2
    cy = el["y"] + el["height"] / 2
    rx = el["width"] / 2
    ry = el["height"] / 2
    fill = _color(el.get("backgroundColor"), "none")
    stroke = _color(el.get("strokeColor"), "#1e1e1e")
    sw = el.get("strokeWidth", 2)
    return (
        f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    )


def _render_text(el: dict) -> str:
    size = el.get("fontSize", 18)
    fill = _color(el.get("strokeColor"), "#1e1e1e")
    align = el.get("textAlign", "left")
    anchor = {"left": "start", "center": "middle", "right": "end"}.get(align, "start")
    x = el["x"]
    if align == "center":
        x += el["width"] / 2
    elif align == "right":
        x += el["width"]
    # Baseline offset — Excalidraw places text with top-align; SVG text uses baseline.
    y = el["y"] + size  # approx ascent
    raw = el.get("text") or el.get("originalText") or ""
    lines = raw.split("\n")
    tspans = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else int(size * 1.25)
        tspans.append(
            f'<tspan x="{x:.1f}" dy="{dy}">{html.escape(line)}</tspan>'
        )
    return (
        f'<text font-family="{FONT_STACK}" font-size="{size}" '
        f'text-anchor="{anchor}" fill="{fill}" '
        f'x="{x:.1f}" y="{y:.1f}">{"".join(tspans)}</text>'
    )


def _render_line_like(el: dict, with_arrow: bool) -> str:
    pts = el.get("points") or [[0, 0], [el["width"], el["height"]]]
    if len(pts) < 2:
        return ""
    x, y = el["x"], el["y"]
    abs_pts = [(x + px, y + py) for px, py in pts]
    stroke = _color(el.get("strokeColor"), "#1e1e1e")
    sw = el.get("strokeWidth", 2)
    marker = ' marker-end="url(#arrowhead)"' if with_arrow else ""
    d = " ".join(
        f"{'M' if i == 0 else 'L'}{px:.1f},{py:.1f}" for i, (px, py) in enumerate(abs_pts)
    )
    return (
        f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}"'
        f' stroke-linecap="round" stroke-linejoin="round"{marker}/>'
    )


def _render_element(el: dict) -> str:
    if el.get("isDeleted"):
        return ""
    t = el["type"]
    if t == "rectangle":
        return _render_rect(el)
    if t == "ellipse":
        return _render_ellipse(el)
    if t == "text":
        return _render_text(el)
    if t == "arrow":
        return _render_line_like(el, with_arrow=True)
    if t == "line":
        return _render_line_like(el, with_arrow=False)
    return ""  # diamond, freedraw, image 등은 스킵


def to_svg(excalidraw_path: Path) -> str:
    doc = json.loads(excalidraw_path.read_text(encoding="utf-8"))
    elements: list[dict] = doc.get("elements", [])
    vx, vy, vw, vh = _bbox(elements)
    bg = doc.get("appState", {}).get("viewBackgroundColor", "#ffffff")

    body = [_render_element(el) for el in elements]
    body_str = "\n  ".join(filter(None, body))

    defs = (
        '<defs>'
        '<marker id="arrowhead" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path d="M0,0 L10,5 L0,10 z" fill="#1e1e1e"/>'
        '</marker>'
        '</defs>'
    )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="{vx:.1f} {vy:.1f} {vw:.1f} {vh:.1f}" '
        f'width="{vw:.0f}" height="{vh:.0f}" '
        f'style="max-width: 100%; height: auto; background: {bg};">\n'
        f'  {defs}\n'
        f'  {body_str}\n'
        f'</svg>\n'
    )


def main() -> None:
    total = 0
    for sub in SUBJECTS:
        folder = CONTENT_ROOT / sub
        if not folder.exists():
            continue
        for src in sorted(folder.glob("*.excalidraw")):
            svg = to_svg(src)
            dst = src.with_suffix(".svg")
            dst.write_text(svg, encoding="utf-8")
            total += 1
            print(f"  ✓ {sub}/{dst.name}")
    print(f"\nSVG 생성 완료: {total}개")


if __name__ == "__main__":
    main()
