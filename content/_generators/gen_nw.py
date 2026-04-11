"""NW 과목 priority-3 카드 4장의 Excalidraw 다이어그램 생성기.

실행: python3 gen_nw.py
출력: ../nw/*.excalidraw
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gen_db import COLORS, arrow, badge, line, rect, text, title_banner  # noqa: E402  # pyright: ignore[reportMissingImports]

OUT_DIR = Path(__file__).resolve().parent.parent / "nw"
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
# Card 1 — OSI 7계층 모델
# ---------------------------------------------------------------------------
def card_osi() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "OSI 7계층 모델",
                        "ISO 제정 · PDU · 대표 장비 · 대표 프로토콜")
    els += badge(1080, 48, "🔥 매회 출제")

    # Layers top(L7) → bottom(L1)
    layers = [
        ("L7", "응용 (Application)",   "Data",    "게이트웨이", "HTTP · FTP · SMTP · DNS · SSH", COLORS["pink"]),
        ("L6", "표현 (Presentation)",  "Data",    "게이트웨이", "JPEG · MPEG · SSL/TLS",         COLORS["purple"]),
        ("L5", "세션 (Session)",       "Data",    "게이트웨이", "TLS · RPC · NetBIOS",           COLORS["orange"]),
        ("L4", "전송 (Transport)",     "Segment", "L4 스위치",  "TCP · UDP (포트번호)",          COLORS["yellow"]),
        ("L3", "네트워크 (Network)",   "Packet",  "라우터",     "IP · ICMP · ARP · OSPF · RIP",  COLORS["green"]),
        ("L2", "데이터링크 (DataLink)","Frame",   "스위치·브리지","이더넷 · HDLC · PPP",          COLORS["blue"]),
        ("L1", "물리 (Physical)",      "Bit",     "리피터·허브","RS-232 · X.21",                 COLORS["gray"]),
    ]
    x0, y0 = 60, 130
    row_h = 62
    layer_w = 620
    for i, (num, name, pdu, dev, proto, color) in enumerate(layers):
        y = y0 + i * (row_h + 6)
        els.append(rect(x0, y, layer_w, row_h, fill=color))
        els.append(text(x0 + 14, y + 10, num, size=18, align="left", color="#c92a2a"))
        els.append(text(x0 + 60, y + 8, name, size=18, align="left"))
        els.append(text(x0 + 60, y + 34, proto, size=12, align="left", color="#444"))
        # PDU badge
        els.append(rect(x0 + layer_w - 240, y + 14, 100, 34, fill="#ffffff"))
        els.append(text(x0 + layer_w - 230, y + 22, pdu, size=14, align="left"))
        # 장비 badge
        els.append(rect(x0 + layer_w - 130, y + 14, 120, 34, fill="#ffffff"))
        els.append(text(x0 + layer_w - 122, y + 22, dev, size=12, align="left"))

    # 좌측 화살표 (캡슐화 방향)
    top_y = y0 + 4
    bot_y = y0 + len(layers) * (row_h + 6) - 6
    els += arrow(x0 - 24, top_y, x0 - 24, bot_y, label=None)
    els.append(text(x0 - 52, top_y - 24, "송신 ↓\n캡슐화", size=12, align="left", color="#555"))
    els += arrow(x0 - 56, bot_y, x0 - 56, top_y, label=None)
    els.append(text(x0 - 90, bot_y + 8, "수신 ↑\n역캡슐화", size=12, align="left", color="#555"))

    # 우측 암기 & 캡슐화
    rx, ry = 720, 130
    els.append(rect(rx, ry, 520, 200, fill=COLORS["yellow"]))
    els.append(text(rx + 16, ry + 12, "암기법: 물데네전세표응", size=20, align="left"))
    els.append(text(rx + 16, ry + 46,
                    "물리 → 데이터링크 → 네트워크 → 전송\n→ 세션 → 표현 → 응용",
                    size=14, align="left", color="#444"))
    els.append(text(rx + 16, ry + 110, "PDU 순서 (L1→L7)", size=16, align="left", color="#c92a2a"))
    els.append(text(rx + 16, ry + 140,
                    "Bit → Frame → Packet → Segment → Data",
                    size=14, align="left"))
    els.append(text(rx + 16, ry + 166,
                    "빈칸문제 단골 — 전송 계층 PDU = Segment",
                    size=12, align="left", color="#c92a2a"))

    # 기출 포인트
    ky = 350
    els.append(rect(720, ky, 520, 310, fill=COLORS["blue"]))
    els.append(text(740, ky + 12, "기출 포인트", size=18, align="left"))
    tips = [
        "• PDU 명칭 빈칸 문제 (비트/프레임/패킷/세그먼트)",
        "• 계층별 대표 장비 매칭",
        "  L1 리피터·허브  L2 스위치·브리지",
        "  L3 라우터  L7 게이트웨이",
        "• ARP = L3 (IP → MAC 변환)",
        "• 이더넷 = L2   TCP/UDP = L4",
        "• 캡슐화 시 각 계층이 헤더 추가",
        "• TCP/IP 4계층과 매핑 주의",
        "  Network Access = L1+L2",
        "  Internet = L3,  Transport = L4",
        "  Application = L5+L6+L7",
    ]
    for i, t in enumerate(tips):
        els.append(text(740, ky + 42 + i * 22, t, size=13, align="left", color="#1864ab"))

    return els


# ---------------------------------------------------------------------------
# Card 2 — 응용 계층 프로토콜
# ---------------------------------------------------------------------------
def card_app_protocols() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "응용 계층 프로토콜",
                        "포트 번호 · 약어 · 역할 매핑 (빈출)")
    els += badge(1080, 48, "🔥 매회 출제")

    # Grid 4 cols x 3 rows
    protos = [
        ("HTTP",   "80",       "TCP", "웹 통신 (비암호)",                COLORS["blue"]),
        ("HTTPS",  "443",      "TCP", "HTTP + TLS/SSL\n암호화 웹 통신",   COLORS["green"]),
        ("FTP",    "20 · 21",  "TCP", "파일 전송\n20:데이터 21:제어",     COLORS["yellow"]),
        ("SSH",    "22",       "TCP", "암호화 원격접속\n(Telnet 대체)",   COLORS["purple"]),
        ("Telnet", "23",       "TCP", "원격접속 (비암호)\nSSH로 대체됨",  COLORS["gray"]),
        ("SMTP",   "25",       "TCP", "이메일 송신",                       COLORS["orange"]),
        ("DNS",    "53",       "UDP", "도메인 → IP 변환",                  COLORS["pink"]),
        ("DHCP",   "67 · 68",  "UDP", "IP 자동 할당\n67:서버 68:클라",    COLORS["blue"]),
        ("POP3",   "110",      "TCP", "이메일 수신\n(서버에서 삭제)",      COLORS["green"]),
        ("IMAP",   "143",      "TCP", "이메일 수신\n(서버에 유지)",        COLORS["yellow"]),
        ("SNMP",   "161 · 162","UDP", "네트워크 장비\n모니터링/관리",      COLORS["orange"]),
        ("TLS/SSL","443 등",   "TCP", "전송계층 암호화\n(HTTPS 기반)",    COLORS["purple"]),
    ]
    x0, y0 = 60, 130
    w, h, gx, gy = 285, 130, 10, 10
    for i, (name, port, tu, desc, color) in enumerate(protos):
        r = i // 4
        c = i % 4
        x = x0 + c * (w + gx)
        y = y0 + r * (h + gy)
        els.append(rect(x, y, w, h, fill=color))
        els.append(text(x + 16, y + 10, name, size=22, align="left"))
        # Port big
        els.append(rect(x + w - 100, y + 10, 86, 36, fill="#ffffff"))
        els.append(text(x + w - 94, y + 16, port, size=18, align="left", color="#c92a2a"))
        # TCP/UDP
        tcp_color = "#1864ab" if tu == "TCP" else "#2b8a3e"
        els.append(text(x + 16, y + 46, tu, size=14, align="left", color=tcp_color))
        els.append(text(x + 16, y + 70, desc, size=13, align="left", color="#444"))

    # 기출 포인트 박스
    ky = 560
    els.append(rect(60, ky, 1180, 130, fill=COLORS["red"]))
    els.append(text(80, ky + 10, "기출 포인트 (혼동 주의)", size=18, align="left"))
    tips = [
        "• SSH 포트 22 — 2025-2회 직접 출제  |  FTP 20(데이터)/21(제어) 이중 포트 주의",
        "• SMTP(25)는 송신 ↔ POP3(110)·IMAP(143)은 수신 — 방향으로 구분",
        "• DNS·SNMP·DHCP = UDP 기반  |  HTTP·HTTPS·FTP·SMTP·SSH = TCP 기반",
        "• HTTPS = HTTP + TLS/SSL (443)  |  Telnet은 평문, SSH는 암호화",
    ]
    for i, t in enumerate(tips):
        els.append(text(96, ky + 42 + i * 22, t, size=13, align="left", color="#c92a2a"))
    return els


# ---------------------------------------------------------------------------
# Card 3 — 보안 공격 유형
# ---------------------------------------------------------------------------
def card_security_types() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "보안 공격 유형",
                        "서비스거부 · 인젝션 · 세션탈취 · 도청")
    els += badge(1080, 48, "🔥 매회 출제")

    # 상단 CIA 3요소 배지
    cia_y = 130
    cia_items = [
        ("기밀성 (Confidentiality)", "정보가 인가된 자에게만",    COLORS["blue"]),
        ("무결성 (Integrity)",       "데이터가 변조되지 않음",    COLORS["green"]),
        ("가용성 (Availability)",    "필요 시 서비스 이용 가능",  COLORS["yellow"]),
    ]
    for i, (t, d, c) in enumerate(cia_items):
        x = 60 + i * 395
        els.append(rect(x, cia_y, 385, 60, fill=c))
        els.append(text(x + 14, cia_y + 8, t, size=16, align="left"))
        els.append(text(x + 14, cia_y + 34, d, size=12, align="left", color="#444"))

    # 분류: 4개 카테고리
    cats = [
        ("가용성 공격 (DoS/DDoS)", COLORS["red"], [
            ("DoS", "단일 공격자 트래픽 폭주"),
            ("DDoS", "봇넷 분산 대량 트래픽"),
            ("SYN Flood", "TCP 3-way 취약점 악용"),
            ("Smurf", "ICMP 브로드캐스트 증폭"),
            ("Ping of Death", "비정상 크기 ICMP"),
            ("Land Attack", "출발지=목적지 위조"),
        ]),
        ("무결성·주입 공격", COLORS["orange"], [
            ("SQL Injection", "악성 SQL 삽입 → DB 조작"),
            ("  대응", "PreparedStatement, 입력검증"),
            ("XSS", "악성 스크립트 브라우저 실행"),
            ("  대응", "이스케이프, CSP 헤더"),
            ("CSRF", "위조 요청을 대신 전송"),
            ("  대응", "CSRF 토큰, Referer 검증"),
        ]),
        ("기밀성 공격 (도청)", COLORS["blue"], [
            ("스니핑 (Sniffing)", "패킷 도청"),
            ("  대응", "HTTPS · VPN 암호화"),
            ("스푸핑 (Spoofing)", "IP/MAC/DNS 위조"),
            ("MITM", "중간자 공격"),
            ("키로거", "키 입력 기록"),
            ("세션 스니핑", "세션 ID 가로채기"),
        ]),
        ("세션·접근 공격", COLORS["purple"], [
            ("세션 하이재킹", "인증 세션 탈취"),
            ("Watering Hole", "타깃 사이트 감염 대기"),
            ("피싱 (Phishing)", "위장 사이트 유도"),
            ("파밍 (Pharming)", "DNS 조작 유도"),
            ("APT", "지능형 지속 공격"),
            ("Zero-Day", "미공개 취약점"),
        ]),
    ]
    x0, y0 = 60, 210
    w, h, gx, gy = 580, 220, 20, 20
    for i, (title, color, items) in enumerate(cats):
        r = i // 2
        c = i % 2
        x = x0 + c * (w + gx)
        y = y0 + r * (h + gy)
        els.append(rect(x, y, w, h, fill=color))
        els.append(text(x + 16, y + 10, title, size=18, align="left"))
        for j, (nm, desc) in enumerate(items):
            ry = y + 44 + j * 28
            els.append(text(x + 20, ry, nm, size=13, align="left"))
            els.append(text(x + 220, ry, desc, size=12, align="left", color="#444"))

    # 하단 기출 포인트
    ky = 670
    els.append(rect(60, ky, 1180, 60, fill=COLORS["yellow"]))
    els.append(text(80, ky + 8, "기출 포인트", size=16, align="left"))
    els.append(text(80, ky + 32,
                    "• SQL Injection(DB) vs XSS(브라우저) 구분  • DoS vs DDoS (단일 vs 분산)  "
                    "• 각 공격 정의 → 이름 맞히기 빈출",
                    size=13, align="left", color="#c92a2a"))
    return els


# ---------------------------------------------------------------------------
# Card 4 — 네트워크 보안 공격 (SYN Flooding / Smurf / Watering Hole / 세션 하이재킹)
# ---------------------------------------------------------------------------
def card_network_attacks() -> list[dict]:
    els: list[dict] = []
    els += title_banner(40, 40, 1200, "네트워크 보안 공격",
                        "SYN Flooding · Smurf · Watering Hole · 세션 하이재킹")
    els += badge(1080, 48, "🔥 매회 출제")

    # 2x2 grid
    x0, y0 = 60, 130
    w, h, gx, gy = 590, 260, 20, 20

    # --- Card (1,1) SYN Flooding ---
    x, y = x0, y0
    els.append(rect(x, y, w, h, fill=COLORS["red"]))
    els.append(text(x + 16, y + 10, "SYN Flooding", size=20, align="left"))
    els.append(text(x + 16, y + 36, "TCP 3-way handshake 취약점 · DoS/DDoS",
                    size=12, align="left", color="#555"))
    # mini sequence
    cx1, cx2 = x + 60, x + 360
    sy = y + 76
    els.append(rect(cx1 - 50, sy, 100, 26, fill="#ffffff"))
    els.append(text(cx1 - 40, sy + 4, "Attacker", size=12, align="left"))
    els.append(rect(cx2 - 50, sy, 100, 26, fill="#ffffff"))
    els.append(text(cx2 - 40, sy + 4, "Server", size=12, align="left"))
    els.append(line(cx1, sy + 26, cx1, sy + 150))
    els.append(line(cx2, sy + 26, cx2, sy + 150))
    els += arrow(cx1, sy + 44, cx2, sy + 44, label="SYN (위조IP)")
    els += arrow(cx2, sy + 80, cx1, sy + 80, label="SYN-ACK")
    els.append(text(cx1 + 40, sy + 108, "ACK 없음 → 백로그 고갈", size=12, align="left", color="#c92a2a"))
    els.append(text(x + 16, y + h - 48, "방어: SYN Cookie · 방화벽 필터 · 임계값",
                    size=12, align="left", color="#1864ab"))
    els.append(text(x + 16, y + h - 28, "2025-2회 출제",
                    size=12, align="left", color="#c92a2a"))

    # --- Card (1,2) Smurf ---
    x, y = x0 + w + gx, y0
    els.append(rect(x, y, w, h, fill=COLORS["orange"]))
    els.append(text(x + 16, y + 10, "Smurf 공격", size=20, align="left"))
    els.append(text(x + 16, y + 36, "ICMP 브로드캐스트 증폭 · DDoS",
                    size=12, align="left", color="#555"))
    # Attacker → Broadcast → hosts → victim
    ax = x + 40
    bx = x + 220
    vx = x + 440
    ny = y + 100
    els.append(rect(ax - 40, ny, 80, 30, fill="#ffffff"))
    els.append(text(ax - 30, ny + 6, "Attacker", size=11, align="left"))
    els.append(rect(bx - 60, ny, 120, 30, fill="#ffffff"))
    els.append(text(bx - 52, ny + 6, "Broadcast Net", size=11, align="left"))
    els.append(rect(vx - 40, ny, 80, 30, fill="#ffffff"))
    els.append(text(vx - 30, ny + 6, "Victim", size=11, align="left"))
    els += arrow(ax + 40, ny + 15, bx - 60, ny + 15, label="ICMP\n(src=피해자)")
    # multiple replies to victim
    for dy in (-30, 0, 30):
        els += arrow(bx + 60, ny + 15 + dy * 0.2, vx - 40, ny + 15 + dy * 0.2)
    els.append(text(x + 16, y + 170, "원리: 출발지 IP를 피해자로 위조 →\n브로드캐스트로 보낸 ICMP Reply가 피해자에게 집중",
                    size=12, align="left", color="#444"))
    els.append(text(x + 16, y + h - 48, "방어: 라우터에서 브로드캐스트 ICMP 차단",
                    size=12, align="left", color="#1864ab"))
    els.append(text(x + 16, y + h - 28, "2024-3회 출제",
                    size=12, align="left", color="#c92a2a"))

    # --- Card (2,1) Watering Hole ---
    x, y = x0, y0 + h + gy
    els.append(rect(x, y, w, h, fill=COLORS["green"]))
    els.append(text(x + 16, y + 10, "Watering Hole", size=20, align="left"))
    els.append(text(x + 16, y + 36, "표적형 · APT 계열 · 사전 감염 후 대기",
                    size=12, align="left", color="#555"))
    # Step diagram: Attacker → infect site → victim visits → infected
    sy = y + 84
    steps = [
        ("공격자", COLORS["gray"]),
        ("자주 방문 사이트\n악성코드 삽입", "#ffffff"),
        ("피해자 방문", "#ffffff"),
        ("자동 감염", COLORS["red"]),
    ]
    sx = x + 20
    for i, (t, c) in enumerate(steps):
        els.append(rect(sx, sy, 130, 64, fill=c))
        els.append(text(sx + 10, sy + 14, t, size=12, align="left"))
        if i < len(steps) - 1:
            els += arrow(sx + 130, sy + 32, sx + 140, sy + 32)
        sx += 140
    els.append(text(x + 16, y + 170, "원리: 공격 대상이 자주 방문하는 사이트를\n미리 감염시켜 두고 방문을 기다림",
                    size=12, align="left", color="#444"))
    els.append(text(x + 16, y + h - 48, "방어: 브라우저/플러그인 최신 패치 · 행위 기반 탐지",
                    size=12, align="left", color="#1864ab"))
    els.append(text(x + 16, y + h - 28, "2024-1회 출제",
                    size=12, align="left", color="#c92a2a"))

    # --- Card (2,2) Session Hijacking ---
    x, y = x0 + w + gx, y0 + h + gy
    els.append(rect(x, y, w, h, fill=COLORS["purple"]))
    els.append(text(x + 16, y + 10, "Session Hijacking", size=20, align="left"))
    els.append(text(x + 16, y + 36, "세션 하이재킹 · 인증 세션 탈취",
                    size=12, align="left", color="#555"))
    # Diagram: Client — Server, Attacker sniffs session
    ucx = x + 60
    scx = x + 440
    acx = x + 250
    ny = y + 96
    els.append(rect(ucx - 50, ny, 100, 30, fill="#ffffff"))
    els.append(text(ucx - 38, ny + 6, "Client", size=12, align="left"))
    els.append(rect(scx - 50, ny, 100, 30, fill="#ffffff"))
    els.append(text(scx - 38, ny + 6, "Server", size=12, align="left"))
    els += arrow(ucx + 50, ny + 15, scx - 50, ny + 15, label="인증 세션")
    els.append(rect(acx - 60, ny + 60, 120, 30, fill=COLORS["red"]))
    els.append(text(acx - 52, ny + 66, "Attacker", size=12, align="left"))
    els += arrow(acx, ny + 60, acx, ny + 30, label="세션ID 탈취")
    els += arrow(acx + 20, ny + 75, scx - 50, ny + 25, label="무단 접속")
    els.append(text(x + 16, y + 180, "취약점: TCP 시퀀스 예측 · 세션 ID 스니핑",
                    size=12, align="left", color="#444"))
    els.append(text(x + 16, y + h - 48, "방어: HTTPS · 로그인 후 세션 재생성 · HttpOnly/Secure",
                    size=12, align="left", color="#1864ab"))
    els.append(text(x + 16, y + h - 28, "2025-1회 출제",
                    size=12, align="left", color="#c92a2a"))

    return els


CARDS = [
    ("nw-protocol-001.excalidraw", card_osi),
    ("nw-protocol-003.excalidraw", card_app_protocols),
    ("nw-security-001.excalidraw", card_security_types),
    ("nw-security-003.excalidraw", card_network_attacks),
]


def main() -> None:
    for name, builder in CARDS:
        els = builder()
        path = save(els, name)
        print(f"  ✓ {path.name}  ({len(els)} elements)")
    print(f"\n생성 완료: {len(CARDS)}개 → {OUT_DIR}")


if __name__ == "__main__":
    main()
