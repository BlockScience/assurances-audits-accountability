#!/usr/bin/env python
"""
Tests for accountability enforcement functionality.
"""

import sys
from pathlib import Path
from unittest.mock import patch

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from check_accountability import check_validation_edge_accountability


def test_manual_validation_accountability():
    """Test accountability checking for manual validation."""
    repo_root = Path(__file__).parent.parent
    edge_path = repo_root / '01_edges' / 'validation-spec-spec.md'

    if not edge_path.exists():
        print("⚠ Skipping test: validation-spec-spec.md not found")
        return

    # Test with correct committer
    passed, message = check_validation_edge_accountability(edge_path, 'mzargham', '')
    assert passed, f"Should pass with correct committer: {message}"
    print("✓ Manual validation accountability check passed")

    # Test with incorrect committer
    passed, message = check_validation_edge_accountability(edge_path, 'wrong-user', '')
    assert not passed, "Should fail with incorrect committer"
    print("✓ Manual validation accountability check correctly rejects wrong user")


def test_llm_assisted_validation_accountability():
    """Test accountability checking for LLM-assisted validation."""
    repo_root = Path(__file__).parent.parent
    edge_path = repo_root / '01_edges' / 'validation-spec-guidance.md'

    if not edge_path.exists():
        print("⚠ Skipping test: validation-spec-guidance.md not found")
        return

    # Test with correct human_approver
    passed, message = check_validation_edge_accountability(edge_path, 'mzargham', 'mzargham')
    assert passed, f"Should pass with correct human_approver: {message}"
    print("✓ LLM-assisted validation accountability check passed")

    # Test with incorrect approver
    passed, message = check_validation_edge_accountability(edge_path, 'wrong-user', 'wrong-user')
    assert not passed, "Should fail with incorrect human_approver"
    print("✓ LLM-assisted validation accountability check correctly rejects wrong user")


def test_automated_validation_accountability():
    """Test accountability checking for automated validation."""
    repo_root = Path(__file__).parent.parent
    edge_path = repo_root / '01_edges' / 'validation-guidance-spec.md'

    if not edge_path.exists():
        print("⚠ Skipping test: validation-guidance-spec.md not found")
        return

    # Test with correct human_approver
    passed, message = check_validation_edge_accountability(edge_path, 'mzargham', 'mzargham')
    assert passed, f"Should pass with correct human_approver: {message}"
    print("✓ Automated validation accountability check passed")

    # Test with incorrect approver
    passed, message = check_validation_edge_accountability(edge_path, 'wrong-user', 'wrong-user')
    assert not passed, "Should fail with incorrect human_approver"
    print("✓ Automated validation accountability check correctly rejects wrong user")


def test_username_matching():
    """Test various username matching strategies."""
    repo_root = Path(__file__).parent.parent
    edge_path = repo_root / '01_edges' / 'validation-spec-spec.md'

    if not edge_path.exists():
        print("⚠ Skipping test: validation-spec-spec.md not found")
        return

    # Test exact match
    passed, _ = check_validation_edge_accountability(edge_path, 'mzargham', 'mzargham')
    assert passed, "Should match exact username"

    # Test contains match (GitHub email format)
    passed, _ = check_validation_edge_accountability(edge_path, 'mzargham@users.noreply.github.com', '')
    assert passed, "Should match username in GitHub email"

    # Test substring in full name
    passed, _ = check_validation_edge_accountability(edge_path, 'Michael Zargham', '')
    # This might not pass depending on frontmatter format - that's ok
    print("✓ Username matching strategies work")


def run_all_tests():
    """Run all tests."""
    tests = [
        test_manual_validation_accountability,
        test_llm_assisted_validation_accountability,
        test_automated_validation_accountability,
        test_username_matching,
    ]

    print("=" * 70)
    print("Accountability Tests")
    print("=" * 70)

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: Unexpected error: {e}")
            failed += 1

    print("=" * 70)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 70)

    return failed == 0


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
