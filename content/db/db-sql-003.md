---
title: "DML 명령어 (SELECT, INSERT, UPDATE, DELETE)"
subject: "DB (데이터베이스)"
priority: 3
frequency: "🔥 매회 출제"
tags:
  - db
  - priority-3
---

# DML 명령어 (SELECT, INSERT, UPDATE, DELETE)

> 🔥 **매회 출제** (priority 3)

![[db-sql-003.svg]]

## 🌱 왜 배우나

DDL(데이터 정의어)로 공책의 칸(표 구조)을 만들었다면, 이제 실제로 글씨를 쓰고, 읽고, 지우고, 고치는 작업이 필요하다. 데이터가 저장만 되고 꺼낼 수 없는 데이터베이스는 물건을 넣기만 하고 뺄 수 없는 자판기와 같다. DML(Data Manipulation Language, 데이터 조작어)은 음식점에서 주문 받기(INSERT), 음식 내오기(SELECT), 주문 수정(UPDATE), 주문 취소(DELETE)에 해당한다. 특히 SELECT는 가장 자주 쓰이면서 작성 순서와 실행 순서가 다르다는 함정이 있어 시험에서 자주 출제된다.

## 📖 핵심 개념

DML(Data Manipulation Language, 데이터 조작어)은 표(테이블)에 저장된 데이터를 조회하고, 넣고, 고치고, 지우는 SQL 명령어다. DDL(데이터 정의어)과 달리 자동 커밋(실행 즉시 확정)되지 않으며, COMMIT(확정)과 ROLLBACK(되돌리기)으로 트랜잭션(Transaction, 하나의 작업 단위)을 제어할 수 있다. SELECT 구문의 작성 순서와 실행 순서가 다르다는 점이 시험 단골 출제 포인트다.

## 🔍 시각화

```
DML 명령어 네 가지:

SELECT ──▶ 데이터 조회 (읽기)      "장부에서 찾아보기"
INSERT ──▶ 데이터 삽입 (쓰기)      "장부에 새 줄 추가"
UPDATE ──▶ 데이터 수정 (고치기)    "장부의 기존 값 변경"
DELETE ──▶ 데이터 삭제 (지우기)    "장부에서 줄 지우기"

⚠ 네 명령 모두 ROLLBACK 가능 (DDL과 다름)

SELECT 절 순서 비교:
  작성 순서: SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY
  실행 순서: FROM → WHERE → GROUP BY → 집계함수 → HAVING → SELECT → ORDER BY
             ~~~                                             ~~~~~~
             데이터를 먼저 가져온 뒤                        마지막에 열 선택
```

## ↔️ 이웃 개념 구분

- **DML vs DDL**: DML은 데이터(값)를 다루고, DDL은 구조(표 자체)를 다룬다. DML은 ROLLBACK 가능, DDL은 자동 커밋.
- **DELETE vs TRUNCATE**: DELETE는 DML이라 WHERE로 선택 삭제 가능하고 ROLLBACK 가능. TRUNCATE는 DDL이라 전체만 삭제되고 ROLLBACK 불가.

**핵심 용어**

- **SELECT 작성(문법) 순서**: `SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY` (이 순서대로 코드를 쓴다).
- **SELECT 실행 순서**: `FROM → WHERE → GROUP BY → 집계함수 → HAVING → SELECT → ORDER BY` (데이터베이스가 실제로 처리하는 순서. 작성 순서와 다르다).
- **INSERT 두 가지 형태**: `INSERT INTO 표(열) VALUES(값)` — 값을 직접 넣기. `INSERT INTO 표(열) SELECT ... FROM ...` — 다른 표에서 조회한 결과를 넣기.
- **UPDATE**: `UPDATE 표 SET 열=값 WHERE 조건` — WHERE를 생략하면 모든 행이 수정된다.
- **DELETE**: `DELETE FROM 표 WHERE 조건` — WHERE를 생략하면 모든 행이 삭제된다. TRUNCATE와 달리 ROLLBACK 가능하고 로그가 남는다.
- **서브쿼리(Subquery)**: SELECT 안에 또 다른 SELECT를 넣는 것. WHERE, FROM, SELECT 절에서 사용 가능. 상관 서브쿼리(Correlated Subquery)는 바깥 쿼리의 행마다 안쪽 쿼리가 실행된다.

## ✅ 스스로 가르쳐보기

**질문**: 친구에게 "SELECT 문의 작성 순서와 실행 순서가 왜 다르고, 그 차이가 실무에서 어떤 함정을 만드는지" 설명해 보라.

체크포인트:
- [ ] 작성 순서 6개 절을 순서대로 말할 수 있는가?
- [ ] 실행 순서가 FROM부터 시작하는 이유를 설명했는가?
- [ ] UPDATE·DELETE에서 WHERE를 빠뜨리면 어떤 일이 생기는지 말했는가?
- [ ] INSERT의 두 가지 형태(VALUES vs SELECT)를 구분했는가?

## 🎯 시험 응용

> **2024-2회**: INSERT INTO...SELECT 구문에서 INSERT와 SELECT 키워드 빈칸 채우기로 출제됨. VALUES를 쓰는 단순 삽입과 SELECT를 쓰는 복사 삽입의 차이를 반드시 구분할 것. SELECT 절의 실행 순서(FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY)와 작성 순서를 혼동하지 말 것.

## 🔗 연결 개념

- [[db-sql-001|DDL 명령어 (CREATE, ALTER, DROP, TRUNCATE)]]
- [[db-sql-004|집계함수와 GROUP BY (COUNT, SUM, AVG, MAX, MIN, HAVING)]]
- `db-transaction-001`
