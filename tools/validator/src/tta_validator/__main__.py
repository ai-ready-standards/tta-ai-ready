"""tta-validator CLI 진입점."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .validate import discover_files, validate_file


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="tta-validator",
        description="TTA AI 레디 표준 적합성 자동 검증 CLI (TTAK.KO-10.0976 등)",
    )
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="검증할 JSON-LD 파일 또는 디렉토리",
    )
    parser.add_argument(
        "--shapes-dir",
        type=Path,
        default=Path("standards/P-01-research-data/2_schema"),
        help="SHACL shapes (.ttl) 디렉토리 (default: P-01의 2_schema)",
    )
    parser.add_argument(
        "--ci",
        action="store_true",
        help="CI 모드: M(Violation) 1건 이상이면 exit code 1",
    )
    parser.add_argument(
        "--expect-fail",
        action="store_true",
        help="음성 테스트: M 위반이 발생해야 통과 (없으면 exit 1)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="상세 결과 텍스트 전체 출력",
    )
    args = parser.parse_args(argv)

    files = discover_files(args.paths)
    if not files:
        print("[error] No .jsonld files found in given paths.", file=sys.stderr)
        return 2

    if not args.shapes_dir.is_dir():
        print(f"[error] Shapes directory not found: {args.shapes_dir}", file=sys.stderr)
        return 2

    total = len(files)
    total_violations = 0
    total_warnings = 0
    total_infos = 0
    failed_files = 0

    print(f"검증 대상: {total}개 파일 / shapes: {args.shapes_dir}")
    print("-" * 60)

    for f in files:
        try:
            result = validate_file(f, args.shapes_dir)
        except Exception as exc:  # noqa: BLE001
            print(f"  ✗ {f.relative_to(Path.cwd()) if f.is_absolute() else f}")
            print(f"    [parse-error] {exc}")
            failed_files += 1
            continue

        rel = f.relative_to(Path.cwd()) if f.is_absolute() and Path.cwd() in f.parents else f
        # 통과 기준: M(Violation) 0건. R(Warning), O(Info)는 통과/실패에 영향 없음.
        passed = result.violations == 0
        marker = "✓" if passed else "✗"
        summary = f"M:{result.violations} R:{result.warnings} O:{result.infos}"
        print(f"  {marker} {rel}  ({summary})")

        if args.verbose and not passed:
            for line in result.text.splitlines():
                if any(k in line for k in ("Severity", "Source Shape", "Focus Node", "Result Path", "Result Message", "Value")):
                    print(f"    {line}")

        total_violations += result.violations
        total_warnings += result.warnings
        total_infos += result.infos
        if not passed:
            failed_files += 1

    print("-" * 60)
    print(f"합계: {total}개 / 위반(M)={total_violations}  경고(R)={total_warnings}  정보(O)={total_infos}")

    if args.expect_fail:
        if total_violations == 0:
            print("\n[expect-fail] M 위반이 발생해야 했지만 0건. 음성 테스트 실패.", file=sys.stderr)
            return 1
        print(f"\n[expect-fail] M 위반 {total_violations}건 발생 — 음성 테스트 통과")
        return 0

    if args.ci and total_violations > 0:
        print(f"\n[CI] M 위반 {total_violations}건 — 머지 차단", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
