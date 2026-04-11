"""정보처리기사 index.md 자동 빌더.

bite-size-study 카드 원본에서 메타 + 본문 섹션(핵심 개념 · 키워드 · 기출 포인트)을
추출해 각 다이어그램 하단에 상세 설명을 배치한 index.md를 재생성한다.

빈출 우선 순서를 유지: priority 3 (🔥) → priority 2 (⭐) → priority 1 (·).
현재는 priority 3만 대상 (본 네임스페이스에 존재하는 파일과 일치하는 카드).

실행: python3 build_index.py
출력: ../index.md 덮어쓰기
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CARD_ROOT = Path("/Users/danny/Documents/PARA/Resource/bite-size-study/content/cards")

# 과목 메타 (인덱스 헤더·폴더·이모지)
SUBJECTS: list[tuple[str, str, str, str]] = [
    # (wiki 폴더, 카드 폴더, 제목, 이모지)
    ("db", "db", "DB (데이터베이스)", "🗄️"),
    ("nw", "network", "NW (네트워크)", "📡"),
    ("os", "os", "OS · 유지보수", "🖥️"),
    ("pg", "programming", "PG (프로그래밍 언어)", "💻"),
    ("se", "software-eng", "SE (소프트웨어 공학)", "🛠️"),
]

PRIORITY_BADGE = {3: "🔥", 2: "⭐", 1: "·"}
PRIORITY_LABEL = {3: "매회 출제", 2: "자주 출제", 1: "가끔 출제"}


@dataclass(frozen=True)
class Card:
    id: str
    subject_folder: str
    wiki_folder: str
    title: str
    priority: int
    summary: str       # 핵심 개념 (prose)
    keywords: list[str]  # 키워드 불릿
    exam_tip: str      # 기출 포인트 (prose, > 인용 제거)
    one_liner: str     # 기존 인덱스 테이블용 1줄 요약


def _parse_card(path: Path, wiki_folder: str) -> Card | None:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.DOTALL)
    if not m:
        return None
    fm = yaml.safe_load(m.group(1))
    body = m.group(2)

    def _section(name: str) -> str:
        pat = rf"###\s*{re.escape(name)}\s*\n(.*?)(?=\n###\s|\n##\s|\Z)"
        sm = re.search(pat, body, re.DOTALL)
        return (sm.group(1).strip() if sm else "")

    summary = _section("핵심 개념")
    keywords_raw = _section("키워드")
    exam_tip = _section("기출 포인트")
    exam_tip = re.sub(r"^>\s*", "", exam_tip).strip()

    keywords: list[str] = []
    for line in keywords_raw.splitlines():
        line = line.strip()
        if line.startswith("- "):
            keywords.append(line[2:].strip())

    return Card(
        id=fm.get("id", path.stem),
        subject_folder=path.parent.name,
        wiki_folder=wiki_folder,
        title=fm.get("title", path.stem),
        priority=int(fm.get("priority", 0)),
        summary=" ".join(summary.split()),
        keywords=keywords,
        exam_tip=" ".join(exam_tip.split()),
        one_liner=_one_liner(fm, keywords),
    )


def _one_liner(fm: dict, keywords: list[str]) -> str:
    tags = fm.get("tags", [])
    if isinstance(tags, list) and tags:
        # 테이블 셀 한 줄용: 앞쪽 태그 3개
        return " · ".join(str(t) for t in tags[:3])
    return keywords[0] if keywords else ""


def _cards_for_subject(wiki_folder: str, card_folder: str) -> list[Card]:
    folder = CARD_ROOT / card_folder
    if not folder.exists():
        return []
    cards: list[Card] = []
    for p in sorted(folder.glob("*.md")):
        c = _parse_card(p, wiki_folder)
        if c and c.priority == 3:
            cards.append(c)
    return cards


def _existing_diagram_ids(wiki_folder: str) -> set[str]:
    folder = ROOT / wiki_folder
    if not folder.exists():
        return set()
    return {p.stem for p in folder.glob("*.excalidraw")}


def _render_card_block(card: Card) -> str:
    svg_rel = f"{card.wiki_folder}/{card.id}.svg"
    lines: list[str] = []
    lines.append(f"### {PRIORITY_BADGE[card.priority]} {card.title}")
    lines.append("")
    lines.append(f"![[{svg_rel}]]")
    lines.append("")
    if card.summary:
        lines.append("**핵심 개념**")
        lines.append("")
        lines.append(card.summary)
        lines.append("")
    if card.keywords:
        lines.append("**키워드**")
        lines.append("")
        for kw in card.keywords:
            lines.append(f"- {kw}")
        lines.append("")
    if card.exam_tip:
        lines.append("> **🎯 기출 포인트** — " + card.exam_tip)
        lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def _render_subject_section(
    emoji: str,
    title: str,
    cards: list[Card],
) -> str:
    header = f"## {emoji} {title} — {len(cards)}/{len(cards)}"
    if not cards:
        return f"{header}\n\n_준비 중_\n\n---\n"

    # 간단 테이블(요약)
    lines: list[str] = [header, ""]
    lines.append("| 빈도 | 개념 | 핵심 |")
    lines.append("|---|---|---|")
    for c in cards:
        badge = PRIORITY_BADGE[c.priority]
        lines.append(f"| {badge} | {c.title} | {c.one_liner} |")
    lines.append("")

    # 카드별 상세
    for c in cards:
        lines.append(_render_card_block(c))

    return "\n".join(lines)


HEADER = """---
title: 정보처리기사 2026 — 빈출 개념 다이어그램
created: 2026-04-10
updated: 2026-04-11
type: summary
exam: 정보처리기사
target_year: 2026
---

# 정보처리기사 2026 — 출제빈도 순 개념 다이어그램

각 개념을 Excalidraw 다이어그램 한 장으로 시각화한 학습 노트.
**빈출 순**(🔥 매회 → ⭐ 자주 → · 가끔)으로 정렬. 각 다이어그램 아래 원본 카드의
핵심 개념·키워드·기출 포인트를 함께 배치해 한 장짜리 요약과 본문 설명을
한 화면에서 볼 수 있게 구성했다.

## 범례
- 🔥 **매회 출제** (priority 3) — 무조건 암기
- ⭐ **자주 출제** (priority 2) — 이해 + 예시 풀이
- · **가끔 출제** (priority 1) — 빠르게 훑기만

## 현재 상태
priority 3 전량 **30 / 30 완료**. 5개 과목 모두 생성.

---
"""


FOOTER = """## 사용법
1. 웹에서는 [공개 사이트](https://cskwork.github.io/certifications-wiki/)에서 바로 열람.
2. Obsidian에서는 파일 트리의 `.excalidraw` 파일을 클릭하면 Excalidraw 플러그인 뷰어로 열림.
3. 편집 후 `export_svg.py` 재실행 → SVG 갱신 → 사이트에 자동 반영.
4. 인덱스 전체 재빌드: `python3 _generators/build_index.py`.

## 원본 카드
카드 원문(Markdown)은 `~/Documents/PARA/Resource/bite-size-study/content/cards/` 아래 과목별 폴더.
다이어그램 아래 설명은 원문을 자동 추출한 것으로, 수작업 편집 대신 `build_index.py`를 재실행해
동기화하는 것이 권장 방식이다.

## 다음 단계 로드맵
- [ ] priority 2 (⭐ 자주) 31장 확장 — DB 4, NW 6, OS 6, PG 13, SE 2
- [ ] priority 1 (· 가끔) 3장 확장
- [ ] 각 다이어그램에 퀴즈 카드 링크 (bite-size-study 연동)
"""


def main() -> None:
    parts: list[str] = [HEADER]
    total = 0
    for wiki_folder, card_folder, title, emoji in SUBJECTS:
        cards = _cards_for_subject(wiki_folder, card_folder)
        existing = _existing_diagram_ids(wiki_folder)
        cards = [c for c in cards if c.id in existing]
        cards.sort(key=lambda c: (-c.priority, c.id))
        parts.append(_render_subject_section(emoji, title, cards))
        parts.append("")
        total += len(cards)

    parts.append(FOOTER)

    out = "\n".join(parts)
    (ROOT / "index.md").write_text(out, encoding="utf-8")
    print(f"✓ index.md 재생성 완료 — {total}개 카드 블록")


if __name__ == "__main__":
    main()
