#!/bin/bash
# AP (Application Profile) 명세의 필수 6 섹션 검사
#
# 본 사업 프레임워크 정의서 Part III에서 1_document/<id>-AP.md가
# 다음 6 섹션을 모두 갖춰야 한다고 규정:
#
#   ## 1. 개요
#   ## 2. 7개 구성요소 적용 결과
#   ## 3. (자원 모델 / 4계층-3계층 매핑)
#   ## 4. 통제어 카테고리
#   ## 5. 핵심 매핑 결정
#   ## 6. 사용 가이드
#
# Placeholder (1_document에 .gitkeep만 있는 경우)는 검사 생략.
#
# 사용법:
#   bash check_ap_sections.sh standards/P-01-research-data ...

set -e

# 6 섹션 시작 패턴 (정규식). "## 1." ~ "## 6."
REQUIRED_PATTERNS=(
  "^## 1\."
  "^## 2\."
  "^## 3\."
  "^## 4\."
  "^## 5\."
  "^## 6\."
)

if [ $# -eq 0 ]; then
  set -- $(ls -d standards/P-*-* 2>/dev/null)
fi

failed=0
checked=0
skipped=0

for pkg in "$@"; do
  pkg="${pkg%/}"

  if [ ! -d "$pkg" ]; then
    continue
  fi

  # 1_document/<id>-AP.md 파일 찾기 (README, .gitkeep 제외)
  ap_files=$(find "$pkg/1_document" -maxdepth 1 -name "*.md" 2>/dev/null | grep -v "/README.md" || true)

  if [ -z "$ap_files" ]; then
    # placeholder 처리
    if [ -f "$pkg/1_document/.gitkeep" ]; then
      echo "$pkg: placeholder (AP 미작성) — 검사 생략"
      skipped=$((skipped + 1))
      continue
    else
      echo "❌ $pkg: 1_document/<id>-AP.md 누락"
      failed=$((failed + 1))
      continue
    fi
  fi

  # 첫 번째 AP 파일에 대해 검사
  ap=$(echo "$ap_files" | head -1)
  echo "=== $ap ==="
  checked=$((checked + 1))

  for pattern in "${REQUIRED_PATTERNS[@]}"; do
    if grep -qE "$pattern" "$ap"; then
      # 패턴 첫 매치 라인 출력
      first_match=$(grep -m1 -E "$pattern" "$ap" | head -1)
      echo "  ✓ $first_match"
    else
      echo "  ❌ '$pattern' 시작 섹션 누락"
      failed=$((failed + 1))
    fi
  done
  echo ""
done

echo "------------------------------------------------------------"
if [ $failed -gt 0 ]; then
  echo "❌ $failed 항목 실패"
  echo "   AP 명세 작성 가이드: https://ai-ready-standards.github.io/tta-ai-ready/framework/#part-iii-6-패키지-요소"
  exit 1
fi

if [ $checked -eq 0 ] && [ $skipped -gt 0 ]; then
  echo "ℹ️ 모든 패키지가 placeholder ($skipped개) — AP 검사 생략"
  exit 0
fi

echo "✅ ${checked}개 AP 명세 모두 6 섹션 완전 (placeholder ${skipped}개 생략)"
