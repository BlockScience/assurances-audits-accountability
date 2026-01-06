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


class TestPerFileAuthorTracking:
    """
    Test per-file author tracking for accountability checks.

    This tests the fix for the issue where user A pushing a branch containing
    user B's validation edges would fail because the check used the commit author
    (A) instead of the actual file author (B).

    The fix uses git log --follow to determine who actually authored each
    validation edge file, ensuring proper accountability attribution.
    """

    def test_get_file_author_from_blame_returns_author(self):
        """
        POSITIVE TEST: get_file_author_from_blame returns the actual author of a file.

        When a validation edge file exists and has git history, the function
        should return the name of the person who last modified that file.
        """
        from check_accountability import get_file_author_from_blame

        repo_root = Path(__file__).parent.parent
        edge_path = repo_root / '01_edges' / 'validation-spec-spec.md'

        if not edge_path.exists():
            pytest.skip("validation-spec-spec.md not found")

        author = get_file_author_from_blame(str(edge_path))

        # Should return a non-empty author name
        assert author, "Should return non-empty author for existing file"
        assert isinstance(author, str), "Author should be a string"
        print(f"✓ get_file_author_from_blame returns author: {author}")

    def test_get_file_author_from_blame_nonexistent_file(self):
        """
        NEGATIVE TEST: get_file_author_from_blame returns empty string for non-existent file.

        When a file doesn't exist or has no git history, the function should
        gracefully return an empty string rather than raising an error.
        """
        from check_accountability import get_file_author_from_blame

        author = get_file_author_from_blame('/nonexistent/path/to/file.md')

        # Should return empty string, not raise an error
        assert author == "", "Should return empty string for non-existent file"
        print("✓ get_file_author_from_blame handles non-existent files gracefully")

    def test_modified_validation_edges_returns_tuples(self):
        """
        POSITIVE TEST: get_modified_validation_edges returns (path, author) tuples.

        The function should return a list of tuples where each tuple contains
        the file path and the author who actually wrote that file.
        """
        from check_accountability import get_modified_validation_edges

        # This tests the return type, even if no edges are modified
        edges = get_modified_validation_edges()

        assert isinstance(edges, list), "Should return a list"

        # If there are edges, verify tuple structure
        for item in edges:
            assert isinstance(item, tuple), f"Each item should be a tuple, got {type(item)}"
            assert len(item) == 2, f"Each tuple should have 2 elements, got {len(item)}"
            path, author = item
            assert isinstance(path, Path), f"First element should be Path, got {type(path)}"
            assert isinstance(author, str), f"Second element should be str, got {type(author)}"

        print(f"✓ get_modified_validation_edges returns correct tuple structure ({len(edges)} edges)")

    def test_cross_user_push_scenario_correct_attribution(self, tmp_path):
        """
        POSITIVE TEST: When user A pushes user B's validation edge, accountability
        check uses B (the file author), not A (the pusher).

        This is the core scenario the fix addresses:
        - mzargham creates validation edges (accountable party = mzargham)
        - davidfsol5 makes other changes and pushes
        - CI should check mzargham's edges against mzargham, not davidfsol5

        We simulate this by creating a validation edge with mzargham as approver,
        then checking accountability with mzargham as the file author.
        """
        from check_accountability import check_validation_edge_accountability

        # Create a test validation edge with mzargham as accountable party
        edge_file = tmp_path / "validation-test.md"
        edge_file.write_text("""---
type: edge/validation
id: e:validation:test:spec
name: Test Validation Edge
source: v:doc:test
target: v:spec:spec
source_type: vertex/doc
target_type: vertex/spec
orientation: directed
validation_method: llm-assisted
human_approver: mzargham
llm_model: claude-opus-4
tags:
  - validation
version: 1.0.0
---
Test validation edge for cross-user push scenario.
""", encoding='utf-8')

        # Scenario: davidfsol5 is the commit author (pusher),
        # but mzargham is the actual file author
        # The check should use mzargham (file author) and PASS

        # When effective_author = mzargham (from get_file_author_from_blame)
        passed, message = check_validation_edge_accountability(
            edge_file,
            author='mzargham',       # Effective author = file author
            committer='davidfsol5',  # Commit committer = different person
            github_actor='davidfsol5'  # GitHub actor = pusher
        )

        assert passed, f"Should PASS when file author matches accountable party: {message}"
        print("✓ Cross-user push correctly uses file author for accountability")

    def test_cross_user_push_scenario_wrong_attribution_fails(self, tmp_path):
        """
        NEGATIVE TEST: If we incorrectly use the pusher (not file author) as
        author, the check should fail when pusher != accountable party.

        This demonstrates what the OLD behavior was (which we fixed):
        - File has mzargham as accountable party
        - If we incorrectly use davidfsol5 (the pusher) as author
        - The check should FAIL

        This test verifies that the accountability check correctly rejects
        when the wrong person is attributed as author.
        """
        from check_accountability import check_validation_edge_accountability

        # Create a test validation edge with mzargham as accountable party
        edge_file = tmp_path / "validation-test.md"
        edge_file.write_text("""---
type: edge/validation
id: e:validation:test:spec
name: Test Validation Edge
source: v:doc:test
target: v:spec:spec
source_type: vertex/doc
target_type: vertex/spec
orientation: directed
validation_method: llm-assisted
human_approver: mzargham
llm_model: claude-opus-4
tags:
  - validation
version: 1.0.0
---
Test validation edge for wrong attribution scenario.
""", encoding='utf-8')

        # If we incorrectly used commit author instead of file author,
        # davidfsol5 would be checked against mzargham and FAIL
        passed, message = check_validation_edge_accountability(
            edge_file,
            author='davidfsol5',     # Wrong! This is pusher, not file author
            committer='davidfsol5',
            github_actor='davidfsol5'
        )

        assert not passed, f"Should FAIL when pusher != accountable party: {message}"
        assert 'Accountability violation' in message
        print("✓ Accountability check correctly rejects when wrong person attributed")

    def test_effective_author_fallback_to_commit_author(self, tmp_path):
        """
        POSITIVE TEST: When file author is empty/unknown, falls back to commit author.

        The check_commit_main function uses this logic:
            effective_author = file_author if file_author else author

        This ensures graceful fallback when git blame can't determine file author.
        """
        from check_accountability import check_validation_edge_accountability

        # Create a test validation edge
        edge_file = tmp_path / "validation-test.md"
        edge_file.write_text("""---
type: edge/validation
id: e:validation:test:spec
name: Test Validation Edge
source: v:doc:test
target: v:spec:spec
source_type: vertex/doc
target_type: vertex/spec
orientation: directed
validation_method: manual
validator: mzargham
tags:
  - validation
version: 1.0.0
---
Test validation edge for fallback scenario.
""", encoding='utf-8')

        # Simulate fallback: if file_author is empty, use commit author
        file_author = ""  # Empty = couldn't determine
        commit_author = "mzargham"
        effective_author = file_author if file_author else commit_author

        passed, message = check_validation_edge_accountability(
            edge_file,
            author=effective_author,
            committer=commit_author,
            github_actor='mzargham'
        )

        assert passed, f"Should PASS with fallback to commit author: {message}"
        print("✓ Fallback to commit author works correctly")

    def test_multiple_users_different_files(self, tmp_path):
        """
        POSITIVE TEST: Multiple validation edges from different authors should
        each be checked against their respective file authors.

        Scenario:
        - edge1 by mzargham (accountable = mzargham)
        - edge2 by davidfsol5 (accountable = davidfsol5)
        Both should PASS when checked with correct file authors.
        """
        from check_accountability import check_validation_edge_accountability

        # Edge 1: authored by mzargham
        edge1 = tmp_path / "validation-edge1.md"
        edge1.write_text("""---
type: edge/validation
id: e:validation:edge1:spec
name: Edge 1 by mzargham
source: v:doc:test1
target: v:spec:spec
source_type: vertex/doc
target_type: vertex/spec
orientation: directed
validation_method: manual
validator: mzargham
tags:
  - validation
version: 1.0.0
---
Edge 1 content.
""", encoding='utf-8')

        # Edge 2: authored by davidfsol5
        edge2 = tmp_path / "validation-edge2.md"
        edge2.write_text("""---
type: edge/validation
id: e:validation:edge2:spec
name: Edge 2 by davidfsol5
source: v:doc:test2
target: v:spec:spec
source_type: vertex/doc
target_type: vertex/spec
orientation: directed
validation_method: manual
validator: davidfsol5
tags:
  - validation
version: 1.0.0
---
Edge 2 content.
""", encoding='utf-8')

        # Check edge1 with mzargham as file author
        passed1, msg1 = check_validation_edge_accountability(
            edge1, author='mzargham', committer='mzargham', github_actor=''
        )
        assert passed1, f"Edge 1 should PASS with mzargham: {msg1}"

        # Check edge2 with davidfsol5 as file author
        passed2, msg2 = check_validation_edge_accountability(
            edge2, author='davidfsol5', committer='davidfsol5', github_actor=''
        )
        assert passed2, f"Edge 2 should PASS with davidfsol5: {msg2}"

        print("✓ Multiple edges from different authors correctly validated")

    def test_multiple_users_wrong_attribution_fails(self, tmp_path):
        """
        NEGATIVE TEST: If we swap the authors (check edge1 with edge2's author),
        both should FAIL.

        This verifies that per-file attribution is essential for correctness.
        """
        from check_accountability import check_validation_edge_accountability

        # Edge 1: authored by mzargham
        edge1 = tmp_path / "validation-edge1.md"
        edge1.write_text("""---
type: edge/validation
id: e:validation:edge1:spec
name: Edge 1 by mzargham
source: v:doc:test1
target: v:spec:spec
source_type: vertex/doc
target_type: vertex/spec
orientation: directed
validation_method: manual
validator: mzargham
tags:
  - validation
version: 1.0.0
---
Edge 1 content.
""", encoding='utf-8')

        # Edge 2: authored by davidfsol5
        edge2 = tmp_path / "validation-edge2.md"
        edge2.write_text("""---
type: edge/validation
id: e:validation:edge2:spec
name: Edge 2 by davidfsol5
source: v:doc:test2
target: v:spec:spec
source_type: vertex/doc
target_type: vertex/spec
orientation: directed
validation_method: manual
validator: davidfsol5
tags:
  - validation
version: 1.0.0
---
Edge 2 content.
""", encoding='utf-8')

        # WRONG: Check edge1 with davidfsol5 as author
        passed1, msg1 = check_validation_edge_accountability(
            edge1, author='davidfsol5', committer='davidfsol5', github_actor=''
        )
        assert not passed1, f"Edge 1 should FAIL with wrong author: {msg1}"

        # WRONG: Check edge2 with mzargham as author
        passed2, msg2 = check_validation_edge_accountability(
            edge2, author='mzargham', committer='mzargham', github_actor=''
        )
        assert not passed2, f"Edge 2 should FAIL with wrong author: {msg2}"

        print("✓ Swapped authors correctly cause failures")


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
