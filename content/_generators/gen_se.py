"""SE 과목 priority-3 카드 6장의 Excalidraw 다이어그램 생성기.

실행: python3 gen_se.py
출력: ../se/*.excalidraw
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gen_db import COLORS, arrow, badge, rect, text, title_banner  # noqa: E402  # pyright: ignore[reportMissingImports]

OUT_DIR = Path(__file__).resolve().parent.parent / "se"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def save(elements: list[dict], name: str) -> Path:
    doc = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {
            "viewBackgroundColor": "#ffffff",
            "gridSize": None,
        },
        "files": {},
    }
    path = OUT_DIR / name
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Card 1 — 모듈 응집도 7단계 (강 → 약)
# ---------------------------------------------------------------------------
def card_cohesion() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "모듈 응집도 (Cohesion) 7단계",
                        "모듈 내부 요소 간 관련성 · 높을수록(강할수록) 좋은 설계")
    els += badge(1080, 48, "🔥 매회 출제")

    # 좌측 방향 화살표 영역 라벨
    els.append(text(60, 130, "강함 (좋음) ↑", size=16, align="left", color="#2b8a3e"))
    els.append(text(60, 690, "약함 (나쁨) ↓", size=16, align="left", color="#c92a2a"))

    # 7단계 수직 사다리 — 강 → 약
    stages = [
        ("1", "Functional",    "기능적 응집도",   "모듈 내 모든 요소가 단일 기능 수행 — 이상적", COLORS["green"]),
        ("2", "Sequential",    "순차적 응집도",   "한 활동의 출력이 다음 활동의 입력 (파이프라인)", COLORS["blue"]),
        ("3", "Communicational","통신적 응집도",   "같은 입력/출력 데이터를 사용하는 활동의 집합", COLORS["yellow"]),
        ("4", "Procedural",    "절차적 응집도",   "특정 순서에 따라 실행되는 활동 (데이터 무관)", COLORS["orange"]),
        ("5", "Temporal",      "시간적 응집도",   "특정 시간대에 함께 실행 (초기화/종료 루틴)",   COLORS["pink"]),
        ("6", "Logical",       "논리적 응집도",   "유사한 성격 기능 묶음 — 제어 플래그로 선택",   COLORS["purple"]),
        ("7", "Coincidental",  "우연적 응집도",   "관련 없는 기능이 우연히 함께 — 최악",          COLORS["red"]),
    ]
    x0, y0 = 220, 130
    w, row_h, gap = 760, 66, 10
    for i, (rank, en, kr, desc, color) in enumerate(stages):
        y = y0 + i * (row_h + gap)
        els.append(rect(x0, y, w, row_h, fill=color))
        els.append(text(x0 + 14, y + 18, rank, size=22, align="left", color="#c92a2a"))
        els.append(text(x0 + 48, y + 10, en, size=18, align="left"))
        els.append(text(x0 + 48, y + 36, kr, size=14, align="left", color="#1864ab"))
        els.append(text(x0 + 280, y + 22, desc, size=13, align="left", color="#444"))

    # 좌측 방향 화살표 (강→약)
    top_y = y0 + 4
    bot_y = y0 + len(stages) * (row_h + gap) - gap - 6
    els += arrow(200, top_y, 200, bot_y)

    # 우측 암기 블록
    rx, ry = 1000, 130
    els.append(rect(rx, ry, 240, 180, fill=COLORS["yellow"]))
    els.append(text(rx + 14, ry + 12, "암기법", size=18, align="left"))
    els.append(text(rx + 14, ry + 44, "기순통절시논우", size=22, align="left", color="#c92a2a"))
    els.append(text(rx + 14, ry + 84,
                    "기능 → 순차\n→ 통신 → 절차\n→ 시간 → 논리 → 우연",
                    size=13, align="left", color="#444"))

    # 혼동 포인트
    cx, cy = 1000, 330
    els.append(rect(cx, cy, 240, 200, fill=COLORS["blue"]))
    els.append(text(cx + 14, cy + 10, "혼동 주의", size=16, align="left"))
    els.append(text(cx + 14, cy + 40, "순차 (Sequential)", size=13, align="left", color="#1864ab"))
    els.append(text(cx + 14, cy + 60, "  → 데이터 흐름", size=12, align="left", color="#444"))
    els.append(text(cx + 14, cy + 84, "절차 (Procedural)", size=13, align="left", color="#1864ab"))
    els.append(text(cx + 14, cy + 104, "  → 실행 순서", size=12, align="left", color="#444"))
    els.append(text(cx + 14, cy + 140, "2024-2회:", size=12, align="left", color="#c92a2a"))
    els.append(text(cx + 14, cy + 158, "순차적 응집도 정의", size=12, align="left", color="#c92a2a"))
    els.append(text(cx + 14, cy + 174, "빈칸 문제 출제", size=12, align="left", color="#c92a2a"))

    # 결합도와의 관계 (하단)
    ly = 740
    els.append(rect(60, ly, 1180, 60, fill=COLORS["gray"]))
    els.append(text(80, ly + 8, "결합도와 반대 방향 — 응집도는 ↑ (높게), 결합도는 ↓ (낮게) 가 좋은 설계",
                    size=15, align="left", color="#c92a2a"))
    els.append(text(80, ly + 34,
                    "세트 암기: 응집도 '기순통절시논우'  ↔  결합도 '자스제외공내'",
                    size=13, align="left", color="#444"))
    return els


# ---------------------------------------------------------------------------
# Card 2 — 모듈 결합도 6단계 (약 → 강)
# ---------------------------------------------------------------------------
def card_coupling() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "모듈 결합도 (Coupling) 6단계",
                        "모듈 간 상호 의존도 · 낮을수록(약할수록) 좋은 설계")
    els += badge(1080, 48, "🔥 매회 출제")

    # 좌측 방향 라벨
    els.append(text(60, 130, "약함 (좋음) ↑", size=16, align="left", color="#2b8a3e"))
    els.append(text(60, 620, "강함 (나쁨) ↓", size=16, align="left", color="#c92a2a"))

    # 6단계 — 약 → 강 (위가 좋음)
    stages = [
        ("1", "Data",     "자료 결합도",   "단순 값(스칼라) 파라미터만 전달 — 최선",       "예) add(a, b)",            COLORS["green"]),
        ("2", "Stamp",    "스탬프 결합도", "자료 구조(레코드·배열) 파라미터 전달, 일부만 사용", "예) print(Student s)", COLORS["blue"]),
        ("3", "Control",  "제어 결합도",   "제어 플래그 파라미터로 상대 모듈 흐름 결정",    "예) sort(list, asc=T)",    COLORS["yellow"]),
        ("4", "External", "외부 결합도",   "외부 선언 변수·포맷·프로토콜 공유",             "예) 외부 DB 스키마 공유",  COLORS["orange"]),
        ("5", "Common",   "공통 결합도",   "전역 변수(공통 데이터) 공유",                   "예) global config",        COLORS["pink"]),
        ("6", "Content",  "내용 결합도",   "다른 모듈 내부 코드·데이터 직접 참조 — 최악",   "예) 포인터로 내부 조작",   COLORS["red"]),
    ]
    x0, y0 = 220, 130
    w, row_h, gap = 760, 72, 10
    for i, (rank, en, kr, desc, ex, color) in enumerate(stages):
        y = y0 + i * (row_h + gap)
        els.append(rect(x0, y, w, row_h, fill=color))
        els.append(text(x0 + 14, y + 22, rank, size=22, align="left", color="#c92a2a"))
        els.append(text(x0 + 48, y + 8, en, size=18, align="left"))
        els.append(text(x0 + 48, y + 34, kr, size=14, align="left", color="#1864ab"))
        els.append(text(x0 + 280, y + 8, desc, size=13, align="left", color="#444"))
        els.append(text(x0 + 280, y + 36, ex, size=12, align="left", color="#666"))

    # 좌측 방향 화살표
    top_y = y0 + 4
    bot_y = y0 + len(stages) * (row_h + gap) - gap - 6
    els += arrow(200, bot_y, 200, top_y)  # 화살표 방향 = 약함쪽(위)으로 좋아짐

    # 우측 암기 블록
    rx, ry = 1000, 130
    els.append(rect(rx, ry, 240, 180, fill=COLORS["yellow"]))
    els.append(text(rx + 14, ry + 12, "암기법 (강→약)", size=16, align="left"))
    els.append(text(rx + 14, ry + 40, "내공외제스자", size=22, align="left", color="#c92a2a"))
    els.append(text(rx + 14, ry + 80,
                    "내용 → 공통\n→ 외부 → 제어\n→ 스탬프 → 자료",
                    size=13, align="left", color="#444"))

    # 키워드 연결
    kx, ky = 1000, 330
    els.append(rect(kx, ky, 240, 200, fill=COLORS["blue"]))
    els.append(text(kx + 14, ky + 10, "키워드 ↔ 유형", size=16, align="left"))
    els.append(text(kx + 14, ky + 40, "전역 변수", size=13, align="left", color="#1864ab"))
    els.append(text(kx + 14, ky + 58, "  → 공통 결합도", size=12, align="left", color="#444"))
    els.append(text(kx + 14, ky + 82, "제어 플래그", size=13, align="left", color="#1864ab"))
    els.append(text(kx + 14, ky + 100, "  → 제어 결합도", size=12, align="left", color="#444"))
    els.append(text(kx + 14, ky + 124, "구조체 파라미터", size=13, align="left", color="#1864ab"))
    els.append(text(kx + 14, ky + 142, "  → 스탬프 결합도", size=12, align="left", color="#444"))
    els.append(text(kx + 14, ky + 170, "2025-1회/2024-2회 출제", size=12, align="left", color="#c92a2a"))

    # 응집도와 반대 — 하단 강조
    ly = 670
    els.append(rect(60, ly, 1180, 60, fill=COLORS["gray"]))
    els.append(text(80, ly + 8, "응집도와 정반대 방향 — 결합도는 ↓ (낮게), 응집도는 ↑ (높게) 가 좋은 설계",
                    size=15, align="left", color="#c92a2a"))
    els.append(text(80, ly + 34,
                    "세트 암기: 결합도 '내공외제스자' (강→약)  ↔  응집도 '기순통절시논우' (강→약)",
                    size=13, align="left", color="#444"))
    return els


# ---------------------------------------------------------------------------
# Card 3 — GoF 생성 패턴 5가지
# ---------------------------------------------------------------------------
def card_gof_creational() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "GoF 생성(Creational) 패턴 5가지",
                        "객체 생성 방식을 캡슐화 · 구체 클래스 은닉 · 생성 유연성 확보")
    els += badge(1080, 48, "🔥 매회 출제")

    # 상단 1줄 요약
    els.append(rect(60, 110, 1180, 44, fill=COLORS["yellow"]))
    els.append(text(80, 122, "객체 생성 메커니즘을 다루며, 시스템이 어떤 구체 클래스를 사용하는지 감추고 생성의 유연성을 높임",
                    size=14, align="left", color="#444"))

    patterns = [
        ("Singleton",        "싱글톤",      "클래스 인스턴스를 하나만 생성하고\n전역 접근점 제공",
         "언제? 로그·설정·커넥션풀 등 단일 인스턴스", COLORS["green"]),
        ("Factory Method",   "팩토리 메서드", "객체 생성을 서브클래스에 위임\n상위=인터페이스, 하위=구체 결정",
         "언제? 생성할 구체 클래스를 런타임 결정",  COLORS["blue"]),
        ("Abstract Factory", "추상 팩토리",  "관련된 객체군(family)을 생성\n구체 팩토리 교체 → 제품군 전체 변경",
         "언제? 제품군 단위로 교체 필요",           COLORS["yellow"]),
        ("Builder",          "빌더",        "복잡한 객체의 생성 과정과 표현을 분리\n동일 절차 → 다른 표현 결과",
         "언제? 생성자 인자가 많거나 단계적 조립",  COLORS["orange"]),
        ("Prototype",        "프로토타입",  "기존 객체를 복제(clone)하여 새 객체 생성\n생성 비용이 클 때 유용",
         "언제? new 비용 큼 / 초기 상태 복제",      COLORS["pink"]),
    ]
    # 2행 레이아웃: 3 + 2
    x0, y0 = 60, 180
    w, h, gx, gy = 385, 220, 15, 20
    positions = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)]
    for (en, kr, desc, hint, color), (c, r) in zip(patterns, positions):
        x = x0 + c * (w + gx)
        y = y0 + r * (h + gy)
        els.append(rect(x, y, w, h, fill=color))
        els.append(text(x + 16, y + 12, en, size=22, align="left"))
        els.append(text(x + 16, y + 42, kr, size=15, align="left", color="#1864ab"))
        els.append(rect(x + 16, y + 72, w - 32, 80, fill="#ffffff"))
        els.append(text(x + 26, y + 82, desc, size=13, align="left"))
        els.append(text(x + 16, y + 162, hint, size=12, align="left", color="#c92a2a"))

    # 하단 암기 블록
    my = 640
    els.append(rect(820, my, 420, 180, fill=COLORS["purple"]))
    els.append(text(836, my + 12, "암기법", size=18, align="left"))
    els.append(text(836, my + 42, "\"AB를 FPS로 만든다\"", size=18, align="left", color="#c92a2a"))
    els.append(text(836, my + 74, "Abstract Factory · Builder", size=13, align="left", color="#444"))
    els.append(text(836, my + 94, "Factory Method · Prototype · Singleton", size=13, align="left", color="#444"))
    els.append(text(836, my + 130, "생성 5 · 구조 7 · 행위 11", size=14, align="left", color="#1864ab"))
    els.append(text(836, my + 152, "(총 23개 패턴) — 분류 매칭 빈출", size=12, align="left", color="#666"))
    return els


# ---------------------------------------------------------------------------
# Card 4 — GoF 구조 패턴 7가지
# ---------------------------------------------------------------------------
def card_gof_structural() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "GoF 구조(Structural) 패턴 7가지",
                        "클래스·객체 조합으로 더 큰 구조 형성 · 인터페이스 호환 · 기능 확장 · 접근 제어")
    els += badge(1080, 48, "🔥 매회 출제")

    # 상단 한 줄
    els.append(rect(60, 110, 1180, 44, fill=COLORS["yellow"]))
    els.append(text(80, 122, "패턴명 영문 + 한글 목적 한 줄 요약 세트로 암기. Adapter · Proxy 빈출 Top 2",
                    size=14, align="left", color="#444"))

    patterns = [
        ("Adapter",    "어댑터",      "호환되지 않는 인터페이스를 연결",     "비유) 110V ↔ 220V 변환기",   COLORS["green"]),
        ("Bridge",     "브리지",      "추상화와 구현을 분리하여 독립 확장", "비유) 리모컨 ↔ TV 모델 분리", COLORS["blue"]),
        ("Composite",  "컴포지트",    "개별 객체와 복합 객체를 동일 취급",   "비유) 파일 / 폴더 트리 구조", COLORS["yellow"]),
        ("Decorator",  "데코레이터",  "객체에 동적으로 새 기능 추가",        "비유) 옷을 겹쳐 입기 (포장지)", COLORS["orange"]),
        ("Facade",     "파사드",      "복잡한 서브시스템에 단순 인터페이스", "비유) 원스톱 창구",            COLORS["pink"]),
        ("Flyweight",  "플라이웨이트", "공유로 다수 유사 객체 효율 지원",    "비유) 바둑판 돌(공유 상태)",   COLORS["purple"]),
        ("Proxy",      "프록시",      "대리 객체로 실제 객체 접근 제어",     "비유) 대리인·경비원",          COLORS["red"]),
    ]
    # 4열 x 2행 (마지막 칸 비움) — Proxy는 첫 행 오른쪽 끝 강조 위치
    x0, y0 = 60, 180
    w, h, gx, gy = 285, 200, 15, 18
    positions = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1)]
    for (en, kr, desc, sim, color), (c, r) in zip(patterns, positions):
        x = x0 + c * (w + gx)
        y = y0 + r * (h + gy)
        els.append(rect(x, y, w, h, fill=color))
        els.append(text(x + 14, y + 12, en, size=20, align="left"))
        els.append(text(x + 14, y + 40, kr, size=14, align="left", color="#1864ab"))
        els.append(rect(x + 14, y + 70, w - 28, 66, fill="#ffffff"))
        els.append(text(x + 22, y + 80, desc, size=13, align="left"))
        els.append(text(x + 14, y + 146, sim, size=12, align="left", color="#c92a2a"))

    # 혼동 주의 박스 (3,1 위치)
    mx, my = 60 + 3 * (w + gx), y0 + 1 * (h + gy)
    els.append(rect(mx, my, w, h, fill=COLORS["gray"]))
    els.append(text(mx + 14, my + 12, "혼동 주의", size=18, align="left"))
    els.append(text(mx + 14, my + 42, "Iterator = 행위 패턴!", size=14, align="left", color="#c92a2a"))
    els.append(text(mx + 14, my + 66, "2024-2회 출제", size=12, align="left", color="#666"))
    els.append(text(mx + 14, my + 96, "빈출 Top 2", size=14, align="left", color="#1864ab"))
    els.append(text(mx + 14, my + 118, "• Adapter (2025-1)", size=12, align="left"))
    els.append(text(mx + 14, my + 136, "• Proxy (2025-2)", size=12, align="left"))
    els.append(text(mx + 14, my + 160, "구조 7개 = ABCDFFP", size=12, align="left", color="#c92a2a"))

    return els


# ---------------------------------------------------------------------------
# Card 5 — GoF 행위 패턴 11가지
# ---------------------------------------------------------------------------
def card_gof_behavioral() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "GoF 행위(Behavioral) 패턴 11가지",
                        "객체 간 책임·알고리즘 분배 · 통신 방식 · 상태 관리 (비중 최대)")
    els += badge(1080, 48, "🔥 매회 출제")

    # 상단 요약
    els.append(rect(60, 110, 1180, 44, fill=COLORS["yellow"]))
    els.append(text(80, 122, "GoF 3분류 중 가장 많은 11가지 — 빈출 Top 3: Iterator · Observer · Strategy",
                    size=14, align="left", color="#c92a2a"))

    patterns = [
        ("Chain of Resp.",   "책임 연쇄",        "요청 처리 가능 객체를 연쇄 탐색",  COLORS["green"]),
        ("Command",          "커맨드",          "요청을 객체로 캡슐화 · Undo/Redo", COLORS["blue"]),
        ("Interpreter",      "인터프리터",      "언어 문법을 클래스로 표현",         COLORS["yellow"]),
        ("Iterator",         "이터레이터",      "내부 노출 없이 순차 접근",          COLORS["orange"]),
        ("Mediator",         "중재자",          "객체 간 통신을 중재 객체가 담당",   COLORS["pink"]),
        ("Memento",          "메멘토",          "객체 상태 저장 · 이전 상태 복원",   COLORS["purple"]),
        ("Observer",         "옵저버",          "상태 변화 시 1:N 자동 통지",        COLORS["red"]),
        ("State",            "상태",            "상태에 따라 행동 변경",             COLORS["green"]),
        ("Strategy",         "전략",            "알고리즘 캡슐화 · 런타임 교체",     COLORS["blue"]),
        ("Template Method",  "템플릿 메서드",   "알고리즘 골격 상위 · 구현 하위",    COLORS["yellow"]),
        ("Visitor",          "방문자",          "구조와 연산 분리 · 이중 디스패치",  COLORS["orange"]),
    ]
    # 4열 x 3행 (마지막 한 칸 비움)
    x0, y0 = 60, 180
    w, h, gx, gy = 285, 140, 15, 15
    for i, (en, kr, desc, color) in enumerate(patterns):
        r = i // 4
        c = i % 4
        x = x0 + c * (w + gx)
        y = y0 + r * (h + gy)
        els.append(rect(x, y, w, h, fill=color))
        els.append(text(x + 12, y + 10, en, size=18, align="left"))
        els.append(text(x + 12, y + 36, kr, size=13, align="left", color="#1864ab"))
        els.append(rect(x + 12, y + 60, w - 24, 68, fill="#ffffff"))
        els.append(text(x + 20, y + 70, desc, size=12, align="left"))

    # 빈 자리(3,2)에 혼동/암기 박스
    bx = x0 + 3 * (w + gx)
    by = y0 + 2 * (h + gy)
    els.append(rect(bx, by, w, h, fill=COLORS["gray"]))
    els.append(text(bx + 12, by + 10, "혼동 주의", size=16, align="left"))
    els.append(text(bx + 12, by + 36, "Facade = 구조 패턴", size=13, align="left", color="#c92a2a"))
    els.append(text(bx + 12, by + 56, "Iterator = 행위 패턴", size=13, align="left", color="#c92a2a"))
    els.append(text(bx + 12, by + 84, "알고리즘 교체 → Strategy", size=12, align="left", color="#444"))
    els.append(text(bx + 12, by + 104, "상태 기반 행동 → State", size=12, align="left", color="#444"))

    # 하단 기출 포인트
    ly = 660
    els.append(rect(60, ly, 1180, 70, fill=COLORS["red"]))
    els.append(text(80, ly + 10, "기출 포인트", size=16, align="left"))
    els.append(text(80, ly + 36,
                    "• 2024-2회: Iterator 설명 빈칸  • 행위 11개 > 구조 7개 > 생성 5개 (총 23)  "
                    "• '행위 아닌 것' 고르는 문제 단골",
                    size=13, align="left", color="#c92a2a"))
    return els


# ---------------------------------------------------------------------------
# Card 6 — UML 다이어그램 종류 (구조 / 행위)
# ---------------------------------------------------------------------------
def card_uml_diagrams() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "UML 다이어그램 종류 (구조 / 행위)",
                        "UML 2.x — 구조: 정적 '무엇이 있는가' / 행위: 동적 '어떻게 동작하는가'")
    els += badge(1080, 48, "🔥 매회 출제")

    # 루트 노드 (상단 중앙)
    rx, ry, rw, rh = 500, 120, 280, 60
    els.append(rect(rx, ry, rw, rh, fill=COLORS["gray"]))
    els.append(text(rx + 40, ry + 18, "UML 2.x 다이어그램", size=20, align="left"))

    # 두 갈래 — 좌측(구조), 우측(행위) 중간 노드
    lx, ly, lw, lh = 200, 240, 320, 56
    els.append(rect(lx, ly, lw, lh, fill=COLORS["blue"]))
    els.append(text(lx + 16, ly + 8, "구조 (Structural) 다이어그램", size=17, align="left"))
    els.append(text(lx + 16, ly + 32, "정적 — 시스템의 구조 표현", size=12, align="left", color="#444"))

    rrx, rry = 760, 240
    els.append(rect(rrx, ry + 120, lw, lh, fill=COLORS["pink"]))
    els.append(text(rrx + 16, rry + 8, "행위 (Behavioral) 다이어그램", size=17, align="left"))
    els.append(text(rrx + 16, rry + 32, "동적 — 시스템의 동작·상호작용", size=12, align="left", color="#444"))

    # 루트 → 두 브랜치 화살표
    els += arrow(rx + rw / 2, ry + rh, lx + lw / 2, ly)
    els += arrow(rx + rw / 2, ry + rh, rrx + lw / 2, rry)

    # 좌측: 구조 6종
    structural = [
        ("클래스 (Class)",        "클래스의 속성·메서드·관계 표현"),
        ("객체 (Object)",         "클래스 인스턴스의 특정 시점 상태"),
        ("컴포넌트 (Component)",  "물리적 컴포넌트·의존 관계"),
        ("배치 (Deployment)",     "하드웨어 노드 위 SW 배치"),
        ("복합 구조 (Composite)", "클래스 내부 구조·협력 표현"),
        ("패키지 (Package)",      "요소를 그룹화하여 구조화"),
    ]
    sx, sy = 120, 320
    sw, sh, sgap = 480, 56, 8
    for i, (nm, desc) in enumerate(structural):
        y = sy + i * (sh + sgap)
        els.append(rect(sx, y, sw, sh, fill=COLORS["blue"]))
        els.append(text(sx + 14, y + 8, nm, size=15, align="left"))
        els.append(text(sx + 14, y + 32, desc, size=12, align="left", color="#444"))
        # 부모(구조 중간 노드) → 항목
        els += arrow(lx + lw / 2, ly + lh, sx + sw / 2, y)

    # 우측: 행위 7종
    behavioral = [
        ("유스케이스 (Use Case)",        "액터와 시스템 간 상호작용"),
        ("시퀀스 (Sequence)",            "시간 흐름에 따른 메시지 교환"),
        ("커뮤니케이션 (Communication)", "객체 간 메시지·관계 중심"),
        ("상태 (State)",                 "객체 상태 변화와 전이"),
        ("활동 (Activity)",              "업무/알고리즘 흐름 (순서도)"),
        ("타이밍 (Timing)",              "시간 축 위 상태 변화"),
        ("상호작용 개요 (Interaction Overview)", "상호작용 다이어그램 흐름 요약"),
    ]
    bx, by = 680, 320
    bw, bh = 560, 56
    for i, (nm, desc) in enumerate(behavioral):
        y = by + i * (bh + sgap)
        els.append(rect(bx, y, bw, bh, fill=COLORS["pink"]))
        els.append(text(bx + 14, y + 8, nm, size=15, align="left"))
        els.append(text(bx + 14, y + 32, desc, size=12, align="left", color="#444"))
        els += arrow(rrx + lw / 2, rry + lh, bx + bw / 2, y)

    # 하단 기출 포인트
    ky = 790
    els.append(rect(60, ky, 1180, 60, fill=COLORS["yellow"]))
    els.append(text(80, ky + 8, "기출 포인트 — '배치 다이어그램'을 행위로 혼동하는 경우 다수",
                    size=15, align="left", color="#c92a2a"))
    els.append(text(80, ky + 34,
                    "상호작용 다이어그램 = 시퀀스·커뮤니케이션·상호작용 개요·타이밍 (행위의 하위 분류)",
                    size=13, align="left", color="#444"))
    return els


CARDS = [
    ("se-cohesion-001.excalidraw",     card_cohesion),
    ("se-coupling-001.excalidraw",     card_coupling),
    ("se-design-001.excalidraw",       card_gof_creational),
    ("se-design-002.excalidraw",       card_gof_structural),
    ("se-design-003.excalidraw",       card_gof_behavioral),
    ("se-requirements-001.excalidraw", card_uml_diagrams),
]


def main() -> None:
    for name, builder in CARDS:
        els = builder()
        path = save(els, name)
        print(f"  ✓ {path.name}  ({len(els)} elements)")
    print(f"\n생성 완료: {len(CARDS)}개 → {OUT_DIR}")


if __name__ == "__main__":
    main()
