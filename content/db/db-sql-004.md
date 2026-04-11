---
title: "집계함수와 GROUP BY (COUNT, SUM, AVG, MAX, MIN, HAVING)"
subject: "DB (데이터베이스)"
priority: 3
frequency: "🔥 매회 출제"
tags:
  - db
  - priority-3
---

# 집계함수와 GROUP BY (COUNT, SUM, AVG, MAX, MIN, HAVING)

> 🔥 **매회 출제** (priority 3)

![[db-sql-004.svg]]

## 핵심 개념

집계함수(Aggregate Function)는 여러 행을 하나의 결과값으로 요약한다. **NULL 처리 규칙**이 함수마다 다르며 이 차이가 매회 출제된다. GROUP BY와 함께 사용하면 그룹별 집계가 가능하고, 그룹 조건 필터링은 WHERE가 아닌 **HAVING**을 사용해야 한다.

## 키워드

- **COUNT(\*)**: NULL을 포함한 **전체 행 수** 반환
- **COUNT(컬럼)**: 해당 컬럼에서 **NULL을 제외**한 행 수 반환
- **SUM / AVG / MAX / MIN**: 모두 NULL을 **자동 제외**하고 계산 (AVG는 NULL 제외 후 나눔)
- **GROUP BY**: 지정 컬럼의 값이 같은 행끼리 묶어 집계; SELECT에는 GROUP BY 컬럼 또는 집계함수만 올 수 있음
- **HAVING vs WHERE**: WHERE는 **그룹화 이전** 행 필터, HAVING은 **그룹화 이후** 집계 결과 필터
- **실행 순서**: FROM → WHERE → GROUP BY → 집계함수 적용 → HAVING → SELECT → ORDER BY

## 🎯 기출 포인트

> **2025-3회**: COUNT(*)와 COUNT(컬럼명)의 NULL 처리 차이 문제 출제. AVG 계산 시 NULL이 포함된 경우 분모가 달라지는 함정 주의. HAVING 절에서 집계함수를 조건으로 쓸 수 있지만 WHERE 절에서는 불가능하다는 점도 빈출 포인트.

## 연결 개념

- [[db-sql-003|DML 명령어 (SELECT, INSERT, UPDATE, DELETE)]]
- [[db-sql-002|JOIN 종류 (INNER, LEFT, RIGHT, FULL OUTER, CROSS, SELF)]]
