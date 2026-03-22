#!/usr/bin/env python
"""
Accountability Verification for Validation Edges and Shared Boundaries

This script provides two types of accountability checks:

1. COMMIT-TIME CHECK: Ensures validation edges are only committed by the
   accountable party listed in the frontmatter (validator for manual,
   human_approver for llm-assisted/automated).

2. CONSISTENCY CHECK: For charts with signatures, verifies that when a
   signature face and assurance face share a validation edge, all three
   objects reference the same accountable human. This ensures the
   "accountability intersection" is coherent.

The consistency check is critical for signed charts because:
- The validation edge records WHO approved the quality assessment
- The assurance face records WHO approved the overall assurance
- The signature face records WHO attested to the document
When these share a validation edge, they MUST reference the same person.

Usage:
    python scripts/check_accountability.py                    # Commit-time check
    python scripts/check_accountability.py --check-consistency # Consistency check

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
import argparse
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any

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


def get_file_author_from_blame(file_path: str) -> str:
    """
    Get the author who actually created/modified a file using git blame.

    For validation edges, we care about who authored the frontmatter
    (specifically the accountability fields). This uses git blame to
    find the actual author of the file content.

    Returns the author name, or empty string if unable to determine.
    """
    try:
        # Use git log to find who last modified this file
        # This is more reliable than blame for newly added files
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%an', '--follow', '--', file_path],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def get_file_author_in_commit(file_path: str, commit: str = 'HEAD') -> str:
    """
    Get the author who actually modified a specific file in a commit.

    Uses git log to find who authored the changes to this file.
    For merge commits or PRs, this checks if the file was actually
    modified by the commit author.

    Returns empty string if file wasn't modified by the commit author.
    """
    try:
        # Check if this file was actually added or modified in this commit
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%an', '--diff-filter=AM', '--', file_path],
            capture_output=True,
            text=True,
            check=True,
            cwd=str(Path(file_path).parent) if Path(file_path).exists() else None
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def get_modified_validation_edges() -> List[Tuple[Path, str]]:
    """
    Get list of validation edges modified in this commit/PR with their authors.

    Returns list of (path, author) tuples for validation edge markdown files
    that were added or modified. Uses git blame/log to find the actual author
    of each file, not just the commit author. This ensures that when user A
    pushes a branch containing user B's validation edges, the check correctly
    attributes those edges to user B.
    """
    try:
        # Get files changed in HEAD commit (Added or Modified only)
        result = subprocess.run(
            ['git', 'diff', '--name-only', '--diff-filter=AM', 'HEAD~1', 'HEAD'],
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
                            # Get who actually authored this file (using git log --follow)
                            file_author = get_file_author_from_blame(file_path)
                            validation_edges.append((path, file_author))
                    except Exception as e:
                        print(f"Warning: Could not parse {path}: {e}")

        return validation_edges

    except subprocess.CalledProcessError as e:
        print(f"Error getting modified files: {e}")
        return []


def check_validation_edge_accountability(
    file_path: Path,
    author: str,
    committer: str,
    github_actor: str
) -> Tuple[bool, str]:
    """
    Check if the author is authorized to commit this validation edge.

    Args:
        file_path: Path to validation edge file
        author: Git author name/username (who wrote the commit)
        committer: Git committer name/username (who merged/applied the commit)
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

        # Check if author matches accountable party
        # The git author is who wrote the commit - this is the primary accountability check
        # Support both full names and GitHub usernames
        accountable_party_normalized = accountable_party.strip().lower()
        author_normalized = author.strip().lower()
        committer_normalized = committer.strip().lower()
        github_actor_normalized = github_actor.strip().lower()

        # Match if any of these conditions are true:
        # 1. Author name matches accountable party (primary check - who wrote the code)
        # 2. Committer name matches accountable party (for direct pushes)
        # 3. GitHub actor matches accountable party (fallback for Actions)
        # 4. Substring matching for name variations (e.g., "mzargham" in "Michael Zargham")

        if (accountable_party_normalized == author_normalized or
            accountable_party_normalized == committer_normalized or
            accountable_party_normalized == github_actor_normalized or
            accountable_party_normalized in author_normalized or
            author_normalized in accountable_party_normalized or
            accountable_party_normalized in committer_normalized or
            committer_normalized in accountable_party_normalized or
            (github_actor_normalized and accountable_party_normalized in github_actor_normalized)):
            return True, f"{file_path}: ✓ Accountability verified ({accountable_party})"
        else:
            return False, (
                f"{file_path}: ✗ Accountability violation\n"
                f"  Accountable party: {accountable_party}\n"
                f"  Git author: {author}\n"
                f"  Git committer: {committer}\n"
                f"  GitHub actor: {github_actor or '(not in GitHub Actions)'}\n"
                f"  Only the accountable party can author this validation edge."
            )

    except Exception as e:
        return False, f"{file_path}: Error checking accountability: {e}"


def extract_username_from_signer(signer_id: str) -> str:
    """
    Extract username from signer vertex ID.

    Examples:
        'v:signer:mzargham' -> 'mzargham'
        'v:signer:alice-smith' -> 'alice-smith'
        'b0:root' -> 'b0:root' (boundary signer, special case)
    """
    if signer_id.startswith('v:signer:'):
        return signer_id[len('v:signer:'):]
    return signer_id


def is_boundary_signature(sig_frontmatter: Dict[str, Any]) -> bool:
    """
    Check if a signature face is a boundary complex signature.

    Boundary signatures have:
    - signer: b0:root (or any b0:* vertex)
    - Tag 'boundary-complex' in tags

    These are foundational signatures that bootstrap the trust chain
    and are exempt from normal accountability matching because they
    represent the axiomatic foundation of the knowledge complex.
    """
    signer = sig_frontmatter.get('signer', '')
    tags = sig_frontmatter.get('tags', [])

    # Check if signer is a boundary vertex
    if signer.startswith('b0:'):
        return True

    # Check for boundary-complex tag
    if 'boundary-complex' in tags:
        return True

    return False


def get_accountable_party_from_edge(frontmatter: Dict[str, Any]) -> Tuple[str, str]:
    """
    Get the accountable party from a validation edge frontmatter.

    Returns:
        (accountable_party, field_name) tuple
    """
    validation_method = frontmatter.get('validation_method', '')

    if validation_method == 'manual':
        return frontmatter.get('validator', ''), 'validator'
    elif validation_method in ['llm-assisted', 'automated']:
        return frontmatter.get('human_approver', ''), 'human_approver'
    else:
        return '', 'unknown'


def normalize_username(name: str) -> str:
    """Normalize a username for comparison."""
    if not name:
        return ''
    # Remove quotes and whitespace, convert to lowercase
    return name.strip().strip('"\'').lower()


def usernames_match(name1: str, name2: str) -> bool:
    """
    Check if two usernames refer to the same person.

    Handles various formats:
    - Exact match: 'mzargham' == 'mzargham'
    - Case insensitive: 'MZargham' == 'mzargham'
    - Substring: 'mzargham' in 'Michael Zargham'
    """
    n1 = normalize_username(name1)
    n2 = normalize_username(name2)

    if not n1 or not n2:
        return False

    return (n1 == n2 or
            n1 in n2 or
            n2 in n1)


def chart_has_signers(chart_frontmatter: Dict[str, Any]) -> bool:
    """
    Check if a chart includes signer vertices.

    A chart has signers if its elements.vertices list contains
    any vertex starting with 'v:signer:'.
    """
    elements = chart_frontmatter.get('elements', {})
    vertices = elements.get('vertices', [])

    for v in vertices:
        if isinstance(v, str) and v.startswith('v:signer:'):
            return True
    return False


def find_signature_faces(root_path: Path) -> List[Path]:
    """Find all signature face files in the repository."""
    faces_dir = root_path / '02_faces'
    if not faces_dir.exists():
        return []

    signature_faces = []
    for f in faces_dir.glob('signature-*.md'):
        signature_faces.append(f)
    return signature_faces


def find_assurance_faces(root_path: Path) -> List[Path]:
    """Find all assurance face files in the repository."""
    faces_dir = root_path / '02_faces'
    if not faces_dir.exists():
        return []

    assurance_faces = []
    for f in faces_dir.glob('assurance-*.md'):
        assurance_faces.append(f)
    return assurance_faces


def find_validation_edge_file(edge_id: str, root_path: Path) -> Optional[Path]:
    """
    Find the file path for a validation edge by its ID.

    Edge ID format: e:validation:doc-name:guidance-name
    File format: validation-doc-name:guidance-name.md
    """
    edges_dir = root_path / '01_edges'
    if not edges_dir.exists():
        return None

    # Convert edge ID to filename
    # e:validation:architecture-spec:guidance-spec -> validation-architecture-spec:guidance-spec.md
    if edge_id.startswith('e:validation:'):
        suffix = edge_id[len('e:validation:'):]
        filename = f"validation-{suffix}.md"
        file_path = edges_dir / filename
        if file_path.exists():
            return file_path

    # Try direct search
    for f in edges_dir.glob('validation-*.md'):
        try:
            content = f.read_text(encoding='utf-8')
            fm, _ = extract_frontmatter(content)
            if fm and fm.get('id') == edge_id:
                return f
        except Exception:
            continue

    return None


def check_shared_validation_edge_consistency(
    signature_face_path: Path,
    root_path: Path
) -> Tuple[bool, str, Dict[str, Any]]:
    """
    Check that a signature face, its corresponding assurance face, and their
    shared validation edge all reference the same accountable human.

    Args:
        signature_face_path: Path to signature face file
        root_path: Repository root path

    Returns:
        (passed, message, details) tuple where details contains the extracted info
    """
    details = {
        'signature_face': str(signature_face_path.name),
        'signer': None,
        'validation_edge': None,
        'assurance_face': None,
        'edge_approver': None,
        'assurance_approver': None,
    }

    try:
        # Read signature face
        sig_content = signature_face_path.read_text(encoding='utf-8')
        sig_fm, _ = extract_frontmatter(sig_content)

        if not sig_fm:
            return False, f"{signature_face_path.name}: No frontmatter found", details

        # Check if this is a boundary signature (bootstrap case)
        if is_boundary_signature(sig_fm):
            signer_id = sig_fm.get('signer', 'b0:root')
            return True, (
                f"{signature_face_path.name}: ✓ Boundary signature (exempt)\n"
                f"  Signer: {signer_id}\n"
                f"  Boundary signatures bootstrap the trust chain"
            ), details

        # Get signer from signature face
        signer_id = sig_fm.get('signer', '')
        if not signer_id:
            return False, f"{signature_face_path.name}: No signer field found", details

        signer_username = extract_username_from_signer(signer_id)
        details['signer'] = signer_username

        # Get validation edge ID
        validation_edge_id = sig_fm.get('validation_edge', '')
        if not validation_edge_id:
            return False, f"{signature_face_path.name}: No validation_edge field found", details

        details['validation_edge'] = validation_edge_id

        # Get assurance face ID (optional but recommended)
        assurance_face_id = sig_fm.get('assurance_face', '')
        details['assurance_face'] = assurance_face_id

        # Find and read validation edge
        edge_path = find_validation_edge_file(validation_edge_id, root_path)
        if not edge_path:
            return False, f"{signature_face_path.name}: Validation edge file not found for {validation_edge_id}", details

        edge_content = edge_path.read_text(encoding='utf-8')
        edge_fm, _ = extract_frontmatter(edge_content)

        if not edge_fm:
            return False, f"{edge_path.name}: No frontmatter found in validation edge", details

        edge_approver, field_name = get_accountable_party_from_edge(edge_fm)
        details['edge_approver'] = edge_approver

        if not edge_approver:
            return False, f"{edge_path.name}: No accountable party in validation edge ({field_name} missing)", details

        # Find corresponding assurance face that shares this validation edge
        assurance_approver = None
        assurance_face_file = None

        for af_path in find_assurance_faces(root_path):
            try:
                af_content = af_path.read_text(encoding='utf-8')
                af_fm, _ = extract_frontmatter(af_content)
                if af_fm and af_fm.get('validation_edge') == validation_edge_id:
                    assurance_approver = af_fm.get('human_approver', '')
                    assurance_face_file = af_path.name
                    details['assurance_face'] = af_fm.get('id', af_path.name)
                    details['assurance_approver'] = assurance_approver
                    break
            except Exception:
                continue

        if not assurance_face_file:
            # No matching assurance face found - this is OK if the chart doesn't require it
            return True, f"{signature_face_path.name}: No matching assurance face found (standalone signature)", details

        if not assurance_approver:
            return False, f"{assurance_face_file}: No human_approver field in assurance face", details

        # Now check all three reference the same person
        matches = []
        mismatches = []

        # Check signer vs edge approver
        if usernames_match(signer_username, edge_approver):
            matches.append(f"signer ({signer_username}) ↔ edge approver ({edge_approver})")
        else:
            mismatches.append(f"signer ({signer_username}) ≠ edge approver ({edge_approver})")

        # Check signer vs assurance approver
        if usernames_match(signer_username, assurance_approver):
            matches.append(f"signer ({signer_username}) ↔ assurance approver ({assurance_approver})")
        else:
            mismatches.append(f"signer ({signer_username}) ≠ assurance approver ({assurance_approver})")

        # Check edge vs assurance approver
        if usernames_match(edge_approver, assurance_approver):
            matches.append(f"edge approver ({edge_approver}) ↔ assurance approver ({assurance_approver})")
        else:
            mismatches.append(f"edge approver ({edge_approver}) ≠ assurance approver ({assurance_approver})")

        if mismatches:
            return False, (
                f"{signature_face_path.name}: Accountability mismatch at shared validation edge\n"
                f"  Shared edge: {validation_edge_id}\n"
                f"  Mismatches:\n" +
                "\n".join(f"    - {m}" for m in mismatches)
            ), details

        return True, (
            f"{signature_face_path.name}: ✓ Accountability consistent\n"
            f"  Shared edge: {validation_edge_id}\n"
            f"  Accountable party: {signer_username}"
        ), details

    except Exception as e:
        return False, f"{signature_face_path.name}: Error checking consistency: {e}", details


def check_all_signature_accountability(root_path: Path = None) -> Tuple[bool, List[str]]:
    """
    Check accountability consistency for all signature faces in the repository.

    For each signature face, verify that it, its shared validation edge,
    and corresponding assurance face all reference the same accountable human.

    Args:
        root_path: Repository root (defaults to current directory)

    Returns:
        (all_passed, messages) tuple
    """
    if root_path is None:
        root_path = Path.cwd()

    signature_faces = find_signature_faces(root_path)

    if not signature_faces:
        return True, ["No signature faces found - accountability consistency check skipped"]

    messages = []
    all_passed = True

    for sig_path in signature_faces:
        passed, message, details = check_shared_validation_edge_consistency(sig_path, root_path)
        messages.append(message)
        if not passed:
            all_passed = False

    return all_passed, messages


def main() -> int:
    """
    Main accountability check function.

    Returns:
        0 if all checks pass, 1 if any check fails
    """
    parser = argparse.ArgumentParser(
        description='Check accountability for validation edges and signatures'
    )
    parser.add_argument(
        '--check-consistency',
        action='store_true',
        help='Check signature-assurance-validation accountability consistency'
    )
    parser.add_argument(
        '--root',
        type=Path,
        default=None,
        help='Repository root path (defaults to current directory)'
    )

    args = parser.parse_args()

    if args.check_consistency:
        return check_consistency_main(args.root)
    else:
        return check_commit_main()


def check_consistency_main(root_path: Path = None) -> int:
    """
    Check accountability consistency for signature faces.

    Returns:
        0 if all checks pass, 1 if any check fails
    """
    print("=" * 70)
    print("Accountability Consistency Check for Signature Faces")
    print("=" * 70)
    print()
    print("Checking that signature faces, assurance faces, and shared")
    print("validation edges all reference the same accountable human.")
    print()

    if root_path is None:
        root_path = Path.cwd()

    all_passed, messages = check_all_signature_accountability(root_path)

    for message in messages:
        print(message)

    print()
    print("=" * 70)
    if all_passed:
        print("✓ All accountability consistency checks PASSED")
        print("=" * 70)
        return 0
    else:
        print("✗ Accountability consistency checks FAILED")
        print("=" * 70)
        print()
        print("IMPORTANT: When a signature face and assurance face share a")
        print("validation edge, all three MUST reference the same accountable")
        print("human. This ensures coherent accountability at the shared boundary.")
        print()
        print("Fields that must match:")
        print("  - Signature face: signer (e.g., v:signer:username)")
        print("  - Validation edge: human_approver or validator")
        print("  - Assurance face: human_approver")
        return 1


def check_commit_main() -> int:
    """
    Original commit-time accountability check.

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

    # Get modified validation edges (returns tuples of (path, file_author))
    validation_edges = get_modified_validation_edges()

    if not validation_edges:
        print("No validation edges modified in this commit.")
        print("✓ Accountability check passed (no validation edges to check)")
        print()
        return 0

    print(f"Found {len(validation_edges)} validation edge(s) to check:")
    for edge_path, file_author in validation_edges:
        print(f"  - {edge_path} (author: {file_author or 'unknown'})")
    print()

    # Check accountability for each validation edge
    all_passed = True
    for edge_path, file_author in validation_edges:
        # Use file-specific author if available, otherwise fall back to commit author
        effective_author = file_author if file_author else author
        passed, message = check_validation_edge_accountability(
            edge_path,
            effective_author,
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
