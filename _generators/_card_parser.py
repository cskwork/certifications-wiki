"""bite-size-study 카드 파서 공용 모듈.

gen_quartz_pages.py / export_svg.py가 공유하는 카드 메타/본문 파서.
원래 build_index.py에 있던 로직을 추출했다.

카드 원본 위치: ~/Documents/PARA/Resource/bite-size-study/content/cards/{subject}/
각 카드는 frontmatter(yaml) + 본문 섹션:
    왜 배우나 / 핵심 개념 / 키워드 / 이해 확인 / 기출 포인트 / 연결 개념
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CARD_ROOT = Path("/Users/danny/Documents/PARA/Resource/bite-size-study/content/cards")
CONTENT_ROOT = ROOT / "content"

# (wiki 폴더, 카드 폴더, 제목, 이모지)
SUBJECTS: list[tuple[str, str, str, str]] = [
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
    why: str
    summary: str
    keywords: list[str]
    self_check: str
    exam_tip: str


def parse_card(path: Path, wiki_folder: str) -> Card | None:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.DOTALL)
    if not m:
        return None
    fm = yaml.safe_load(m.group(1))
    body = m.group(2)

    def _section(name: str) -> str:
        pat = rf"###\s*{re.escape(name)}\s*\n(.*?)(?=\n###\s|\n##\s|\Z)"
        sm = re.search(pat, body, re.DOTALL)
        return sm.group(1).strip() if sm else ""

    why = _section("왜 배우나")
    summary = _section("핵심 개념")
    keywords_raw = _section("키워드")
    self_check = _section("이해 확인")
    exam_tip = re.sub(r"^>\s*", "", _section("기출 포인트")).strip()

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
        why=why,
        summary=" ".join(summary.split()),
        keywords=keywords,
        self_check=self_check,
        exam_tip=" ".join(exam_tip.split()),
    )


def existing_svg_ids(wiki_folder: str) -> set[str]:
    """content/{wiki_folder}/ 아래 존재하는 svg 스템 목록 반환."""
    folder = CONTENT_ROOT / wiki_folder
    if not folder.exists():
        return set()
    return {p.stem for p in folder.glob("*.svg")}


def card_folder_of(wiki_folder: str) -> str:
    for wf, cf, _, _ in SUBJECTS:
        if wf == wiki_folder:
            return cf
    raise KeyError(wiki_folder)
