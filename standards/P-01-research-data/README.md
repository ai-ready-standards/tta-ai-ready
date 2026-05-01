# P-01 — 연구데이터 메타데이터 (AI 레디 패키지)

## 대상 표준

- **표준명**: 연구데이터 관리 및 공유를 위한 메타데이터
- **제정**: 2017년 (TTA)
- **소관**: PG606
- **본 수행사 직접 개발 표준** — 본 사업의 첫 번째 파일럿이자 가장 이상적인 조건의 파일럿

## 국제 연계 어휘

- [DataCite Metadata Schema 4.5](https://schema.datacite.org/) — 연구데이터 인용 메타데이터
- [W3C DCAT v3](https://www.w3.org/TR/vocab-dcat-3/) — 데이터셋 일반 어휘
- [W3C PROV-O](https://www.w3.org/TR/prov-o/) — 출처·계보
- [MLCommons Croissant 1.0](https://mlcommons.org/croissant/) — 운영 시맨틱

## 패키지 구성

| 디렉토리 | 내용 | 상태 |
| --- | --- | --- |
| [`schema/`](./schema/) | JSON-LD 1.1 스키마 + DataCite·DCAT v3 매핑 | 🚧 |
| [`shapes/`](./shapes/) | pySHACL 검증 규칙 | 🚧 |
| [`examples/`](./examples/) | 예시 데이터셋 3종 | 🚧 |

## 신규 4개 구성요소 적용 현황

본 파일럿은 신규 4개 구성요소(검증·계보·사용제약·품질)를 **모두** 적용하는 가장 완전한 형태로 개발됩니다.

- [ ] SHACL 검증 규칙
- [ ] PROV-O 출처·계보
- [ ] DUO 사용 제약
- [ ] ISO 5259 품질 프로파일

## 일정

WBS C-5 (수행계획서 2.3절). 2026년 8월 착수, 11월 중순 완료.

## 검증

```bash
tta-validator standards/P-01-research-data/examples/
```
