#!/usr/bin/env bash
#
# 위키 서브트리(정보처리기사)를 이 Quartz 레포의 content/로 동기화한다.
# 편집 워크플로:
#   1) Obsidian에서 /Users/danny/wiki/certifications/정보처리기사/ 편집
#   2) 필요 시 _generators 아래 스크립트 재실행
#   3) 이 스크립트 실행해 content/ 최신화
#   4) git add content && git commit && git push  → GitHub Actions가 배포
#
set -euo pipefail

SRC="/Users/danny/wiki/certifications/정보처리기사/"
DST="$(cd "$(dirname "$0")" && pwd)/content/"

if [[ ! -d "$SRC" ]]; then
  echo "❌ source not found: $SRC" >&2
  exit 1
fi

echo "→ sync $SRC  →  $DST"

rsync -av --delete \
  --exclude='_generators/__pycache__' \
  --exclude='.obsidian' \
  --exclude='.DS_Store' \
  "$SRC" "$DST"

echo ""
echo "✓ sync complete. files in content/:"
find "$DST" -maxdepth 2 -type f \( -name '*.md' -o -name '*.svg' -o -name '*.excalidraw' \) | wc -l | xargs -I{} echo "  {} files"
