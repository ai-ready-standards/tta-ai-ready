"""매핑 매트릭스 CSV 품질 검사.

본 사업 프레임워크 정의서 Part VI 권고 기준:
- mapping_priority의 'primary' 비율 80% 이상
- mapping_confidence의 'high' 비율 75% 이상
- 매핑 부재 ('none') 비율 5% 이하

P-01 실적 (참고): primary 88.2%, high 81.7%, none 0% — 모두 기준 초과 통과.

사용법:
    python check_mapping_quality.py mappings/tta-0976_x_components.csv
    python check_mapping_quality.py mappings/*.csv
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path


THRESHOLDS = {
    "primary_ratio": 0.80,
    "high_confidence_ratio": 0.75,
    "max_none_ratio": 0.05,
}


def check_csv(csv_path: Path) -> tuple[bool, list[str]]:
    if not csv_path.is_file():
        return False, [f"파일 없음: {csv_path}"]

    issues: list[str] = []

    # BOM 처리
    with csv_path.open(encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        return False, [f"빈 CSV: {csv_path}"]

    total = len(rows)

    # mapping_priority 분포
    priority_counts: dict[str, int] = {}
    for row in rows:
        p = (row.get("mapping_priority") or "").strip().lower()
        priority_counts[p] = priority_counts.get(p, 0) + 1

    primary = priority_counts.get("primary", 0)
    primary_ratio = primary / total
    none_count = priority_counts.get("none", 0)
    none_ratio = none_count / total

    # mapping_confidence 분포
    conf_counts: dict[str, int] = {}
    for row in rows:
        c = (row.get("mapping_confidence") or "").strip().lower()
        conf_counts[c] = conf_counts.get(c, 0) + 1

    high = conf_counts.get("high", 0)
    high_ratio = high / total

    # 출력
    print(f"=== {csv_path} ===")
    print(f"  총 {total}행")
    print(f"  mapping_priority 분포:")
    for p in sorted(priority_counts.keys()):
        n = priority_counts[p]
        marker = " ★" if p == "primary" else ""
        print(f"    {p:<14} {n:>4} ({100 * n / total:>5.1f}%){marker}")
    print(f"  mapping_confidence 분포:")
    for c in sorted(conf_counts.keys()):
        n = conf_counts[c]
        marker = " ★" if c == "high" else ""
        print(f"    {c:<14} {n:>4} ({100 * n / total:>5.1f}%){marker}")

    # 기준 검사
    print(f"  품질 기준:")

    if primary_ratio >= THRESHOLDS["primary_ratio"]:
        print(
            f"    ✓ primary 비율 {100 * primary_ratio:.1f}% "
            f">= 기준 {100 * THRESHOLDS['primary_ratio']:.0f}%"
        )
    else:
        msg = (
            f"primary 비율 {100 * primary_ratio:.1f}% "
            f"< 기준 {100 * THRESHOLDS['primary_ratio']:.0f}%"
        )
        print(f"    ❌ {msg}")
        issues.append(msg)

    if high_ratio >= THRESHOLDS["high_confidence_ratio"]:
        print(
            f"    ✓ high confidence {100 * high_ratio:.1f}% "
            f">= 기준 {100 * THRESHOLDS['high_confidence_ratio']:.0f}%"
        )
    else:
        msg = (
            f"high confidence {100 * high_ratio:.1f}% "
            f"< 기준 {100 * THRESHOLDS['high_confidence_ratio']:.0f}%"
        )
        print(f"    ❌ {msg}")
        issues.append(msg)

    if none_ratio <= THRESHOLDS["max_none_ratio"]:
        print(
            f"    ✓ none 비율 {100 * none_ratio:.1f}% "
            f"<= 기준 {100 * THRESHOLDS['max_none_ratio']:.0f}%"
        )
    else:
        msg = (
            f"none 비율 {100 * none_ratio:.1f}% "
            f"> 기준 {100 * THRESHOLDS['max_none_ratio']:.0f}%"
        )
        print(f"    ❌ {msg}")
        issues.append(msg)

    print()
    return len(issues) == 0, issues


def main() -> int:
    if len(sys.argv) < 2:
        print(
            "사용법: python check_mapping_quality.py <csv_path>...",
            file=sys.stderr,
        )
        return 2

    all_passed = True
    paths = [Path(p) for p in sys.argv[1:]]

    if not paths:
        print("ℹ️ 검사할 CSV 파일이 없습니다.")
        return 0

    for path in paths:
        passed, _ = check_csv(path)
        if not passed:
            all_passed = False

    print("------------------------------------------------------------")
    if all_passed:
        print("✅ 모든 매핑 매트릭스가 품질 기준 충족")
        return 0
    else:
        print("❌ 일부 매핑 매트릭스가 품질 기준 미달")
        return 1


if __name__ == "__main__":
    sys.exit(main())
