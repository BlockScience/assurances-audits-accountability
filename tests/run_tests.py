#!/usr/bin/env python
"""
Test runner for knowledge-complex-demo.

Runs all test suites and reports results.
"""

import sys
import subprocess
from pathlib import Path


def run_test_suite(test_file: Path) -> bool:
    """Run a test suite and return success status."""
    print(f"\n{'=' * 70}")
    print(f"Running: {test_file.name}")
    print('=' * 70)

    result = subprocess.run(
        [sys.executable, str(test_file)],
        capture_output=False,
        text=True
    )

    return result.returncode == 0


def main():
    """Run all test suites."""
    tests_dir = Path(__file__).parent

    test_suites = [
        # Core template and verification tests
        tests_dir / 'test_template_parser.py',
        tests_dir / 'test_verification.py',
        tests_dir / 'test_accountability.py',

        # Template generation tests (Phase 2)
        tests_dir / 'test_template_generation.py',

        # Critical functionality tests
        tests_dir / 'test_dependency_hierarchy.py',
        tests_dir / 'test_compilation.py',

        # Infrastructure tests
        tests_dir / 'test_cache.py',
        tests_dir / 'test_topology.py',
        tests_dir / 'test_verify_chart.py',
        tests_dir / 'test_parse.py',
    ]

    print("=" * 70)
    print("Knowledge Complex Regression Test Suite")
    print("=" * 70)

    results = {}
    for test_suite in test_suites:
        if not test_suite.exists():
            print(f"⚠ Warning: {test_suite.name} not found")
            continue

        results[test_suite.name] = run_test_suite(test_suite)

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    passed = sum(1 for success in results.values() if success)
    failed = sum(1 for success in results.values() if not success)

    for name, success in results.items():
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"{status}: {name}")

    print("=" * 70)
    print(f"Total: {passed} passed, {failed} failed")
    print("=" * 70)

    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
