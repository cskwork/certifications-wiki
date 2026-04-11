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

## 🌱 왜 배우나

"apple,banana,cherry" 같은 CSV 한 줄을 받아 과일 이름별로 나누거나, 사용자가 입력한 "  홍길동  "에서 양쪽 공백을 제거하거나, 본문 속 "구버전"을 "신버전"으로 바꾸는 일은 데이터 처리의 90%를 차지한다. 이를 직접 for문으로 쓰면 지저분하다. 긴 리본을 칼 없이 손으로 뜯는 것과 다르지 않다. Python은 split(자르기), join(이어 붙이기), replace(바꾸기), strip(공백 털기) 같은 전용 가위·풀·지우개를 문자열의 메서드로 제공해 한 줄로 문자열을 가공할 수 있게 했다. 또 문자열은 불변이므로 메서드는 원본을 건드리지 않고 새 문자열을 반환한다.

## 📖 핵심 개념

Python 문자열은 **불변(immutable)**이며, 모든 문자열 메서드는 원본을 변경하지 않고 **새로운 문자열을 반환**한다. split, join, replace는 가장 빈출되는 메서드이며, 메서드 체인으로 연속 호출하는 출력 추적이 핵심이다.

**핵심 용어**

- **split(구분자)**: 구분자로 분리 → 리스트 반환. `"a,b,c".split(",")` → `['a','b','c']`
- **join(리스트)**: 리스트를 구분자로 결합. `"-".join(['a','b'])` → `"a-b"`
- **replace(old, new)**: 모든 old를 new로 치환. `"aab".replace("a","x")` → `"xxb"`
- **find(str)**: str의 첫 번째 인덱스 반환. 없으면 -1
- **upper() / lower()**: 대소문자 변환
- **strip()**: 양쪽 공백 제거 (lstrip, rstrip은 한쪽만)
- **count(str)**: str의 등장 횟수
- **startswith(str) / endswith(str)**: 접두사/접미사 확인 (bool)

## ✅ 이해 확인

1. `"a,b,c".split(",")`의 반환값과 그 타입은?
   <details><summary>정답</summary>`['a', 'b', 'c']`, 타입은 **리스트(list)**. split은 문자열을 잘라서 리스트로 반환한다.</details>
2. `"-".join(['a','b','c'])`의 결과는? join의 호출 주체는 무엇인가?
   <details><summary>정답</summary>`"a-b-c"`. 호출 주체는 **구분자 문자열**(`"-"`)이고 인자가 리스트다. "리스트.join(구분자)"가 아니라 "구분자.join(리스트)" 순서에 주의.</details>
3. `"banana".replace("a", "X")`의 결과는? 첫 번째 매칭만 바꾸는가?
   <details><summary>정답</summary>`"bXnXnX"`. replace는 **모든** 매칭을 치환한다. 첫 번째만 바꾸려면 `replace("a", "X", 1)`처럼 세 번째 인자로 횟수를 지정해야 한다.</details>

## 🎯 시험 응용

> - **매회 출제**: split → join → replace 등 메서드 체인 결과 추적 > - **출제 패턴**: 문자열 조작 후 출력값 쓰기. 인덱싱/슬라이싱과 혼합 출제 > - **핵심**: split은 리스트 반환, join은 문자열 반환. 반환 타입에 주의 > - **주의**: replace는 **모든** 매칭을 치환 (첫 번째만이 아님)

## 🔗 연결 개념

- [[pg-language-014|Java String 메서드]]
- [[pg-language-004|Python 핵심 문법]]
