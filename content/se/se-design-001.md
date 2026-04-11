---
title: "디자인패턴 - GoF 생성패턴 5가지"
subject: "SE (소프트웨어 공학)"
priority: 3
frequency: "🔥 매회 출제"
tags:
  - se
  - priority-3
---

# 디자인패턴 - GoF 생성패턴 5가지

> 🔥 **매회 출제** (priority 3)

![[se-design-001.svg]]

## 🌱 왜 배우나

객체를 만들 때마다 `new` 키워드로 구체 클래스를 직접 호출하면, 나중에 그 클래스를 바꾸거나 초기화 방식이 복잡해질 때 코드 전체를 고쳐야 한다. 이는 마치 요리할 때마다 시장에서 식재료를 직접 사러 가는 것과 같아서, 재료가 바뀌면 레시피 전체가 망가진다. 생성 패턴은 "객체를 어떻게 만들 것인가"라는 반복되는 문제를 검증된 레시피로 제공해 생성 로직을 사용 코드로부터 분리한다. 그래서 구체 클래스 교체나 복잡한 초기화도 한 곳만 고치면 되는 유연성이 확보된다.

## 📖 핵심 개념

GoF(Gang of Four) 디자인패턴은 생성(Creational), 구조(Structural), 행위(Behavioral) 3가지로 분류된다. **생성패턴**은 객체 생성 메커니즘을 다루며, 시스템이 어떤 구체 클래스를 사용하는지 감추고 객체 생성의 유연성을 높인다. 생성패턴 5가지는 암기 필수 항목이다.

**핵심 용어**

- **Abstract Factory**: 관련된 객체군(family)을 생성하는 인터페이스 제공. 구체 팩토리를 교체하면 제품군 전체가 바뀜
- **Builder**: 복잡한 객체의 생성 과정과 표현을 분리. 동일한 생성 절차로 다른 표현 결과를 만듦
- **Factory Method**: 객체 생성을 서브클래스에 위임. 상위 클래스는 인터페이스만 정의하고 하위 클래스가 구체 클래스를 결정
- **Prototype**: 기존 객체를 복제(clone)하여 새 객체를 생성. 생성 비용이 클 때 유용
- **Singleton**: 클래스의 인스턴스를 하나만 생성하고 전역 접근점을 제공

## ✅ 이해 확인

1. GoF 생성 패턴 5가지를 모두 쓰시오.
   <details><summary>정답</summary>Abstract Factory, Builder, Factory Method, Prototype, Singleton ("AB를 FPS로 만든다").</details>
2. "애플리케이션 전체에서 설정 관리자는 딱 하나만 존재해야 한다"는 요구사항에 맞는 패턴은?
   <details><summary>정답</summary>Singleton. 인스턴스를 하나만 생성하고 전역 접근점을 제공하는 것이 정의다.</details>
3. Abstract Factory와 Factory Method의 차이는 무엇인가?
   <details><summary>정답</summary>Factory Method는 "하나의 객체" 생성을 서브클래스에 위임하는 패턴이고, Abstract Factory는 "서로 관련된 객체군(family) 전체"를 생성하는 인터페이스를 제공한다. 즉 단일 제품 vs 제품군이 핵심 차이다.</details>

## 🎯 시험 응용

> 암기법: **"AB를 FPS로 만든다"** (Abstract Factory, Builder, Factory Method, Prototype, Singleton). 생성패턴은 총 5개, 구조패턴 7개(어댑터, 브리지, 컴포지트, 데코레이터, 퍼사드, 플라이웨이트, 프록시), 행위패턴 11개이다. 패턴 이름과 분류를 정확히 매칭하는 문제가 자주 출제된다.

## 🔗 연결 개념

- [[se-requirements-001|UML 다이어그램 종류 (구조/행위 분류)]]
- `se-architecture-001`
