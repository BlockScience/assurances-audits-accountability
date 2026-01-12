"""
Accountability Verification for Validation Edges and Shared Boundaries

This module provides accountability checks for the AAA framework:

1. COMMIT-TIME CHECK: Ensures validation edges are only committed by the
   accountable party listed in the frontmatter.

2. CONSISTENCY CHECK: For charts with signatures, verifies that when a
   signature face and assurance face share a validation edge, all three
   objects reference the same accountable human.
"""

import os
import subprocess
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any

from .parse import extract_frontmatter, ParseError


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
    except subprocess.CalledProcessError:
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
    except subprocess.CalledProcessError:
        return ""


def get_github_actor() -> str:
    """Get GitHub username from environment (when running in Actions)."""
    return os.getenv('GITHUB_ACTOR', '')


def get_file_author_from_blame(file_path: str) -> str:
    """Get the author who created/modified a file using git log."""
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%an', '--follow', '--', file_path],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def normalize_username(name: str) -> str:
    """Normalize a username for comparison."""
    if not name:
        return ''
    return name.strip().strip('"\'').lower()


def usernames_match(name1: str, name2: str) -> bool:
    """Check if two usernames refer to the same person."""
    n1 = normalize_username(name1)
    n2 = normalize_username(name2)

    if not n1 or not n2:
        return False

    return (n1 == n2 or n1 in n2 or n2 in n1)


def get_accountable_party_from_edge(frontmatter: Dict[str, Any]) -> Tuple[str, str]:
    """Get the accountable party from a validation edge frontmatter."""
    validation_method = frontmatter.get('validation_method', '')

    if validation_method == 'manual':
        return frontmatter.get('validator', ''), 'validator'
    elif validation_method in ['llm-assisted', 'automated']:
        return frontmatter.get('human_approver', ''), 'human_approver'
    else:
        return '', 'unknown'


def extract_username_from_signer(signer_id: str) -> str:
    """Extract username from signer vertex ID."""
    if signer_id.startswith('v:signer:'):
        return signer_id[len('v:signer:'):]
    return signer_id


def is_boundary_signature(sig_frontmatter: Dict[str, Any]) -> bool:
    """Check if a signature face is a boundary complex signature."""
    signer = sig_frontmatter.get('signer', '')
    tags = sig_frontmatter.get('tags', [])

    if signer.startswith('b0:'):
        return True

    if 'boundary-complex' in tags:
        return True

    return False


def check_validation_edge_accountability(
    file_path: Path,
    author: str,
    committer: str,
    github_actor: str
) -> Tuple[bool, str]:
    """
    Check if the author is authorized to commit this validation edge.

    Returns:
        (passed, message) tuple
    """
    try:
        content = file_path.read_text(encoding='utf-8')
        frontmatter, _ = extract_frontmatter(content)

        if not frontmatter:
            return False, f"{file_path}: No frontmatter found"

        validation_method = frontmatter.get('validation_method', '')

        if validation_method == 'manual':
            accountable_party = frontmatter.get('validator', '')
        elif validation_method in ['llm-assisted', 'automated']:
            accountable_party = frontmatter.get('human_approver', '')
        else:
            return False, f"{file_path}: Unknown validation_method '{validation_method}'"

        if not accountable_party:
            return False, f"{file_path}: No accountable party found"

        accountable_party_normalized = accountable_party.strip().lower()
        author_normalized = author.strip().lower()
        committer_normalized = committer.strip().lower()
        github_actor_normalized = github_actor.strip().lower()

        if (accountable_party_normalized == author_normalized or
            accountable_party_normalized == committer_normalized or
            accountable_party_normalized == github_actor_normalized or
            accountable_party_normalized in author_normalized or
            author_normalized in accountable_party_normalized or
            accountable_party_normalized in committer_normalized or
            committer_normalized in accountable_party_normalized or
            (github_actor_normalized and accountable_party_normalized in github_actor_normalized)):
            return True, f"{file_path}: Accountability verified ({accountable_party})"
        else:
            return False, (
                f"{file_path}: Accountability violation\n"
                f"  Accountable party: {accountable_party}\n"
                f"  Git author: {author}\n"
                f"  Git committer: {committer}\n"
                f"  GitHub actor: {github_actor or '(not in GitHub Actions)'}"
            )

    except Exception as e:
        return False, f"{file_path}: Error checking accountability: {e}"


def find_signature_faces(root_path: Path) -> List[Path]:
    """Find all signature face files in the repository."""
    faces_dir = root_path / '02_faces'
    if not faces_dir.exists():
        return []

    return list(faces_dir.glob('signature-*.md'))


def find_assurance_faces(root_path: Path) -> List[Path]:
    """Find all assurance face files in the repository."""
    faces_dir = root_path / '02_faces'
    if not faces_dir.exists():
        return []

    return list(faces_dir.glob('assurance-*.md'))


def find_validation_edge_file(edge_id: str, root_path: Path) -> Optional[Path]:
    """Find the file path for a validation edge by its ID."""
    edges_dir = root_path / '01_edges'
    if not edges_dir.exists():
        return None

    if edge_id.startswith('e:validation:'):
        suffix = edge_id[len('e:validation:'):]
        filename = f"validation-{suffix}.md"
        file_path = edges_dir / filename
        if file_path.exists():
            return file_path

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
        sig_content = signature_face_path.read_text(encoding='utf-8')
        sig_fm, _ = extract_frontmatter(sig_content)

        if not sig_fm:
            return False, f"{signature_face_path.name}: No frontmatter found", details

        if is_boundary_signature(sig_fm):
            signer_id = sig_fm.get('signer', 'b0:root')
            return True, (
                f"{signature_face_path.name}: Boundary signature (exempt)\n"
                f"  Signer: {signer_id}"
            ), details

        signer_id = sig_fm.get('signer', '')
        if not signer_id:
            return False, f"{signature_face_path.name}: No signer field found", details

        signer_username = extract_username_from_signer(signer_id)
        details['signer'] = signer_username

        validation_edge_id = sig_fm.get('validation_edge', '')
        if not validation_edge_id:
            return False, f"{signature_face_path.name}: No validation_edge field found", details

        details['validation_edge'] = validation_edge_id

        assurance_face_id = sig_fm.get('assurance_face', '')
        details['assurance_face'] = assurance_face_id

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
            return True, f"{signature_face_path.name}: No matching assurance face found (standalone signature)", details

        if not assurance_approver:
            return False, f"{assurance_face_file}: No human_approver field in assurance face", details

        matches = []
        mismatches = []

        if usernames_match(signer_username, edge_approver):
            matches.append(f"signer ({signer_username}) <-> edge approver ({edge_approver})")
        else:
            mismatches.append(f"signer ({signer_username}) != edge approver ({edge_approver})")

        if usernames_match(signer_username, assurance_approver):
            matches.append(f"signer ({signer_username}) <-> assurance approver ({assurance_approver})")
        else:
            mismatches.append(f"signer ({signer_username}) != assurance approver ({assurance_approver})")

        if usernames_match(edge_approver, assurance_approver):
            matches.append(f"edge approver ({edge_approver}) <-> assurance approver ({assurance_approver})")
        else:
            mismatches.append(f"edge approver ({edge_approver}) != assurance approver ({assurance_approver})")

        if mismatches:
            return False, (
                f"{signature_face_path.name}: Accountability mismatch at shared validation edge\n"
                f"  Shared edge: {validation_edge_id}\n"
                f"  Mismatches:\n" +
                "\n".join(f"    - {m}" for m in mismatches)
            ), details

        return True, (
            f"{signature_face_path.name}: Accountability consistent\n"
            f"  Shared edge: {validation_edge_id}\n"
            f"  Accountable party: {signer_username}"
        ), details

    except Exception as e:
        return False, f"{signature_face_path.name}: Error checking consistency: {e}", details


def check_all_signature_accountability(root_path: Path = None) -> Tuple[bool, List[str]]:
    """Check accountability consistency for all signature faces."""
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
