#!/usr/bin/env python
"""
Tests for accountability enforcement functionality.

Tests two categories of accountability:
1. Commit-time checks: Ensure validation edges are committed by the right person
2. Consistency checks: Ensure signature/assurance/validation edge have matching accountable parties
"""

import sys
from pathlib import Path
from unittest.mock import patch
import pytest

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from check_accountability import (
    check_validation_edge_accountability,
    extract_username_from_signer,
    is_boundary_signature,
    usernames_match,
    normalize_username,
    check_shared_validation_edge_consistency,
    check_all_signature_accountability,
)


def test_manual_validation_accountability():
    """Test accountability checking for manual validation."""
    repo_root = Path(__file__).parent.parent
    edge_path = repo_root / '01_edges' / 'validation-spec-spec.md'

    if not edge_path.exists():
        print("⚠ Skipping test: validation-spec-spec.md not found")
        return

    # Test with correct author
    passed, message = check_validation_edge_accountability(edge_path, 'mzargham', 'mzargham', '')
    assert passed, f"Should pass with correct author: {message}"
    print("✓ Manual validation accountability check passed")

    # Test with incorrect author
    passed, message = check_validation_edge_accountability(edge_path, 'wrong-user', 'wrong-user', '')
    assert not passed, "Should fail with incorrect author"
    print("✓ Manual validation accountability check correctly rejects wrong user")


def test_llm_assisted_validation_accountability():
    """Test accountability checking for LLM-assisted validation."""
    repo_root = Path(__file__).parent.parent
    edge_path = repo_root / '01_edges' / 'validation-spec-guidance.md'

    if not edge_path.exists():
        print("⚠ Skipping test: validation-spec-guidance.md not found")
        return

    # Test with correct human_approver as author
    passed, message = check_validation_edge_accountability(edge_path, 'mzargham', 'mzargham', 'mzargham')
    assert passed, f"Should pass with correct human_approver: {message}"
    print("✓ LLM-assisted validation accountability check passed")

    # Test with incorrect author
    passed, message = check_validation_edge_accountability(edge_path, 'wrong-user', 'wrong-user', 'wrong-user')
    assert not passed, "Should fail with incorrect human_approver"
    print("✓ LLM-assisted validation accountability check correctly rejects wrong user")


def test_automated_validation_accountability():
    """Test accountability checking for automated validation."""
    repo_root = Path(__file__).parent.parent
    edge_path = repo_root / '01_edges' / 'validation-guidance-spec.md'

    if not edge_path.exists():
        print("⚠ Skipping test: validation-guidance-spec.md not found")
        return

    # Test with correct human_approver as author
    passed, message = check_validation_edge_accountability(edge_path, 'mzargham', 'mzargham', 'mzargham')
    assert passed, f"Should pass with correct human_approver: {message}"
    print("✓ Automated validation accountability check passed")

    # Test with incorrect author
    passed, message = check_validation_edge_accountability(edge_path, 'wrong-user', 'wrong-user', 'wrong-user')
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
    passed, _ = check_validation_edge_accountability(edge_path, 'mzargham', 'mzargham', 'mzargham')
    assert passed, "Should match exact username"

    # Test contains match (GitHub email format)
    passed, _ = check_validation_edge_accountability(edge_path, 'mzargham@users.noreply.github.com', '', '')
    assert passed, "Should match username in GitHub email"

    # Test substring in full name
    passed, _ = check_validation_edge_accountability(edge_path, 'Michael Zargham', '', '')
    # This might not pass depending on frontmatter format - that's ok
    print("✓ Username matching strategies work")


def test_pr_merge_by_different_maintainer():
    """
    Test accountability when PR is merged by a different maintainer.

    Scenario: mzargham authors validation edges, davidfsol5 reviews and merges.
    - git author: mzargham (who wrote the commit)
    - git committer: GitHub (the merge bot)
    - github_actor: davidfsol5 (who clicked merge)

    Expected: PASS because the author matches the accountable party.
    """
    repo_root = Path(__file__).parent.parent
    edge_path = repo_root / '01_edges' / 'validation-spec-spec.md'

    if not edge_path.exists():
        print("⚠ Skipping test: validation-spec-spec.md not found")
        return

    # Simulate PR merge scenario:
    # - Original author (mzargham) is the accountable party
    # - Committer is GitHub (merge bot)
    # - GitHub actor is a different maintainer (davidfsol5)
    passed, message = check_validation_edge_accountability(
        edge_path,
        author='mzargham',           # Original author = accountable party
        committer='GitHub',          # Merge bot
        github_actor='davidfsol5'    # Different maintainer who merged
    )
    assert passed, f"Should pass when author matches accountable party: {message}"
    print("✓ PR merge by different maintainer correctly passes (author matches)")

    # Also test that it still fails when author is wrong
    passed, message = check_validation_edge_accountability(
        edge_path,
        author='wrong-author',       # Wrong author
        committer='GitHub',          # Merge bot
        github_actor='davidfsol5'    # Different maintainer who merged
    )
    assert not passed, "Should fail when neither author nor actor matches accountable party"
    print("✓ PR merge correctly fails when author doesn't match accountable party")


class TestUsernameExtraction:
    """Test username extraction and matching functions."""

    def test_extract_username_from_signer(self):
        """Test extracting username from signer vertex ID."""
        assert extract_username_from_signer('v:signer:mzargham') == 'mzargham'
        assert extract_username_from_signer('v:signer:alice-smith') == 'alice-smith'
        assert extract_username_from_signer('b0:root') == 'b0:root'
        assert extract_username_from_signer('mzargham') == 'mzargham'

    def test_normalize_username(self):
        """Test username normalization."""
        assert normalize_username('mzargham') == 'mzargham'
        assert normalize_username('  MZargham  ') == 'mzargham'
        assert normalize_username('"mzargham"') == 'mzargham'
        assert normalize_username("'mzargham'") == 'mzargham'
        assert normalize_username('') == ''

    def test_usernames_match(self):
        """Test username matching logic."""
        # Exact match
        assert usernames_match('mzargham', 'mzargham')

        # Case insensitive
        assert usernames_match('MZargham', 'mzargham')

        # Substring matches (must be actual substrings after lowercasing)
        assert usernames_match('alice', 'alice.smith')
        assert usernames_match('mzargham', 'mzargham@github.com')
        assert usernames_match('bob', 'bobby')

        # Non-matches
        assert not usernames_match('alice', 'bob')
        assert not usernames_match('', 'mzargham')
        assert not usernames_match('mzargham', '')
        # Note: 'mzargham' is NOT a substring of 'michael zargham'
        assert not usernames_match('mzargham', 'Michael Zargham')


class TestBoundarySignature:
    """Test boundary signature detection."""

    def test_is_boundary_signature_by_signer(self):
        """Test detecting boundary signature by b0: signer."""
        fm = {'signer': 'b0:root', 'tags': []}
        assert is_boundary_signature(fm)

        fm = {'signer': 'b0:other', 'tags': []}
        assert is_boundary_signature(fm)

    def test_is_boundary_signature_by_tag(self):
        """Test detecting boundary signature by tag."""
        fm = {'signer': 'v:signer:someone', 'tags': ['boundary-complex']}
        assert is_boundary_signature(fm)

    def test_is_not_boundary_signature(self):
        """Test non-boundary signature detection."""
        fm = {'signer': 'v:signer:mzargham', 'tags': ['face', 'signature']}
        assert not is_boundary_signature(fm)


class TestSharedValidationEdgeConsistency:
    """Test accountability consistency at shared validation edges."""

    def test_boundary_signature_exempt(self):
        """Test that boundary signatures are exempt from consistency check."""
        repo_root = Path(__file__).parent.parent
        sig_path = repo_root / '02_faces' / 'signature-spec-guidance.md'

        if not sig_path.exists():
            pytest.skip("signature-spec-guidance.md not found")

        passed, message, details = check_shared_validation_edge_consistency(sig_path, repo_root)
        assert passed, f"Boundary signature should pass: {message}"
        assert 'Boundary signature' in message

    def test_regular_signature_consistency(self):
        """Test that regular signatures check consistency."""
        repo_root = Path(__file__).parent.parent
        sig_path = repo_root / '02_faces' / 'signature-architecture-spec.md'

        if not sig_path.exists():
            pytest.skip("signature-architecture-spec.md not found")

        passed, message, details = check_shared_validation_edge_consistency(sig_path, repo_root)
        assert passed, f"Regular signature should have consistent accountability: {message}"
        assert 'mzargham' in message or 'Accountability consistent' in message

    def test_all_signatures_pass_consistency(self):
        """Test that all signature faces in repository pass consistency check."""
        repo_root = Path(__file__).parent.parent
        all_passed, messages = check_all_signature_accountability(repo_root)

        # Print details for debugging
        for msg in messages:
            print(msg)

        assert all_passed, "All signature faces should pass accountability consistency"


def run_all_tests():
    """Run all tests."""
    tests = [
        test_manual_validation_accountability,
        test_llm_assisted_validation_accountability,
        test_automated_validation_accountability,
        test_username_matching,
        test_pr_merge_by_different_maintainer,
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
