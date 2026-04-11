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

DDL로 공책의 칸(테이블 구조)을 만들었다면, 이제 실제로 **글씨를 쓰고, 읽고, 지우고, 고치는** 작업이 필요하다. 데이터가 저장되고 꺼내지지 않는 DB는 창고에 물건을 넣기만 하고 한 번도 꺼낼 수 없는 자판기와 같다. DML은 음식점의 "주문 받기·음식 내오기·주문 수정·주문 취소"에 해당하는 일상 업무다. 특히 SELECT는 가장 자주 쓰이면서 **작성 순서와 실행 순서가 다르다**는 함정이 있어 시험에서도 자주 출제된다. 그래서 DML의 각 명령어와 SELECT의 절 순서를 정확히 익혀야 한다.

## 📖 핵심 개념

DML(Data Manipulation Language, 데이터 조작어)은 테이블에 저장된 **데이터를 조회·삽입·수정·삭제**하는 SQL 명령어다. DDL과 달리 **자동 커밋되지 않으며** COMMIT/ROLLBACK으로 트랜잭션을 제어할 수 있다. SELECT 구문의 절 순서는 시험 단골 출제 포인트다.

**핵심 용어**

- **SELECT 작성(문법) 순서**: `SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY` (순서 암기 필수)
- **SELECT 실행 순서**: `FROM → WHERE → GROUP BY → 집계함수 → HAVING → SELECT → ORDER BY` (작성 순서와 다름에 주의)
- **INSERT 두 가지 형태**: `INSERT INTO 테이블(컬럼) VALUES(값)` (직접 삽입) vs `INSERT INTO 테이블(컬럼) SELECT ... FROM ...` (조회 결과 삽입)
- **UPDATE**: `UPDATE 테이블 SET 컬럼=값 WHERE 조건` — WHERE 생략 시 전체 행 수정
- **DELETE**: `DELETE FROM 테이블 WHERE 조건` — WHERE 생략 시 전체 행 삭제 (TRUNCATE와 달리 ROLLBACK 가능, 로그 남김)
- **서브쿼리**: WHERE, FROM, SELECT 절에서 중첩 SELECT 사용 가능; 상관 서브쿼리는 외부 쿼리 행마다 실행

## ✅ 이해 확인

1. `UPDATE 학생 SET 학년 = 2` 처럼 WHERE 절을 생략하면 어떤 일이 일어나는가?
   <details><summary>정답</summary>테이블의 **모든 행**의 학년이 2로 바뀐다. WHERE 생략은 전체 행 대상이라는 점이 함정 포인트다.</details>
2. SELECT 문의 **작성 순서**를 SELECT부터 차례로 쓰면?
   <details><summary>정답</summary>SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY.</details>
3. SELECT 문의 **실행 순서**는 작성 순서와 어떻게 다른가?
   <details><summary>정답</summary>실행은 FROM → WHERE → GROUP BY → 집계함수 → HAVING → SELECT → ORDER BY 순이다. 데이터를 먼저 고른 뒤(FROM/WHERE) 묶고(GROUP BY) 최종적으로 SELECT로 컬럼을 선택한다.</details>

## 🎯 시험 응용

> **2024-2회**: INSERT INTO...SELECT 구문에서 INSERT와 SELECT 키워드 빈칸 채우기로 출제됨. VALUES를 쓰는 단순 삽입과 SELECT를 쓰는 복사 삽입의 차이를 반드시 구분할 것. SELECT 절의 실행 순서(FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY)와 작성 순서를 혼동하지 말 것.

## 🔗 연결 개념

- [[db-sql-001|DDL 명령어 (CREATE, ALTER, DROP, TRUNCATE)]]
- [[db-sql-004|집계함수와 GROUP BY (COUNT, SUM, AVG, MAX, MIN, HAVING)]]
- `db-transaction-001`
