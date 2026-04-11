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

## 핵심 개념

Java의 String은 **불변 객체(Immutable)**로, 문자열 조작 메서드는 원본을 변경하지 않고 **새로운 String을 반환**한다. substring, charAt, length 등의 메서드로 문자열을 다루며, 인덱스가 0부터 시작한다는 점이 코드 추적의 핵심이다.

## 키워드

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

## 🎯 기출 포인트

> - **매회 출제**: String 메서드를 활용한 출력 결과 추적은 단골 문제 > - **출제 패턴**: substring 범위 계산, charAt 인덱스, length/indexOf 반환값 > - **핵심**: substring(start, end)에서 **end 인덱스는 미포함** > - **주의**: `==`는 참조 비교, `equals()`는 내용 비교. 시험에서 자주 함정으로 출제

## 연결 개념

- `pg-language-009`
- [[pg-language-017|Python 문자열 메서드]]
