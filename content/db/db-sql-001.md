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

데이터베이스를 공책이라고 하면, 먼저 해야 할 일은 어떤 칸을 만들지 줄을 긋는 일이다. 이름 칸, 전화번호 칸, 주소 칸. 나중에 주소 칸이 너무 좁으면 늘려야 하고, 필요 없어진 칸은 지워야 한다. DDL(Data Definition Language, 데이터 정의어)이 없으면 표(테이블)를 만들 수도, 고칠 수도, 지울 수도 없어서 데이터베이스는 아무 일도 시작할 수 없다. 가구 없는 집에 이사해 놓고 옷장·책상을 살 방법이 없는 상황과 같다. 데이터를 담기 전에 그릇부터 만드는 언어, 그것이 DDL이다.

## 📖 핵심 개념

DDL(Data Definition Language, 데이터 정의어)은 데이터베이스의 구조(스키마, Schema — 표의 이름·열·타입 등 뼈대 설계)를 만들고, 바꾸고, 지우는 SQL(Structured Query Language, 구조적 질의 언어) 명령어 모음이다. DDL 명령어는 실행 즉시 자동 커밋(Auto Commit — 실행하면 바로 확정되어 되돌릴 수 없음)된다. 따라서 ROLLBACK(되돌리기)이 불가능하다. DDL이 다루는 대상은 테이블, 뷰(View, 가상 테이블), 인덱스(Index, 검색 속도를 높이는 색인), 스키마 등이다.

## 🔍 시각화

```
DDL 명령어 네 가지와 하는 일:

CREATE ──▶ 새 표(테이블) 만들기        "옷장을 새로 산다"
ALTER  ──▶ 기존 표 구조 변경            "서랍을 추가/제거한다"
DROP   ──▶ 표 자체를 완전 삭제          "옷장째로 버린다"
TRUNCATE ▶ 표는 남기고 데이터만 전부 삭제 "옷장은 두고 옷만 다 버린다"

⚠ 네 명령 모두 자동 커밋 → ROLLBACK 불가
```

## ↔️ 이웃 개념 구분

- **DDL vs DML**: DDL은 구조(표 자체)를 다루고, DML(Data Manipulation Language, 데이터 조작어)은 데이터(표 안의 값)를 다룬다. DDL은 자동 커밋, DML은 ROLLBACK 가능.
- **DROP vs TRUNCATE vs DELETE**: DROP은 표+데이터 모두 삭제, TRUNCATE는 표는 남기고 데이터 전부 삭제(자동 커밋), DELETE는 조건 지정 가능하고 ROLLBACK 가능.

**핵심 용어**

- **CREATE**: 테이블, 뷰, 인덱스 등 객체를 새로 만든다. 예: `CREATE TABLE 학생 (학번 INT PRIMARY KEY, 이름 VARCHAR(20) NOT NULL);`
- **ALTER**: 기존 객체의 구조를 변경한다. `ADD`(열 추가), `MODIFY`(열 타입 변경), `DROP COLUMN`(열 삭제), `RENAME`(이름 변경).
- **DROP**: 객체를 구조째 완전 삭제한다. `CASCADE`(참조하는 모든 객체를 함께 삭제), `RESTRICT`(참조 객체가 있으면 삭제 거부).
- **TRUNCATE**: 테이블의 모든 데이터만 삭제하고 구조는 유지한다. 로그를 남기지 않아 ROLLBACK 불가.
- **제약조건(Constraint)**: PRIMARY KEY(기본키), FOREIGN KEY(외래키), UNIQUE(유일값), NOT NULL(빈값 금지), CHECK(값 조건), DEFAULT(기본값) — CREATE/ALTER 시 함께 정의한다.

## ✅ 스스로 가르쳐보기

**질문**: 친구에게 "DDL 명령어 네 가지가 각각 무엇을 하고, DML과 어떻게 다른지" 설명해 보라.

체크포인트:
- [ ] CREATE·ALTER·DROP·TRUNCATE 각각의 역할을 한 줄로 말했는가?
- [ ] DROP과 TRUNCATE의 차이를 "구조 삭제 여부"로 구분했는가?
- [ ] DDL은 자동 커밋, DML은 ROLLBACK 가능하다는 차이를 언급했는가?
- [ ] CASCADE와 RESTRICT의 의미를 설명할 수 있는가?

## 🎯 시험 응용

> DDL vs DML vs DCL 분류가 단골 출제된다. **DDL = CREATE/ALTER/DROP/TRUNCATE**, **DML = SELECT/INSERT/UPDATE/DELETE**, **DCL = GRANT/REVOKE**. TRUNCATE는 DDL이므로 AUTO COMMIT 된다는 점, CASCADE/RESTRICT 옵션은 DROP에서 참조 무결성 처리 방식이라는 점을 구분할 것.

## 🔗 연결 개념

- [[db-sql-002|JOIN 종류 (INNER, LEFT, RIGHT, FULL OUTER, CROSS, SELF)]]
- [[db-modeling-001|정규화 단계 (1NF~BCNF) — 각 단계 조건과 이상 현상]]
