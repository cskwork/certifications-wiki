"""OS/MT 과목 priority-3 카드 3장의 Excalidraw 다이어그램 생성기.

실행: python3 gen_os.py
출력: ../os/*.excalidraw
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gen_db import COLORS, arrow, badge, rect, text, title_banner  # noqa: E402  # pyright: ignore[reportMissingImports]

OUT_DIR = Path(__file__).resolve().parent.parent / "os"
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
# Card 1 — CPU 스케줄링 알고리즘 (FCFS, SJF, SRT, RR, 우선순위)
# ---------------------------------------------------------------------------
def card_cpu_scheduling() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "CPU 스케줄링 알고리즘",
                        "FCFS · SJF · SRT · RR · 우선순위  (선점 vs 비선점)")
    els += badge(1080, 48, "🔥 매회 출제")

    # 선점/비선점 분류 박스 (상단)
    cy = 110
    els.append(rect(60, cy, 585, 56, fill=COLORS["blue"]))
    els.append(text(76, cy + 8, "선점 (Preemptive)", size=16, align="left", color="#1864ab"))
    els.append(text(76, cy + 32, "SRT · RR · 우선순위(선점형) · 다단계 큐",
                    size=13, align="left", color="#444"))
    els.append(rect(655, cy, 585, 56, fill=COLORS["pink"]))
    els.append(text(671, cy + 8, "비선점 (Non-preemptive)", size=16, align="left", color="#c92a2a"))
    els.append(text(671, cy + 32, "FCFS · SJF · HRN · 우선순위(비선점형)",
                    size=13, align="left", color="#444"))

    # 5개 알고리즘 카드 그리드 (1x5)
    algs = [
        ("FCFS", "First-Come First-Served", "비선점",
         "도착 순서대로 실행\n단순·기아 없음\n콘보이 효과 ↑", COLORS["gray"]),
        ("SJF", "Shortest Job First", "비선점",
         "짧은 버스트 우선\n최적 평균대기시간\n기아 발생 가능", COLORS["green"]),
        ("SRT", "Shortest Remaining", "선점",
         "남은 버스트 최단\nSJF의 선점 버전\n오버헤드 有", COLORS["yellow"]),
        ("RR", "Round Robin", "선점",
         "타임퀀텀 순환\n공평성 ↑\nTQ가 성능 좌우", COLORS["orange"]),
        ("우선순위", "Priority", "선점/비선점",
         "우선순위 번호 기준\n기아(Starvation)\n→ 에이징으로 해결", COLORS["purple"]),
    ]
    x0, y0 = 60, 180
    w, h, gap = 230, 170, 12
    for i, (name, eng, mode, desc, color) in enumerate(algs):
        x = x0 + i * (w + gap)
        els.append(rect(x, y0, w, h, fill=color))
        els.append(text(x + 14, y0 + 10, name, size=22, align="left"))
        els.append(text(x + 14, y0 + 40, eng, size=11, align="left", color="#555"))
        mode_color = "#1864ab" if "선점" in mode and "비" not in mode.split("/")[0] else "#c92a2a"
        els.append(rect(x + w - 96, y0 + 12, 82, 24, fill="#ffffff"))
        els.append(text(x + w - 90, y0 + 16, mode, size=11, align="left", color=mode_color))
        els.append(text(x + 14, y0 + 66, desc, size=12, align="left", color="#444"))

    # 예제 테이블 (프로세스 도착/버스트)
    ty = 370
    els.append(rect(60, ty, 400, 200, fill=COLORS["gray"]))
    els.append(text(76, ty + 10, "예제 프로세스", size=16, align="left"))
    els.append(text(76, ty + 34, "(도착시간=0 가정)", size=11, align="left", color="#555"))
    headers = ["프로세스", "버스트"]
    hx = [80, 240]
    hy = ty + 60
    for i, hh in enumerate(headers):
        els.append(rect(hx[i], hy, 150, 30, fill=COLORS["blue"]))
        els.append(text(hx[i] + 12, hy + 6, hh, size=14, align="left"))
    procs = [("P1", "6"), ("P2", "4"), ("P3", "2")]
    for r, (p, b) in enumerate(procs):
        ry = hy + 30 + r * 32
        els.append(rect(hx[0], ry, 150, 32, fill="#ffffff"))
        els.append(text(hx[0] + 14, ry + 8, p, size=14, align="left"))
        els.append(rect(hx[1], ry, 150, 32, fill="#ffffff"))
        els.append(text(hx[1] + 14, ry + 8, b, size=14, align="left"))

    # 간트 차트 3종
    gx = 480
    gy = ty
    els.append(rect(gx, gy, 760, 200, fill=COLORS["yellow"]))
    els.append(text(gx + 16, gy + 10, "간트 차트 (Gantt Chart) — 평균대기시간 계산", size=16, align="left"))

    def gantt(y_: int, label: str, blocks: list[tuple[str, int, str]], avg: str) -> None:
        els.append(text(gx + 16, y_, label, size=13, align="left", color="#c92a2a"))
        bx = gx + 100
        unit = 40  # px per time unit
        t = 0
        for name, dur, color in blocks:
            els.append(rect(bx + t * unit, y_ - 4, dur * unit, 28, fill=color))
            els.append(text(bx + t * unit + (dur * unit) / 2 - 8, y_ + 2, name, size=13))
            t += dur
        # end tick
        els.append(text(bx + t * unit + 4, y_ + 2, str(t), size=11, align="left", color="#555"))
        els.append(text(bx + 480, y_ + 2, avg, size=12, align="left", color="#1864ab"))

    gantt(gy + 50,
          "FCFS",
          [("P1", 6, "#ffffff"), ("P2", 4, "#ffffff"), ("P3", 2, "#ffffff")],
          "평균대기 (0+6+10)/3 = 5.33")
    gantt(gy + 100,
          "SJF",
          [("P3", 2, "#c3fae8"), ("P2", 4, "#c3fae8"), ("P1", 6, "#c3fae8")],
          "평균대기 (0+2+6)/3 = 2.67  ← 최적")
    gantt(gy + 150,
          "RR (TQ=2)",
          [("P1", 2, "#ffe8cc"), ("P2", 2, "#ffe8cc"), ("P3", 2, "#ffe8cc"),
           ("P1", 2, "#ffe8cc"), ("P2", 2, "#ffe8cc"), ("P1", 2, "#ffe8cc")],
          "평균반환 (12+10+6)/3 = 9.33")

    # 공식 박스 (하단)
    fy = 590
    els.append(rect(60, fy, 1180, 80, fill=COLORS["green"]))
    els.append(text(80, fy + 10, "핵심 공식 (암기 필수)", size=16, align="left"))
    els.append(text(80, fy + 36,
                    "• 반환시간 = 완료시간 − 도착시간     "
                    "• 대기시간 = 반환시간 − 버스트시간",
                    size=14, align="left", color="#1864ab"))
    els.append(text(80, fy + 56,
                    "• RR: TQ↑ → FCFS에 수렴, TQ↓ → 문맥교환 오버헤드 ↑  "
                    "• 기아 해결: 에이징(Aging)",
                    size=13, align="left", color="#c92a2a"))
    return els


# ---------------------------------------------------------------------------
# Card 2 — 소프트웨어 테스트 기법 (화이트박스 vs 블랙박스)
# ---------------------------------------------------------------------------
def card_testing_methods() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "소프트웨어 테스트 기법",
                        "화이트박스 (구조 기반) vs 블랙박스 (명세 기반)")
    els += badge(1080, 48, "🔥 매회 출제")

    # 상단 대비 슬로건
    sy = 110
    els.append(rect(60, sy, 585, 60, fill=COLORS["blue"]))
    els.append(text(76, sy + 10, "White Box — 코드 내부 보임", size=18, align="left", color="#1864ab"))
    els.append(text(76, sy + 36, "로직/경로/조건을 뜯어보며 테스트",
                    size=13, align="left", color="#444"))
    els.append(rect(655, sy, 585, 60, fill=COLORS["pink"]))
    els.append(text(671, sy + 10, "Black Box — 명세만 봄", size=18, align="left", color="#c92a2a"))
    els.append(text(671, sy + 36, "입력 → 출력만 검증, 내부 구조 무관",
                    size=13, align="left", color="#444"))

    # White box column
    wx, wy = 60, 190
    ww, wh = 585, 340
    els.append(rect(wx, wy, ww, wh, fill=COLORS["green"]))
    els.append(text(wx + 16, wy + 10, "화이트박스 기법 (구조적 · Structural)",
                    size=18, align="left"))
    els.append(text(wx + 16, wy + 38,
                    "소스 코드 내부 로직 기반 — 커버리지 측정이 핵심",
                    size=12, align="left", color="#555"))

    white_items = [
        ("구문 커버리지", "Statement", "모든 문장 1회 실행"),
        ("분기 커버리지", "Branch/Decision", "T/F 분기 모두 실행"),
        ("조건 커버리지", "Condition", "개별 조건 T/F 실행"),
        ("조건/결정 커버리지", "Condition/Decision", "분기+조건 동시 만족"),
        ("MC/DC", "Modified C/D", "조건의 독립적 영향"),
        ("경로 커버리지", "Path", "모든 경로 실행 (최강)"),
        ("기초 경로 검사", "Basis Path", "McCabe 순환복잡도"),
        ("제어 흐름", "Control Flow", "제어구조 기반"),
        ("데이터 흐름", "Data Flow", "변수 정의-사용"),
        ("루프 테스트", "Loop Testing", "반복문 경계 검사"),
    ]
    for i, (kor, eng, desc) in enumerate(white_items):
        r = i // 2
        c = i % 2
        bx = wx + 14 + c * 282
        by = wy + 70 + r * 52
        els.append(rect(bx, by, 274, 46, fill="#ffffff"))
        els.append(text(bx + 10, by + 4, kor, size=13, align="left"))
        els.append(text(bx + 10, by + 22, eng, size=10, align="left", color="#1864ab"))
        els.append(text(bx + 128, by + 24, desc, size=10, align="left", color="#555"))

    # Black box column
    bx0, by0 = 655, 190
    bw, bh = 585, 340
    els.append(rect(bx0, by0, bw, bh, fill=COLORS["yellow"]))
    els.append(text(bx0 + 16, by0 + 10, "블랙박스 기법 (기능적 · Functional)",
                    size=18, align="left"))
    els.append(text(bx0 + 16, by0 + 38,
                    "외부 명세/요구사항 기반 — 내부 구조 무관",
                    size=12, align="left", color="#555"))

    black_items = [
        ("동치 분할", "Equivalence Part.", "유효/무효 클래스 분할"),
        ("경계값 분석", "Boundary Value", "경계 부근 값 테스트"),
        ("원인-결과", "Cause-Effect", "입력-출력 그래프화"),
        ("의사결정 테이블", "Decision Table", "조건 조합 표"),
        ("상태 전이", "State Transition", "상태 변화 검사"),
        ("유스케이스", "Use Case", "시나리오 기반"),
        ("오류 추정", "Error Guessing", "경험적 예측 (경험기반)"),
        ("비교 테스트", "Comparison", "같은 입력 다른 구현"),
        ("분류 트리", "Classification", "입력을 트리로 분류"),
        ("페어와이즈", "Pairwise", "조합 최소화"),
    ]
    for i, (kor, eng, desc) in enumerate(black_items):
        r = i // 2
        c = i % 2
        bbx = bx0 + 14 + c * 282
        bby = by0 + 70 + r * 52
        els.append(rect(bbx, bby, 274, 46, fill="#ffffff"))
        els.append(text(bbx + 10, bby + 4, kor, size=13, align="left"))
        els.append(text(bbx + 10, bby + 22, eng, size=10, align="left", color="#c92a2a"))
        els.append(text(bbx + 128, bby + 24, desc, size=10, align="left", color="#555"))

    # 하단 V&V 박스
    vy = 550
    els.append(rect(60, vy, 1180, 120, fill=COLORS["purple"]))
    els.append(text(80, vy + 10, "검증(Verification) vs 확인(Validation) — 빈칸 단골",
                    size=16, align="left"))
    els.append(text(80, vy + 42, "Verification — \"올바르게 만들고 있는가?\"",
                    size=14, align="left", color="#1864ab"))
    els.append(text(80, vy + 62, "  개발 과정 · 명세 대로 구현되고 있는지 · 개발자 관점",
                    size=12, align="left", color="#555"))
    els.append(text(640, vy + 42, "Validation — \"올바른 것을 만들었는가?\"",
                    size=14, align="left", color="#c92a2a"))
    els.append(text(640, vy + 62, "  완성품 · 사용자 요구를 충족하는지 · 사용자 관점",
                    size=12, align="left", color="#555"))
    els.append(text(80, vy + 90,
                    "기출: '동치 분할·경계값 = 블랙박스', '구문·분기·조건·경로 = 화이트박스' 분류 매회 출제",
                    size=13, align="left", color="#c92a2a"))
    return els


# ---------------------------------------------------------------------------
# Card 3 — 테스트 커버리지 (문장·분기·조건·MC/DC·경로)
# ---------------------------------------------------------------------------
def card_test_coverage() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "테스트 커버리지 강도",
                        "문장 < 분기 < 조건 < MC/DC < 경로  (약 → 강)")
    els += badge(1080, 48, "🔥 매회 출제")

    # 계층 포함 다이어그램 — 중첩된 직사각형
    hx, hy = 60, 120
    levels = [
        ("경로 Path",     "모든 실행 경로",       COLORS["purple"], 5),
        ("MC/DC",         "조건의 독립적 영향",   COLORS["pink"],   4),
        ("조건 Condition","개별 조건 T/F",        COLORS["orange"], 3),
        ("분기 Decision", "T/F 분기 모두",        COLORS["yellow"], 2),
        ("문장 Statement","모든 문장 1회",        COLORS["green"],  1),
    ]
    base_w, base_h = 560, 420
    for i, (name, desc, color, strength) in enumerate(levels):
        shrink = i * 36
        x = hx + shrink
        y = hy + shrink
        w = base_w - shrink * 2
        h = base_h - shrink * 2
        els.append(rect(x, y, w, h, fill=color))
        els.append(text(x + 12, y + 8, name, size=15, align="left"))
        els.append(text(x + w - 100, y + 8, f"강도 {strength}",
                        size=11, align="left", color="#555"))

    # 중앙 라벨 설명
    els.append(text(hx + 140, hy + 240, "바깥쪽이 더 강한 커버리지\n(더 많은 테스트 필요)",
                    size=12, align="left", color="#444"))

    # 우측 상세 카드들
    rx = 650
    ry = 120
    cards = [
        ("문장 Statement", COLORS["green"],
         "모든 실행 가능 문장을\n최소 1회 실행",
         "if (a>0) x=1; → a=1 만으로 OK"),
        ("분기 Decision/Branch", COLORS["yellow"],
         "모든 조건문의 T/F 분기를\n모두 실행",
         "if(a&&b) → 전체식 T/F 각 1회"),
        ("조건 Condition", COLORS["orange"],
         "개별 Boolean 조건 각각이\nT/F를 모두 취함",
         "if(a&&b) → a=T,a=F / b=T,b=F"),
        ("MC/DC", COLORS["pink"],
         "각 조건이 독립적으로\n결정 결과에 영향",
         "항공 SW 표준 (DO-178C)"),
        ("경로 Path", COLORS["purple"],
         "모든 실행 경로를 실행\n(가장 강력)",
         "경우의 수 폭발 → 실현 곤란"),
    ]
    card_w, card_h, gap = 590, 76, 8
    for i, (name, color, desc, ex) in enumerate(cards):
        y = ry + i * (card_h + gap)
        els.append(rect(rx, y, card_w, card_h, fill=color))
        els.append(text(rx + 14, y + 8, name, size=16, align="left"))
        els.append(text(rx + 14, y + 32, desc, size=12, align="left", color="#444"))
        els.append(text(rx + 300, y + 32, "예: " + ex, size=11, align="left", color="#c92a2a"))

    # 하단 강도 화살표 + 기출 포인트
    ay = 560
    els.append(rect(60, ay, 1180, 50, fill=COLORS["gray"]))
    els.append(text(76, ay + 14, "약함", size=14, align="left", color="#555"))
    els += arrow(140, ay + 24, 1180, ay + 24)
    els.append(text(1180, ay + 14, "강함", size=14, align="left", color="#c92a2a"))
    # 단계 라벨 on arrow
    steps = ["문장", "분기", "조건", "조건/결정", "MC/DC", "경로"]
    for i, st in enumerate(steps):
        sx = 200 + i * 170
        els.append(rect(sx, ay + 8, 140, 32, fill="#ffffff"))
        els.append(text(sx + 14, ay + 14, st, size=13, align="left"))

    # 기출 포인트
    ky = 625
    els.append(rect(60, ky, 1180, 80, fill=COLORS["yellow"]))
    els.append(text(80, ky + 8, "기출 포인트", size=16, align="left"))
    els.append(text(80, ky + 32,
                    "• 2025-2회: if(A&&B) 분기 vs 조건 커버리지 최소 테스트 케이스 비교",
                    size=12, align="left", color="#c92a2a"))
    els.append(text(80, ky + 52,
                    "• 분기 = 전체식 T/F   조건 = 개별 T/F (분기 미보장 가능)   "
                    "• MC/DC = 분기+조건+독립성",
                    size=12, align="left", color="#c92a2a"))
    return els


CARDS = [
    ("mt-scheduling-001.excalidraw", card_cpu_scheduling),
    ("mt-testing-001.excalidraw",    card_testing_methods),
    ("mt-testing-003.excalidraw",    card_test_coverage),
]


def main() -> None:
    for name, builder in CARDS:
        els = builder()
        path = save(els, name)
        print(f"  ✓ {path.name}  ({len(els)} elements)")
    print(f"\n생성 완료: {len(CARDS)}개 → {OUT_DIR}")


if __name__ == "__main__":
    main()
