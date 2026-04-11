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

"2025-01-15"에서 연도만 꺼내고 싶다. "  홍길동  "의 양쪽 빈칸을 털고 싶다. 이메일 주소에서 `@` 뒤만 잘라내고 싶다. 프로그램은 이런 글자 가공 작업을 하루에도 수백 번씩 한다. 글자 하나하나 반복문으로 뜯으면 코드가 길어지고 실수가 많아진다. Java는 String 클래스(문자열 전용 도구 상자)에 자주 쓰는 기능을 메서드(method)로 미리 박아 두었다. `length()`로 글자 수 세기, `substring()`으로 일부 오려내기, `charAt()`으로 특정 위치의 한 글자만 꺼내기.

## 📖 핵심 개념

String은 Java에서 문자열을 다루는 클래스(class)다. 클래스는 "설계도"라고 이해하면 된다. **가장 큰 특성은 불변(immutable)**이다. 한번 만들어진 문자열의 내용은 절대 바뀌지 않는다. `replace()`나 `substring()`을 호출해도 원본은 그대로다. 대신 바뀐 결과가 담긴 새 문자열이 따로 만들어져 돌아온다. **인덱스는 0부터 센다.** 인덱스(index)는 문자 한 개의 위치 번호다. `"abc"`에서 a는 0번, b는 1번, c는 2번이다. **substring(start, end)는 end 미포함이다.** `substring(0, 4)`는 0, 1, 2, 3번 위치까지만 가져간다. 4번 위치는 안 들어간다. 이 규칙이 시험 단골 함정이다. **문자열 비교는 `==`가 아니라 `equals()`다.** `==`는 "같은 객체(메모리 주소)를 가리키냐"를 묻고, `equals()`는 "글자 내용이 같냐"를 묻는다. `new String("hello")`로 새로 만든 문자열과 기존 `"hello"`를 `==`로 비교하면 false가 나온다. 내용은 같아도 서로 다른 객체이기 때문이다.

**핵심 용어**

- **String**: Java에서 문자열을 다루는 클래스. 불변(immutable)
- **length()**: 문자열의 글자 수를 반환. `"abc".length()` → 3
- **charAt(index)**: 해당 인덱스(위치 번호, 0부터 시작)의 문자 하나를 반환. `"abc".charAt(1)` → 'b'
- **substring(start, end)**: start부터 end-1까지의 부분 문자열을 반환. end는 미포함. `"abcde".substring(1,4)` → "bcd"
- **substring(start)**: start부터 끝까지 반환. `"abcde".substring(2)` → "cde"
- **indexOf(str)**: str이 처음 나타나는 인덱스를 반환. 없으면 -1
- **toUpperCase() / toLowerCase()**: 대문자/소문자 변환
- **replace(old, new)**: old를 new로 치환한 새 문자열 반환
- **split(regex)**: 구분자(regex)로 분리하여 String 배열로 반환
- **trim()**: 양쪽 공백을 제거한 새 문자열 반환
- **equals(str)**: 문자열 내용을 비교하여 같으면 true 반환

## 🎯 시험 응용

> - **매회 출제**: String 메서드를 활용한 출력 결과 추적은 단골 문제 > - **출제 패턴**: substring 범위 계산, charAt 인덱스, length/indexOf 반환값 > - **핵심**: substring(start, end)에서 **end 인덱스는 미포함** > - **주의**: `==`는 참조 비교, `equals()`는 내용 비교. 시험에서 자주 함정으로 출제

## 🔗 연결 개념

- `pg-language-009`
- [[pg-language-017|Python 문자열 메서드]]
