"""Quartz v4 content 트리 자동 빌더.

bite-size-study 카드를 Quartz가 소비하는 **개별 markdown 페이지**로 변환한다.
각 카드는 독립 파일이 되고, 카드 사이 관계(연결 개념)는 `[[wikilink]]`로
표현되어 Quartz의 Graph View/백링크/위키링크가 자동으로 활성화된다.

실행: python3 gen_quartz_pages.py
출력:
    content/index.md                 루트 MOC
    content/{wiki_folder}/index.md   과목별 허브
    content/{wiki_folder}/{id}.md    카드별 페이지

카드 md 파일만 생성한다. svg/excalidraw 자산은 content/{wiki_folder}/에
이미 존재한다고 가정 (export_svg.py가 관리).
"""
from __future__ import annotations

import re
from pathlib import Path

from _card_parser import (
    CARD_ROOT,
    CONTENT_ROOT,
    PRIORITY_BADGE,
    PRIORITY_LABEL,
    SUBJECTS,
    Card,
    card_folder_of,
    existing_svg_ids,
    parse_card,
)

# 연결 개념: `card-id` 패턴만 매칭. 한글 괄호 설명은 버린다.
RELATED_ID_RE = re.compile(r"`([a-z]+-[a-z0-9-]+)`")


def _collect_cards() -> list[Card]:
    """priority 3 + svg가 존재하는 카드만 대상."""
    cards: list[Card] = []
    for wiki_folder, card_folder, _, _ in SUBJECTS:
        folder = CARD_ROOT / card_folder
        if not folder.exists():
            continue
        svgs = existing_svg_ids(wiki_folder)
        for path in sorted(folder.glob("*.md")):
            card = parse_card(path, wiki_folder)
            if card and card.priority == 3 and card.id in svgs:
                cards.append(card)
    return cards


def _build_related(card_md_path: Path, known_ids: dict[str, Card]) -> list[str]:
    """카드 md 본문에서 '연결 개념' 섹션을 파싱해 위키링크 리스트 반환."""
    text = card_md_path.read_text(encoding="utf-8")
    match = re.search(
        r"###\s*연결 개념\s*\n(.*?)(?=\n###\s|\n##\s|\Z)",
        text,
        re.DOTALL,
    )
    if not match:
        return []

    seen: set[str] = set()
    links: list[str] = []
    for related_id in RELATED_ID_RE.findall(match.group(1)):
        if related_id in seen:
            continue
        seen.add(related_id)
        target = known_ids.get(related_id)
        if target is None:
            # 생성 목록에 없는 카드는 plain code로 남겨 깨진 위키링크 방지.
            links.append(f"`{related_id}`")
        else:
            links.append(f"[[{related_id}|{target.title}]]")
    return links


def _render_card_page(card: Card, links: list[str], subject_title: str) -> str:
    badge = PRIORITY_BADGE[card.priority]
    label = PRIORITY_LABEL[card.priority]

    fm = [
        "---",
        f'title: "{card.title}"',
        f'subject: "{subject_title}"',
        f"priority: {card.priority}",
        f'frequency: "{badge} {label}"',
        "tags:",
        f"  - {card.wiki_folder}",
        f"  - priority-{card.priority}",
        "---",
        "",
    ]

    body: list[str] = [
        f"# {card.title}",
        "",
        f"> {badge} **{label}** (priority {card.priority})",
        "",
        f"![[{card.id}.svg]]",
        "",
    ]

    if card.summary:
        body += ["## 핵심 개념", "", card.summary, ""]

    if card.keywords:
        body += ["## 키워드", ""]
        body += [f"- {kw}" for kw in card.keywords]
        body.append("")

    if card.exam_tip:
        body += ["## 🎯 기출 포인트", "", f"> {card.exam_tip}", ""]

    if links:
        body += ["## 연결 개념", ""]
        body += [f"- {link}" for link in links]
        body.append("")

    return "\n".join(fm + body)


def _render_subject_index(subject_title: str, emoji: str, cards: list[Card]) -> str:
    lines = [
        "---",
        f'title: "{emoji} {subject_title}"',
        "---",
        "",
        f"# {emoji} {subject_title}",
        "",
        f"총 **{len(cards)}개** 빈출 개념. 출제 빈도 순 정렬.",
        "",
    ]
    for card in cards:
        badge = PRIORITY_BADGE[card.priority]
        lines.append(f"- {badge} [[{card.id}|{card.title}]]")
    lines.append("")
    return "\n".join(lines)


def _render_root_index(
    subject_counts: list[tuple[str, str, str, int]],
) -> str:
    total = sum(c for *_, c in subject_counts)
    lines = [
        "---",
        'title: "정보처리기사 2026 — 빈출 개념 그래프"',
        "---",
        "",
        "# 정보처리기사 2026",
        "",
        "[jzhao.xyz](https://jzhao.xyz/posts/networked-thought) 스타일의 "
        "networked-thought wiki. 각 개념을 독립 페이지로 두고 서로 링크했다. "
        "우측 **Graph View**에서 전체 구조를 한눈에 볼 수 있다.",
        "",
        "## 범례",
        "- 🔥 매회 출제 (priority 3) — 무조건 암기",
        "- ⭐ 자주 출제 (priority 2) — 이해 + 예시 풀이",
        "- · 가끔 출제 (priority 1) — 빠르게 훑기",
        "",
        f"## 과목 ({total}개 개념)",
        "",
    ]
    for wiki_folder, subject_title, emoji, count in subject_counts:
        lines.append(
            f"- {emoji} [[{wiki_folder}/index|{subject_title}]] — {count}개"
        )
    lines += [
        "",
        "## 소스",
        "",
        "카드 원본은 `~/Documents/PARA/Resource/bite-size-study/content/cards/`. "
        "페이지를 수동 편집하지 말고 원본 카드를 고친 뒤 "
        "`python3 _generators/gen_quartz_pages.py`로 재생성할 것.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    all_cards = _collect_cards()
    known_ids = {c.id: c for c in all_cards}

    CONTENT_ROOT.mkdir(exist_ok=True)

    subject_counts: list[tuple[str, str, str, int]] = []
    for wiki_folder, _, subject_title, emoji in SUBJECTS:
        subject_cards = [c for c in all_cards if c.wiki_folder == wiki_folder]
        if not subject_cards:
            continue
        subject_cards.sort(key=lambda c: (-c.priority, c.id))

        subject_dir = CONTENT_ROOT / wiki_folder
        subject_dir.mkdir(exist_ok=True)

        for card in subject_cards:
            card_md_path = CARD_ROOT / card_folder_of(wiki_folder) / f"{card.id}.md"
            links = _build_related(card_md_path, known_ids)
            page = _render_card_page(card, links, subject_title)
            (subject_dir / f"{card.id}.md").write_text(page, encoding="utf-8")

        (subject_dir / "index.md").write_text(
            _render_subject_index(subject_title, emoji, subject_cards),
            encoding="utf-8",
        )

        subject_counts.append((wiki_folder, subject_title, emoji, len(subject_cards)))
        print(f"  ✓ {emoji} {subject_title}: {len(subject_cards)}개")

    (CONTENT_ROOT / "index.md").write_text(
        _render_root_index(subject_counts),
        encoding="utf-8",
    )

    total = sum(c for *_, c in subject_counts)
    print(
        f"\n✓ content/ 재생성 완료 — 카드 {total}개 + "
        f"과목 허브 {len(subject_counts)}개 + 루트 MOC"
    )


if __name__ == "__main__":
    main()
