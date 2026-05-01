# P-03 — 비정형 데이터 태깅·라벨링 (AI 레디 패키지)

## 대상 표준

- **표준번호**: TTAK.KO-10.1343-Part2
- **표준명**: 데이터 가공 공정 직무 구성 - 제2부 비정형 데이터 태깅 및 라벨링
- **소관**: PG606
- **연계**: NIA AI Hub 600종 데이터셋

## 국제 연계 어휘

- [MLCommons Croissant 1.0 RAI Extension](https://mlcommons.org/croissant/) — 책임 있는 AI 어휘
- [DUO (Data Use Ontology)](https://github.com/EBISPOT/DUO) — 사용 제약

## 패키지 구성

| 디렉토리 | 내용 | 상태 |
| --- | --- | --- |
| [`schema/`](./schema/) | Croissant RAI 연계 JSON-LD 스키마 | 🚧 |
| [`shapes/`](./shapes/) | 라벨 품질 자동 검증 (SHACL + 통계) | 🚧 |
| [`examples/`](./examples/) | PyTorch DataLoader 호환 Python 로더 + 예시 | 🚧 |

## 핵심 차별점

- PyTorch DataLoader 한 줄 로딩 호환
- 라벨 품질 자동 검증 (SHACL + 통계 검사)
- DUO 어휘 기반 사용 제약

## 일정

WBS C-7 (수행계획서 2.3절). 2026년 9월 착수, 11월 중순 완료.
