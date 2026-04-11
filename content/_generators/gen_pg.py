"""PG 과목 priority-3 카드 11장의 Excalidraw 다이어그램 생성기.

실행: python3 gen_pg.py
출력: ../pg/*.excalidraw
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gen_db import COLORS, arrow, badge, line, rect, text, title_banner  # noqa: E402  # pyright: ignore[reportMissingImports]

OUT_DIR = Path(__file__).resolve().parent.parent / "pg"
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
# Card 1 — 연결 리스트
# ---------------------------------------------------------------------------
def card_linked_list() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "연결 리스트 (Linked List)",
                        "노드 = data + next · 동적 할당 · 삽입/삭제 O(1)")
    els += badge(1080, 48, "🔥 매회 출제")

    # 단일 연결 리스트 노드 체인
    els.append(text(60, 120, "단일 연결 리스트 (Singly)", size=16, align="left", color="#1864ab"))
    x, y = 60, 150
    nw, nh = 110, 60
    data_vals = ["3", "1", "4", "2"]
    for i, val in enumerate(data_vals):
        nx = x + i * (nw + 40)
        els.append(rect(nx, y, nw, nh, fill=COLORS["blue"]))
        els.append(line(nx + nw * 0.6, y, nx + nw * 0.6, y + nh))
        els.append(text(nx + 18, y + 18, val, size=20, align="left"))
        els.append(text(nx + nw * 0.6 + 8, y + 22, "next", size=11, align="left", color="#555"))
        if i < len(data_vals) - 1:
            els += arrow(nx + nw, y + nh / 2, nx + nw + 40, y + nh / 2)
        else:
            els += arrow(nx + nw, y + nh / 2, nx + nw + 40, y + nh / 2)
            els.append(text(nx + nw + 44, y + 18, "NULL", size=14, align="left", color="#c92a2a"))
    els.append(text(20, y + 18, "head→", size=14, align="left", color="#2b8a3e"))

    # 이중 연결 리스트
    els.append(text(60, 240, "이중 연결 리스트 (Doubly)", size=16, align="left", color="#862e9c"))
    y2 = 270
    dvals = ["A", "B", "C"]
    dnw = 140
    for i, val in enumerate(dvals):
        nx = x + i * (dnw + 40)
        els.append(rect(nx, y2, dnw, nh, fill=COLORS["purple"]))
        els.append(line(nx + 40, y2, nx + 40, y2 + nh))
        els.append(line(nx + 96, y2, nx + 96, y2 + nh))
        els.append(text(nx + 6, y2 + 22, "prev", size=10, align="left", color="#555"))
        els.append(text(nx + 54, y2 + 18, val, size=20, align="left"))
        els.append(text(nx + 102, y2 + 22, "next", size=10, align="left", color="#555"))
        if i < len(dvals) - 1:
            els += arrow(nx + dnw, y2 + nh / 2 - 8, nx + dnw + 40, y2 + nh / 2 - 8)
            els += arrow(nx + dnw + 40, y2 + nh / 2 + 10, nx + dnw, y2 + nh / 2 + 10)

    # 원형 연결 리스트
    els.append(text(60, 360, "원형 연결 리스트 (Circular)", size=16, align="left", color="#c92a2a"))
    y3 = 390
    cvals = ["1", "2", "3"]
    cnw = 110
    for i, val in enumerate(cvals):
        nx = x + i * (cnw + 40)
        els.append(rect(nx, y3, cnw, nh, fill=COLORS["pink"]))
        els.append(line(nx + 66, y3, nx + 66, y3 + nh))
        els.append(text(nx + 18, y3 + 18, val, size=20, align="left"))
        if i < len(cvals) - 1:
            els += arrow(nx + cnw, y3 + nh / 2, nx + cnw + 40, y3 + nh / 2)
    # 마지막 → 첫 노드로 돌아감
    last_x = x + (len(cvals) - 1) * (cnw + 40) + cnw
    els += arrow(last_x + 20, y3 + nh + 6, x + cnw / 2, y3 + nh + 6)
    els += arrow(last_x + 20, y3 + nh + 6, last_x + 20, y3 + nh / 2)
    els += arrow(x + cnw / 2, y3 + nh + 6, x + cnw / 2, y3 + nh)
    els.append(text(last_x + 30, y3 + nh + 14, "tail.next → head", size=11, align="left", color="#555"))

    # C 코드 블록
    cx, cy = 720, 120
    els.append(rect(cx, cy, 520, 240, fill=COLORS["yellow"]))
    els.append(text(cx + 14, cy + 10, "C 노드 구조 & 순회", size=18, align="left"))
    els.append(text(cx + 14, cy + 40,
                    "typedef struct Node {\n"
                    "    int data;\n"
                    "    struct Node *next;\n"
                    "} Node;\n\n"
                    "Node *p = head;\n"
                    "while (p != NULL) {\n"
                    "    printf(\"%d \", p->data);\n"
                    "    p = p->next;\n"
                    "}",
                    size=13, align="left"))

    # 배열 vs 연결리스트 비교표
    tx, ty = 720, 380
    els.append(rect(tx, ty, 520, 220, fill=COLORS["green"]))
    els.append(text(tx + 14, ty + 10, "배열 vs 연결 리스트", size=18, align="left"))
    headers = ["구분", "배열", "연결 리스트"]
    hw = [120, 180, 200]
    hx = tx + 14
    hy = ty + 44
    for i, h in enumerate(headers):
        els.append(rect(hx + sum(hw[:i]), hy, hw[i], 30, fill="#ffffff"))
        els.append(text(hx + sum(hw[:i]) + 8, hy + 6, h, size=13, align="left"))
    rows = [
        ("메모리",     "연속",           "불연속(동적)"),
        ("임의 접근",  "O(1)",           "O(n)"),
        ("삽입/삭제",  "O(n) 이동 필요", "O(1) 포인터만"),
        ("크기",       "고정",           "동적"),
    ]
    for r, row in enumerate(rows):
        ry = hy + 30 + r * 32
        for i, v in enumerate(row):
            els.append(rect(hx + sum(hw[:i]), ry, hw[i], 32, fill="#ffffff"))
            els.append(text(hx + sum(hw[:i]) + 8, ry + 8, v, size=12, align="left"))

    # 기출 포인트
    py = 620
    els.append(rect(60, py, 1180, 70, fill=COLORS["red"]))
    els.append(text(80, py + 10, "기출 포인트", size=16, align="left"))
    els.append(text(80, py + 38,
                    "• 2025-1회: 순회 코드 → 출력 35421   • 2025-2회: 삽입 후 순회 → 3 1 2   "
                    "• p->data == (*p).data",
                    size=13, align="left", color="#c92a2a"))
    return els


# ---------------------------------------------------------------------------
# Card 2 — C언어 포인터 기초
# ---------------------------------------------------------------------------
def card_c_pointer() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "C언어 포인터 기초",
                        "주소 연산자(&) · 역참조 연산자(*) · 메모리 모델")
    els += badge(1080, 48, "🔥 매회 출제")

    # 메모리 다이어그램: a 변수 + p 포인터
    els.append(text(60, 120, "메모리 다이어그램  —  int a = 10; int *p = &a;",
                    size=16, align="left", color="#1864ab"))

    # 테이블: 변수명 | 주소 | 값
    tx, ty = 60, 150
    col_w = [130, 170, 140]
    col_h = 44
    headers = ["변수명", "주소", "값"]
    for i, h in enumerate(headers):
        els.append(rect(tx + sum(col_w[:i]), ty, col_w[i], col_h, fill=COLORS["blue"]))
        els.append(text(tx + sum(col_w[:i]) + 14, ty + 12, h, size=15, align="left"))
    rows = [
        ("a",  "0x1000", "10"),
        ("p",  "0x2000", "0x1000"),
    ]
    for r, row in enumerate(rows):
        ry = ty + col_h + r * col_h
        fill = COLORS["yellow"] if r == 0 else COLORS["green"]
        for i, v in enumerate(row):
            els.append(rect(tx + sum(col_w[:i]), ry, col_w[i], col_h, fill=fill))
            els.append(text(tx + sum(col_w[:i]) + 14, ry + 12, v, size=15, align="left"))

    # p가 a를 가리키는 화살표
    els += arrow(tx + 450, ty + col_h + col_h + col_h / 2,
                 tx + 200, ty + col_h + col_h / 2, label="참조")

    # 연산자 설명 박스
    ox, oy = 520, 120
    els.append(rect(ox, oy, 720, 280, fill=COLORS["gray"]))
    els.append(text(ox + 14, oy + 10, "포인터 연산자 정리", size=18, align="left"))
    ops = [
        ("int *p;",   "정수형 포인터 변수 선언"),
        ("&a",        "변수 a의 주소 (주소 연산자)"),
        ("*p",        "p가 가리키는 값 (역참조)"),
        ("p = &a;",   "a의 주소를 p에 저장"),
        ("*p = 20;",  "p가 가리키는 곳에 20 저장 → a == 20"),
        ("**pp",      "이중 포인터 역참조 (pp→p→값)"),
        ("NULL",      "아무것도 가리키지 않음 (사용 금지)"),
        ("arr[i]",    "*(arr + i) 와 동일"),
    ]
    for i, (op, desc) in enumerate(ops):
        r = i // 2
        c = i % 2
        rx = ox + 14 + c * 350
        ry = oy + 46 + r * 58
        els.append(rect(rx, ry, 330, 50, fill="#ffffff"))
        els.append(text(rx + 10, ry + 6, op, size=14, align="left", color="#c92a2a"))
        els.append(text(rx + 10, ry + 28, desc, size=12, align="left", color="#444"))

    # Swap 예제
    sx, sy = 60, 430
    els.append(rect(sx, sy, 580, 240, fill=COLORS["yellow"]))
    els.append(text(sx + 14, sy + 10, "빈출: 포인터 swap 예제", size=18, align="left"))
    els.append(text(sx + 14, sy + 42,
                    "void swap(int *a, int *b) {\n"
                    "    int tmp = *a;\n"
                    "    *a = *b;\n"
                    "    *b = tmp;\n"
                    "}\n"
                    "int main() {\n"
                    "    int x = 1, y = 2;\n"
                    "    swap(&x, &y);\n"
                    "    printf(\"%d %d\", x, y); // 2 1\n"
                    "}",
                    size=13, align="left"))

    # 포인터와 배열
    bx, by = 660, 430
    els.append(rect(bx, by, 580, 240, fill=COLORS["green"]))
    els.append(text(bx + 14, by + 10, "포인터 ↔ 배열 관계", size=18, align="left"))
    els.append(text(bx + 14, by + 42,
                    "int a[] = {10, 20, 30, 40};\n"
                    "int *p = a;       // 배열명 = 첫 원소 주소\n"
                    "*(p + 2)   ==  a[2]   // 30\n"
                    "p[3]       ==  a[3]   // 40\n\n"
                    "주의:\n"
                    "• 초기화 안 한 포인터 사용 금지\n"
                    "• NULL 포인터 역참조 → 세그폴트\n"
                    "• 포인터 + n = n × sizeof(type) 이동",
                    size=13, align="left"))
    return els


# ---------------------------------------------------------------------------
# Card 3 — Java 상속과 오버라이딩
# ---------------------------------------------------------------------------
def card_java_inheritance() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "Java 상속과 오버라이딩",
                        "extends · @Override · super · 동적/정적 바인딩")
    els += badge(1080, 48, "🔥 매회 출제")

    # UML 상속 다이어그램
    px, py = 100, 140
    pw, ph = 260, 160
    els.append(rect(px, py, pw, ph, fill=COLORS["blue"]))
    els.append(text(px + 10, py + 10, "Animal (부모)", size=16, align="left"))
    els.append(line(px, py + 36, px + pw, py + 36))
    els.append(text(px + 10, py + 44, "+ String sound()", size=13, align="left"))
    els.append(text(px + 10, py + 66, "+ void speak()", size=13, align="left"))
    els.append(text(px + 10, py + 96, "sound() { \"...\" }", size=12, align="left", color="#555"))
    els.append(text(px + 10, py + 116,
                    "speak() {\n  print(sound());\n}", size=12, align="left", color="#555"))

    cx, cy = 100, 340
    els.append(rect(cx, cy, pw, 130, fill=COLORS["green"]))
    els.append(text(cx + 10, cy + 10, "Dog extends Animal", size=16, align="left"))
    els.append(line(cx, cy + 36, cx + pw, cy + 36))
    els.append(text(cx + 10, cy + 44, "@Override", size=12, align="left", color="#c92a2a"))
    els.append(text(cx + 10, cy + 64, "+ String sound()", size=13, align="left"))
    els.append(text(cx + 10, cy + 88,
                    "sound() { \"멍멍\" }", size=12, align="left", color="#555"))

    # extends 화살표 (자식 → 부모)
    els += arrow(cx + pw / 2, cy, px + pw / 2, py + ph)
    els.append(text(cx + pw / 2 + 10, cy - 26, "extends", size=13, align="left", color="#1864ab"))

    # 오버라이딩 규칙 박스
    rx, ry = 420, 140
    els.append(rect(rx, ry, 820, 200, fill=COLORS["yellow"]))
    els.append(text(rx + 14, ry + 10, "오버라이딩 4대 규칙", size=18, align="left"))
    rules = [
        ("1. 시그니처 동일", "메서드명 · 파라미터 · 반환형 일치"),
        ("2. 접근제한 강화 불가", "부모 public → 자식 private 불가"),
        ("3. 예외 강화 불가", "부모보다 큰 checked 예외 throws 불가"),
        ("4. static/final/private X", "인스턴스 메서드만 오버라이딩"),
    ]
    for i, (name, desc) in enumerate(rules):
        r = i // 2
        c = i % 2
        bx = rx + 14 + c * 400
        by = ry + 42 + r * 74
        els.append(rect(bx, by, 385, 66, fill="#ffffff"))
        els.append(text(bx + 10, by + 8, name, size=14, align="left", color="#c92a2a"))
        els.append(text(bx + 10, by + 32, desc, size=12, align="left", color="#444"))

    # 바인딩 코드 예제
    bx2, by2 = 420, 360
    els.append(rect(bx2, by2, 820, 310, fill=COLORS["green"]))
    els.append(text(bx2 + 14, by2 + 10, "동적 바인딩 vs 정적 바인딩 (시험 단골)",
                    size=18, align="left"))
    els.append(text(bx2 + 14, by2 + 46,
                    "Animal a = new Dog();\n"
                    "a.speak();      // → sound() 호출 시 Dog의 sound()\n"
                    "                //   = \"멍멍\" (동적 바인딩)\n\n"
                    "• instance method → 실제 객체 타입 (Dog) 기준\n"
                    "• static method → 참조 변수 타입 (Animal) 기준\n"
                    "• field        → 참조 변수 타입 기준",
                    size=13, align="left"))
    els.append(rect(bx2 + 14, by2 + 200, 790, 96, fill="#ffffff"))
    els.append(text(bx2 + 24, by2 + 208,
                    "생성자 호출 순서: 부모 → 자식 (super() 자동 삽입)\n"
                    "extends (클래스 상속, 단일) ≠ implements (인터페이스, 다중)\n"
                    "super.method() = 부모의 원본 메서드 명시 호출",
                    size=12, align="left", color="#1864ab"))

    # 하단 C 카드
    sy = 690
    els.append(rect(60, sy, 1180, 0, fill=COLORS["gray"]))
    return els


# ---------------------------------------------------------------------------
# Card 4 — Python 핵심 문법
# ---------------------------------------------------------------------------
def card_python_basics() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "Python 핵심 문법",
                        "들여쓰기 · 동적 타이핑 · 슬라이싱 · 컴프리헨션 · 집합")
    els += badge(1080, 48, "🔥 매회 출제")

    # 상단 6개 카드
    items = [
        ("들여쓰기",     "블록을 중괄호 대신\n공백 4칸으로 구분",    COLORS["blue"]),
        ("동적 타이핑",  "x = 1  → int\nx = 'a' → str (재할당 가능)", COLORS["green"]),
        ("조건문",       "if / elif / else\n:(콜론) + 들여쓰기",      COLORS["yellow"]),
        ("반복문",       "for x in iter:\nwhile 조건:",               COLORS["pink"]),
        ("함수",         "def name(a, b):\n    return a + b",         COLORS["orange"]),
        ("입출력",       "print(x)\ninput() (항상 str)",               COLORS["purple"]),
    ]
    x0, y0 = 60, 130
    w, h, gx = 190, 120, 10
    for i, (t, d, c) in enumerate(items):
        x = x0 + i * (w + gx)
        els.append(rect(x, y0, w, h, fill=c))
        els.append(text(x + 12, y0 + 10, t, size=16, align="left"))
        els.append(text(x + 12, y0 + 38, d, size=12, align="left", color="#444"))

    # 컬렉션 4종
    els.append(text(60, 270, "컬렉션 4종", size=18, align="left", color="#1864ab"))
    cols = [
        ("list",  "[1, 2, 3]",     "순서 O · 가변 · 중복 O",  COLORS["blue"]),
        ("tuple", "(1, 2, 3)",     "순서 O · 불변 · 중복 O",  COLORS["green"]),
        ("dict",  "{'a': 1}",      "키-값 · 가변 · 키 유일",  COLORS["yellow"]),
        ("set",   "{1, 2, 3}",     "순서 X · 가변 · 중복 X",  COLORS["pink"]),
    ]
    for i, (name, syn, desc, c) in enumerate(cols):
        x = 60 + i * 300
        y = 300
        els.append(rect(x, y, 290, 90, fill=c))
        els.append(text(x + 12, y + 8, name, size=18, align="left", color="#c92a2a"))
        els.append(text(x + 12, y + 34, syn, size=14, align="left"))
        els.append(text(x + 12, y + 58, desc, size=12, align="left", color="#444"))

    # 슬라이싱 예제
    sx, sy = 60, 410
    els.append(rect(sx, sy, 580, 260, fill=COLORS["yellow"]))
    els.append(text(sx + 14, sy + 10, "슬라이싱 [start:end:step]",
                    size=18, align="left"))
    els.append(text(sx + 14, sy + 42,
                    "s = \"abcdefg\"\n"
                    "s[2:5]    → 'cde'    (end 미포함)\n"
                    "s[::2]    → 'aceg'   (step=2)\n"
                    "s[::-1]   → 'gfedcba' (역순)\n"
                    "s[-3:]    → 'efg'    (뒤에서 3개)\n\n"
                    "lst = [10, 20, 30, 40, 50]\n"
                    "lst[1:4]  → [20, 30, 40]",
                    size=13, align="left"))

    # 컴프리헨션 & 집합연산
    cx, cy = 660, 410
    els.append(rect(cx, cy, 580, 260, fill=COLORS["green"]))
    els.append(text(cx + 14, cy + 10, "컴프리헨션 & 집합 연산",
                    size=18, align="left"))
    els.append(text(cx + 14, cy + 42,
                    "# 딕셔너리 컴프리헨션 (2025-2회 출제)\n"
                    "data = {'a':1,'b':2,'c':3,'d':4}\n"
                    "{k:v for k,v in data.items() if v%2==0}\n"
                    "→ {'b': 2, 'd': 4}\n\n"
                    "# 집합 연산\n"
                    "a = {1,2,3,4}; b = {3,4,5,6}\n"
                    "a & b → {3,4}   (교집합)\n"
                    "a | b → {1..6}  (합집합)\n"
                    "a - b → {1,2}   (차집합)",
                    size=13, align="left"))
    return els


# ---------------------------------------------------------------------------
# Card 5 — C 배열과 반복문
# ---------------------------------------------------------------------------
def card_c_array_loop() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "C언어 배열과 반복문",
                        "1차원·2차원 배열 · for 루프 · 버블 정렬 트레이싱")
    els += badge(1080, 48, "🔥 매회 출제")

    # 1차원 배열 메모리
    els.append(text(60, 120, "1차원 배열  int a[5] = {3, 1, 4, 1, 5};",
                    size=16, align="left", color="#1864ab"))
    ax, ay = 60, 150
    vals = ["3", "1", "4", "1", "5"]
    cell = 80
    for i, v in enumerate(vals):
        x = ax + i * cell
        els.append(rect(x, ay, cell, 56, fill=COLORS["blue"]))
        els.append(text(x + 28, ay + 14, v, size=22, align="left"))
        els.append(text(x + 22, ay + 62, f"a[{i}]", size=12, align="left", color="#555"))

    # 2차원 배열
    els.append(text(60, 250, "2차원 배열  int a[2][3] = {{1,2,3},{4,5,6}};",
                    size=16, align="left", color="#862e9c"))
    grid2 = [[1, 2, 3], [4, 5, 6]]
    bx, by = 60, 280
    cw = 70
    for r in range(2):
        for c in range(3):
            els.append(rect(bx + c * cw, by + r * cw, cw, cw, fill=COLORS["purple"]))
            els.append(text(bx + c * cw + 28, by + r * cw + 20, str(grid2[r][c]), size=20, align="left"))
            els.append(text(bx + c * cw + 4, by + r * cw + 4, f"[{r}][{c}]", size=10, align="left", color="#555"))
    els.append(text(bx + 3 * cw + 30, by + 40,
                    "a[1][2] → 6\n행·열 순서 주의",
                    size=13, align="left", color="#444"))

    # for 루프 3요소
    fx, fy = 680, 120
    els.append(rect(fx, fy, 560, 160, fill=COLORS["yellow"]))
    els.append(text(fx + 14, fy + 10, "for 루프 3요소", size=18, align="left"))
    els.append(text(fx + 14, fy + 42,
                    "for ( 초기화 ; 조건 ; 증감 ) { 본문 }",
                    size=14, align="left", color="#c92a2a"))
    els.append(text(fx + 14, fy + 72,
                    "for (int i = 0; i < 5; i++) {\n"
                    "    sum += a[i];     // 배열 순회\n"
                    "}",
                    size=13, align="left"))

    # 버블 정렬 트레이싱
    tx, ty = 680, 300
    els.append(rect(tx, ty, 560, 370, fill=COLORS["green"]))
    els.append(text(tx + 14, ty + 10, "버블 정렬 트레이싱 (빈출)",
                    size=18, align="left"))
    els.append(text(tx + 14, ty + 42,
                    "int a[] = {3,1,4,1,5};\n"
                    "for (i=0; i<4; i++)\n"
                    "  for (j=0; j<4-i; j++)\n"
                    "    if (a[j] > a[j+1]) swap;",
                    size=13, align="left"))
    steps = [
        "i=0: {1, 3, 1, 4, 5}",
        "i=1: {1, 1, 3, 4, 5}",
        "i=2: {1, 1, 3, 4, 5}",
        "i=3: {1, 1, 3, 4, 5}",
        "→ a[0]=1, a[2]=3, a[4]=5",
    ]
    for i, s in enumerate(steps):
        color = "#c92a2a" if i == len(steps) - 1 else "#1864ab"
        els.append(text(tx + 14, ty + 150 + i * 28, s, size=14, align="left", color=color))

    # 하단: 배열-포인터 관계 & swap
    sx, sy = 60, 460
    els.append(rect(sx, sy, 580, 210, fill=COLORS["orange"]))
    els.append(text(sx + 14, sy + 10, "배열 ↔ 포인터 & swap", size=18, align="left"))
    els.append(text(sx + 14, sy + 42,
                    "int a[] = {10,20,30,40};\n"
                    "int *p = a;          // 배열명 = 첫 원소 주소\n"
                    "*(p+2) == a[2]       // 30\n\n"
                    "// swap 패턴 (기출)\n"
                    "tmp = a[i];\n"
                    "a[i] = a[j];\n"
                    "a[j] = tmp;",
                    size=13, align="left"))
    return els


# ---------------------------------------------------------------------------
# Card 6 — C 재귀 함수
# ---------------------------------------------------------------------------
def card_c_recursion() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "C언어 재귀 함수",
                        "종료 조건(Base) + 재귀식(Recursive) · 호출 스택")
    els += badge(1080, 48, "🔥 매회 출제")

    # factorial 정의
    fx, fy = 60, 130
    els.append(rect(fx, fy, 560, 220, fill=COLORS["yellow"]))
    els.append(text(fx + 14, fy + 10, "factorial(n) 정의", size=18, align="left"))
    els.append(text(fx + 14, fy + 44,
                    "int factorial(int n) {\n"
                    "    if (n <= 1) return 1;   // 종료 조건\n"
                    "    return n * factorial(n-1); // 재귀식\n"
                    "}",
                    size=14, align="left"))
    els.append(rect(fx + 14, fy + 140, 540, 62, fill="#ffffff"))
    els.append(text(fx + 24, fy + 148, "핵심 2요소", size=14, align="left", color="#c92a2a"))
    els.append(text(fx + 24, fy + 170,
                    "① 종료 조건 (Base Case) — 없으면 무한 재귀 → 스택오버플로우\n"
                    "② 재귀식 (Recursive Case) — 문제를 더 작은 부분문제로",
                    size=11, align="left", color="#444"))

    # 호출 스택 시각화 factorial(3)
    sx, sy = 660, 130
    els.append(rect(sx, sy, 580, 420, fill=COLORS["blue"]))
    els.append(text(sx + 14, sy + 10, "호출 스택 시각화 — factorial(3)",
                    size=18, align="left"))
    stack = [
        ("factorial(3)", "return 3 * factorial(2)", "= 3 * 2 = 6"),
        ("factorial(2)", "return 2 * factorial(1)", "= 2 * 1 = 2"),
        ("factorial(1)", "return 1  (Base)",        "= 1"),
    ]
    fx2 = sx + 14
    fy2 = sy + 44
    for i, (call, body, ret) in enumerate(stack):
        y = fy2 + i * 110
        fill = COLORS["pink"] if i == len(stack) - 1 else "#ffffff"
        els.append(rect(fx2, y, 550, 100, fill=fill))
        els.append(text(fx2 + 12, y + 8, call, size=16, align="left", color="#c92a2a"))
        els.append(text(fx2 + 12, y + 34, body, size=13, align="left"))
        els.append(text(fx2 + 12, y + 60, ret, size=13, align="left", color="#1864ab"))
        if i < len(stack) - 1:
            els += arrow(fx2 + 275, y + 100, fx2 + 275, y + 110)
    els.append(text(sx + 14, sy + 380,
                    "쌓기 → 종료조건 만남 → 풀면서 반환 (LIFO)",
                    size=13, align="left", color="#c92a2a"))

    # 피보나치 트레이싱
    px, py = 60, 380
    els.append(rect(px, py, 560, 180, fill=COLORS["green"]))
    els.append(text(px + 14, py + 10, "피보나치  f(n)=f(n-1)+f(n-2)",
                    size=18, align="left"))
    els.append(text(px + 14, py + 42,
                    "int f(int n) {\n"
                    "    if (n < 2) return n;\n"
                    "    return f(n-1) + f(n-2);\n"
                    "}\n"
                    "f(6) = 8  (0,1,1,2,3,5,8)",
                    size=13, align="left"))

    # 재귀 vs 반복
    cx, cy = 60, 580
    els.append(rect(cx, cy, 1180, 90, fill=COLORS["orange"]))
    els.append(text(cx + 14, cy + 10, "재귀 vs 반복", size=18, align="left"))
    els.append(text(cx + 14, cy + 40,
                    "• 재귀: 코드 간결, 직관적 / 스택 메모리 ↑, 호출 오버헤드",
                    size=13, align="left"))
    els.append(text(cx + 14, cy + 62,
                    "• 반복: 메모리/성능 우수 / 트리·분할정복은 재귀가 더 자연스러움",
                    size=13, align="left"))
    return els


# ---------------------------------------------------------------------------
# Card 7 — C 진수 변환 & 비트 연산
# ---------------------------------------------------------------------------
def card_c_bitop() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "C언어 진수 변환과 비트 연산",
                        "2·8·10·16진수 · &, |, ^, ~, <<, >> · printf 서식")
    els += badge(1080, 48, "🔥 매회 출제")

    # 진수 변환 표
    tx, ty = 60, 130
    els.append(rect(tx, ty, 580, 300, fill=COLORS["blue"]))
    els.append(text(tx + 14, ty + 10, "진수 변환표", size=18, align="left"))
    headers = ["10", "2", "8", "16"]
    hw = 120
    for i, h in enumerate(headers):
        els.append(rect(tx + 20 + i * hw, ty + 44, hw - 10, 36, fill="#ffffff"))
        els.append(text(tx + 20 + i * hw + 10, ty + 50, h + "진수", size=14, align="left"))
    rows = [
        ("10", "1010",   "12",  "A"),
        ("15", "1111",   "17",  "F"),
        ("26", "11010",  "32",  "1A"),
        ("87", "1010111","127", "57"),
        ("255","11111111","377","FF"),
    ]
    for r, row in enumerate(rows):
        ry = ty + 80 + r * 40
        for i, v in enumerate(row):
            els.append(rect(tx + 20 + i * hw, ry, hw - 10, 40, fill=COLORS["yellow"] if r == 3 else "#ffffff"))
            els.append(text(tx + 20 + i * hw + 10, ry + 10, v, size=14, align="left"))

    # 변환 알고리즘 (87 → 16)
    ax, ay = 660, 130
    els.append(rect(ax, ay, 580, 300, fill=COLORS["green"]))
    els.append(text(ax + 14, ay + 10,
                    "10 → 16 변환 알고리즘 (빈출: 87→57)",
                    size=18, align="left"))
    els.append(text(ax + 14, ay + 46,
                    "87 ÷ 16 = 5 ... 7    → hex[0]='7'\n"
                    " 5 ÷ 16 = 0 ... 5    → hex[1]='5'\n"
                    "역순 출력 → \"57\"",
                    size=14, align="left"))
    els.append(text(ax + 14, ay + 140,
                    "while (n > 0) {\n"
                    "    int r = n % 16;\n"
                    "    if (r < 10) hex[i] = r + '0';\n"
                    "    else        hex[i] = r - 10 + 'A';\n"
                    "    n = n / 16;\n"
                    "    i++;\n"
                    "}",
                    size=13, align="left"))

    # 비트 연산자 표
    bx, by = 60, 450
    els.append(rect(bx, by, 720, 220, fill=COLORS["yellow"]))
    els.append(text(bx + 14, by + 10, "비트 연산자", size=18, align="left"))
    ops = [
        ("&",  "AND",   "양쪽 1",          "0x1A & 0x0F = 0x0A"),
        ("|",  "OR",    "하나라도 1",      "0x1A | 0x0F = 0x1F"),
        ("^",  "XOR",   "다르면 1",        "0x1A ^ 0x0F = 0x15"),
        ("~",  "NOT",   "비트 반전",       "~0x0F = 0xFFFFFFF0"),
        ("<<", "Shift L","왼쪽 이동 ×2",   "3 << 2 = 12"),
        (">>", "Shift R","오른쪽 이동 /2", "8 >> 1 = 4"),
    ]
    for i, (sym, name, desc, ex) in enumerate(ops):
        r = i // 2
        c = i % 2
        rx = bx + 14 + c * 350
        ry = by + 44 + r * 56
        els.append(rect(rx, ry, 340, 50, fill="#ffffff"))
        els.append(text(rx + 10, ry + 6, sym, size=16, align="left", color="#c92a2a"))
        els.append(text(rx + 46, ry + 8, f"{name} — {desc}", size=12, align="left"))
        els.append(text(rx + 46, ry + 28, ex, size=12, align="left", color="#1864ab"))

    # printf 서식
    px, py = 800, 450
    els.append(rect(px, py, 440, 220, fill=COLORS["orange"]))
    els.append(text(px + 14, py + 10, "printf 서식", size=18, align="left"))
    els.append(text(px + 14, py + 42,
                    "%d  → 10진수\n"
                    "%o  → 8진수\n"
                    "%x  → 16진수 소문자\n"
                    "%X  → 16진수 대문자\n"
                    "%c  → 문자\n\n"
                    "int n = 255;\n"
                    "%d→255  %o→377  %X→FF",
                    size=14, align="left"))
    return els


# ---------------------------------------------------------------------------
# Card 8 — Java try-catch-finally
# ---------------------------------------------------------------------------
def card_java_exception() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "Java 예외처리 try-catch-finally",
                        "예외 → catch → finally (항상 실행)")
    els += badge(1080, 48, "🔥 매회 출제")

    # 흐름도
    els.append(text(60, 120, "실행 흐름", size=16, align="left", color="#1864ab"))
    flow = [
        ("try",     COLORS["blue"]),
        ("예외 발생?", COLORS["yellow"]),
        ("catch",   COLORS["pink"]),
        ("finally", COLORS["green"]),
        ("다음 코드",  COLORS["gray"]),
    ]
    fx, fy = 60, 150
    fw, fh, fg = 180, 60, 40
    for i, (t, c) in enumerate(flow):
        x = fx + i * (fw + fg)
        els.append(rect(x, fy, fw, fh, fill=c))
        els.append(text(x + fw / 2 - len(t) * 9, fy + 18, t, size=16))
        if i < len(flow) - 1:
            els += arrow(x + fw, fy + fh / 2, x + fw + fg, fy + fh / 2)
    # Yes/No 표시
    els.append(text(fx + 1 * (fw + fg) + fw + 4, fy - 4, "Y", size=12, align="left", color="#c92a2a"))
    els.append(text(fx + 2 * (fw + fg) - 20, fy + fh + 12, "N: 건너뜀", size=11, align="left", color="#555"))

    # 예외 계층도
    ex, ey = 60, 240
    els.append(rect(ex, ey, 580, 330, fill=COLORS["yellow"]))
    els.append(text(ex + 14, ey + 10, "예외 클래스 계층", size=18, align="left"))
    els.append(text(ex + 14, ey + 44, "Throwable", size=15, align="left", color="#c92a2a"))
    els.append(text(ex + 34, ey + 68, "├── Error (복구 불가)", size=13, align="left"))
    els.append(text(ex + 34, ey + 92, "└── Exception", size=13, align="left"))
    els.append(text(ex + 54, ey + 116, "├── RuntimeException (Unchecked)", size=13, align="left", color="#1864ab"))
    unchecked = [
        "│    ├── ArithmeticException  (÷0)",
        "│    ├── ArrayIndexOutOfBoundsException",
        "│    ├── NullPointerException",
        "│    ├── NumberFormatException",
        "│    └── ClassCastException",
    ]
    for i, u in enumerate(unchecked):
        els.append(text(ex + 54, ey + 140 + i * 22, u, size=12, align="left", color="#444"))
    els.append(text(ex + 54, ey + 260, "└── IOException, SQLException ... (Checked)",
                    size=13, align="left", color="#2b8a3e"))
    els.append(text(ex + 14, ey + 294,
                    "Checked = 컴파일 시 처리 강제 · Unchecked = 런타임",
                    size=12, align="left", color="#555"))

    # 코드 예제 + 출력
    cx, cy = 660, 240
    els.append(rect(cx, cy, 580, 330, fill=COLORS["green"]))
    els.append(text(cx + 14, cy + 10, "코드 예제 & 출력", size=18, align="left"))
    els.append(text(cx + 14, cy + 42,
                    "try {\n"
                    "    int[] arr = {1,2,3};\n"
                    "    System.out.print(arr[1] + \" \"); // 2\n"
                    "    arr[5] = 10;         // 예외!\n"
                    "    System.out.print(\"X \");  // 건너뜀\n"
                    "} catch (ArrayIndexOutOf...Exception e) {\n"
                    "    System.out.print(\"E \");\n"
                    "} finally {\n"
                    "    System.out.print(\"F\");\n"
                    "}",
                    size=13, align="left"))
    els.append(rect(cx + 14, cy + 240, 540, 76, fill="#ffffff"))
    els.append(text(cx + 24, cy + 250, "출력: 2 E F", size=18, align="left", color="#c92a2a"))
    els.append(text(cx + 24, cy + 284,
                    "try 내 예외 발생 이후 코드는 건너뜀",
                    size=12, align="left", color="#444"))

    # throw vs throws + finally return
    ty2 = 585
    els.append(rect(60, ty2, 1180, 90, fill=COLORS["orange"]))
    els.append(text(80, ty2 + 8, "핵심 규칙", size=16, align="left"))
    els.append(text(80, ty2 + 32,
                    "• throw = 예외 발생시킴 (명령문)   "
                    "• throws = 메서드 선언부에 발생 예외 명시",
                    size=13, align="left"))
    els.append(text(80, ty2 + 54,
                    "• finally에 return이 있으면 try/catch의 return을 덮어씀   "
                    "• finally는 예외 여부 무관하게 항상 실행",
                    size=13, align="left", color="#c92a2a"))
    return els


# ---------------------------------------------------------------------------
# Card 9 — Java 재귀함수
# ---------------------------------------------------------------------------
def card_java_recursion() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "Java 재귀함수",
                        "static 메서드 재귀 · 호출 트리 · 출력 순서 (전/후)")
    els += badge(1080, 48, "🔥 매회 출제")

    # 숫자 뒤집기 (2025-1회 패턴)
    fx, fy = 60, 130
    els.append(rect(fx, fy, 560, 280, fill=COLORS["yellow"]))
    els.append(text(fx + 14, fy + 10, "숫자 뒤집기  f(1234) → 4321",
                    size=18, align="left"))
    els.append(text(fx + 14, fy + 42,
                    "static void f(int n) {\n"
                    "    if (n <= 0) return;\n"
                    "    System.out.print(n % 10);\n"
                    "    f(n / 10);\n"
                    "}\n"
                    "f(1234);",
                    size=13, align="left"))
    steps = [
        "f(1234) → print 4, f(123)",
        "f(123)  → print 3, f(12)",
        "f(12)   → print 2, f(1)",
        "f(1)    → print 1, f(0)",
        "f(0)    → return",
    ]
    for i, s in enumerate(steps):
        els.append(text(fx + 14, fy + 170 + i * 22, s, size=13, align="left"))

    # 호출 트리 factorial
    tx, ty = 660, 130
    els.append(rect(tx, ty, 580, 280, fill=COLORS["blue"]))
    els.append(text(tx + 14, ty + 10, "호출 트리  factorial(4) = 24",
                    size=18, align="left"))
    tree = [
        ("fact(4)", "= 4 * fact(3)",  0),
        ("fact(3)", "= 3 * fact(2)",  1),
        ("fact(2)", "= 2 * fact(1)",  2),
        ("fact(1)", "= 1  (Base)",    3),
    ]
    for call, body, depth in tree:
        ry = ty + 48 + depth * 56
        rx = tx + 14 + depth * 30
        els.append(rect(rx, ry, 460, 48, fill="#ffffff"))
        els.append(text(rx + 10, ry + 4, call, size=14, align="left", color="#c92a2a"))
        els.append(text(rx + 10, ry + 24, body, size=12, align="left"))
    els.append(text(tx + 14, ty + 274,
                    "복귀: 1 → 2 → 6 → 24",
                    size=14, align="left", color="#c92a2a"))

    # 출력 위치 (전/후)
    ox, oy = 60, 430
    els.append(rect(ox, oy, 580, 240, fill=COLORS["green"]))
    els.append(text(ox + 14, oy + 10, "출력 위치가 순서를 결정",
                    size=18, align="left"))
    els.append(text(ox + 14, oy + 42,
                    "// 재귀 호출 '전' 출력 → 순방향\n"
                    "void forward(int n) {\n"
                    "    if (n <= 0) return;\n"
                    "    print(n + \" \");\n"
                    "    forward(n - 1);\n"
                    "}\n"
                    "forward(3) → \"3 2 1\"\n\n"
                    "// 재귀 호출 '후' 출력 → 역방향\n"
                    "void backward(int n) {\n"
                    "    if (n <= 0) return;\n"
                    "    backward(n - 1);\n"
                    "    print(n + \" \");\n"
                    "}\n"
                    "backward(3) → \"1 2 3\"",
                    size=12, align="left"))

    # 재귀+오버라이딩
    rx, ry = 660, 430
    els.append(rect(rx, ry, 580, 240, fill=COLORS["pink"]))
    els.append(text(rx + 14, ry + 10, "고난도: 재귀 + 오버라이딩 (2024-2회)",
                    size=16, align="left"))
    els.append(text(rx + 14, ry + 42,
                    "class A {\n"
                    "    int f(int n) {\n"
                    "        if (n<=1) return 1;\n"
                    "        return n * f(n-1); // 곱\n"
                    "    }\n"
                    "}\n"
                    "class B extends A {\n"
                    "    @Override\n"
                    "    int f(int n) {\n"
                    "        if (n<=1) return 1;\n"
                    "        return n + f(n-1); // 합 (재정의)\n"
                    "    }\n"
                    "}\n"
                    "A o = new B();\n"
                    "o.f(4); // 동적 바인딩 → 4+3+2+1 = 10",
                    size=12, align="left"))
    return els


# ---------------------------------------------------------------------------
# Card 10 — Java String 메서드
# ---------------------------------------------------------------------------
def card_java_string() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "Java String 메서드",
                        "불변 객체 · 인덱스 0부터 · substring(start, end): end 미포함")
    els += badge(1080, 48, "🔥 매회 출제")

    # 메서드 그리드
    methods = [
        ("length()",         "\"abc\".length()",          "→ 3"),
        ("charAt(i)",        "\"abc\".charAt(1)",         "→ 'b'"),
        ("substring(s,e)",   "\"abcde\".substring(1,4)",  "→ \"bcd\""),
        ("substring(s)",     "\"abcde\".substring(2)",    "→ \"cde\""),
        ("indexOf(str)",     "\"Hello\".indexOf(\"ll\")", "→ 2"),
        ("replace(o,n)",     "\"aab\".replace(\"a\",\"x\")", "→ \"xxb\""),
        ("toUpperCase()",    "\"abc\".toUpperCase()",     "→ \"ABC\""),
        ("toLowerCase()",    "\"ABC\".toLowerCase()",     "→ \"abc\""),
        ("split(regex)",     "\"a,b,c\".split(\",\")",    "→ {\"a\",\"b\",\"c\"}"),
        ("trim()",           "\"  ab  \".trim()",         "→ \"ab\""),
        ("equals(str)",      "\"a\".equals(\"a\")",       "→ true (내용 비교)"),
        ("concat(str)",      "\"ab\".concat(\"cd\")",     "→ \"abcd\""),
    ]
    x0, y0 = 60, 130
    w, h, gx, gy = 390, 78, 10, 10
    for i, (sig, call, ret) in enumerate(methods):
        r = i // 3
        c = i % 3
        x = x0 + c * (w + gx)
        y = y0 + r * (h + gy)
        els.append(rect(x, y, w, h, fill=COLORS["blue"]))
        els.append(text(x + 12, y + 6, sig, size=15, align="left", color="#c92a2a"))
        els.append(text(x + 12, y + 30, call, size=12, align="left"))
        els.append(text(x + 12, y + 50, ret, size=12, align="left", color="#1864ab"))

    # 트레이싱
    ty = 490
    els.append(rect(60, ty, 580, 180, fill=COLORS["yellow"]))
    els.append(text(80, ty + 10,
                    "트레이싱  s = \"Information\"",
                    size=17, align="left"))
    els.append(text(80, ty + 40,
                    "인덱스: I=0 n=1 f=2 o=3 r=4 m=5 a=6 t=7 i=8 o=9 n=10",
                    size=12, align="left", color="#555"))
    els.append(text(80, ty + 66,
                    "s.substring(0, 4) → \"Info\"\n"
                    "s.charAt(5)       → 'm'\n"
                    "s.length()        → 11\n"
                    "출력: Infom11",
                    size=13, align="left"))

    # == vs equals
    ex, ey = 660, 490
    els.append(rect(ex, ey, 580, 180, fill=COLORS["red"]))
    els.append(text(ex + 14, ey + 10, "== vs equals (시험 함정)",
                    size=18, align="left"))
    els.append(text(ex + 14, ey + 42,
                    "String a = \"hello\";\n"
                    "String b = \"hello\";\n"
                    "String c = new String(\"hello\");\n\n"
                    "a == b       → true   (문자열 풀)\n"
                    "a == c       → false  (new로 별도 객체)\n"
                    "a.equals(c)  → true   (내용 비교)",
                    size=13, align="left"))
    return els


# ---------------------------------------------------------------------------
# Card 11 — Python 문자열 메서드
# ---------------------------------------------------------------------------
def card_python_string() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "Python 문자열 메서드",
                        "불변(immutable) · 메서드 체인 · 슬라이싱 [::]")
    els += badge(1080, 48, "🔥 매회 출제")

    # 메서드 그리드
    methods = [
        ("len(s)",          "len(\"abc\")",            "→ 3"),
        ("upper()",         "\"abc\".upper()",         "→ \"ABC\""),
        ("lower()",         "\"ABC\".lower()",         "→ \"abc\""),
        ("strip()",         "\"  ab  \".strip()",      "→ \"ab\""),
        ("replace(o,n)",    "\"aab\".replace(\"a\",\"x\")", "→ \"xxb\""),
        ("split(sep)",      "\"a,b,c\".split(\",\")",  "→ ['a','b','c']"),
        ("sep.join(list)",  "\"-\".join(['a','b'])",    "→ \"a-b\""),
        ("find(str)",       "\"Hello\".find(\"l\")",   "→ 2"),
        ("count(str)",      "\"abab\".count(\"a\")",   "→ 2"),
        ("startswith(s)",   "\"abc\".startswith(\"a\")", "→ True"),
        ("endswith(s)",     "\"abc\".endswith(\"z\")", "→ False"),
        ("f-string",        "f\"{name}: {score}\"",    "→ \"홍길동: 95\""),
    ]
    x0, y0 = 60, 130
    w, h, gx, gy = 390, 78, 10, 10
    for i, (sig, call, ret) in enumerate(methods):
        r = i // 3
        c = i % 3
        x = x0 + c * (w + gx)
        y = y0 + r * (h + gy)
        els.append(rect(x, y, w, h, fill=COLORS["green"]))
        els.append(text(x + 12, y + 6, sig, size=15, align="left", color="#c92a2a"))
        els.append(text(x + 12, y + 30, call, size=12, align="left"))
        els.append(text(x + 12, y + 50, ret, size=12, align="left", color="#1864ab"))

    # 슬라이싱 예제
    sx, sy = 60, 490
    els.append(rect(sx, sy, 580, 180, fill=COLORS["yellow"]))
    els.append(text(sx + 14, sy + 10,
                    "슬라이싱 [start:end:step] — 빈출",
                    size=17, align="left"))
    els.append(text(sx + 14, sy + 42,
                    "s = \"Hello World\"\n"
                    "s[0:5]   → \"Hello\"\n"
                    "s[6:]    → \"World\"\n"
                    "s[::2]   → \"HloWrd\"\n"
                    "s[::-1]  → \"dlroW olleH\"  (역순)\n"
                    "s[-5:]   → \"World\"",
                    size=13, align="left"))

    # 메서드 체인 트레이싱
    cx, cy = 660, 490
    els.append(rect(cx, cy, 580, 180, fill=COLORS["pink"]))
    els.append(text(cx + 14, cy + 10,
                    "메서드 체인 트레이싱 (매회 출제)",
                    size=17, align="left"))
    els.append(text(cx + 14, cy + 42,
                    "s = \"apple,banana,cherry\"\n"
                    "a = s.split(\",\")\n"
                    "  → ['apple','banana','cherry']\n"
                    "b = \"-\".join(a)\n"
                    "  → \"apple-banana-cherry\"\n"
                    "c = b.replace(\"banana\",\"grape\")\n"
                    "  → \"apple-grape-cherry\"",
                    size=13, align="left"))
    return els


CARDS = [
    ("pg-data-structure-002.excalidraw", card_linked_list),
    ("pg-language-001.excalidraw",       card_c_pointer),
    ("pg-language-003.excalidraw",       card_java_inheritance),
    ("pg-language-004.excalidraw",       card_python_basics),
    ("pg-language-007.excalidraw",       card_c_array_loop),
    ("pg-language-008.excalidraw",       card_c_recursion),
    ("pg-language-010.excalidraw",       card_c_bitop),
    ("pg-language-011.excalidraw",       card_java_exception),
    ("pg-language-013.excalidraw",       card_java_recursion),
    ("pg-language-014.excalidraw",       card_java_string),
    ("pg-language-017.excalidraw",       card_python_string),
]


def main() -> None:
    for name, builder in CARDS:
        els = builder()
        path = save(els, name)
        print(f"  ✓ {path.name}  ({len(els)} elements)")
    print(f"\n생성 완료: {len(CARDS)}개 → {OUT_DIR}")


if __name__ == "__main__":
    main()
