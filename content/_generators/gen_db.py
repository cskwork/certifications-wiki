"""DB 과목 priority-3 카드 6장의 Excalidraw 다이어그램 생성기.

실행: python3 gen_db.py
출력: ../db/*.excalidraw
"""
from __future__ import annotations

import json
import random
import time
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "db"
OUT_DIR.mkdir(parents=True, exist_ok=True)

NOW_MS = int(time.time() * 1000)
_rng = random.Random(20260410)

COLORS = {
    "ink": "#1e1e1e",
    "yellow": "#fff3bf",
    "blue": "#d0ebff",
    "green": "#c3fae8",
    "pink": "#ffdeeb",
    "purple": "#e5dbff",
    "orange": "#ffe8cc",
    "red": "#ffc9c9",
    "gray": "#f1f3f5",
}


def _seed() -> int:
    return _rng.randint(1, 2**31 - 1)


def _base(type_: str, x: float, y: float, w: float, h: float, **extra) -> dict:
    el = {
        "id": f"{type_}-{_seed()}",
        "type": type_,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": COLORS["ink"],
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "index": None,
        "roundness": {"type": 3} if type_ == "rectangle" else None,
        "seed": _seed(),
        "version": 1,
        "versionNonce": _seed(),
        "isDeleted": False,
        "boundElements": None,
        "updated": NOW_MS,
        "link": None,
        "locked": False,
    }
    el.update(extra)
    return el


def rect(x, y, w, h, fill=COLORS["yellow"], stroke=COLORS["ink"]) -> dict:
    return _base(
        "rectangle", x, y, w, h,
        backgroundColor=fill,
        strokeColor=stroke,
    )


def ellipse(x, y, w, h, fill=COLORS["blue"]) -> dict:
    el = _base("ellipse", x, y, w, h, backgroundColor=fill)
    el["roundness"] = {"type": 2}
    return el


def text(x, y, content: str, size: int = 18, align: str = "center", color: str = COLORS["ink"]) -> dict:
    # crude width/height estimation — Obsidian Excalidraw re-measures on open.
    lines = content.split("\n")
    # Korean chars are ~1.0em wide at size, ASCII ~0.55em.
    def line_w(s: str) -> float:
        return sum((1.0 if ord(c) > 127 else 0.55) for c in s) * size
    w = max((line_w(l) for l in lines), default=size) + 12
    h = int(size * 1.25 * len(lines)) + 4
    return _base(
        "text", x, y, w, h,
        strokeColor=color,
        text=content,
        fontSize=size,
        fontFamily=1,
        textAlign=align,
        verticalAlign="top",
        baseline=int(size * 0.9),
        containerId=None,
        originalText=content,
        lineHeight=1.25,
    )


def arrow(x1, y1, x2, y2, stroke=COLORS["ink"], label: str | None = None) -> list[dict]:
    el = _base(
        "arrow", x1, y1, x2 - x1, y2 - y1,
        strokeColor=stroke,
        roundness={"type": 2},
        points=[[0, 0], [x2 - x1, y2 - y1]],
        lastCommittedPoint=None,
        startBinding=None,
        endBinding=None,
        startArrowhead=None,
        endArrowhead="arrow",
    )
    out = [el]
    if label:
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2 - 24
        out.append(text(mx - len(label) * 5, my, label, size=14))
    return out


def line(x1, y1, x2, y2, stroke=COLORS["ink"]) -> dict:
    return _base(
        "line", x1, y1, x2 - x1, y2 - y1,
        strokeColor=stroke,
        roundness={"type": 2},
        points=[[0, 0], [x2 - x1, y2 - y1]],
        lastCommittedPoint=None,
        startBinding=None,
        endBinding=None,
        startArrowhead=None,
        endArrowhead=None,
    )


def title_banner(x: float, y: float, w: float, title: str, subtitle: str | None = None) -> list[dict]:
    out = [rect(x, y, w, 56, fill=COLORS["gray"])]
    out.append(text(x + 16, y + 10, title, size=22, align="left"))
    if subtitle:
        out.append(text(x + 16, y + 36, subtitle, size=12, align="left", color="#555"))
    return out


def badge(x: float, y: float, txt: str, fill: str = COLORS["red"]) -> list[dict]:
    w = len(txt) * 12 + 20
    return [
        rect(x, y, w, 28, fill=fill),
        text(x + 10, y + 6, txt, size=13),
    ]


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
# Card 1 — 정규화 단계 1NF~BCNF
# ---------------------------------------------------------------------------
def card_normalization() -> list[dict]:
    els = []
    els += title_banner(40, 40, 1200, "정규화 단계 (1NF → BCNF)",
                        "중복 제거 · 이상현상(삽입/삭제/갱신) 방지")
    els += badge(1080, 48, "🔥 매회 출제")

    stages = [
        ("비정규형", "반복그룹 有", COLORS["gray"]),
        ("1NF",  "원자값만 허용",         COLORS["blue"]),
        ("2NF",  "부분 함수 종속 제거",    COLORS["green"]),
        ("3NF",  "이행 함수 종속 제거",    COLORS["yellow"]),
        ("BCNF", "결정자 = 후보키",       COLORS["orange"]),
        ("4NF",  "다치 종속 제거",        COLORS["pink"]),
        ("5NF",  "조인 종속 제거",        COLORS["purple"]),
    ]
    x0, y0 = 60, 140
    box_w, box_h, gap = 160, 100, 24
    for i, (name, cond, color) in enumerate(stages):
        x = x0 + i * (box_w + gap)
        els.append(rect(x, y0, box_w, box_h, fill=color))
        els.append(text(x + box_w / 2 - len(name) * 8, y0 + 18, name, size=22))
        els.append(text(x + 10, y0 + 54, cond, size=13, align="left"))
        if i < len(stages) - 1:
            ax1 = x + box_w
            ax2 = x + box_w + gap
            els += arrow(ax1, y0 + box_h / 2, ax2, y0 + box_h / 2)

    # 암기 블록
    ey = 300
    els.append(rect(60, ey, 1180, 80, fill=COLORS["yellow"]))
    els.append(text(80, ey + 14, "암기법: 도·부·이·결·다·조", size=20, align="left"))
    els.append(
        text(80, ey + 46,
             "도메인 원자값 → 부분종속 → 이행종속 → 결정자=후보키 → 다치종속 → 조인종속",
             size=14, align="left", color="#444")
    )

    # 이상현상
    iy = 410
    els += [rect(60, iy, 1180, 120, fill=COLORS["red"])]
    els += [text(80, iy + 12, "이상현상(Anomaly) — 정규화로 제거 대상", size=18, align="left")]
    anomalies = [
        ("삽입 이상", "원치 않는 데이터 강제 삽입"),
        ("삭제 이상", "필요한 데이터까지 함께 삭제"),
        ("갱신 이상", "일부만 수정되어 불일치 발생"),
    ]
    for i, (name, desc) in enumerate(anomalies):
        cx = 80 + i * 390
        els.append(rect(cx, iy + 46, 370, 60, fill="#fff5f5"))
        els.append(text(cx + 14, iy + 54, name, size=16, align="left"))
        els.append(text(cx + 14, iy + 78, desc, size=13, align="left", color="#555"))
    return els


# ---------------------------------------------------------------------------
# Card 2 — 릴레이션 구성요소
# ---------------------------------------------------------------------------
def card_relation_parts() -> list[dict]:
    els = []
    els += title_banner(40, 40, 1200, "릴레이션 구성 요소",
                        "Tuple · Attribute · Domain · Degree · Cardinality")
    els += badge(1080, 48, "🔥 매회 출제")

    # Table grid: 4 columns x 6 rows (header + 5 data)
    cols = ["학번", "이름", "학과", "학년"]
    rows_data = [
        ["2024001", "김철수", "컴공",  "3"],
        ["2024002", "이영희", "전자",  "2"],
        ["2024003", "박민수", "기계",  "4"],
        ["2024004", "정수진", "컴공",  "1"],
        ["2024005", "홍길동", "경영",  "3"],
    ]
    tx, ty = 200, 150
    col_w, row_h = 150, 48

    # header row
    for c, name in enumerate(cols):
        els.append(rect(tx + c * col_w, ty, col_w, row_h, fill=COLORS["blue"]))
        els.append(text(tx + c * col_w + col_w / 2 - len(name) * 9, ty + 12, name, size=18))
    # data rows
    for r, row in enumerate(rows_data):
        for c, val in enumerate(row):
            els.append(rect(tx + c * col_w, ty + (r + 1) * row_h, col_w, row_h, fill="#ffffff"))
            els.append(text(tx + c * col_w + col_w / 2 - len(val) * 6, ty + (r + 1) * row_h + 14, val, size=14))

    # Annotations
    # Attribute (column) callout — points to header
    els += arrow(tx + col_w * 1.5, ty - 70, tx + col_w * 1.5, ty - 4)
    els.append(text(tx + col_w + 10, ty - 100, "Attribute (속성/열)\nDegree = 4", size=16, align="left", color="#1864ab"))

    # Tuple (row) callout — points to a data row
    row_y = ty + row_h * 2 + row_h / 2
    els += arrow(tx + col_w * 4 + 120, row_y, tx + col_w * 4 + 4, row_y)
    els.append(text(tx + col_w * 4 + 130, row_y - 20, "Tuple (튜플/행)\nCardinality = 5", size=16, align="left", color="#2b8a3e"))

    # Domain callout — points to 학년 column cells
    els += arrow(tx - 40, ty + row_h * 3.5, tx + col_w * 3 - 4, ty + row_h * 3.5)
    els.append(text(tx - 260, ty + row_h * 3.5 - 24, "Domain (도메인)\n예) 학년 ∈ {1,2,3,4}", size=16, align="left", color="#862e9c"))

    # Legend box
    ly = ty + row_h * 6 + 60
    els.append(rect(60, ly, 1180, 120, fill=COLORS["yellow"]))
    els.append(text(80, ly + 12, "용어 매핑 (영문 ↔ 한글)", size=18, align="left"))
    mapping = [
        "• Degree       = 차수       = 속성(컬럼) 개수 = 4",
        "• Cardinality  = 카디널리티 = 튜플(행) 개수   = 5",
        "• Domain       = 도메인     = 속성이 가질 수 있는 값의 범위",
        "• NULL은 0·공백과 다름 — '값 없음'",
    ]
    for i, line_txt in enumerate(mapping):
        els.append(text(96, ly + 42 + i * 18, line_txt, size=13, align="left", color="#444"))
    return els


# ---------------------------------------------------------------------------
# Card 3 — DDL
# ---------------------------------------------------------------------------
def card_ddl() -> list[dict]:
    els = []
    els += title_banner(40, 40, 1200, "DDL — Data Definition Language",
                        "스키마(구조) 정의 · 자동 커밋 · ROLLBACK 불가")
    els += badge(1080, 48, "🔥 매회 출제")

    commands = [
        ("CREATE",   "객체 생성",              "CREATE TABLE 학생 (\n  학번 INT PRIMARY KEY,\n  이름 VARCHAR(20) NOT NULL\n);", COLORS["green"]),
        ("ALTER",    "구조 변경",              "ALTER TABLE 학생\n  ADD 전화번호 VARCHAR(20);", COLORS["blue"]),
        ("DROP",     "객체 완전 삭제",         "DROP TABLE 학생\n  [CASCADE | RESTRICT];", COLORS["pink"]),
        ("TRUNCATE", "데이터만 삭제\n(구조 유지)", "TRUNCATE TABLE 학생;", COLORS["orange"]),
    ]
    x0, y0 = 60, 140
    w, h, gap = 285, 260, 20
    for i, (name, desc, code, color) in enumerate(commands):
        x = x0 + i * (w + gap)
        els.append(rect(x, y0, w, h, fill=color))
        els.append(text(x + 20, y0 + 16, name, size=26, align="left"))
        els.append(text(x + 20, y0 + 54, desc, size=14, align="left", color="#555"))
        # code box
        els.append(rect(x + 16, y0 + 100, w - 32, h - 120, fill="#ffffff"))
        els.append(text(x + 28, y0 + 112, code, size=12, align="left"))

    # Bottom comparison
    cy = 430
    els.append(rect(60, cy, 1180, 140, fill=COLORS["yellow"]))
    els.append(text(80, cy + 12, "DDL vs DML vs DCL  — 시험 단골 분류 문제", size=18, align="left"))
    rows = [
        ("DDL", "CREATE · ALTER · DROP · TRUNCATE", "스키마 정의, 자동 커밋"),
        ("DML", "SELECT · INSERT · UPDATE · DELETE", "데이터 조작, COMMIT/ROLLBACK 가능"),
        ("DCL", "GRANT · REVOKE",                   "권한 제어"),
    ]
    for i, (kind, cmds, note) in enumerate(rows):
        y = cy + 44 + i * 28
        els.append(text(90, y, kind, size=15, align="left", color="#c92a2a"))
        els.append(text(160, y, cmds, size=14, align="left"))
        els.append(text(700, y, note, size=13, align="left", color="#666"))
    return els


# ---------------------------------------------------------------------------
# Card 4 — JOIN 종류
# ---------------------------------------------------------------------------
def card_joins() -> list[dict]:
    els = []
    els += title_banner(40, 40, 1200, "JOIN 종류",
                        "두 테이블을 공통 속성으로 결합")
    els += badge(1080, 48, "🔥 매회 출제")

    joins = [
        ("INNER JOIN",       "양쪽 모두 일치하는 행만\n(교집합)",                    COLORS["green"]),
        ("LEFT OUTER JOIN",  "왼쪽 전부 + 오른쪽 일치\n불일치 → 오른쪽 NULL",        COLORS["blue"]),
        ("RIGHT OUTER JOIN", "오른쪽 전부 + 왼쪽 일치\n불일치 → 왼쪽 NULL",          COLORS["yellow"]),
        ("FULL OUTER JOIN",  "양쪽 전부 반환\n불일치 쪽은 NULL (합집합)",            COLORS["purple"]),
        ("CROSS JOIN",       "조건 없이 모든 조합\n결과 행 수 = m × n (카티션 곱)", COLORS["orange"]),
        ("SELF JOIN",        "같은 테이블끼리 조인\n별칭(Alias) 사용",               COLORS["pink"]),
    ]
    x0, y0 = 60, 140
    w, h, gx, gy = 380, 160, 20, 20
    for i, (name, desc, color) in enumerate(joins):
        r = i // 3
        c = i % 3
        x = x0 + c * (w + gx)
        y = y0 + r * (h + gy)
        # Card frame
        els.append(rect(x, y, w, h, fill=color))
        els.append(text(x + 16, y + 14, name, size=20, align="left"))
        els.append(text(x + 16, y + 50, desc, size=14, align="left", color="#444"))
        # Mini venn (two circles)
        cx1, cy1 = x + 80, y + 115
        cx2 = cx1 + 40
        a = ellipse(cx1 - 30, cy1 - 25, 60, 50, fill="#ffffff")
        b = ellipse(cx2 - 30, cy1 - 25, 60, 50, fill="#ffffff")
        els += [a, b]
        els.append(text(cx1 - 6, cy1 - 14, "A", size=14))
        els.append(text(cx2 + 22, cy1 - 14, "B", size=14))

    # Natural / equi note
    ny = 500
    els.append(rect(60, ny, 1180, 80, fill=COLORS["gray"]))
    els.append(text(80, ny + 12, "NATURAL JOIN · EQUI JOIN", size=18, align="left"))
    els.append(text(80, ny + 44,
                    "• NATURAL: 같은 이름 속성을 자동 조인 조건으로 사용  "
                    "• EQUI: '=' 연산자로 조인",
                    size=13, align="left", color="#444"))
    return els


# ---------------------------------------------------------------------------
# Card 5 — DML
# ---------------------------------------------------------------------------
def card_dml() -> list[dict]:
    els = []
    els += title_banner(40, 40, 1200, "DML — Data Manipulation Language",
                        "데이터 조회·삽입·수정·삭제 · COMMIT/ROLLBACK 가능")
    els += badge(1080, 48, "🔥 매회 출제")

    ops = [
        ("SELECT", "조회", "SELECT 컬럼 FROM 테이블\nWHERE 조건;", COLORS["green"]),
        ("INSERT", "삽입", "INSERT INTO T(컬럼)\nVALUES (값);", COLORS["blue"]),
        ("UPDATE", "수정", "UPDATE T SET 컬럼=값\nWHERE 조건;", COLORS["yellow"]),
        ("DELETE", "삭제", "DELETE FROM T\nWHERE 조건;", COLORS["pink"]),
    ]
    x0, y0 = 60, 140
    w, h, gap = 285, 180, 20
    for i, (name, desc, code, color) in enumerate(ops):
        x = x0 + i * (w + gap)
        els.append(rect(x, y0, w, h, fill=color))
        els.append(text(x + 20, y0 + 14, name, size=24, align="left"))
        els.append(text(x + 20, y0 + 50, desc, size=14, align="left", color="#555"))
        els.append(rect(x + 16, y0 + 80, w - 32, h - 96, fill="#ffffff"))
        els.append(text(x + 28, y0 + 92, code, size=12, align="left"))

    # SELECT 작성/실행 순서
    sy = 360
    els.append(rect(60, sy, 1180, 220, fill=COLORS["yellow"]))
    els.append(text(80, sy + 12, "SELECT 절 순서 — 작성 순서 ≠ 실행 순서 (시험 단골)",
                    size=18, align="left"))

    def chip_row(target: list[dict], label: str, items: list[str], ry: int, tint: str) -> None:
        target.append(text(80, ry, label, size=14, align="left", color="#555"))
        cx = 230
        for j, item in enumerate(items):
            iw = len(item) * 12 + 28
            target.append(rect(cx, ry - 6, iw, 34, fill=tint))
            target.append(text(cx + 14, ry, item, size=14))
            if j < len(items) - 1:
                target.extend(arrow(cx + iw + 2, ry + 10, cx + iw + 20, ry + 10))
            cx += iw + 22

    chip_row(els, "작성 순서",
             ["SELECT", "FROM", "WHERE", "GROUP BY", "HAVING", "ORDER BY"],
             sy + 70, "#ffffff")
    chip_row(els, "실행 순서",
             ["FROM", "WHERE", "GROUP BY", "집계", "HAVING", "SELECT", "ORDER BY"],
             sy + 150, COLORS["blue"])

    # INSERT 두 형태
    iy = 610
    els.append(rect(60, iy, 1180, 100, fill=COLORS["gray"]))
    els.append(text(80, iy + 12, "INSERT 두 가지 형태", size=18, align="left"))
    els.append(text(80, iy + 44,
                    "① 직접 삽입: INSERT INTO T(col) VALUES (값)",
                    size=14, align="left"))
    els.append(text(80, iy + 70,
                    "② 조회 삽입: INSERT INTO T(col) SELECT ... FROM ...   ← 2024-2회 기출",
                    size=14, align="left", color="#c92a2a"))
    return els


# ---------------------------------------------------------------------------
# Card 6 — 집계함수 + GROUP BY
# ---------------------------------------------------------------------------
def card_aggregate() -> list[dict]:
    els = []
    els += title_banner(40, 40, 1200, "집계함수 & GROUP BY",
                        "COUNT · SUM · AVG · MAX · MIN + HAVING")
    els += badge(1080, 48, "🔥 매회 출제")

    # Pipeline flow
    py = 150
    steps = ["FROM", "WHERE", "GROUP BY", "집계함수", "HAVING", "SELECT", "ORDER BY"]
    tints = [COLORS["gray"], COLORS["blue"], COLORS["green"], COLORS["yellow"],
             COLORS["orange"], COLORS["pink"], COLORS["purple"]]
    x = 60
    for i, (s, tint) in enumerate(zip(steps, tints)):
        w = 150
        els.append(rect(x, py, w, 60, fill=tint))
        els.append(text(x + w / 2 - len(s) * 7, py + 18, s, size=16))
        if i < len(steps) - 1:
            els += arrow(x + w, py + 30, x + w + 14, py + 30)
        x += w + 14
    els.append(text(60, py - 28, "실행 순서 파이프라인 →", size=14, align="left", color="#555"))

    # NULL 처리 테이블
    ny = 260
    els.append(rect(60, ny, 560, 360, fill=COLORS["yellow"]))
    els.append(text(80, ny + 14, "NULL 처리 규칙", size=20, align="left"))
    els.append(text(80, ny + 48,
                    "COUNT(*) 만 NULL 포함, 나머지는 모두 NULL 제외",
                    size=13, align="left", color="#c92a2a"))

    headers = ["함수", "NULL 포함?", "비고"]
    hx = [80, 240, 380]
    hy = ny + 86
    for i, h in enumerate(headers):
        els.append(rect(hx[i], hy, 150 if i < 2 else 200, 34, fill=COLORS["blue"]))
        els.append(text(hx[i] + 12, hy + 8, h, size=14, align="left"))
    rows = [
        ("COUNT(*)",    "O 포함",   "전체 행 수"),
        ("COUNT(컬럼)", "X 제외",   "NULL 제외 행 수"),
        ("SUM",         "X 제외",   "NULL은 0이 아님"),
        ("AVG",         "X 제외",   "분모도 NULL 제외"),
        ("MAX / MIN",   "X 제외",   "NULL은 비교 대상 아님"),
    ]
    for r, (fn, inc, note) in enumerate(rows):
        ry = hy + 34 + r * 38
        for i, val in enumerate([fn, inc, note]):
            els.append(rect(hx[i], ry, 150 if i < 2 else 200, 38, fill="#ffffff"))
            els.append(text(hx[i] + 12, ry + 12, val, size=13, align="left"))

    # HAVING vs WHERE
    hy2 = 260
    els.append(rect(640, hy2, 600, 360, fill=COLORS["green"]))
    els.append(text(660, hy2 + 14, "WHERE vs HAVING", size=20, align="left"))
    els.append(text(660, hy2 + 50, "WHERE", size=16, align="left", color="#1864ab"))
    els.append(text(660, hy2 + 76, "• 그룹화 '이전' 행 필터", size=13, align="left"))
    els.append(text(660, hy2 + 96, "• 집계함수 사용 불가", size=13, align="left"))
    els.append(text(660, hy2 + 140, "HAVING", size=16, align="left", color="#c92a2a"))
    els.append(text(660, hy2 + 166, "• 그룹화 '이후' 집계 결과 필터", size=13, align="left"))
    els.append(text(660, hy2 + 186, "• 집계함수 조건으로 사용 가능", size=13, align="left"))

    els.append(rect(660, hy2 + 220, 560, 120, fill="#ffffff"))
    els.append(text(678, hy2 + 232,
                    "SELECT 학과, COUNT(*)\n"
                    "FROM 학생\n"
                    "WHERE 학년 >= 2        -- 행 필터\n"
                    "GROUP BY 학과\n"
                    "HAVING COUNT(*) >= 3;  -- 그룹 필터",
                    size=13, align="left"))
    return els


CARDS = [
    ("db-modeling-001.excalidraw", card_normalization),
    ("db-relation-001.excalidraw", card_relation_parts),
    ("db-sql-001.excalidraw",      card_ddl),
    ("db-sql-002.excalidraw",      card_joins),
    ("db-sql-003.excalidraw",      card_dml),
    ("db-sql-004.excalidraw",      card_aggregate),
]


def main() -> None:
    for name, builder in CARDS:
        els = builder()
        path = save(els, name)
        print(f"  ✓ {path.name}  ({len(els)} elements)")
    print(f"\n생성 완료: {len(CARDS)}개 → {OUT_DIR}")


if __name__ == "__main__":
    main()
