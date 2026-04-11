---
title: "네트워크 보안 공격 (SYN Flooding, Smurf, Watering Hole, 세션 하이재킹)"
subject: "NW (네트워크)"
priority: 3
frequency: "🔥 매회 출제"
tags:
  - nw
  - priority-3
---

# 네트워크 보안 공격 (SYN Flooding, Smurf, Watering Hole, 세션 하이재킹)

> 🔥 **매회 출제** (priority 3)

![[nw-security-003.svg]]

## 🌱 왜 배우나

전화 상담실에 장난 전화가 한꺼번에 수천 통 걸려 와 정작 진짜 고객의 전화는 연결조차 안 되는 상황을 상상해 보자. TCP 연결 요청(SYN)만 계속 보내고 마지막 응답(ACK)은 보내지 않으면 서버는 반쯤 열린 연결을 붙잡은 채 자리를 비울 수 없고, 결국 정상 사용자도 접속하지 못한다. 마치 식당에 가짜 예약 전화가 밀려들어 빈 테이블이 남아돌지만 예약 장부는 꽉 차 있는 것과 같다. 이런 공격들이 각각 다른 프로토콜 취약점(3-way handshake, ICMP, 세션 ID)을 노리기 때문에 원리별로 구분해 방어 전략을 세우려고 이 개념이 등장했다.

## 📖 핵심 개념

네트워크 보안 공격은 DoS/DDoS 계열(SYN Flooding, Smurf)과 세션/접근 탈취 계열(세션 하이재킹, Watering Hole)로 구분된다. 각 공격의 원리(어떤 취약점을 이용하는가)와 방어 방법이 시험 핵심이다. TCP 3-way handshake 취약점을 이용한 SYN Flooding은 가장 빈출 주제다.

**핵심 용어**

- **원리**: TCP 3-way handshake 취약점 이용. 다수의 SYN 패킷을 위조된 IP로 전송 → 서버가 SYN-ACK을 보내도 ACK 미수신 → 서버의 백로그(backlog) 큐 고갈
- **분류**: DoS/DDoS 공격
- **방어**: SYN Cookie, 방화벽 필터링, 연결 임계값 설정
- **원리**: 출발지 IP를 피해자 IP로 위조 후, 브로드캐스트 주소로 ICMP Echo Request 전송 → 네트워크 내 모든 호스트가 피해자에게 Reply 집중
- **분류**: DDoS (증폭 공격, Amplification Attack)
- **방어**: 라우터에서 외부→내부 브로드캐스트 패킷 차단
- **원리**: 공격 대상이 자주 방문하는 웹사이트를 사전에 악성코드로 감염시켜 대기 → 피해자가 방문 시 자동 감염
- **분류**: 표적형 공격 (APT 계열)
- **방어**: 웹 브라우저/플러그인 최신 패치, 행위 기반 탐지
- **원리**: 합법적인 사용자의 인증된 세션 ID를 탈취하여 해당 세션에 무단 참여
- **취약점**: TCP 시퀀스 번호 예측, 세션 ID 스니핑
- **방어**: HTTPS 사용, 세션 ID 재생성(로그인 후), HttpOnly/Secure 쿠키 속성

## ✅ 이해 확인

1. **SYN Flooding** 공격이 TCP의 어떤 단계를 악용하는가?
   <details><summary>정답</summary>3-way handshake 중 마지막 ACK를 보내지 않아, 서버의 백로그 큐에 반쯤 열린 연결이 가득 차게 만든다.</details>
2. **Smurf 공격**이 "증폭(Amplification) 공격"으로 분류되는 이유는?
   <details><summary>정답</summary>출발지 IP를 피해자로 위조한 ICMP Echo Request를 브로드캐스트 주소로 보내면, 네트워크 내 모든 호스트가 피해자에게 Reply를 돌려줘 공격 트래픽이 수십~수백 배로 증폭된다.</details>
3. **Watering Hole**과 **세션 하이재킹**의 공격 방식은 어떻게 다른가?
   <details><summary>정답</summary>Watering Hole은 표적이 자주 방문하는 웹사이트를 미리 감염시켜 "기다리는" 수동형 표적 공격(APT 계열). 세션 하이재킹은 이미 인증된 사용자의 세션 ID를 탈취해 "가로채는" 능동형 공격. 전자는 배포 경로, 후자는 인증 상태를 노린다.</details>

## 🎯 시험 응용

> **2025-2회**: SYN Flooding 공격 원리 출제 — "TCP 3-way handshake 취약점 이용" > **2025-1회**: 세션 하이재킹 출제 — "인증된 세션을 가로채는 공격" > **2024-1회**: Watering Hole 출제 — "자주 방문하는 사이트를 감염시켜 대기" > **2024-3회**: Smurf 공격 출제 — "브로드캐스트 주소를 이용한 증폭 DDoS"

## 🔗 연결 개념

- [[nw-security-001|보안 공격 유형]]
- `nw-protocol-002`
