---
title: "보안 공격 유형"
subject: "NW (네트워크)"
priority: 3
frequency: "🔥 매회 출제"
tags:
  - nw
  - priority-3
---

# 보안 공격 유형

> 🔥 **매회 출제** (priority 3)

![[nw-security-001.svg]]

## 🌱 왜 배우나

입력창에 무엇을 넣든 의심 없이 DB에 넘기는 웹사이트를 상상해 보자. 누군가 로그인 폼에 SQL 구문을 적어 넣으면 회원 정보 전체가 유출될 수 있고, 게시글에 스크립트를 심으면 다른 사용자의 쿠키가 공격자에게 전송된다. 마치 건물 출입문을 잠그지 않아 아무나 들어와 서류를 뒤지거나, 다른 사람 신분증을 훔쳐 쓰는 것과 같다. 이런 다양한 공격 수법이 각기 다른 원리로 동작하기 때문에, 방어를 설계하기 전에 공격의 분류 체계부터 정확히 알아야 해서 이 개념이 등장했다.

## 📖 핵심 개념

네트워크 및 웹 보안 공격은 시스템의 가용성, 기밀성, 무결성을 위협하는 행위이다. 정보처리기사에서는 각 공격의 원리, 대상, 대응 방법을 구분할 수 있어야 한다. 공격 유형은 서비스 거부 공격, 인젝션 공격, 세션 탈취 공격, 네트워크 도청 등으로 분류된다.

**핵심 용어**

- **DoS/DDoS**: 서비스 거부 공격. DoS는 단일 공격자가, DDoS는 다수의 좀비 PC(봇넷)가 대량 트래픽을 보내 서비스를 마비시킴. SYN Flood, Smurf, Land Attack, Ping of Death 등
- **SQL Injection**: 입력 필드에 악의적인 SQL 구문을 삽입하여 데이터베이스를 비정상적으로 조작. 대응: PreparedStatement(매개변수화 쿼리), 입력 값 검증
- **XSS(Cross-Site Scripting)**: 악성 스크립트를 웹 페이지에 삽입하여 다른 사용자의 브라우저에서 실행. 쿠키·세션 탈취. 대응: 입출력 값 이스케이프 처리, CSP 헤더
- **CSRF(Cross-Site Request Forgery)**: 인증된 사용자가 자신의 의지와 무관하게 공격자가 의도한 요청을 서버에 전송하게 만드는 공격. 대응: CSRF 토큰, Referer 검증
- **스니핑(Sniffing)**: 네트워크상의 패킷을 도청하여 정보를 수집. 대응: 암호화 통신(HTTPS, VPN), 스위칭 환경 사용

## ✅ 이해 확인

1. **DoS**와 **DDoS**의 차이는 무엇인가?
   <details><summary>정답</summary>DoS는 단일 공격자, DDoS는 다수의 좀비 PC(봇넷)를 동원한 분산 공격. 규모와 차단 난이도가 다르다.</details>
2. 사용자가 입력한 값에 `<script>` 태그를 넣어 다른 사용자의 쿠키를 탈취하는 공격은 무엇이며, 대응 방법은?
   <details><summary>정답</summary>**XSS(Cross-Site Scripting)**. 대응: 입출력 값 이스케이프 처리, CSP 헤더 설정, HttpOnly 쿠키 속성.</details>
3. **SQL Injection**, **XSS**, **CSRF**는 각각 어디를 노리는 공격인가?
   <details><summary>정답</summary>SQL Injection은 서버의 DB, XSS는 다른 사용자의 브라우저, CSRF는 인증된 사용자가 의도하지 않은 요청을 서버에 보내게 만드는 공격. "대상"이 핵심 구분점이다.</details>

## 🎯 시험 응용

> 각 공격 유형의 정의를 제시하고 공격 이름을 묻는 문제가 빈출된다. 특히 **SQL Injection**과 **XSS**의 차이(DB 조작 vs 브라우저 스크립트 실행), **DoS**와 **DDoS**의 차이(단일 vs 분산)를 명확히 구분해야 한다. DDoS 세부 공격인 **SYN Flood**(TCP 3-Way Handshake 악용, 대량 SYN 패킷 전송)와 **Smurf Attack**(ICMP 브로드캐스트 악용)도 서술형으로 출제된다.

## 🔗 연결 개념

- `nw-security-002`
- [[nw-protocol-001|OSI 7계층 모델]]
