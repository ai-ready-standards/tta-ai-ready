# AI Ready Data 자체 어휘 (SKOS)

> ⚠️ **본 어휘는 사업 운영 어휘입니다 — 5종 표준 본체의 일부가 아닙니다.**
> 본 디렉토리의 어휘들은 본 사업이 5종 표준을 분류·매핑·운영하기 위해 정의한 **방법론 어휘**입니다.
> "AI Ready Data 형식의 표준 본문" 이 아니므로, 5종 표준을 사용·구현하시는 분께는 직접 필요하지 않습니다.
> 이 구분에 대한 상세는 사이트 [용어집](https://ai-ready-standards.github.io/tta-ai-ready/glossary/) 상단 안내를 참조하세요.

본 디렉토리는 TTA AI Ready Data가 정의하는 자체 어휘를 SKOS Concept Scheme 형식으로 보관합니다. 외부 어휘로 표현되지 않거나 한국어 권위 어휘가 필요한 경우에만 정의합니다.

## 어휘 목록

| 파일 | Concept Scheme | 분류축 | 술어(권장) | 카디널리티 |
| --- | --- | --- | --- | --- |
| [`aird-datatype.ttl`](./aird-datatype.ttl) | `aird-dt:DataTypeScheme` | **구조축** (데이터 형태) | `dct:type` | 1 (필수) |
| [`aird-intendeduse.ttl`](./aird-intendeduse.ttl) | `aird-iu:IntendedUseScheme` | **목적축** (활용 의도) | `aird:intendedUse` | 0..n (다중 허용) |

## 다축 분류 원칙

데이터의 **구조**(예: 표 형식, 그래프)와 **사용 목적**(예: ML 학습, RAG 코퍼스)은 직교 차원입니다. 한 데이터셋이 "표 형식이면서 ML 학습용이면서 통계 분석용"인 경우가 일반적이므로 단일 축으로 강제 분류하지 않고 두 슬롯을 병행 사용합니다.

## 외부 매핑

자체 어휘 개념의 외부 표준 정합성은 [`../../mappings/`](../../mappings/) 의 SKOS 매핑 파일로 관리합니다.

- `aird-datatype-to-schemaorg.ttl` — schema.org 매핑

## 거버넌스

자체 어휘에 새 Concept을 추가하거나 매핑을 변경하는 작업은 PG606 표준 제·개정 11단계 절차를 따릅니다. Concept 추가는 표준 단위가 아닌 어휘 단위 변경이므로, 별도의 "어휘/인프라 변경" 이슈 템플릿 도입이 권장됩니다 (후속 과제).

## URI 베이스

현재 URI 베이스는 공개 사이트 URL을 가정한 잠정값입니다.

```
https://ai-ready-standards.github.io/tta-ai-ready/vocab/datatype/
https://ai-ready-standards.github.io/tta-ai-ready/vocab/intendeduse/
```

정식 URI 정책 결정 후 일괄 갱신합니다.
