# 기여 가이드 (Contributing)

본 저장소는 TTA 발주 사업의 산출물을 공개하는 미러입니다. 직접 푸시는 코어 팀(CODEOWNERS 참조)에 한정되며, 외부 기여는 GitHub Issue 및 Pull Request를 통해 제안할 수 있습니다.

## 운영 모델

- **마스터 저장소**: TTA 내부망 GitLab Enterprise (개발·심의·승인이 일어나는 곳)
- **공개 미러**: 본 GitHub 저장소 (자동 검증·승인을 통과한 패키지만 동기화)
- **편집 권한 3계층**: TC 편집자(쓰기) · 일반 열람자(읽기) · 자동화 봇(CI 전용)

## 기여 방법

### 1. 이슈 등록

- 신규 표준 AI 레디화 제안: `enhancement` 라벨
- 스키마/검증 오류: `bug` 라벨
- 매뉴얼/문서 보완: `documentation` 라벨

### 2. Pull Request

1. 이슈에서 작업을 협의한 후 PR을 생성합니다.
2. 모든 PR은 다음 CI 체크를 통과해야 머지됩니다.
   - JSON-LD 1.1 문법 검증
   - SHACL 적합성 검증 (pySHACL)
   - 예시 데이터셋 로딩 테스트
   - Python 단위 테스트 (커버리지 80% 이상)
   - 코드 린트 (flake8 / ruff, 경고 0건)
3. 코드 변경은 CODEOWNERS의 리뷰가 필수입니다.

### 3. 커밋 메시지 규칙

[Conventional Commits](https://www.conventionalcommits.org/) 형식을 권장합니다.

```
<type>(<scope>): <subject>

예:
feat(P-01): add JSON-LD schema for research data
fix(validator): correct SHACL shape for required fields
docs(framework): update 7 schema components definition
```

`type`: feat, fix, docs, refactor, test, chore

## 산출물 품질 기준

본 사업의 산출물은 4계층 품질 보증 체계를 따릅니다.

| 계층 | 주체 | 시점 |
| --- | --- | --- |
| L1 작성자 셀프 체크 | 작성 담당자 | 산출물 작성 직후 |
| L2 PM 검토 | PM (박사급) | 주간 PM 회의 |
| L3 외부 전문가 Peer Review | 외부 전문가 2인 이상 | 단계별 산출물 완성 시 |
| L4 자동화 검증 | CI/CD | 커밋 시점 |

| 산출물 유형 | 정량 통과 기준 |
| --- | --- |
| JSON-LD 스키마 | 문법 오류 0건, 국제 어휘 매핑 100% 검증 |
| SHACL 검증 파일 | 테스트 케이스 90% 이상 통과 |
| Python 참조 코드 | 단위 테스트 커버리지 80% 이상, 린트 경고 0건 |
| 예시 데이터셋 | 로딩·실행 성공률 100% |

## 보안

- 본 저장소에는 **공개 가능한 산출물만** 동기화합니다. 내부망 전용 자료, 인증 키, 발주처 미공개 자료는 절대 커밋하지 마십시오.
- 보안 사항 신고: GitHub Security Advisory 또는 사업 책임자에게 직접 연락

## 행동 규범

상호 존중과 건설적 협력을 원칙으로 합니다.
