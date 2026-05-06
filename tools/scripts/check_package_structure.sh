#!/bin/bash
# 6-패키지 구조 완전성 검사
#
# 본 사업 프레임워크 정의서 Part III에서 모든 AI 레디 표준이 갖춰야 할
# 6개 디렉토리 구조를 강제한다.
#
# 사용법:
#   bash check_package_structure.sh standards/P-01-research-data standards/P-02-public-data
#
# 인자가 없으면 standards/P-*-* 모두 검사.

set -e

REQUIRED_DIRS=(
  "1_document"
  "2_schema"
  "3_code"
  "4_validator"
  "5_examples"
  "6_changelog"
)

# 인자 없으면 모든 P-XX 패키지 자동 탐색
if [ $# -eq 0 ]; then
  set -- $(ls -d standards/P-*-* 2>/dev/null)
fi

failed=0
total_packages=0

for pkg in "$@"; do
  pkg="${pkg%/}"

  # 빈 인자나 기존에 없는 디렉토리는 스킵
  if [ ! -d "$pkg" ]; then
    continue
  fi

  total_packages=$((total_packages + 1))
  echo "=== $pkg ==="

  # README.md 의무
  if [ ! -f "$pkg/README.md" ]; then
    echo "  ❌ $pkg/README.md 누락"
    failed=$((failed + 1))
  else
    echo "  ✓ README.md"
  fi

  # 6 디렉토리 의무
  for dir in "${REQUIRED_DIRS[@]}"; do
    if [ ! -d "$pkg/$dir" ]; then
      echo "  ❌ $dir/ 디렉토리 누락"
      failed=$((failed + 1))
    else
      echo "  ✓ $dir/"
    fi
  done
  echo ""
done

echo "------------------------------------------------------------"
if [ $failed -gt 0 ]; then
  echo "❌ ${total_packages}개 패키지 중 $failed 항목 미달"
  echo "   참조: https://ai-ready-standards.github.io/tta-ai-ready/framework/#part-iii-6-패키지-요소"
  exit 1
fi

echo "✅ ${total_packages}개 패키지 모두 6-패키지 구조 완전"
