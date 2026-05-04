# 5_examples — JSON-LD Instance Examples

3개 도메인의 완전한 JSON-LD 인스턴스. 모두 `2_schema/context.jsonld` 참조.

| 파일 | 도메인 | 시작 계층 | 시연 패턴 |
|---|---|---|---|
| `kisti_dataon.jsonld` | 정보과학 (KISTI) | Repository | 4계층 + ★ Boolean Activation Slot 활성 + 다국어 |
| `nie_environmental.jsonld` | 환경 (국립생태원) | Dataset → 2 Files | Coverage dual-purpose (공간/시간 동시 시연) |
| `rda_agriculture.jsonld` | 농업 (농촌진흥청) | Repository → Collection → Dataset → File | 4계층 완전 시연 + Boolean Slot 비활성 |

## 1. KISTI DataON (`kisti_dataon.jsonld`)

**시연 포인트**:
- Repository 계층 (R1-R21 거의 모두 채움)
- 다국어 라벨 (ko + en)
- ★ **Boolean Activation Slot 활성**: `QualityManagement: "yes"` → `hasQualityMetadata` 추가됨 (Decision-Q4)
- 4계층 구조: Repository → Collection (1개)
- 다중 Subject (정보과학 + 컴퓨터과학) — SKOS Concept 패턴

**용도**: TTA-AP의 모든 핵심 기능 시연.

## 2. NIE Environmental (`nie_environmental.jsonld`)

**시연 포인트**:
- Dataset 계층부터 시작 (Repository 미포함, 즉 단독 데이터셋)
- Dataset → 2 Files 관계 (계층 분리)
- ★ **Coverage dual-purpose 양쪽 시연**:
  - File 1 (`main.csv`): 공간 형식 — `"한반도 전역 (북위 33°-43°, 동경 124°-132°)"`
  - File 2 (`metadata.json`): 시간 형식 — `"2025-01-01T00:00:00+09:00 to 2025-12-31T23:59:59+09:00"`
- 한국 도메인 라벨 + ORCID 식별자 + 환경부 Funder
- KOGL 라이선스 한국 사례

**용도**: Decision-3.1 (Coverage dual-purpose) sh:or 패턴 검증.

## 3. RDA Agriculture (`rda_agriculture.jsonld`)

**시연 포인트**:
- **★ 4계층 완전 시연**: Repository → Collection → Dataset → File (4 levels nested)
- ★ Boolean Activation Slot **비활성**: `QualityManagement: "no"` → `hasQualityMetadata` 미포함
- 정부 리포지터리 (RepositoryType: governmental)
- 공공데이터 라이선스 (KOGL)
- 다중 File: CSV + GeoJSON (FileType별 시연)
- FileSize 단위: B + MB 혼용 (정규화 시연 — Issue-002 fallback)

**용도**: TTA의 4계층 구조의 완전한 시연 + 한국 공공데이터 정렬.

## 검증 방법

```bash
cd D:\ARD\packages\tta-0976\

# 각 예시 검증
python 4_validator/validate.py 5_examples/kisti_dataon.jsonld
python 4_validator/validate.py 5_examples/nie_environmental.jsonld
python 4_validator/validate.py 5_examples/rda_agriculture.jsonld

# 또는 Pydantic fallback (pySHACL 미설치 시)
python 4_validator/validate.py --fallback-pydantic 5_examples/kisti_dataon.jsonld
```

기대: 3개 모두 `✓ Conforms: True`.

## Python 코드로 로드

```python
from tta_0976.loader import load_from_jsonld

# alpha-3 → alpha-2 자동 변환 (Decision-002)
# Subject Class → SKOS Concept 자동 처리 (Decision-2)
repo = load_from_jsonld('5_examples/kisti_dataon.jsonld')
print(repo.RepositoryName.ko)  # "DataON"
print(repo.QualityManagement)  # BooleanPlus.yes
```

## 사용된 결정 사항 매트릭스

| 결정 | kisti_dataon | nie_environmental | rda_agriculture |
|---|---|---|---|
| Decision-002 (alpha-2) | ✓ KR | — (Dataset only) | ✓ KR |
| Decision-2 (SKOS Concept) | ✓ 2 Concepts | ✓ 2 Concepts | ✓ 다층 |
| Decision-Q4 (Boolean Slot 활성) | ✓ yes → 활성 | — | ✓ no → 비활성 |
| Decision-3.1 (Coverage dual) | — | ✓ 시간+공간 양쪽 | ✓ 시간+공간 양쪽 |
| 4계층 구조 | Repository → Collection | Dataset → File | **★ 4계층 모두** |
| 다국어 라벨 | ✓ ko+en | ✓ ko+en | ✓ ko+en |
