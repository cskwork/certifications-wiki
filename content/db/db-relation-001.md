---
title: "릴레이션 구성 요소 (Tuple, Attribute, Domain, Degree, Cardinality)"
subject: "DB (데이터베이스)"
priority: 3
frequency: "🔥 매회 출제"
tags:
  - db
  - priority-3
---

# 릴레이션 구성 요소 (Tuple, Attribute, Domain, Degree, Cardinality)

> 🔥 **매회 출제** (priority 3)

![[db-relation-001.svg]]

## 🌱 왜 배우나

엑셀 시트를 떠올려 보자. 열이 몇 개인지, 행이 몇 개인지, 그리고 "학년" 칸에는 1~4만 들어가야 한다는 규칙이 있다면 이 시트는 꽤 잘 정리된 것이다. 하지만 사람마다 "컬럼 수"를 "필드 수"라고 부르고, 누구는 "레코드 수"를 "행 수"라고 부른다면 팀 대화가 엉망이 된다. 관계형 DB 세계에서는 이 용어들을 **한 가지로 통일**해 놓았는데, 그것이 Tuple/Attribute/Degree/Cardinality/Domain이다. 도서관에서 책 한 권의 위치를 "3층 서가 B 5번째 칸"이라고 모두가 같은 말로 부르는 것과 같다. 그래서 이 기초 어휘를 먼저 배운다.

## 📖 핵심 개념

관계형 데이터베이스에서 릴레이션(Relation)은 **2차원 테이블** 형태로 데이터를 저장한다. 릴레이션을 구성하는 각 요소의 정확한 영문 용어와 한글 용어를 매핑하고, 개수 계산 방법을 숙지하는 것이 시험 핵심이다.

**핵심 용어**

- **Tuple(튜플)**: 릴레이션의 **행(Row)**, 하나의 레코드(Record)/인스턴스(Instance)에 해당. 개수 = **Cardinality(카디널리티)**
- **Attribute(속성)**: 릴레이션의 **열(Column)**, 필드(Field)에 해당. 개수 = **Degree(차수/디그리)**
- **Domain(도메인)**: 각 속성이 가질 수 있는 **값의 범위**. 예: 학년 속성의 도메인 = {1, 2, 3, 4}
- **Degree(차수)**: 릴레이션을 구성하는 **속성(컬럼)의 수**
- **Cardinality(카디널리티)**: 릴레이션에 저장된 **튜플(행)의 수**
- **Null**: 아직 알 수 없거나 적용 불가능한 값; 0이나 공백과 다름

## ✅ 이해 확인

1. 학생(학번, 이름, 학과) 릴레이션에 10명의 데이터가 들어 있다. Degree와 Cardinality는 각각 얼마인가?
   <details><summary>정답</summary>Degree = 3, Cardinality = 10 — Degree는 속성(컬럼) 수, Cardinality는 튜플(행) 수다.</details>
2. "학년" 속성에 허용되는 값의 집합 {1, 2, 3, 4}을 가리키는 용어는?
   <details><summary>정답</summary>Domain(도메인) — 속성이 가질 수 있는 값의 범위를 의미한다.</details>
3. 기출에서 Cardinality를 "행의 수"가 아닌 "관계에 참여하는 엔티티 수"로 묻는 경우와 어떻게 구분하는가?
   <details><summary>정답</summary>릴레이션(테이블) 문맥이면 튜플 수, ER 다이어그램 문맥이면 1:N·M:N 같은 관계 대응 수를 의미한다. 문제에서 대상이 테이블인지 관계인지를 먼저 확인해야 한다.</details>

## 🎯 시험 응용

> 매회 1문제 이상 출제되는 최빈출 주제. **2024-2회**: Cardinality/Degree 값 계산 문제. **2025-1회**: degree, cardinality, foreign key, domain 용어 설명 매칭. **2025-2회**: Attribute 정의 문제. **2025-3회**: Tuple/Instance/Cardinality 용어 문제. 영문 Degree=속성 수, Cardinality=튜플 수를 반드시 암기할 것.

## 🔗 연결 개념

- [[db-modeling-001|정규화 단계 (1NF~BCNF) — 각 단계 조건과 이상 현상]]
- `db-integrity-001`
- `db-relational-001`
