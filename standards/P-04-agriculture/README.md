# P-04 — 농업 AI 학습 데이터 (AI 레디 패키지)

## 대상 표준

- **표준번호**: TTAK.KO-10.1533
- **표준명**: 농업 분야 인공지능 학습 데이터 플랫폼 관리를 위한 메타데이터 스키마
- **제정**: 2024년 12월
- **소관**: PG606

## 국제 연계 어휘

- [MLCommons Croissant 1.0](https://mlcommons.org/croissant/) — ML 데이터셋 메타데이터
- [ISO/IEC 5259](https://www.iso.org/standard/81088.html) — 데이터 품질

## 패키지 구성

| 디렉토리 | 내용 | 상태 |
| --- | --- | --- |
| [`schema/`](./schema/) | Croissant 매핑 + 농업 특화 어휘 | 🚧 |
| [`shapes/`](./shapes/) | 영상 해상도·라벨 일관성·센서 결측률 SHACL | 🚧 |
| [`examples/`](./examples/) | 작물 유형·생육 단계·촬영 조건별 예시 | 🚧 |

## 농업 특화 어휘

- 작물 유형 (Crop type)
- 생육 단계 (Growth stage)
- 촬영 조건 (Capture conditions)
- 센서 메타데이터

## 핵심 차별점

- 영상·센서 결측률 SHACL 자동 검사
- ISO 5259 품질 차원 차용

## 일정

WBS C-8 (수행계획서 2.3절). 2026년 9월 착수, 11월 중순 완료.
