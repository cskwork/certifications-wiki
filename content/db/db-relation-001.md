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

## 핵심 개념

관계형 데이터베이스에서 릴레이션(Relation)은 **2차원 테이블** 형태로 데이터를 저장한다. 릴레이션을 구성하는 각 요소의 정확한 영문 용어와 한글 용어를 매핑하고, 개수 계산 방법을 숙지하는 것이 시험 핵심이다.

## 키워드

- **Tuple(튜플)**: 릴레이션의 **행(Row)**, 하나의 레코드(Record)/인스턴스(Instance)에 해당. 개수 = **Cardinality(카디널리티)**
- **Attribute(속성)**: 릴레이션의 **열(Column)**, 필드(Field)에 해당. 개수 = **Degree(차수/디그리)**
- **Domain(도메인)**: 각 속성이 가질 수 있는 **값의 범위**. 예: 학년 속성의 도메인 = {1, 2, 3, 4}
- **Degree(차수)**: 릴레이션을 구성하는 **속성(컬럼)의 수**
- **Cardinality(카디널리티)**: 릴레이션에 저장된 **튜플(행)의 수**
- **Null**: 아직 알 수 없거나 적용 불가능한 값; 0이나 공백과 다름

## 🎯 기출 포인트

> 매회 1문제 이상 출제되는 최빈출 주제. **2024-2회**: Cardinality/Degree 값 계산 문제. **2025-1회**: degree, cardinality, foreign key, domain 용어 설명 매칭. **2025-2회**: Attribute 정의 문제. **2025-3회**: Tuple/Instance/Cardinality 용어 문제. 영문 Degree=속성 수, Cardinality=튜플 수를 반드시 암기할 것.

## 연결 개념

- [[db-modeling-001|정규화 단계 (1NF~BCNF) — 각 단계 조건과 이상 현상]]
- `db-integrity-001`
- `db-relational-001`
