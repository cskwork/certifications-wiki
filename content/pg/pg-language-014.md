---
title: "Java String 메서드"
subject: "PG (프로그래밍 언어)"
priority: 3
frequency: "🔥 매회 출제"
tags:
  - pg
  - priority-3
---

# Java String 메서드

> 🔥 **매회 출제** (priority 3)

![[pg-language-014.svg]]

## 🌱 왜 배우나

사용자 이름에서 성만 떼거나, "2025-01-15"에서 연도만 꺼내거나, 공백을 제거하고 검증하는 일은 거의 모든 프로그램에서 필요하다. 문자열을 일일이 char 배열로 반복문 돌리며 처리하면 코드가 길고 버그도 잦다. 가위와 자 없이 종이 한 장에서 원하는 부분만 정확히 오려내려 애쓰는 꼴이다. String 메서드는 "자주 쓰는 문자열 조작을 표준 도구로 제공하자"는 아이디어다. length, substring, charAt, indexOf만 있어도 대부분의 문자열 작업이 한 줄로 끝난다. 또 String은 불변 객체여서, 메서드는 원본을 건드리지 않고 새 String을 반환한다.

## 📖 핵심 개념

Java의 String은 **불변 객체(Immutable)**로, 문자열 조작 메서드는 원본을 변경하지 않고 **새로운 String을 반환**한다. substring, charAt, length 등의 메서드로 문자열을 다루며, 인덱스가 0부터 시작한다는 점이 코드 추적의 핵심이다.

**핵심 용어**

- **length()**: 문자열 길이 반환. `"abc".length()` → 3
- **charAt(index)**: 해당 인덱스의 문자 반환. `"abc".charAt(1)` → 'b'
- **substring(start, end)**: start부터 end-1까지 부분 문자열. `"abcde".substring(1,4)` → "bcd"
- **substring(start)**: start부터 끝까지. `"abcde".substring(2)` → "cde"
- **indexOf(str)**: str이 처음 나타나는 인덱스. 없으면 -1
- **toUpperCase() / toLowerCase()**: 대소문자 변환
- **replace(old, new)**: 문자/문자열 치환
- **split(regex)**: 구분자로 분리하여 String 배열 반환
- **trim()**: 양쪽 공백 제거
- **equals(str)**: 문자열 내용 비교 (`==`는 참조 비교)

## ✅ 이해 확인

1. `"Information".substring(0, 4)`의 결과는? end 인덱스는 포함되는가?
   <details><summary>정답</summary>`"Info"`. substring의 end 인덱스는 **미포함**이므로 인덱스 0,1,2,3번 문자만 포함한다.</details>
2. `String a = "hello"; String c = new String("hello");`일 때 `a == c`와 `a.equals(c)`의 결과는?
   <details><summary>정답</summary>`a == c`는 **false**(서로 다른 객체의 참조 비교), `a.equals(c)`는 **true**(내용 비교). 문자열 비교는 반드시 `equals()`를 써야 한다. `==`는 참조 비교라 문자열 풀에 있지 않은 경우 false가 나올 수 있다.</details>
3. `"Information".charAt(5)`와 `"Information".length()`의 결과는?
   <details><summary>정답</summary>`charAt(5)` = `'m'` (I=0, n=1, f=2, o=3, r=4, m=5), `length()` = `11`. 인덱스는 0부터지만 length는 실제 글자 수를 반환한다는 점에 주의.</details>

## 🎯 시험 응용

> - **매회 출제**: String 메서드를 활용한 출력 결과 추적은 단골 문제 > - **출제 패턴**: substring 범위 계산, charAt 인덱스, length/indexOf 반환값 > - **핵심**: substring(start, end)에서 **end 인덱스는 미포함** > - **주의**: `==`는 참조 비교, `equals()`는 내용 비교. 시험에서 자주 함정으로 출제

## 🔗 연결 개념

- `pg-language-009`
- [[pg-language-017|Python 문자열 메서드]]
