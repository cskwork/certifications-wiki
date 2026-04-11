---
title: "Python 문자열 메서드"
subject: "PG (프로그래밍 언어)"
priority: 3
frequency: "🔥 매회 출제"
tags:
  - pg
  - priority-3
---

# Python 문자열 메서드

> 🔥 **매회 출제** (priority 3)

![[pg-language-017.svg]]

## 핵심 개념

Python 문자열은 **불변(immutable)**이며, 모든 문자열 메서드는 원본을 변경하지 않고 **새로운 문자열을 반환**한다. split, join, replace는 가장 빈출되는 메서드이며, 메서드 체인으로 연속 호출하는 출력 추적이 핵심이다.

## 키워드

- **split(구분자)**: 구분자로 분리 → 리스트 반환. `"a,b,c".split(",")` → `['a','b','c']`
- **join(리스트)**: 리스트를 구분자로 결합. `"-".join(['a','b'])` → `"a-b"`
- **replace(old, new)**: 모든 old를 new로 치환. `"aab".replace("a","x")` → `"xxb"`
- **find(str)**: str의 첫 번째 인덱스 반환. 없으면 -1
- **upper() / lower()**: 대소문자 변환
- **strip()**: 양쪽 공백 제거 (lstrip, rstrip은 한쪽만)
- **count(str)**: str의 등장 횟수
- **startswith(str) / endswith(str)**: 접두사/접미사 확인 (bool)

## 🎯 기출 포인트

> - **매회 출제**: split → join → replace 등 메서드 체인 결과 추적 > - **출제 패턴**: 문자열 조작 후 출력값 쓰기. 인덱싱/슬라이싱과 혼합 출제 > - **핵심**: split은 리스트 반환, join은 문자열 반환. 반환 타입에 주의 > - **주의**: replace는 **모든** 매칭을 치환 (첫 번째만이 아님)

## 연결 개념

- [[pg-language-014|Java String 메서드]]
- [[pg-language-004|Python 핵심 문법]]
