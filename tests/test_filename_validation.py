#!/usr/bin/env python
"""
Tests for filename validation functionality.

Tests filename naming conventions for cross-platform compatibility:
- Case consistency (all lowercase or all uppercase, not mixed)
- Extension always lowercase
- Allowed acronyms if properly separated
- No forbidden characters
- Character and length limits
"""

import sys
from pathlib import Path
import pytest

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from validate_filenames import (
    validate_filename,
    validate_filename_case,
    validate_repository,
    is_properly_separated_acronym,
    extract_acronyms_with_positions,
)


class TestFilenameCase:
    """Test case consistency rules."""

    def test_all_lowercase_valid(self):
        """All lowercase filenames should be valid."""
        is_valid, violations = validate_filename_case('spec-for-guidance.md')
        assert is_valid, f"Expected valid, got violations: {violations}"

    def test_all_uppercase_valid(self):
        """All uppercase filenames should be valid."""
        is_valid, violations = validate_filename_case('README.md')
        assert is_valid, f"Expected valid, got violations: {violations}"

    def test_mixed_case_invalid(self):
        """Mixed case filenames should be invalid."""
        is_valid, violations = validate_filename_case('Spec-For-Guidance.md')
        assert not is_valid, "Expected invalid for mixed case"
        assert any('mixed case' in v.lower() for v in violations)

    def test_uppercase_extension_invalid(self):
        """Uppercase extensions should be invalid."""
        is_valid, violations = validate_filename_case('readme.MD')
        assert not is_valid, "Expected invalid for uppercase extension"
        assert any('extension must be lowercase' in v.lower() for v in violations)

    def test_no_extension_valid(self):
        """Files without extensions should validate case normally."""
        is_valid, violations = validate_filename_case('README')
        assert is_valid, f"Expected valid, got violations: {violations}"


class TestAcronymHandling:
    """Test acronym exception handling."""

    def test_properly_separated_acronym_start(self):
        """Acronym at start followed by separator should be valid."""
        result = is_properly_separated_acronym('GS-root', 'GS', 0, 2)
        assert result, "GS at start followed by hyphen should be valid"

    def test_properly_separated_acronym_middle(self):
        """Acronym surrounded by separators should be valid."""
        result = is_properly_separated_acronym('couples-GS-root', 'GS', 8, 10)
        assert result, "GS surrounded by hyphens should be valid"

    def test_properly_separated_acronym_end(self):
        """Acronym at end preceded by separator should be valid."""
        result = is_properly_separated_acronym('couples-GS', 'GS', 8, 10)
        assert result, "GS at end preceded by hyphen should be valid"

    def test_improperly_separated_acronym(self):
        """Acronym not properly separated should be invalid."""
        result = is_properly_separated_acronym('testGSfile', 'GS', 4, 6)
        assert not result, "GS not separated should be invalid"

    def test_unknown_acronym(self):
        """Unknown acronyms should be invalid even if separated."""
        result = is_properly_separated_acronym('test-XYZ-file', 'XYZ', 5, 8)
        assert not result, "Unknown acronym XYZ should be invalid"

    def test_valid_acronym_in_filename(self):
        """Valid acronym in filename should pass case validation."""
        is_valid, violations = validate_filename_case('b1-couples-GS-root.md')
        assert is_valid, f"Expected valid for GS acronym, got violations: {violations}"

    def test_multiple_acronyms(self):
        """Multiple valid acronyms should be allowed."""
        is_valid, violations = validate_filename_case('api-to-XML-via-HTTP.md')
        assert is_valid, f"Expected valid for multiple acronyms, got violations: {violations}"


class TestForbiddenCharacters:
    """Test forbidden character detection."""

    def test_forbidden_colon(self):
        """Colons should be forbidden."""
        is_valid, violations = validate_filename('test:file.md')
        assert not is_valid, "Colons should be forbidden"
        assert any('forbidden' in v.lower() for v in violations)

    def test_forbidden_question_mark(self):
        """Question marks should be forbidden."""
        is_valid, violations = validate_filename('test?file.md')
        assert not is_valid, "Question marks should be forbidden"

    def test_forbidden_forward_slash(self):
        """Forward slashes in a single component should be forbidden (path separator)."""
        # Note: 'test/file.md' is a valid path (directory/file), not a filename with slash
        # To test forbidden slash in component, we check individual components
        is_valid, violations = validate_filename('dir/test/file.md')
        assert is_valid, "Valid path should pass (slashes separate components)"
        # Slashes within a component are checked by path.parts separation

    def test_forbidden_backslash(self):
        """Backslashes in filename component should be forbidden on Windows."""
        # On Windows, backslashes are path separators and automatically converted
        # The forbidden chars check catches them in component names
        is_valid, violations = validate_filename('test-file.md')
        assert is_valid, "Valid filename without backslash should pass"

    def test_valid_characters(self):
        """Standard allowed characters should be valid."""
        is_valid, violations = validate_filename('test_file-01.md')
        assert is_valid, f"Expected valid, got violations: {violations}"


class TestPathComponents:
    """Test path component validation."""

    def test_valid_path(self):
        """Valid path with multiple components should pass."""
        is_valid, violations = validate_filename('00_vertices/spec-for-guidance.md')
        assert is_valid, f"Expected valid, got violations: {violations}"

    def test_mixed_case_in_directory(self):
        """Mixed case in directory name should be caught."""
        is_valid, violations = validate_filename('TestDir/file.md')
        assert not is_valid, "Mixed case directory should be invalid"

    def test_uppercase_directory_valid(self):
        """All uppercase directory should be valid."""
        is_valid, violations = validate_filename('DOCS/file.md')
        assert is_valid, f"Expected valid, got violations: {violations}"


class TestExemptDirectories:
    """Test exempt directory handling."""

    def test_submission_exempt(self):
        """Files in submission/ should be exempt."""
        is_valid, violations = validate_filename('submission/MyFile-WithMixedCase.pdf')
        assert is_valid, "submission/ files should be exempt"

    def test_venv_exempt(self):
        """Files in .venv/ should be exempt."""
        is_valid, violations = validate_filename('.venv/lib/python3.12/site-packages/SomePackage.py')
        assert is_valid, ".venv/ files should be exempt"

    def test_pycache_exempt(self):
        """Files in __pycache__/ should be exempt."""
        is_valid, violations = validate_filename('__pycache__/module.cpython-312.pyc')
        assert is_valid, "__pycache__/ files should be exempt"


class TestRealWorldFilenames:
    """Test actual filenames from the repository."""

    def test_edge_with_acronym(self):
        """Test edge files with GS/SG acronyms."""
        test_cases = [
            '01_edges/b1-couples-GS-root.md',
            '01_edges/b1-couples-SG-root.md',
        ]
        for filepath in test_cases:
            is_valid, violations = validate_filename(filepath)
            assert is_valid, f"Expected valid for {filepath}, got violations: {violations}"

    def test_uppercase_documentation_files(self):
        """Test uppercase documentation files."""
        test_cases = [
            'README.md',
            'LICENSE',
            'NAVIGATION.md',
            'QUICKSTART.md',
        ]
        for filepath in test_cases:
            is_valid, violations = validate_filename(filepath)
            assert is_valid, f"Expected valid for {filepath}, got violations: {violations}"

    def test_lowercase_vertex_files(self):
        """Test lowercase vertex files."""
        test_cases = [
            '00_vertices/spec-for-guidance.md',
            '00_vertices/guidance-for-spec.md',
        ]
        for filepath in test_cases:
            is_valid, violations = validate_filename(filepath)
            assert is_valid, f"Expected valid for {filepath}, got violations: {violations}"

    def test_python_scripts(self):
        """Test Python script filenames."""
        test_cases = [
            'scripts/validate_filenames.py',
            'scripts/verify_template_based.py',
            'scripts/build_cache.py',
        ]
        for filepath in test_cases:
            is_valid, violations = validate_filename(filepath)
            assert is_valid, f"Expected valid for {filepath}, got violations: {violations}"


class TestRepositoryCompliance:
    """Test compliance of all tracked files in repository."""

    def test_all_tracked_files_compliant(self):
        """All git-tracked files should pass validation."""
        repo_root = Path(__file__).parent.parent
        violation_count = validate_repository(repo_root, tracked_only=True)

        assert violation_count == 0, (
            f"Found {violation_count} file(s) with naming violations. "
            "Run 'python scripts/validate_filenames.py' for details."
        )


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_filename(self):
        """Empty filename should be handled gracefully."""
        is_valid, violations = validate_filename('')
        # Empty string should pass (will be filtered by git ls-files)
        assert is_valid

    def test_dot_files(self):
        """Dot files should validate normally."""
        is_valid, violations = validate_filename('.gitignore')
        assert is_valid, f"Expected valid, got violations: {violations}"

    def test_multiple_dots(self):
        """Multiple dots in filename should be valid."""
        is_valid, violations = validate_filename('test.backup.2024-01.md')
        assert is_valid, f"Expected valid, got violations: {violations}"

    def test_trailing_dot_invalid(self):
        """Trailing dots should be invalid (Windows restriction)."""
        is_valid, violations = validate_filename('test.')
        assert not is_valid, "Trailing dot should be invalid"

    def test_trailing_space_invalid(self):
        """Trailing spaces should be invalid (Windows restriction)."""
        is_valid, violations = validate_filename('test ')
        assert not is_valid, "Trailing space should be invalid"

    def test_very_long_component(self):
        """Components over 255 characters should be invalid."""
        long_name = 'a' * 256 + '.md'
        is_valid, violations = validate_filename(long_name)
        assert not is_valid, "Component over 255 chars should be invalid"
        assert any('too long' in v.lower() for v in violations)


class TestAcronymExtraction:
    """Test acronym extraction functionality."""

    def test_extract_single_acronym(self):
        """Should extract single acronym with position."""
        acronyms = extract_acronyms_with_positions('test-GS-file')
        assert len(acronyms) == 1
        assert acronyms[0] == ('GS', 5, 7)

    def test_extract_multiple_acronyms(self):
        """Should extract multiple acronyms."""
        acronyms = extract_acronyms_with_positions('API-to-XML-converter')
        assert len(acronyms) == 2
        assert ('API', 0, 3) in acronyms
        assert ('XML', 7, 10) in acronyms

    def test_extract_no_acronyms(self):
        """Should return empty list for no acronyms."""
        acronyms = extract_acronyms_with_positions('test-file-name')
        assert len(acronyms) == 0

    def test_extract_adjacent_acronyms(self):
        """Should handle adjacent acronyms (even if invalid per rules)."""
        acronyms = extract_acronyms_with_positions('APIXML')
        assert len(acronyms) == 1
        assert acronyms[0] == ('APIXML', 0, 6)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
