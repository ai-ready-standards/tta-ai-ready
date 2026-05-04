# 매핑 빌드 스크립트 (참고용 보존)

본 디렉토리의 `_*.py` 스크립트는 `mappings/tta-0976_*.csv` 산출물을 만들 때 사용한 일회성 빌드 스크립트입니다. 결과물(CSV)이 이미 `mappings/`에 있으므로 일반 사용자는 이 스크립트를 실행할 필요가 없습니다.

향후 P-02~P-05의 매핑 빌드 시 참고용으로 보존합니다.

| 스크립트 | 출력물 |
| --- | --- |
| `_extract_sample.py` | tta-0976_review_sample.csv |
| `_append_11_50.py` + `_append_51_93.py` | tta-0976_x_components.csv (93행) |
| `_build_enum_mapping.py` | tta-0976_enumerations_mapping.csv (117행) |

⚠️ 스크립트 내부에 Windows 절대경로(`D:\ARD\...`)가 포함되어 있습니다. 다른 환경에서 실행하려면 경로 수정 필요.
