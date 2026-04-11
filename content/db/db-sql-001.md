---
title: "DDL 명령어 (CREATE, ALTER, DROP, TRUNCATE)"
subject: "DB (데이터베이스)"
priority: 3
frequency: "🔥 매회 출제"
tags:
  - db
  - priority-3
---

# DDL 명령어 (CREATE, ALTER, DROP, TRUNCATE)

> 🔥 **매회 출제** (priority 3)

![[db-sql-001.svg]]

## 🌱 왜 배우나

데이터베이스를 "공책"이라고 하면, 먼저 해야 할 일은 **어떤 칸을 만들지 그리는 일**이다. 이름 칸, 전화번호 칸, 주소 칸. 나중에 주소 칸이 너무 좁아 늘려야 할 수도 있고, 필요 없어진 칸을 지워야 할 수도 있다. DDL이 없다면 테이블을 만들 수도, 고칠 수도, 지울 수도 없어 DB는 아무 일도 시작할 수 없다. 마치 가구 없는 집에 이사해 놓고 옷장·책상을 살 방법이 없는 상황이다. 그래서 데이터를 "담기 전에 그릇부터 설계"하는 언어가 필요해졌고, 그게 DDL이다.

## 📖 핵심 개념

DDL(Data Definition Language, 데이터 정의어)은 데이터베이스 **스키마(구조)**를 정의, 변경, 삭제하는 SQL 명령어 집합이다. DDL 명령어는 실행 즉시 **자동 커밋(Auto Commit)**되므로 ROLLBACK이 불가능하다. 대상은 테이블, 뷰, 인덱스, 스키마, 도메인 등이다.

**핵심 용어**

- **CREATE**: 테이블, 뷰, 인덱스 등 객체 생성. `CREATE TABLE 학생 (학번 INT PRIMARY KEY, 이름 VARCHAR(20) NOT NULL);`
- **ALTER**: 기존 객체 구조 변경. `ADD`(컬럼 추가), `MODIFY`(컬럼 타입 변경), `DROP COLUMN`(컬럼 삭제), `RENAME`(이름 변경)
- **DROP**: 객체 완전 삭제(구조+데이터). `CASCADE`는 참조하는 모든 객체 함께 삭제, `RESTRICT`는 참조 객체 있으면 삭제 거부
- **TRUNCATE**: 테이블의 **모든 데이터만 삭제**(구조 유지). DROP과 달리 테이블 자체는 남으며, DELETE와 달리 로그를 남기지 않아 ROLLBACK 불가
- **제약조건**: PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, DEFAULT — CREATE/ALTER 시 함께 정의

## ✅ 이해 확인

1. 테이블의 구조는 그대로 두고 데이터만 모두 비우고 싶을 때 사용하는 DDL 명령어는?
   <details><summary>정답</summary>TRUNCATE — 구조는 유지하고 모든 행을 제거한다. DELETE와 달리 롤백이 불가하다.</details>
2. 다른 테이블이 참조 중인 테이블을 DROP 하려고 한다. 참조 테이블까지 함께 지우려면 어떤 옵션이 필요한가?
   <details><summary>정답</summary>CASCADE — 참조하는 모든 객체를 함께 삭제한다. RESTRICT는 참조가 있으면 삭제를 거부한다.</details>
3. DELETE와 TRUNCATE의 차이 세 가지를 들어 보라.
   <details><summary>정답</summary>(1) DELETE는 DML, TRUNCATE는 DDL. (2) DELETE는 WHERE로 선택 삭제 가능, TRUNCATE는 전체만. (3) DELETE는 로그를 남겨 ROLLBACK 가능, TRUNCATE는 자동 커밋되어 ROLLBACK 불가.</details>

## 🎯 시험 응용

> DDL vs DML vs DCL 분류가 단골 출제된다. **DDL = CREATE/ALTER/DROP/TRUNCATE**, **DML = SELECT/INSERT/UPDATE/DELETE**, **DCL = GRANT/REVOKE**. TRUNCATE는 DDL이므로 AUTO COMMIT 된다는 점, CASCADE/RESTRICT 옵션은 DROP에서 참조 무결성 처리 방식이라는 점을 구분할 것.

## 🔗 연결 개념

- [[db-sql-002|JOIN 종류 (INNER, LEFT, RIGHT, FULL OUTER, CROSS, SELF)]]
- [[db-modeling-001|정규화 단계 (1NF~BCNF) — 각 단계 조건과 이상 현상]]
