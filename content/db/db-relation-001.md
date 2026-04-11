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

엑셀 시트 하나를 떠올려 보자. 열이 몇 개이고 행이 몇 개인지, "학년" 칸에는 1~4만 들어가야 한다는 규칙이 있다. 그런데 누구는 열을 "필드"라 부르고 또 누구는 "속성"이라 부른다면 대화가 뒤엉킨다. 관계형 데이터베이스(Relational Database) 세계는 이 용어를 Tuple·Attribute·Degree·Cardinality·Domain 다섯 개로 통일해 두었다. 도서관에서 책 위치를 "3층 B서가 5번 칸"이라고 누구나 같은 말로 부르는 것과 같은 이유다.

## 📖 핵심 개념

릴레이션(Relation)은 관계형 데이터베이스가 데이터를 담는 2차원 표를 가리키는 학술 용어다. 쉽게 말해 "테이블"과 같은 뜻이다. 릴레이션은 다섯 가지 요소로 설명한다. 가로 한 줄(행)이 **튜플(Tuple)**, 세로 한 줄(열)이 **속성(Attribute)**이다. 속성의 개수가 **차수(Degree)**, 튜플의 개수가 **카디널리티(Cardinality)**다. 각 속성이 가질 수 있는 값의 범위가 **도메인(Domain)**이다. 예를 들어 "학년" 속성의 도메인은 {1, 2, 3, 4}로 정해 둘 수 있다. 시험 핵심은 이 다섯 용어의 영문·한글 매핑, 그리고 개수를 세는 방법이다.

**핵심 용어**

- **Tuple(튜플)**: 릴레이션의 행. 레코드(Record) 또는 인스턴스(Instance)와 같은 뜻.
- **Attribute(속성)**: 릴레이션의 열. 필드(Field)와 같은 뜻.
- **Domain(도메인)**: 속성이 가질 수 있는 값의 범위. 예: 학년 → {1, 2, 3, 4}.
- **Degree(차수)**: 속성(열)의 개수.
- **Cardinality(카디널리티)**: 튜플(행)의 개수.
- **Null**: 아직 값을 모르거나 적용할 수 없을 때 쓰는 표시. 숫자 0이나 빈 문자열과 다르다.

## 🎯 시험 응용

> 매회 1문제 이상 나오는 최빈출 주제다. **2024-2회**: Cardinality/Degree 값 계산. **2025-1회**: degree, cardinality, foreign key, domain 용어 매칭. **2025-2회**: Attribute 정의. **2025-3회**: Tuple/Instance/Cardinality 용어 문제. 영문 Degree=속성 수, Cardinality=튜플 수는 반드시 암기하라.

## 🔗 연결 개념

- [[db-modeling-001|정규화 단계 (1NF~BCNF) — 각 단계 조건과 이상 현상]]
- `db-integrity-001`
- `db-relational-001`
