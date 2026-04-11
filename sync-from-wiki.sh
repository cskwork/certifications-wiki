#!/usr/bin/env bash
#
# bite-size-study 카드 원본 → 이 Quartz 레포의 content/ 재생성.
#
# 새 워크플로(networked-thought 구조):
#   1) ~/Documents/PARA/Resource/bite-size-study/content/cards/ 에서 카드 편집
#   2) 이 스크립트 실행 → content/ 재빌드(과목별 개별 .md + MOC)
#   3) git add -A && git commit && git push → GitHub Actions가 배포
#
# 구조:
#   _generators/_card_parser.py       카드 파서(공용)
#   _generators/gen_quartz_pages.py   카드 → 개별 페이지 생성
#   _generators/export_svg.py         .excalidraw → .svg
#
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_ROOT"

echo "→ 카드 → Quartz 페이지 재생성"
python3 _generators/gen_quartz_pages.py

echo ""
echo "✓ content/ 파일 수:"
find content -type f \( -name '*.md' -o -name '*.svg' -o -name '*.excalidraw' \) | wc -l | xargs -I{} echo "  {} files"
