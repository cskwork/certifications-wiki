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

## 🌱 왜 배우나

파일을 열었는데 파일이 없거나, 나눗셈인데 분모가 0이거나, 네트워크가 끊기는 일은 "정상 흐름"이 아니다. 이때마다 `if`로 일일이 체크하면 본래 로직이 에러 처리 코드에 파묻혀 알아보기 어렵다. try-catch는 "정상 시나리오는 try 안에 깔끔하게 쓰고, 사고 대응은 catch에 몰아 쓰자"는 아이디어다. 화재 발생 시 자동으로 비상구를 여는 스프링클러처럼, 예외가 터지면 정상 흐름은 중단되고 대응 블록으로 자동 점프한다. finally는 "불이 났든 말든 마지막에 꼭 문은 잠그고 나가자"는 뒷정리용으로 등장했다.

## 📖 핵심 개념

Java의 예외처리는 **try-catch-finally** 구조로 런타임 오류를 제어한다. try 블록에서 예외가 발생하면 **즉시 실행이 중단**되고 catch 블록으로 이동한다. finally 블록은 **예외 발생 여부와 관계없이 항상 실행**된다.

**핵심 용어**

- **try**: 예외가 발생할 수 있는 코드 블록
- **catch(예외타입 변수)**: 해당 타입의 예외를 포착하여 처리
- **finally**: 예외 발생 여부와 무관하게 반드시 실행 (자원 해제 용도)
- **throw**: 예외를 명시적으로 발생시킴
- **throws**: 메서드 선언부에서 발생 가능한 예외를 명시

## ✅ 이해 확인

1. try 블록 중간에 예외가 발생하면 try의 나머지 코드는 어떻게 되는가?
   <details><summary>정답</summary>즉시 중단되고 해당 예외 타입에 맞는 catch 블록으로 점프한다. 예외 발생 지점 이후의 try 코드는 **실행되지 않는다**.</details>
2. 예외가 발생하지 **않은** 경우에도 finally 블록은 실행되는가?
   <details><summary>정답</summary>실행된다. finally는 예외 발생 여부와 상관없이 항상 실행되어, 파일 닫기/DB 연결 해제 같은 뒷정리에 쓰인다.</details>
3. 다음 코드에서 `func()`의 반환값은?
   ```java
   try { return 1; } catch(Exception e) { return 2; } finally { return 3; }
   ```
   <details><summary>정답</summary>**3**. finally에 return이 있으면 try/catch의 return을 덮어쓴다. 단, finally에서 return을 사용하는 것은 try/catch의 결과를 가려서 디버깅이 어려워지므로 실무에서는 피해야 한다.</details>

## 🎯 시험 응용

> - **2025-1회**: `a/b` (b=0)에서 ArithmeticException 발생 → catch 실행 후 finally 실행. 답: 출력1출력5 > - **출제 패턴**: try 블록 내 예외 발생 지점 이후 코드는 실행되지 않음. catch-finally 순서 추적 > - **핵심**: 예외 발생 시 try의 나머지 코드는 **건너뜀**. finally는 **무조건 실행** > - **주의**: finally에 return이 있으면 try/catch의 return을 덮어씀

## 🔗 연결 개념

- [[pg-language-003|Java 상속과 오버라이딩]]
- `pg-language-006`
