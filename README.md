# 정보처리기사 2026 — 빈출 개념 다이어그램

> 정보처리기사 실기 시험 2026년 대비 학습 노트. 시험에 매회 나오는 핵심 개념을 Excalidraw
> 다이어그램 한 장에 압축한 시각 정리본.

## 🔗 공개 사이트 — [cskwork.github.io/certifications-wiki](https://cskwork.github.io/certifications-wiki/)

모바일·데스크톱 모두 바로 열립니다. 로그인 불필요.

---

## 현재 범위

**priority 3 (🔥 매회 출제) 30 / 30 완료.** 5과목 전부 커버.

| 과목 | 장수 | 대표 개념 |
|---|---|---|
| 🗄️ DB (데이터베이스) | 6 | 릴레이션 구성요소 · 정규화 · DDL · DML · JOIN · 집계·GROUP BY |
| 📡 NW (네트워크) | 4 | OSI 7계층 · 응용층 프로토콜 · 보안 공격 유형 · 네트워크 공격 |
| 🖥️ OS · 유지보수 | 3 | CPU 스케줄링 · 테스트 기법 · 테스트 커버리지 |
| 💻 PG (프로그래밍 언어) | 11 | 연결리스트 · C 포인터/재귀/비트 · Java 상속/예외/String · Python 문법/문자열 |
| 🛠️ SE (소프트웨어 공학) | 6 | 응집도 · 결합도 · GoF 생성/구조/행위 · UML 분류 |

다음 단계: priority 2 (⭐ 자주, 31장), priority 1 (· 가끔, 3장) 확장 예정.

## 특징

- **시각 우선** — 암기가 아니라 한 장짜리 다이어그램으로 구조를 이해.
- **빈출 순 정렬** — 🔥 매회 출제 개념부터 보도록 인덱스 배치.
- **출제 포인트 표시** — 각 다이어그램에 기출 회차와 함정 강조.
- **무의존성 렌더링** — Puppeteer/Playwright 없이 순수 Python으로 Excalidraw → SVG 변환.

## 편집 및 배포 흐름

1. **편집** — `~/wiki/certifications/정보처리기사/`에서 Obsidian Excalidraw 플러그인으로
   직접 `.excalidraw` 파일을 연다. 또는 `_generators/gen_*.py` 해당 함수를 수정해 일괄 재생성.
2. **SVG 재렌더** — `python3 content/_generators/export_svg.py` 실행.
3. **동기화** — 레포 루트에서 `./sync-from-wiki.sh` 실행 → 위키 서브트리가 `content/`로 복사.
4. **커밋·푸시** — `git add content && git commit -m "..." && git push` → GitHub Actions가
   `npx quartz build` 실행 후 Pages에 자동 배포(약 30초).

## 콘텐츠 구조

```
content/
├── index.md               # 5과목 전체 인덱스 + 빈출 순 SVG 임베드
├── _generators/           # Python 다이어그램·SVG 생성기
│   ├── gen_db.py / gen_nw.py / gen_os.py / gen_pg.py / gen_se.py
│   └── export_svg.py      # .excalidraw → .svg 변환기 (무의존성)
├── db/  (6장)  # 데이터베이스
├── nw/  (4장)  # 네트워크
├── os/  (3장)  # 운영체제·유지보수
├── pg/  (11장) # 프로그래밍 언어
└── se/  (6장)  # 소프트웨어 공학
```

## 로컬 미리보기

```bash
npm ci
npx quartz build --serve --port 8080
# → http://localhost:8080
```

## 기술 스택

- **[Quartz v4](https://quartz.jzhao.xyz)** — Obsidian 볼트 → 정적 사이트 빌더.
  Obsidian flavored wikilink 임베드 `![[db/x.svg]]`를 자동으로 `<img>`로 변환.
- **순수 Python SVG 변환기** — `.excalidraw` JSON을 rectangle · ellipse · text · arrow · line
  SVG 요소로 직접 렌더. Puppeteer/Playwright 같은 브라우저 런타임 의존성 없음.
- **Noto Sans KR** — 한글 렌더링 확보 (Google Fonts).
- **GitHub Actions** — push 시 자동 빌드·배포, 약 30초 내 완료.

## 원본 카드

Markdown 카드 원문은 [bite-size-study](https://github.com/cskwork/bite-size-study) 레포의
`content/cards/` 아래에 있다. 이 사이트의 다이어그램은 카드의 "핵심 개념 / 키워드 / 기출 포인트"
섹션을 시각화한 요약판이다.

## 라이선스

Quartz v4 기반(MIT). 학습 콘텐츠는 개인 학습·참고용.
