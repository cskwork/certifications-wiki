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

프로그램에서 문자열(글자들의 나열)을 다루는 일은 매우 잦다. 사용자 이름에서 성만 떼어내거나, "2025-01-15"에서 연도만 꺼내거나, 공백을 지우는 작업이 그렇다. 이걸 글자 하나하나 반복문으로 처리하면 코드가 길고 실수가 잦다. Java는 이런 문자열 조작을 한 줄로 끝낼 수 있도록 String 클래스(문자열 전용 도구 모음)에 미리 만들어둔 메서드(기능)를 제공한다. `length()`는 글자 수 세기, `substring()`은 원하는 부분만 오려내기, `charAt()`은 특정 위치의 글자 하나 꺼내기다. 또 Java의 String은 불변 객체(immutable object)여서, 메서드를 호출해도 원본 문자열은 바뀌지 않고 항상 새로운 문자열이 만들어진다.

## 📖 핵심 개념

String은 Java에서 문자열을 다루는 클래스(설계도)다. 가장 중요한 특성은 불변(immutable)이라는 점으로, 한번 만들어진 문자열의 내용은 절대 바뀌지 않는다. `substring()`이나 `replace()` 같은 메서드를 호출하면 원본은 그대로 두고 새 문자열을 만들어서 돌려준다. 인덱스(위치 번호)는 0부터 시작한다. `substring(start, end)`에서 start 위치는 포함하고 end 위치는 포함하지 않는다(end 미포함 규칙). 문자열 비교는 `==`가 아니라 `equals()` 메서드를 써야 한다. `==`는 두 변수가 같은 객체를 가리키는지(참조 비교)를 확인하고, `equals()`는 문자열 내용이 같은지(값 비교)를 확인하기 때문이다.

## 🔍 시각화

```
┌─ "Information" 인덱스 맵 ─────────────────┐
│                                           │
│  위치:  0  1  2  3  4  5  6  7  8  9  10  │
│  글자:  I  n  f  o  r  m  a  t  i  o  n   │
│                                           │
│  substring(0, 4) → I n f o = "Info"       │
│                    ↑─────↑                │
│                  start  end(미포함)        │
│                                           │
│  charAt(5) → 'm'                          │
│  length()  → 11 (글자 수)                  │
└───────────────────────────────────────────┘

┌─ == vs equals 차이 ───────────────────────┐
│                                           │
│  String a = "hello";  ─┐                  │
│  String b = "hello";  ─┤→ 문자열 풀(같은  │
│                        │   객체를 공유)    │
│  a == b  → true                           │
│                                           │
│  String c = new String("hello"); → 별도   │
│  a == c      → false (다른 객체)          │
│  a.equals(c) → true  (내용 동일)          │
└───────────────────────────────────────────┘
```

## ↔️ 이웃 개념 구분

- **substring vs charAt**: `substring()`은 여러 글자를 잘라서 문자열(String)로 반환하고, `charAt()`은 딱 한 글자를 문자(char)로 반환한다.
- **`==` vs `equals()`**: `==`는 두 변수가 메모리에서 같은 객체를 가리키는지 비교하고, `equals()`는 문자열 내용이 같은지 비교한다. 문자열 비교는 항상 `equals()`를 써야 한다.

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

## ✅ 스스로 가르쳐보기

> 친구에게 `"Information".substring(0, 4)`의 결과가 왜 "Info"인지, 그리고 왜 문자열 비교에 `==` 대신 `equals()`를 써야 하는지를 설명해 보세요.

체크포인트:
- [ ] substring의 end 인덱스가 미포함이라는 규칙을 말했는가
- [ ] 인덱스가 0부터 시작한다는 점을 언급했는가
- [ ] `==`는 참조(주소) 비교, `equals()`는 내용 비교임을 구분했는가

## 🎯 시험 응용

> - **매회 출제**: String 메서드를 활용한 출력 결과 추적은 단골 문제 > - **출제 패턴**: substring 범위 계산, charAt 인덱스, length/indexOf 반환값 > - **핵심**: substring(start, end)에서 **end 인덱스는 미포함** > - **주의**: `==`는 참조 비교, `equals()`는 내용 비교. 시험에서 자주 함정으로 출제

## 🔗 연결 개념

- `pg-language-009`
- [[pg-language-017|Python 문자열 메서드]]
