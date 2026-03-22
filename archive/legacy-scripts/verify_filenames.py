#!/usr/bin/env python3
r"""
Validate filenames against cross-platform naming conventions.

Rules:
1. Cross-platform compatibility (Windows, macOS, Linux)
2. Filename (before extension): all lowercase OR all uppercase (not mixed)
3. Extension (after final dot): always lowercase
4. Acronyms: allowed if surrounded by separators (-, _, .) or at start followed by separator
5. Human-readable: words separated by hyphens, fields separated by underscores
6. No forbidden characters: < > : " / \ | ? *
7. No trailing spaces or dots
8. Max 255 characters per path component
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple

# Ensure UTF-8 encoding for Windows console (only when running standalone, not under pytest)
if sys.platform == 'win32' and 'pytest' not in sys.modules:
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    except (AttributeError, ValueError):
        # Already wrapped or can't wrap (e.g., under pytest)
        pass

# Allowed acronyms (can be mixed case if properly separated)
ALLOWED_ACRONYMS = {
    'GS',  # Guidance-Spec
    'SG',  # Spec-Guidance
    'XML',
    'HTML',
    'JSON',
    'CSV',
    'PDF',
    'API',
    'CLI',
    'GUI',
    'SQL',
    'HTTP',
    'HTTPS',
    'URL',
    'URI',
    'UUID',
    'ISO',
    'ANSI',
    'IEEE',
    'INCOSE',
    'SaaS',
    'PaaS',
    'IaaS',
}

# Directories exempt from validation (external/legacy content)
EXEMPT_DIRECTORIES = {
    'submission/',
    '.git/',
    '.venv/',
    'venv/',
    'env/',
    '__pycache__/',
    '.pytest_cache/',
    'node_modules/',
    'dist/',
    'build/',
}

# Forbidden characters on Windows (and generally problematic)
# Note: Forward slash (/) and backslash (\) are path separators, not filename characters
FORBIDDEN_CHARS = r'[<>:"|?*\\/]'

# Separators: hyphen (word separator), underscore (field separator), dot (extension separator)
SEPARATOR_PATTERN = r'[-_.]'


def is_exempt(filepath: str) -> bool:
    """Check if file is in an exempt directory."""
    # Check if in exempt directory
    for exempt_dir in EXEMPT_DIRECTORIES:
        if filepath.startswith(exempt_dir):
            return True
    return False


def extract_acronyms_with_positions(text: str) -> List[Tuple[str, int, int]]:
    """
    Extract all acronym-like patterns and their positions from text.

    Returns list of (acronym, start_pos, end_pos) tuples.
    """
    acronyms = []
    # Find sequences of 2+ uppercase letters
    for match in re.finditer(r'[A-Z]{2,}', text):
        acronyms.append((match.group(), match.start(), match.end()))
    return acronyms


def is_properly_separated_acronym(text: str, acronym: str, start: int, end: int) -> bool:
    """
    Check if an acronym is properly separated by hyphens, underscores, or dots.

    Valid patterns:
    - At start of text followed by separator: "GS-root"
    - At end of text preceded by separator: "couples-GS"
    - Surrounded by separators: "couples-GS-root"
    """
    # Check if acronym is in allowed list
    if acronym not in ALLOWED_ACRONYMS:
        return False

    # Check character before (if not at start)
    before_ok = start == 0 or re.match(SEPARATOR_PATTERN, text[start - 1])

    # Check character after (if not at end)
    after_ok = end == len(text) or re.match(SEPARATOR_PATTERN, text[end])

    return before_ok and after_ok


def validate_filename_case(filename: str) -> Tuple[bool, List[str]]:
    """
    Validate filename follows case rules:
    - Filename (before extension): all lowercase OR all uppercase
    - Extension: always lowercase
    - Acronyms: allowed if properly separated

    Returns (is_valid, list_of_violations)
    """
    violations = []

    # Split into name and extension
    if '.' in filename:
        parts = filename.rsplit('.', 1)
        name = parts[0]
        extension = '.' + parts[1]
    else:
        name = filename
        extension = ''

    # Check extension is lowercase
    if extension and extension != extension.lower():
        violations.append(f"Extension must be lowercase: '{extension}' should be '{extension.lower()}'")

    # Check if name is all lowercase or all uppercase
    is_all_lower = name == name.lower()
    is_all_upper = name == name.upper()

    if is_all_lower or is_all_upper:
        # Valid: consistent case
        return (len(violations) == 0, violations)

    # Mixed case - check if it's only due to properly separated acronyms
    # Remove all allowed acronyms and check if remaining text is lowercase
    temp_name = name
    acronyms = extract_acronyms_with_positions(name)

    if not acronyms:
        # Mixed case but no acronyms found - invalid
        violations.append(
            f"Filename must be all lowercase or all uppercase (not mixed case): '{name}'"
        )
        return (False, violations)

    # Check each acronym is properly separated
    all_acronyms_valid = True
    invalid_acronyms = []

    for acronym, start, end in acronyms:
        if not is_properly_separated_acronym(name, acronym, start, end):
            all_acronyms_valid = False
            invalid_acronyms.append(acronym)

    if not all_acronyms_valid:
        violations.append(
            f"Invalid acronyms (not in allowed list or not properly separated): {invalid_acronyms}"
        )
        return (False, violations)

    # Replace all valid acronyms with lowercase equivalents and check result
    temp_name = name
    for acronym, start, end in sorted(acronyms, key=lambda x: x[1], reverse=True):
        temp_name = temp_name[:start] + acronym.lower() + temp_name[end:]

    if temp_name != temp_name.lower():
        violations.append(
            f"Filename has mixed case beyond allowed acronyms: '{name}'"
        )
        return (False, violations)

    return (len(violations) == 0, violations)


def validate_filename(filepath: str) -> Tuple[bool, List[str]]:
    """
    Validate a single filename against naming conventions.

    Returns:
        (is_valid, list_of_violations)
    """
    violations = []

    # Skip exempt files
    if is_exempt(filepath):
        return (True, [])

    path = Path(filepath)

    # Check each component of the path
    for component in path.parts:
        # Skip root or current directory markers
        if component in ('/', '.', '..'):
            continue

        # Check for forbidden characters
        if re.search(FORBIDDEN_CHARS, component):
            violations.append(f"Contains forbidden characters: '{component}'")

        # Check for trailing spaces or dots (Windows restriction)
        if component.endswith(' ') or component.endswith('.'):
            violations.append(f"Trailing space or dot: '{component}'")

        # Check length (255 char limit per component)
        if len(component) > 255:
            violations.append(f"Component too long (>255 chars): '{component}'")

        # Check case rules
        case_valid, case_violations = validate_filename_case(component)
        if not case_valid:
            violations.extend(case_violations)

    is_valid = len(violations) == 0
    return (is_valid, violations)


def validate_repository(repo_path: Path = None, tracked_only: bool = True) -> int:
    """
    Validate all files in repository.

    Args:
        repo_path: Path to repository root (default: current directory)
        tracked_only: Only check git-tracked files (default: True)

    Returns:
        Number of files with violations
    """
    if repo_path is None:
        repo_path = Path.cwd()

    violation_count = 0
    files_checked = 0

    if tracked_only:
        # Get git-tracked files
        import subprocess
        result = subprocess.run(
            ['git', 'ls-files'],
            cwd=repo_path,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"Error: Failed to get git-tracked files", file=sys.stderr)
            return -1

        files = result.stdout.strip().split('\n')
    else:
        # Get all files recursively
        files = [str(p.relative_to(repo_path)) for p in repo_path.rglob('*') if p.is_file()]

    for filepath in files:
        if not filepath:  # Skip empty lines
            continue

        files_checked += 1
        is_valid, violations = validate_filename(filepath)

        if not is_valid:
            violation_count += 1
            print(f"\n❌ {filepath}")
            for violation in violations:
                print(f"   - {violation}")

    # Print summary
    print(f"\n{'='*70}")
    print(f"Files checked: {files_checked}")
    print(f"Files with violations: {violation_count}")
    print(f"Files compliant: {files_checked - violation_count}")

    if violation_count == 0:
        print("\n✅ All filenames are compliant!")
    else:
        print(f"\n⚠️  {violation_count} file(s) need attention")

    return violation_count


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Validate filenames against cross-platform naming conventions'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Check all files, not just git-tracked files'
    )
    parser.add_argument(
        '--file',
        type=str,
        help='Check a single file'
    )

    args = parser.parse_args()

    if args.file:
        # Validate single file
        is_valid, violations = validate_filename(args.file)
        if is_valid:
            print(f"✅ {args.file} is compliant")
            sys.exit(0)
        else:
            print(f"❌ {args.file}")
            for violation in violations:
                print(f"   - {violation}")
            sys.exit(1)
    else:
        # Validate repository
        violation_count = validate_repository(tracked_only=not args.all)
        sys.exit(0 if violation_count == 0 else 1)
