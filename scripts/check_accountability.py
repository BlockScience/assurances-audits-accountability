#!/usr/bin/env python
"""
Accountability Verification for Validation Edges

Ensures that validation edges are only committed by the accountable party
listed in the frontmatter (validator for manual, human_approver for
llm-assisted/automated).

This script is designed to run in GitHub Actions CI to enforce accountability
via required status checks on pull requests.

Usage:
    python scripts/check_accountability.py

Exit codes:
    0 - All accountability checks passed
    1 - Accountability violation found or error occurred

Environment variables (GitHub Actions):
    GITHUB_ACTOR - The GitHub username of the person who triggered the workflow
    GITHUB_EVENT_NAME - The event that triggered the workflow (push, pull_request)
"""

import sys
import os
import subprocess
from pathlib import Path
from typing import List, Tuple, Optional

sys.path.insert(0, str(Path(__file__).parent))
from parse_chart import extract_frontmatter, ParseError


class AccountabilityError(Exception):
    """Error raised when accountability check fails."""
    pass


def get_git_author() -> str:
    """Get the git author of the most recent commit."""
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%an'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error getting git author: {e}")
        return ""


def get_git_committer() -> str:
    """Get the git committer of the most recent commit."""
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%cn'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error getting git committer: {e}")
        return ""


def get_github_actor() -> str:
    """Get GitHub username from environment (when running in Actions)."""
    return os.getenv('GITHUB_ACTOR', '')


def get_modified_validation_edges() -> List[Path]:
    """
    Get list of validation edges modified in this commit/PR.

    Returns paths to validation edge markdown files that were added or modified.
    """
    try:
        # Get files changed in HEAD commit
        result = subprocess.run(
            ['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'],
            capture_output=True,
            text=True,
            check=True
        )
        changed_files = result.stdout.strip().split('\n')

        # Filter for validation edges
        validation_edges = []
        for file_path in changed_files:
            if not file_path:
                continue
            path = Path(file_path)

            # Check if it's a markdown file in edges directory
            if path.suffix == '.md' and '01_edges' in path.parts:
                # Check if it's a validation edge by reading frontmatter
                if path.exists():
                    try:
                        content = path.read_text(encoding='utf-8')
                        frontmatter, _ = extract_frontmatter(content)
                        if frontmatter and frontmatter.get('type') == 'edge/validation':
                            validation_edges.append(path)
                    except Exception as e:
                        print(f"Warning: Could not parse {path}: {e}")

        return validation_edges

    except subprocess.CalledProcessError as e:
        print(f"Error getting modified files: {e}")
        return []


def check_validation_edge_accountability(
    file_path: Path,
    committer: str,
    github_actor: str
) -> Tuple[bool, str]:
    """
    Check if the committer is authorized to commit this validation edge.

    Args:
        file_path: Path to validation edge file
        committer: Git committer name/username
        github_actor: GitHub actor username (from Actions)

    Returns:
        (passed, message) tuple
    """
    try:
        content = file_path.read_text(encoding='utf-8')
        frontmatter, _ = extract_frontmatter(content)

        if not frontmatter:
            return False, f"{file_path}: No frontmatter found"

        # Get validation method and accountable party
        validation_method = frontmatter.get('validation_method', '')

        if validation_method == 'manual':
            # For manual validation, validator is the accountable party
            accountable_party = frontmatter.get('validator', '')
        elif validation_method in ['llm-assisted', 'automated']:
            # For llm-assisted or automated, human_approver is accountable
            accountable_party = frontmatter.get('human_approver', '')
        else:
            return False, f"{file_path}: Unknown validation_method '{validation_method}'"

        if not accountable_party:
            return False, f"{file_path}: No accountable party found (validator or human_approver missing)"

        # Check if committer matches accountable party
        # Support both full names and GitHub usernames
        accountable_party_normalized = accountable_party.strip().lower()
        committer_normalized = committer.strip().lower()
        github_actor_normalized = github_actor.strip().lower()

        # Match if any of these conditions are true:
        # 1. Committer name matches accountable party
        # 2. GitHub actor matches accountable party
        # 3. Accountable party is contained in committer name (e.g., "Alice Smith" contains "alice")
        # 4. Committer contains accountable party (e.g., committer "alice.smith" matches "alice")

        if (accountable_party_normalized == committer_normalized or
            accountable_party_normalized == github_actor_normalized or
            accountable_party_normalized in committer_normalized or
            committer_normalized in accountable_party_normalized or
            (github_actor_normalized and accountable_party_normalized in github_actor_normalized)):
            return True, f"{file_path}: ✓ Accountability verified ({accountable_party})"
        else:
            return False, (
                f"{file_path}: ✗ Accountability violation\n"
                f"  Accountable party: {accountable_party}\n"
                f"  Git committer: {committer}\n"
                f"  GitHub actor: {github_actor or '(not in GitHub Actions)'}\n"
                f"  Only the accountable party can commit this validation edge."
            )

    except Exception as e:
        return False, f"{file_path}: Error checking accountability: {e}"


def main() -> int:
    """
    Main accountability check function.

    Returns:
        0 if all checks pass, 1 if any check fails
    """
    print("=" * 70)
    print("Accountability Verification for Validation Edges")
    print("=" * 70)
    print()

    # Get committer information
    committer = get_git_committer()
    author = get_git_author()
    github_actor = get_github_actor()

    print(f"Git author: {author}")
    print(f"Git committer: {committer}")
    if github_actor:
        print(f"GitHub actor: {github_actor}")
    print()

    # Get modified validation edges
    validation_edges = get_modified_validation_edges()

    if not validation_edges:
        print("No validation edges modified in this commit.")
        print("✓ Accountability check passed (no validation edges to check)")
        print()
        return 0

    print(f"Found {len(validation_edges)} validation edge(s) to check:")
    for edge in validation_edges:
        print(f"  - {edge}")
    print()

    # Check accountability for each validation edge
    all_passed = True
    for edge_path in validation_edges:
        passed, message = check_validation_edge_accountability(
            edge_path,
            committer,
            github_actor
        )
        print(message)
        if not passed:
            all_passed = False

    print()
    print("=" * 70)
    if all_passed:
        print("✓ All accountability checks PASSED")
        print("=" * 70)
        return 0
    else:
        print("✗ Accountability checks FAILED")
        print("=" * 70)
        print()
        print("IMPORTANT: Validation edges can only be committed by the")
        print("accountable party listed in the frontmatter:")
        print("  - For 'manual' validation: the 'validator' field")
        print("  - For 'llm-assisted' or 'automated': the 'human_approver' field")
        print()
        print("This ensures clear accountability and trust in the validation process.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
