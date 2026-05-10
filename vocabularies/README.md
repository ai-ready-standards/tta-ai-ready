# Vocabularies — 외부 어휘 캐시 + 자체 어휘

본 디렉토리는 두 종류의 어휘를 보관합니다.

| 하위 디렉토리 | 용도 | 출처 |
| --- | --- | --- |
| [`cached/`](./cached/) | **외부 어휘 캐시** — 본 사업이 참조·매핑하는 국제 표준 어휘의 RDF 정의 | W3C, MLCommons, EBI 등 |
| [`aird/`](./aird/) | **자체 어휘** — TTA AI Ready Data가 정의하는 한국어 권위 어휘 (SKOS Concept Scheme) | TTA PG606 |

자체 어휘는 외부 어휘로 의미를 다 표현할 수 없을 때만 정의하며, 가능한 모든 자체 개념은 `mappings/aird-*-to-*.ttl` 에서 외부 어휘와의 정합성을 SKOS 매핑 술어(`skos:exactMatch` / `closeMatch` / `relatedMatch`)로 명시합니다.

## 외부 어휘 캐시 (`cached/`)

## 왜 캐시하나

- **검증 속도**: CI 매 실행마다 11개 사이트에 접속하면 느리고 외부 사이트가 잠시 다운되면 CI가 실패함
- **재현성**: 어휘 버전을 git에 고정 → 어떤 시점이든 동일하게 검증
- **오프라인 작업**: 네트워크 없이도 검증 가능

## 자동 갱신

`.github/workflows/vocab-refresh.yml` 워크플로우가 **매주 월요일 새벽**에 자동 실행되어:
1. 11개 어휘를 최신본으로 다운로드
2. 변경이 있으면 자동 PR 생성
3. PM 리뷰·머지를 거쳐 캐시 갱신

긴급 갱신이 필요하면 수동 트리거 가능: GitHub Actions → "Vocab Refresh" → "Run workflow"

## 검증 흐름

```
context.jsonld + shapes/*.ttl
       ↓
   IRI 추출 (수십~수백 개)
       ↓
   prefix → vocabulary 매핑 (MANIFEST.json)
       ↓
   각 IRI가 해당 vocabulary에 정의되어 있는지 확인
       ↓
   100% 정의됨 → ✅  /  하나라도 미정의 → ❌
```

수동 검증:
```bash
tta-verify-mappings
```

## 캐시된 어휘

| Prefix | 파일 | 정식 출처 |
| --- | --- | --- |
| dcat | dcat.ttl | https://www.w3.org/ns/dcat3.ttl |
| dct | dct.ttl | https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| dcmitype | dcmitype.ttl | http://purl.org/dc/dcmitype/ |
| prov | prov.ttl | http://www.w3.org/ns/prov-o |
| sh | sh.ttl | https://www.w3.org/ns/shacl.ttl |
| skos | skos.rdf | https://www.w3.org/2009/08/skos-reference/skos.rdf |
| schema | schema.ttl | https://schema.org/ |
| duo | duo.owl | https://github.com/EBISPOT/DUO |
| cc | cc.rdf | https://creativecommons.org |
| foaf | foaf.rdf | http://xmlns.com/foaf/spec/ |
| datacite | datacite.ttl | https://sparontologies.github.io/datacite/ |

상세 메타데이터는 [`MANIFEST.json`](./cached/MANIFEST.json) 참조.

## 어휘 자체 갱신 (수동)

```bash
bash tools/scripts/fetch_vocabularies.sh
```

(스크립트 위치: `tools/scripts/fetch_vocabularies.sh`)
