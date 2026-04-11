# 정보처리기사 2026 — 빈출 개념 다이어그램 (Quartz 사이트)

정보처리기사 실기 2026 대비 학습 노트를 Excalidraw 다이어그램으로 시각화한 정적 사이트.
Obsidian 볼트 기반 콘텐츠를 [Quartz v4](https://quartz.jzhao.xyz)로 빌드해
GitHub Pages에 배포한다.

## 공개 URL
https://cskwork.github.io/certifications-wiki

## 콘텐츠 구조
```
content/
├── index.md               # 5과목 전체 인덱스 + 빈출 순 SVG 임베드
├── _generators/           # Python 다이어그램·SVG 생성기
│   ├── gen_db.py / gen_nw.py / gen_os.py / gen_pg.py / gen_se.py
│   └── export_svg.py      # .excalidraw → .svg 변환기 (무의존성)
├── db/  (6장 priority 3)  # 데이터베이스
├── nw/  (4장 priority 3)  # 네트워크
├── os/  (3장 priority 3)  # 운영체제·유지보수
├── pg/  (11장 priority 3) # 프로그래밍 언어
└── se/  (6장 priority 3)  # 소프트웨어 공학
```

priority 3 (🔥 매회 출제) 30장 전부 완료. priority 2 (⭐ 자주) / priority 1 (· 가끔) 확장 예정.

## 편집 및 배포 흐름

1. **편집**: `/Users/danny/wiki/certifications/정보처리기사/` 에서 Obsidian Excalidraw 플러그인으로
   직접 `.excalidraw` 파일을 연다. 레이아웃·텍스트 구조를 통째로 바꾸려면 `_generators/gen_*.py`
   해당 함수를 수정하고 재실행하는 편이 일관성 측면에서 안전하다.
2. **SVG 재생성**: `python3 _generators/export_svg.py` → 모든 `.excalidraw`가 옆자리 `.svg`로 재렌더링.
3. **동기화**: 레포 루트에서 `./sync-from-wiki.sh` 실행 → 위키 서브트리가 `content/`로 복사.
4. **커밋·푸시**: `git add content && git commit -m "..." && git push` → GitHub Actions(`deploy.yml`)가
   `npx quartz build` 실행 후 `public/`을 Pages로 배포.

## 로컬 미리보기
```bash
npm ci
npx quartz build --serve --port 8080
```
→ http://localhost:8080

## 기술 메모
- **Quartz v4.5.2** — Obsidian flavored wikilink 임베드 `![[db/x.svg]]`를 `<img>`로 자동 변환.
- **순수 Python SVG 변환기** — Puppeteer/Playwright 없이 `.excalidraw` JSON을 직접 SVG로 렌더.
  rectangle · ellipse · text · arrow · line만 지원하지만 본 프로젝트의 다이어그램엔 충분.
- **폰트**: Noto Sans KR (Google Fonts) — 한글 렌더링 확보.
- **ignorePatterns**: `**/*.excalidraw` — 원본 JSON은 사이트 빌드에서 제외, SVG만 노출.

## 원본 카드
Markdown 카드 원문은 [bite-size-study](https://github.com/cskwork/bite-size-study) 레포의
`content/cards/` 아래에 있다. 이 사이트의 다이어그램은 카드의 "핵심 개념 / 키워드 / 기출 포인트"
섹션을 시각화한 요약판이다.
