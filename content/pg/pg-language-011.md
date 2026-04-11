---
title: "Java 예외처리 try-catch-finally"
subject: "PG (프로그래밍 언어)"
priority: 3
frequency: "🔥 매회 출제"
tags:
  - pg
  - priority-3
---

# Java 예외처리 try-catch-finally

> 🔥 **매회 출제** (priority 3)

![[pg-language-011.svg]]

## 핵심 개념

Java의 예외처리는 **try-catch-finally** 구조로 런타임 오류를 제어한다. try 블록에서 예외가 발생하면 **즉시 실행이 중단**되고 catch 블록으로 이동한다. finally 블록은 **예외 발생 여부와 관계없이 항상 실행**된다.

## 키워드

- **try**: 예외가 발생할 수 있는 코드 블록
- **catch(예외타입 변수)**: 해당 타입의 예외를 포착하여 처리
- **finally**: 예외 발생 여부와 무관하게 반드시 실행 (자원 해제 용도)
- **throw**: 예외를 명시적으로 발생시킴
- **throws**: 메서드 선언부에서 발생 가능한 예외를 명시

## 🎯 기출 포인트

> - **2025-1회**: `a/b` (b=0)에서 ArithmeticException 발생 → catch 실행 후 finally 실행. 답: 출력1출력5 > - **출제 패턴**: try 블록 내 예외 발생 지점 이후 코드는 실행되지 않음. catch-finally 순서 추적 > - **핵심**: 예외 발생 시 try의 나머지 코드는 **건너뜀**. finally는 **무조건 실행** > - **주의**: finally에 return이 있으면 try/catch의 return을 덮어씀

## 연결 개념

- [[pg-language-003|Java 상속과 오버라이딩]]
- `pg-language-006`
