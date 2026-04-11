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

## 🌱 왜 배우나

학생 500명의 성적표를 한 장씩 보는 것과 "학과별 평균 점수"를 한눈에 보는 것은 전혀 다른 일이다. 경영진이나 교사가 원하는 건 보통 후자, 즉 **요약된 숫자**다. 집계함수와 GROUP BY가 없다면 우리는 전체 데이터를 엑셀로 내려받아 손으로 평균을 계산해야 할 것이다. 마치 카페에서 "오늘 매출 총액과 메뉴별 판매량"을 알고 싶은데 영수증 수백 장을 일일이 세는 꼴이다. DB는 이 요약을 한 줄 쿼리로 해주는데, 대신 NULL이 섞이거나 WHERE/HAVING을 헷갈리면 값이 틀어지므로 그 규칙을 정확히 알아야 한다.

## 📖 핵심 개념

집계함수(Aggregate Function)는 여러 행을 하나의 결과값으로 요약한다. **NULL 처리 규칙**이 함수마다 다르며 이 차이가 매회 출제된다. GROUP BY와 함께 사용하면 그룹별 집계가 가능하고, 그룹 조건 필터링은 WHERE가 아닌 **HAVING**을 사용해야 한다.

**핵심 용어**

- **COUNT(\*)**: NULL을 포함한 **전체 행 수** 반환
- **COUNT(컬럼)**: 해당 컬럼에서 **NULL을 제외**한 행 수 반환
- **SUM / AVG / MAX / MIN**: 모두 NULL을 **자동 제외**하고 계산 (AVG는 NULL 제외 후 나눔)
- **GROUP BY**: 지정 컬럼의 값이 같은 행끼리 묶어 집계; SELECT에는 GROUP BY 컬럼 또는 집계함수만 올 수 있음
- **HAVING vs WHERE**: WHERE는 **그룹화 이전** 행 필터, HAVING은 **그룹화 이후** 집계 결과 필터
- **실행 순서**: FROM → WHERE → GROUP BY → 집계함수 적용 → HAVING → SELECT → ORDER BY

## ✅ 이해 확인

1. 점수 컬럼에 `80, NULL, 70, NULL, 90`이 있을 때 `AVG(점수)`의 값은?
   <details><summary>정답</summary>80 — AVG는 NULL을 자동 제외하므로 (80+70+90)/3 = 80. NULL을 0으로 계산하지 않는다.</details>
2. "학과별로 평균 점수가 80 이상인 학과만" 조회하려면 WHERE와 HAVING 중 어디에 조건을 써야 하는가?
   <details><summary>정답</summary>HAVING `AVG(점수) >= 80` — 집계 결과에 대한 조건은 GROUP BY 이후에 적용되는 HAVING에만 쓸 수 있다.</details>
3. `SELECT 학과, 이름, COUNT(*) FROM 학생 GROUP BY 학과`는 왜 오류인가?
   <details><summary>정답</summary>GROUP BY에 없는 비집계 컬럼 `이름`이 SELECT에 있기 때문이다. SELECT에는 GROUP BY 컬럼 또는 집계함수만 올 수 있다.</details>

## 🎯 시험 응용

> **2025-3회**: COUNT(*)와 COUNT(컬럼명)의 NULL 처리 차이 문제 출제. AVG 계산 시 NULL이 포함된 경우 분모가 달라지는 함정 주의. HAVING 절에서 집계함수를 조건으로 쓸 수 있지만 WHERE 절에서는 불가능하다는 점도 빈출 포인트.

## 🔗 연결 개념

- [[db-sql-003|DML 명령어 (SELECT, INSERT, UPDATE, DELETE)]]
- [[db-sql-002|JOIN 종류 (INNER, LEFT, RIGHT, FULL OUTER, CROSS, SELF)]]
