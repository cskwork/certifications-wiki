---
title: 정보처리기사 2026 — 빈출 개념 다이어그램
created: 2026-04-10
updated: 2026-04-10
type: summary
exam: 정보처리기사
target_year: 2026
---

# 정보처리기사 2026 — 출제빈도 순 개념 다이어그램

각 개념을 Excalidraw 다이어그램 한 장으로 시각화한 학습 노트.
**빈출 순**(🔥 매회 → ⭐ 자주 → · 가끔)으로 정렬. Obsidian Excalidraw 플러그인에서
바로 열고 편집 가능하며, `excalidraw.com`에 드래그하면 웹에서도 열린다.

## 범례
- 🔥 **매회 출제** (priority 3) — 무조건 암기
- ⭐ **자주 출제** (priority 2) — 이해 + 예시 풀이
- · **가끔 출제** (priority 1) — 빠르게 훑기만

## 현재 상태
priority 3 전량 **30 / 30 완료**. 5개 과목 모두 생성.

| 과목 | 완료 | 파일 위치 | 생성기 |
|---|---|---|---|
| 🗄️ DB (데이터베이스) | 6/6 | `db/` | `_generators/gen_db.py` |
| 📡 NW (네트워크) | 4/4 | `nw/` | `_generators/gen_nw.py` |
| 🖥️ OS · 유지보수 | 3/3 | `os/` | `_generators/gen_os.py` |
| 💻 PG (프로그래밍 언어) | 11/11 | `pg/` | `_generators/gen_pg.py` |
| 🛠️ SE (소프트웨어 공학) | 6/6 | `se/` | `_generators/gen_se.py` |

다음 단계: priority 2 (31장), priority 1 (3장) 확장은 별도 세션.

---

## 🗄️ DB (데이터베이스) — 6/6

| 빈도 | 개념 | 다이어그램 | 핵심 |
|---|---|---|---|
| 🔥 | 릴레이션 구성 요소 | [[db/db-relation-001.svg\|보기]] | Degree=속성 수, Cardinality=튜플 수 |
| 🔥 | 정규화 단계 (1NF~BCNF) | [[db/db-modeling-001.svg\|보기]] | 도·부·이·결·다·조 |
| 🔥 | DDL 명령어 | [[db/db-sql-001.svg\|보기]] | CREATE/ALTER/DROP/TRUNCATE — 자동 커밋 |
| 🔥 | DML 명령어 | [[db/db-sql-003.svg\|보기]] | SELECT 작성/실행 순서 |
| 🔥 | JOIN 종류 | [[db/db-sql-002.svg\|보기]] | INNER/LEFT/RIGHT/FULL/CROSS/SELF |
| 🔥 | 집계함수 & GROUP BY | [[db/db-sql-004.svg\|보기]] | COUNT(*)만 NULL 포함 |

### 임베드 미리보기
![[db/db-relation-001.svg]]
![[db/db-modeling-001.svg]]
![[db/db-sql-001.svg]]
![[db/db-sql-003.svg]]
![[db/db-sql-002.svg]]
![[db/db-sql-004.svg]]

---

## 📡 NW (네트워크) — 4/4

| 빈도 | 개념 | 다이어그램 | 핵심 |
|---|---|---|---|
| 🔥 | OSI 7계층 모델 | [[nw/nw-protocol-001.svg\|보기]] | 물데네전세표응 / PDU·장비·프로토콜 |
| 🔥 | 응용 계층 프로토콜 | [[nw/nw-protocol-003.svg\|보기]] | HTTP 80, HTTPS 443, SSH 22, FTP 20/21 |
| 🔥 | 보안 공격 유형 | [[nw/nw-security-001.svg\|보기]] | CIA 3요소 기반 분류 |
| 🔥 | 네트워크 보안 공격 | [[nw/nw-security-003.svg\|보기]] | SYN Flooding · Smurf · Watering Hole · 세션 하이재킹 |

### 임베드 미리보기
![[nw/nw-protocol-001.svg]]
![[nw/nw-protocol-003.svg]]
![[nw/nw-security-001.svg]]
![[nw/nw-security-003.svg]]

---

## 🖥️ OS · 유지보수 — 3/3

| 빈도 | 개념 | 다이어그램 | 핵심 |
|---|---|---|---|
| 🔥 | CPU 스케줄링 알고리즘 | [[os/mt-scheduling-001.svg\|보기]] | FCFS/SJF/SRT/RR/우선순위 + 간트 차트 |
| 🔥 | 테스트 기법 (화이트/블랙) | [[os/mt-testing-001.svg\|보기]] | 구조 기반 vs 명세 기반 |
| 🔥 | 테스트 커버리지 | [[os/mt-testing-003.svg\|보기]] | 문장 ⊂ 분기 ⊂ 조건 ⊂ MC/DC ⊂ 경로 |

### 임베드 미리보기
![[os/mt-scheduling-001.svg]]
![[os/mt-testing-001.svg]]
![[os/mt-testing-003.svg]]

---

## 💻 PG (프로그래밍 언어) — 11/11

| 빈도 | 개념 | 다이어그램 | 핵심 |
|---|---|---|---|
| 🔥 | 연결 리스트 | [[pg/pg-data-structure-002.svg\|보기]] | 단일 / 이중 / 원형 + 배열 비교 |
| 🔥 | C 포인터 기초 | [[pg/pg-language-001.svg\|보기]] | `&a`, `*p`, 메모리 주소 |
| 🔥 | Java 상속과 오버라이딩 | [[pg/pg-language-003.svg\|보기]] | extends + 오버라이딩 4대 규칙 |
| 🔥 | Python 핵심 문법 | [[pg/pg-language-004.svg\|보기]] | 들여쓰기·컬렉션·슬라이싱 |
| 🔥 | C 배열과 반복문 | [[pg/pg-language-007.svg\|보기]] | 1차원·2차원 메모리 + for 3요소 |
| 🔥 | C 재귀 함수 | [[pg/pg-language-008.svg\|보기]] | 종료조건 + 호출 스택 |
| 🔥 | C 진수 변환 & 비트 연산 | [[pg/pg-language-010.svg\|보기]] | 2/8/10/16 변환 + 비트 연산자 |
| 🔥 | Java 예외처리 | [[pg/pg-language-011.svg\|보기]] | try → catch → finally + Throwable |
| 🔥 | Java 재귀함수 | [[pg/pg-language-013.svg\|보기]] | 호출 트리 + 역순 출력 |
| 🔥 | Java String 메서드 | [[pg/pg-language-014.svg\|보기]] | == vs equals 함정 |
| 🔥 | Python 문자열 메서드 | [[pg/pg-language-017.svg\|보기]] | 슬라이싱 `[::]` + split/join |

### 임베드 미리보기
![[pg/pg-data-structure-002.svg]]
![[pg/pg-language-001.svg]]
![[pg/pg-language-003.svg]]
![[pg/pg-language-004.svg]]
![[pg/pg-language-007.svg]]
![[pg/pg-language-008.svg]]
![[pg/pg-language-010.svg]]
![[pg/pg-language-011.svg]]
![[pg/pg-language-013.svg]]
![[pg/pg-language-014.svg]]
![[pg/pg-language-017.svg]]

---

## 🛠️ SE (소프트웨어 공학) — 6/6

| 빈도 | 개념 | 다이어그램 | 핵심 |
|---|---|---|---|
| 🔥 | 모듈 응집도 7단계 | [[se/se-cohesion-001.svg\|보기]] | 기순통절시논우 (강→약) |
| 🔥 | 모듈 결합도 6단계 | [[se/se-coupling-001.svg\|보기]] | 자스제외공내 (약→강, 반대 방향) |
| 🔥 | GoF 생성 패턴 5가지 | [[se/se-design-001.svg\|보기]] | Singleton·Factory·AbsFactory·Builder·Prototype |
| 🔥 | GoF 구조 패턴 7가지 | [[se/se-design-002.svg\|보기]] | Adapter·Bridge·Composite·Decorator·Facade·Flyweight·Proxy |
| 🔥 | GoF 행위 패턴 11가지 | [[se/se-design-003.svg\|보기]] | Strategy vs State 구분 |
| 🔥 | UML 다이어그램 분류 | [[se/se-requirements-001.svg\|보기]] | 구조 6 / 행위 7 |

### 임베드 미리보기
![[se/se-cohesion-001.svg]]
![[se/se-coupling-001.svg]]
![[se/se-design-001.svg]]
![[se/se-design-002.svg]]
![[se/se-design-003.svg]]
![[se/se-requirements-001.svg]]

---

## 사용법
1. Obsidian 파일 트리에서 `.excalidraw` 파일 클릭 → 플러그인 뷰어로 열림.
2. 웹에서 열고 싶다면 `excalidraw.com`에 파일을 드래그 & 드롭.
3. 편집 후 동일 이름으로 저장하면 임베드 미리보기도 자동 갱신.
4. 전체 재생성:
   ```bash
   cd _generators
   python3 gen_db.py && python3 gen_nw.py && python3 gen_os.py && python3 gen_pg.py && python3 gen_se.py
   ```

## 원본 카드
카드 원문(Markdown)은 `~/Documents/PARA/Resource/bite-size-study/content/cards/` 아래 과목별 폴더.
다이어그램은 원문의 "핵심 개념 / 키워드 / 기출 포인트" 섹션을 시각화한 요약판.

## 다음 단계 로드맵
- [ ] priority 2 (⭐ 자주) 31장 확장 — DB 4, NW 6, OS 6, PG 13, SE 2
- [ ] priority 1 (· 가끔) 3장 확장
- [ ] GitHub Pages 공개 — Obsidian Publish 또는 Quartz로 정적 빌드
- [ ] 각 다이어그램에 퀴즈 카드 링크 (bite-size-study 연동)
