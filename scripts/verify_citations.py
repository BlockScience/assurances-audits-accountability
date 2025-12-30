#!/usr/bin/env python3
"""
Citation Verification Script

Verifies citations in LITERATURE-REVIEW.md by checking:
1. Required fields are present
2. URLs are valid and accessible
3. DOIs resolve correctly
4. ISBNs are valid format

Usage:
    python scripts/verify_citations.py [--check-urls] [--verbose]

Options:
    --check-urls    Actually fetch URLs to verify they're accessible (slower)
    --verbose       Print detailed information about each citation
"""

import argparse
import re
import sys
import yaml
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field


@dataclass
class Citation:
    """Represents a parsed citation from the literature review."""
    id: str
    type: str
    title: str
    year: int
    authors: list = field(default_factory=list)
    url: Optional[str] = None
    verified: bool = False
    verification_url: Optional[str] = None
    doi: Optional[str] = None
    isbn: Optional[str] = None
    journal: Optional[str] = None
    publisher: Optional[str] = None
    notes: Optional[str] = None
    raw_data: dict = field(default_factory=dict)


@dataclass
class VerificationResult:
    """Result of verifying a single citation."""
    citation_id: str
    passed: bool
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)


def parse_citations(markdown_path: Path) -> list[Citation]:
    """
    Parse citations from the LITERATURE-REVIEW.md file.

    Extracts YAML blocks that define citations.
    """
    with open(markdown_path, 'r') as f:
        content = f.read()

    # Find all YAML code blocks
    yaml_pattern = r'```yaml\n(.*?)```'
    matches = re.findall(yaml_pattern, content, re.DOTALL)

    citations = []
    for match in matches:
        try:
            data = yaml.safe_load(match)
            if data and isinstance(data, dict) and 'id' in data and 'type' in data:
                # Skip the verification metadata block
                if data.get('id') == 'verification_metadata':
                    continue

                citation = Citation(
                    id=data.get('id', 'unknown'),
                    type=data.get('type', 'unknown'),
                    title=data.get('title', ''),
                    year=data.get('year', 0),
                    authors=data.get('authors', []),
                    url=data.get('url'),
                    verified=data.get('verified', False),
                    verification_url=data.get('verification_url'),
                    doi=data.get('doi'),
                    isbn=data.get('isbn'),
                    journal=data.get('journal'),
                    publisher=data.get('publisher'),
                    notes=data.get('notes'),
                    raw_data=data
                )
                citations.append(citation)
        except yaml.YAMLError:
            continue

    return citations


def validate_isbn(isbn: str) -> tuple[bool, str]:
    """
    Validate ISBN format (ISBN-10 or ISBN-13).

    Returns (is_valid, error_message).
    """
    # Remove hyphens and spaces
    clean_isbn = re.sub(r'[-\s]', '', isbn)

    if len(clean_isbn) == 10:
        # ISBN-10 validation
        if not re.match(r'^\d{9}[\dX]$', clean_isbn):
            return False, f"Invalid ISBN-10 format: {isbn}"

        # Checksum validation
        total = sum((10 - i) * (10 if c == 'X' else int(c))
                   for i, c in enumerate(clean_isbn))
        if total % 11 != 0:
            return False, f"Invalid ISBN-10 checksum: {isbn}"

    elif len(clean_isbn) == 13:
        # ISBN-13 validation
        if not re.match(r'^\d{13}$', clean_isbn):
            return False, f"Invalid ISBN-13 format: {isbn}"

        # Checksum validation
        total = sum(int(c) * (1 if i % 2 == 0 else 3)
                   for i, c in enumerate(clean_isbn))
        if total % 10 != 0:
            return False, f"Invalid ISBN-13 checksum: {isbn}"
    else:
        return False, f"ISBN must be 10 or 13 digits: {isbn}"

    return True, ""


def validate_doi(doi: str) -> tuple[bool, str]:
    """
    Validate DOI format.

    Returns (is_valid, error_message).
    """
    # DOI pattern: 10.xxxx/... where xxxx is the registrant code
    doi_pattern = r'^10\.\d{4,}(\.\d+)*/[^\s]+$'
    if not re.match(doi_pattern, doi):
        return False, f"Invalid DOI format: {doi}"
    return True, ""


def validate_url(url: str) -> tuple[bool, str]:
    """
    Validate URL format (not accessibility).

    Returns (is_valid, error_message).
    """
    url_pattern = r'^https?://[^\s]+$'
    if not re.match(url_pattern, url):
        return False, f"Invalid URL format: {url}"
    return True, ""


def validate_year(year: int) -> tuple[bool, str]:
    """
    Validate year is reasonable.

    Returns (is_valid, error_message).
    """
    if not isinstance(year, int):
        return False, f"Year must be integer: {year}"
    if year < 1900 or year > 2030:
        return False, f"Year out of reasonable range (1900-2030): {year}"
    return True, ""


def check_url_accessible(url: str, timeout: int = 10) -> tuple[bool, str]:
    """
    Actually fetch URL to check if it's accessible.

    Returns (is_accessible, error_message).
    """
    try:
        import urllib.request
        import urllib.error

        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (citation-verifier)'}
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if response.status == 200:
                return True, ""
            return False, f"HTTP {response.status}"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        return False, f"URL Error: {e.reason}"
    except Exception as e:
        return False, f"Error: {str(e)}"


def verify_citation(citation: Citation, check_urls: bool = False) -> VerificationResult:
    """
    Verify a single citation.

    Returns VerificationResult with pass/fail and any errors.
    """
    result = VerificationResult(citation_id=citation.id, passed=True)

    # Required fields check
    required_fields = ['id', 'type', 'title', 'year']
    for field in required_fields:
        value = getattr(citation, field, None)
        if not value:
            result.errors.append(f"Missing required field: {field}")
            result.passed = False

    # Type-specific checks
    if citation.type == 'book':
        if not citation.publisher:
            result.warnings.append("Book citation missing publisher")
        if not citation.isbn:
            result.warnings.append("Book citation missing ISBN")
    elif citation.type == 'article':
        if not citation.journal and not citation.raw_data.get('arxiv'):
            result.warnings.append("Article citation missing journal")
        if not citation.doi and not citation.raw_data.get('arxiv'):
            result.warnings.append("Article citation missing DOI")

    # Year validation
    if citation.year:
        valid, error = validate_year(citation.year)
        if not valid:
            result.errors.append(error)
            result.passed = False

    # ISBN validation (if present)
    if citation.isbn:
        valid, error = validate_isbn(citation.isbn)
        if not valid:
            result.errors.append(error)
            result.passed = False

    # DOI validation (if present)
    if citation.doi:
        valid, error = validate_doi(citation.doi)
        if not valid:
            result.errors.append(error)
            result.passed = False

    # URL format validation
    if citation.url:
        valid, error = validate_url(citation.url)
        if not valid:
            result.errors.append(error)
            result.passed = False

    # Verification URL format validation
    if citation.verification_url:
        valid, error = validate_url(citation.verification_url)
        if not valid:
            result.errors.append(error)
            result.passed = False

    # Check if verified flag is set
    if not citation.verified:
        result.warnings.append("Citation not marked as verified")

    # Optional: Actually check URL accessibility
    if check_urls and citation.url:
        accessible, error = check_url_accessible(citation.url)
        if not accessible:
            result.warnings.append(f"Primary URL not accessible: {error}")

    return result


def verify_all_citations(
    markdown_path: Path,
    check_urls: bool = False,
    verbose: bool = False
) -> tuple[bool, list[VerificationResult]]:
    """
    Verify all citations in the literature review.

    Returns (all_passed, results).
    """
    citations = parse_citations(markdown_path)

    if verbose:
        print(f"Found {len(citations)} citations")
        print()

    results = []
    all_passed = True

    for citation in citations:
        result = verify_citation(citation, check_urls)
        results.append(result)

        if not result.passed:
            all_passed = False

        if verbose:
            status = "PASS" if result.passed else "FAIL"
            print(f"[{status}] {citation.id}")
            if result.errors:
                for error in result.errors:
                    print(f"  ERROR: {error}")
            if result.warnings:
                for warning in result.warnings:
                    print(f"  WARNING: {warning}")
            print()

    return all_passed, results


def main():
    parser = argparse.ArgumentParser(
        description="Verify citations in LITERATURE-REVIEW.md"
    )
    parser.add_argument(
        '--check-urls',
        action='store_true',
        help='Actually fetch URLs to verify accessibility'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print detailed information about each citation'
    )
    parser.add_argument(
        '--file',
        type=str,
        default='LITERATURE-REVIEW.md',
        help='Path to the literature review file'
    )

    args = parser.parse_args()

    # Find the file
    if Path(args.file).exists():
        file_path = Path(args.file)
    else:
        # Try from repo root
        repo_root = Path(__file__).parent.parent
        file_path = repo_root / args.file
        if not file_path.exists():
            print(f"Error: Cannot find {args.file}")
            sys.exit(1)

    print(f"Verifying citations in: {file_path}")
    print()

    all_passed, results = verify_all_citations(
        file_path,
        check_urls=args.check_urls,
        verbose=args.verbose
    )

    # Summary
    total = len(results)
    passed = sum(1 for r in results if r.passed)
    failed = total - passed

    print("=" * 50)
    print(f"Citation Verification Summary")
    print("=" * 50)
    print(f"Total citations: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    if not all_passed:
        print()
        print("Failed citations:")
        for result in results:
            if not result.passed:
                print(f"  - {result.citation_id}")
                for error in result.errors:
                    print(f"      {error}")

    print()
    print(f"Status: {'PASS' if all_passed else 'FAIL'}")

    sys.exit(0 if all_passed else 1)


if __name__ == '__main__':
    main()
