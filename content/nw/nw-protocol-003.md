---
title: "응용 계층 프로토콜 (HTTP, HTTPS, FTP, SMTP, DNS, SNMP, SSH)"
subject: "NW (네트워크)"
priority: 3
frequency: "🔥 매회 출제"
tags:
  - nw
  - priority-3
---

# 응용 계층 프로토콜 (HTTP, HTTPS, FTP, SMTP, DNS, SNMP, SSH)

> 🔥 **매회 출제** (priority 3)

![[nw-protocol-003.svg]]

## 핵심 개념

OSI 7계층 중 응용 계층(Layer 7)에 위치한 프로토콜들은 각각 고유한 포트 번호와 기능을 가진다. 정보처리기사 시험에서는 프로토콜 약어, 포트 번호, 역할의 매핑이 반드시 출제된다. 특히 SSH(22), HTTP(80), HTTPS(443), FTP(20/21), SMTP(25), DNS(53), SNMP(161) 조합은 핵심 암기 대상이다.

## 🎯 기출 포인트

> **2025-2회**: SSH 포트 번호 22 직접 출제 — "SSH가 사용하는 포트 번호는?" > **매회 반복**: 프로토콜 약어와 포트 번호 매핑 (특히 FTP 20/21 이중 포트 주의) > **혼동 주의**: FTP는 20(데이터 전송)과 21(제어 명령) 두 포트를 사용함 > **SMTP vs POP3**: SMTP는 **송신(25)**, POP3는 **수신(110)** — 방향으로 구분

## 연결 개념

- [[nw-protocol-001|OSI 7계층 모델]]
- `nw-security-002`
