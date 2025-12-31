#!/usr/bin/env python3
"""
Tests for the citation verification script.

Tests both valid and invalid citation fixtures to ensure
the verification script correctly identifies errors.
"""

import pytest
import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from verify_citations import (
    parse_citations,
    verify_citation,
    verify_all_citations,
    validate_isbn,
    validate_doi,
    validate_url,
    validate_year,
    Citation,
)


class TestValidateFunctions:
    """Test individual validation functions."""

    # ISBN validation tests
    def test_valid_isbn_13(self):
        """Test valid ISBN-13."""
        valid, error = validate_isbn("978-0-13-468599-1")
        assert valid, f"Should be valid: {error}"

    def test_valid_isbn_10(self):
        """Test valid ISBN-10."""
        valid, error = validate_isbn("0-201-63361-2")
        assert valid, f"Should be valid: {error}"

    def test_valid_isbn_10_with_x(self):
        """Test valid ISBN-10 with X check digit."""
        valid, error = validate_isbn("0-8044-2957-X")
        assert valid, f"Should be valid: {error}"

    def test_invalid_isbn_checksum(self):
        """Test ISBN with invalid checksum."""
        valid, error = validate_isbn("978-0-13-468599-0")
        assert not valid, "Should be invalid (bad checksum)"
        assert "checksum" in error.lower()

    def test_invalid_isbn_length(self):
        """Test ISBN with wrong length."""
        valid, error = validate_isbn("978-0-13-46859")
        assert not valid, "Should be invalid (wrong length)"
        assert "10 or 13" in error

    # DOI validation tests
    def test_valid_doi(self):
        """Test valid DOI."""
        valid, error = validate_doi("10.1234/test.2023.0042")
        assert valid, f"Should be valid: {error}"

    def test_valid_doi_complex(self):
        """Test valid DOI with complex suffix."""
        valid, error = validate_doi("10.1090/S0273-0979-09-01249-X")
        assert valid, f"Should be valid: {error}"

    def test_invalid_doi_format(self):
        """Test DOI with invalid format."""
        valid, error = validate_doi("not-a-valid-doi")
        assert not valid, "Should be invalid"
        assert "format" in error.lower()

    def test_invalid_doi_missing_prefix(self):
        """Test DOI missing 10. prefix."""
        valid, error = validate_doi("1234/test.2023")
        assert not valid, "Should be invalid (missing 10.)"

    # URL validation tests
    def test_valid_https_url(self):
        """Test valid HTTPS URL."""
        valid, error = validate_url("https://www.example.com/path")
        assert valid, f"Should be valid: {error}"

    def test_valid_http_url(self):
        """Test valid HTTP URL."""
        valid, error = validate_url("http://www.example.com/path")
        assert valid, f"Should be valid: {error}"

    def test_invalid_url_ftp(self):
        """Test FTP URL (should be invalid)."""
        valid, error = validate_url("ftp://ftp.example.com/file")
        assert not valid, "Should be invalid (not http/https)"

    def test_invalid_url_no_protocol(self):
        """Test URL without protocol."""
        valid, error = validate_url("www.example.com/path")
        assert not valid, "Should be invalid (no protocol)"

    # Year validation tests
    def test_valid_year_current(self):
        """Test current year."""
        valid, error = validate_year(2024)
        assert valid, f"Should be valid: {error}"

    def test_valid_year_old(self):
        """Test old but valid year."""
        valid, error = validate_year(1950)
        assert valid, f"Should be valid: {error}"

    def test_invalid_year_too_old(self):
        """Test year that's too old."""
        valid, error = validate_year(1850)
        assert not valid, "Should be invalid (too old)"
        assert "range" in error.lower()

    def test_invalid_year_future(self):
        """Test year in far future."""
        valid, error = validate_year(2099)
        assert not valid, "Should be invalid (future)"
        assert "range" in error.lower()


class TestParseCitations:
    """Test citation parsing from markdown files."""

    def test_parse_valid_citations(self):
        """Test parsing valid citations fixture."""
        fixtures_dir = Path(__file__).parent / 'fixtures'
        valid_file = fixtures_dir / 'citations_valid.md'

        citations = parse_citations(valid_file)

        assert len(citations) == 5, f"Expected 5 citations, got {len(citations)}"

        # Check first citation
        book = next(c for c in citations if c.id == 'Valid-Book-2020')
        assert book.type == 'book'
        assert book.year == 2020
        assert book.isbn == '978-0-13-468599-1'
        assert book.verified is True

    def test_parse_invalid_citations(self):
        """Test parsing invalid citations fixture."""
        fixtures_dir = Path(__file__).parent / 'fixtures'
        invalid_file = fixtures_dir / 'citations_invalid.md'

        citations = parse_citations(invalid_file)

        assert len(citations) == 9, f"Expected 9 citations, got {len(citations)}"


class TestVerifyCitation:
    """Test individual citation verification."""

    def test_verify_valid_book(self):
        """Test verification of valid book citation."""
        citation = Citation(
            id='Test-Book',
            type='book',
            title='Test Book Title',
            year=2020,
            authors=['Author, Test'],
            publisher='Test Publisher',
            isbn='978-0-13-468599-1',
            url='https://www.example.com/book',
            verified=True,
            verification_url='https://www.example.com/verify'
        )

        result = verify_citation(citation)
        assert result.passed, f"Should pass: {result.errors}"

    def test_verify_missing_title(self):
        """Test verification catches missing title."""
        citation = Citation(
            id='Missing-Title',
            type='book',
            title='',  # Empty title
            year=2020,
            authors=['Author, Test'],
        )

        result = verify_citation(citation)
        assert not result.passed, "Should fail (missing title)"
        assert any('title' in e.lower() for e in result.errors)

    def test_verify_bad_isbn(self):
        """Test verification catches bad ISBN."""
        citation = Citation(
            id='Bad-ISBN',
            type='book',
            title='Test Book',
            year=2020,
            isbn='978-0-13-468599-0',  # Bad checksum
            verified=True,
        )

        result = verify_citation(citation)
        assert not result.passed, "Should fail (bad ISBN)"
        assert any('isbn' in e.lower() or 'checksum' in e.lower() for e in result.errors)

    def test_verify_bad_doi(self):
        """Test verification catches bad DOI."""
        citation = Citation(
            id='Bad-DOI',
            type='article',
            title='Test Article',
            year=2023,
            journal='Test Journal',
            doi='not-a-valid-doi',
            verified=True,
        )

        result = verify_citation(citation)
        assert not result.passed, "Should fail (bad DOI)"
        assert any('doi' in e.lower() for e in result.errors)

    def test_verify_bad_url(self):
        """Test verification catches bad URL."""
        citation = Citation(
            id='Bad-URL',
            type='article',
            title='Test Article',
            year=2023,
            url='not-a-valid-url',
            verified=True,
        )

        result = verify_citation(citation)
        assert not result.passed, "Should fail (bad URL)"
        assert any('url' in e.lower() for e in result.errors)


class TestVerifyAllCitations:
    """Test bulk citation verification."""

    def test_verify_all_valid(self):
        """Test that all valid citations pass."""
        fixtures_dir = Path(__file__).parent / 'fixtures'
        valid_file = fixtures_dir / 'citations_valid.md'

        all_passed, results = verify_all_citations(valid_file)

        assert all_passed, "All valid citations should pass"
        assert len(results) == 5
        for result in results:
            assert result.passed, f"{result.citation_id} should pass: {result.errors}"

    def test_verify_all_invalid_fail(self):
        """Test that invalid citations are caught."""
        fixtures_dir = Path(__file__).parent / 'fixtures'
        invalid_file = fixtures_dir / 'citations_invalid.md'

        all_passed, results = verify_all_citations(invalid_file)

        assert not all_passed, "Should have failures"

        # Check specific expected failures
        failed_ids = [r.citation_id for r in results if not r.passed]

        assert 'Missing-Title' in failed_ids, "Missing-Title should fail"
        assert 'Bad-ISBN-Checksum' in failed_ids, "Bad-ISBN-Checksum should fail"
        assert 'Bad-ISBN-Length' in failed_ids, "Bad-ISBN-Length should fail"
        assert 'Bad-DOI' in failed_ids, "Bad-DOI should fail"
        assert 'Bad-URL' in failed_ids, "Bad-URL should fail"
        assert 'Bad-Year-Old' in failed_ids, "Bad-Year-Old should fail"
        assert 'Bad-Year-Future' in failed_ids, "Bad-Year-Future should fail"
        assert 'Missing-Year' in failed_ids, "Missing-Year should fail"
        assert 'Bad-Verification-URL' in failed_ids, "Bad-Verification-URL should fail"


class TestRealLiteratureReview:
    """Test the actual literature-review.md file."""

    def test_literature_review_passes(self):
        """Verify that the real literature review file passes all checks."""
        # Try multiple paths to find the file
        possible_paths = [
            Path(__file__).parent.parent / 'docs' / 'references' / 'literature-review.md',
            Path.cwd() / 'docs' / 'references' / 'literature-review.md',
        ]

        lit_review = None
        for path in possible_paths:
            if path.exists():
                lit_review = path
                break

        if lit_review is None:
            pytest.skip("docs/references/literature-review.md not found")

        all_passed, results = verify_all_citations(lit_review)

        # Print failures for debugging
        if not all_passed:
            for result in results:
                if not result.passed:
                    print(f"FAILED: {result.citation_id}")
                    for error in result.errors:
                        print(f"  - {error}")

        assert all_passed, "literature-review.md should pass all citation checks"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
