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

이사 간 집에 옷장도 책상도 없다면 옷과 책을 둘 곳이 없다. 데이터베이스도 똑같다. 데이터를 넣기 전에 표(테이블)부터 만들어 두어야 한다. 나중에 주소 칸이 좁으면 늘리고, 필요 없어진 칸은 지워야 한다. 이런 "그릇 만들기" 작업을 담당하는 언어가 DDL(Data Definition Language, 데이터 정의어)이다. DDL이 없으면 데이터베이스는 아무 일도 시작할 수 없다.

## 📖 핵심 개념

DDL은 데이터베이스의 구조, 즉 스키마(Schema — 표의 이름·열·타입 같은 뼈대)를 만들고 바꾸고 지우는 SQL(Structured Query Language) 명령어 모음이다. DDL이 다루는 대상은 테이블, 뷰(View, 가상 테이블), 인덱스(Index, 검색 속도를 높이는 색인), 스키마 등이다. 한 가지 중요한 특성은 **자동 커밋**이다. DDL은 실행하는 순간 바로 확정되어 되돌릴 수 없다. 즉 ROLLBACK(되돌리기)이 불가능하다. 실수로 DROP 한 번이면 끝이니 조심해야 한다.

**핵심 용어**

- **CREATE**: 테이블·뷰·인덱스 같은 객체를 새로 만든다. 예: `CREATE TABLE 학생 (학번 INT PRIMARY KEY, 이름 VARCHAR(20) NOT NULL);`
- **ALTER**: 기존 객체의 구조를 바꾼다. `ADD`(열 추가), `MODIFY`(열 타입 변경), `DROP COLUMN`(열 삭제), `RENAME`(이름 변경).
- **DROP**: 객체를 구조째 삭제한다. `CASCADE`는 참조하는 객체까지 함께 지우고, `RESTRICT`는 참조가 남아 있으면 삭제를 거부한다.
- **TRUNCATE**: 테이블의 모든 데이터만 지우고 구조는 그대로 둔다. 로그를 남기지 않아 ROLLBACK 불가.
- **제약조건(Constraint)**: PRIMARY KEY(기본키), FOREIGN KEY(외래키), UNIQUE(유일값), NOT NULL(빈값 금지), CHECK(값 조건), DEFAULT(기본값). CREATE나 ALTER 시점에 함께 정의한다.

## 🎯 시험 응용

> DDL vs DML vs DCL 분류가 단골로 나온다. **DDL = CREATE/ALTER/DROP/TRUNCATE**, **DML = SELECT/INSERT/UPDATE/DELETE**, **DCL = GRANT/REVOKE**. TRUNCATE가 DDL이라 자동 커밋된다는 점, CASCADE/RESTRICT가 DROP의 참조 무결성 처리 옵션이라는 점을 꼭 구분하라.

## 🔗 연결 개념

- [[db-sql-002|JOIN 종류 (INNER, LEFT, RIGHT, FULL OUTER, CROSS, SELF)]]
- [[db-modeling-001|정규화 단계 (1NF~BCNF) — 각 단계 조건과 이상 현상]]
