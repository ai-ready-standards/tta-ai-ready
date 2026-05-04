#!/bin/bash
# 국제 어휘 11종 다운로드 스크립트
# 각 어휘를 자체 권장 형식으로 받아 vocabularies/cached/ 에 저장한다.
#
# 본 스크립트는 .github/workflows/vocab-refresh.yml에서 주 1회 자동 실행되며,
# 변경이 감지되면 자동 PR을 생성한다.
#
# 수동 실행: bash tools/scripts/fetch_vocabularies.sh

set -e

# 저장소 루트 자동 탐지 (스크립트 위치 기준)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$( cd "$SCRIPT_DIR/../.." && pwd )"
DEST="$REPO_ROOT/vocabularies/cached"
mkdir -p "$DEST"
cd "$DEST"

# prefix | url | local file | Accept header
declare -a FETCHES=(
  "dcat|https://www.w3.org/ns/dcat3.ttl|dcat.ttl|text/turtle"
  "dct|https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl|dct.ttl|text/turtle"
  "dcmitype|http://purl.org/dc/dcmitype/|dcmitype.ttl|text/turtle"
  "prov|http://www.w3.org/ns/prov-o|prov.ttl|text/turtle"
  "sh|https://www.w3.org/ns/shacl.ttl|sh.ttl|text/turtle"
  "skos|https://www.w3.org/2009/08/skos-reference/skos.rdf|skos.rdf|application/rdf+xml"
  "schema|https://schema.org/version/latest/schemaorg-current-https.ttl|schema.ttl|text/turtle"
  "duo|https://raw.githubusercontent.com/EBISPOT/DUO/master/src/ontology/duo.owl|duo.owl|application/rdf+xml"
  "cc|https://creativecommons.org/schema.rdf|cc.rdf|application/rdf+xml"
  "foaf|http://xmlns.com/foaf/spec/index.rdf|foaf.rdf|application/rdf+xml"
  "datacite|https://sparontologies.github.io/datacite/current/datacite.ttl|datacite.ttl|text/turtle"
)

echo "정식 어휘 11종 다운로드 시작 → $DEST"
failed=0
for entry in "${FETCHES[@]}"; do
    IFS='|' read -r prefix url file accept <<< "$entry"
    echo -n "  [$prefix] $url ... "
    if curl -sSL -H "Accept: $accept" -o "$file" "$url" 2>/dev/null; then
        size=$(wc -c < "$file" | tr -d ' ')
        # HTML이 반환된 경우 감지
        if head -1 "$file" | grep -qi '^<!doctype\|^<html'; then
            echo "✗ HTML 반환 (${size} bytes) — URL 재검토 필요"
            failed=$((failed+1))
        else
            echo "✓ ${size} bytes → $file"
        fi
    else
        echo "✗ 다운로드 실패"
        failed=$((failed+1))
    fi
done

if [ $failed -gt 0 ]; then
    echo ""
    echo "❌ $failed 개 어휘 다운로드 실패"
    exit 1
fi

echo ""
echo "✅ 11개 어휘 모두 다운로드 완료"
ls -lh *.ttl *.rdf *.owl 2>/dev/null
