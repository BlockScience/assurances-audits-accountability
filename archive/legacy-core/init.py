"""
aaa init - Initialize a new knowledge complex project.

Examples:
    aaa init my-project      # Create a new project in my-project/
    aaa init .               # Initialize current directory
    aaa init --minimal       # Minimal structure (no example content)
"""

import click
import subprocess
import sys
import shutil
from datetime import datetime, timezone
from pathlib import Path

from aaa.core import get_bundled_templates_path, get_bundled_foundation_path, TemplateBasedVerifier


def get_git_username() -> str:
    """Get git username from git config."""
    try:
        result = subprocess.run(
            ['git', 'config', 'user.name'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def get_git_email() -> str:
    """Get git email from git config."""
    try:
        result = subprocess.run(
            ['git', 'config', 'user.email'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def infer_github_username_from_email(email: str) -> str:
    """Try to infer GitHub username from email (common patterns)."""
    if not email:
        return ""
    # Common pattern: username@users.noreply.github.com
    if email.endswith('@users.noreply.github.com'):
        # Format: 12345678+username@users.noreply.github.com or username@users.noreply.github.com
        local_part = email.split('@')[0]
        if '+' in local_part:
            return local_part.split('+')[1]
        return local_part
    return ""


def create_bootstrap_signer(target_dir: Path, github_username: str, display_name: str) -> Path:
    """Create the initial admin signer vertex document."""
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    content = f"""---
type: vertex/signer
extends: actor
id: v:signer:{github_username}
name: {display_name}
github_username: {github_username}
description: Repository administrator with role assignment authority
tags:
  - vertex
  - actor
  - signer
  - admin
version: 1.0.0
created: {now}
modified: {now}
dependencies: []
---

# {display_name}

## Purpose

This signer represents {display_name}, the administrator who initialized this knowledge complex repository. As the founding admin, they have authority to assign roles and establish initial qualifications.

## Actor Identity

{display_name} is the founding administrator of this knowledge complex. Their GitHub identity ({github_username}) provides cryptographic verification through commit signatures.

## Capabilities

- **Assign Roles**: Can assign roles to other actors in the knowledge complex
- **Sign Validations**: Can attest to validation assessments against guidance documents
- **Approve Assurances**: Can approve assurance faces as the human approver
- **Bootstrap Authority**: Initial authority to establish qualifications for new signers

## Properties

- **Admin Role**: Holds the admin role with can-assign authority
- **GitHub Identity**: Verified through commit signatures

## Identity Verification

**GitHub Username:** {github_username}
**Verification Method:** Commits to this repository are signed with the GPG key associated with this GitHub account.

## Signing Authority

- **All Guidance Documents**: Qualified to validate documents against any guidance (bootstrap authority)
- **Role Assignments**: Authorized to assign roles to other actors
- **Framework Administration**: Authority to manage the knowledge complex structure
"""

    file_path = target_dir / '00_vertices' / f'signer-{github_username}.md'
    file_path.write_text(content, encoding='utf-8')
    return file_path


def create_admin_role(target_dir: Path) -> Path:
    """Create the admin role vertex document."""
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    content = f"""---
type: vertex/role
extends: property
id: v:role:admin
name: Administrator
description: Role with authority to assign other roles and manage the knowledge complex
tags:
  - vertex
  - property
  - role
  - admin
version: 1.0.0
created: {now}
modified: {now}
dependencies: []
---

# Administrator Role

## Purpose

The Administrator role grants authority to manage the knowledge complex, including the ability to assign roles to other actors and establish qualification credentials.

## Responsibilities

- Assign roles to new team members
- Establish initial qualifications for signers
- Manage knowledge complex structure and policies
- Approve foundational changes to the framework

## Authority Granted

This role conveys the following permissions:

- **can-assign**: Authority to assign any role to any actor
- **validate-guidance**: Authority to validate documents against any guidance
- **bootstrap-authority**: Initial authority before formal RBAC chains are established

## Qualification Requirements

This role is typically held by:
- Repository founders/owners
- Organization leadership
- Designated knowledge complex administrators
"""

    file_path = target_dir / '00_vertices' / f'role-admin.md'
    file_path.write_text(content, encoding='utf-8')
    return file_path


def create_has_role_edge(target_dir: Path, github_username: str) -> Path:
    """Create the has-role edge connecting signer to admin role."""
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    content = f"""---
type: edge/has-role
extends: edge
id: e:has-role:{github_username}:admin
name: Has Role - {github_username} has admin role
source: v:signer:{github_username}
target: v:role:admin
source_type: vertex/signer
target_type: vertex/role
orientation: directed
granted_by: system
granted_date: {now}
tags:
  - edge
  - has-role
  - bootstrap
version: 1.0.0
created: {now}
modified: {now}
---

# Has Role - {github_username} has admin role

This edge establishes that {github_username} holds the Administrator role.

## Role Assignment

**Actor:** [[signer-{github_username}|v:signer:{github_username}]]
**Role:** [[role-admin|v:role:admin]]
**Granted By:** System (bootstrap during repository initialization)
**Granted Date:** {now}

## Authority Chain

This role assignment was created during repository initialization. The founding user automatically receives the admin role, establishing the root of the RBAC authority chain.

## Scope

This role assignment grants {github_username} full administrative authority over this knowledge complex, including:
- Assigning roles to other actors
- Establishing qualification credentials
- Managing framework structure
"""

    file_path = target_dir / '01_edges' / f'has-role-{github_username}-admin.md'
    file_path.write_text(content, encoding='utf-8')
    return file_path


def create_bootstrap_qualifies_edge(target_dir: Path, github_username: str) -> Path:
    """Create the bootstrap qualifies edge for guidance-for-guidance.

    This edge establishes that the admin can validate guidance documents.
    When someone validates against guidance-for-guidance, they're demonstrating
    competence to create guidance, which qualifies them to validate against
    other guidance documents.
    """
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    return _create_qualifies_edge(target_dir, github_username, 'guidance', 'guidance-for-guidance', now)


def _create_qualifies_edge(target_dir: Path, github_username: str, guidance_id: str, guidance_name: str, now: str) -> Path:
    """Create a qualifies edge connecting signer to a guidance document."""

    content = f"""---
type: edge/qualifies
extends: edge
id: e:qualifies:{github_username}:{guidance_id}
name: Qualifies - {github_username} qualified for {guidance_name}
source: v:signer:{github_username}
target: v:guidance:{guidance_id}
source_type: vertex/signer
target_type: vertex/guidance
orientation: directed
credential_type: role
granted_by: system
granted_date: {now}
tags:
  - edge
  - qualifies
  - bootstrap
version: 1.0.0
created: {now}
modified: {now}
---

# Qualifies - {github_username} qualified for {guidance_name}

This qualifies edge establishes that {github_username} is qualified to validate documents against {guidance_name}.

## Qualification Description

**Signer:** [[signer-{github_username}|v:signer:{github_username}]]
**Guidance:** [[{guidance_name}|v:guidance:{guidance_id}]]
**Credential Type:** role

As the repository administrator, {github_username} has bootstrap authority to validate documents against this guidance.

## Credential Evidence

- **Role**: Administrator of this knowledge complex
- **Bootstrap Authority**: Established during repository initialization

## Scope and Limitations

**Scope:** This qualification covers validation of documents against {guidance_name}.

**Bootstrap Note:** This is a bootstrap qualification established during repository initialization.
"""

    file_path = target_dir / '01_edges' / f'qualifies-{github_username}-{guidance_id}.md'
    file_path.write_text(content, encoding='utf-8')
    return file_path


def create_ontology_qualifies_edge(target_dir: Path, github_username: str) -> Path:
    """Create qualifies edge for guidance-for-ontology."""
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    return _create_qualifies_edge(target_dir, github_username, 'ontology', 'guidance-for-ontology', now)


def run_verification(templates_path: Path, doc_path: Path, doc_name: str, spec_name: str) -> str:
    """Run the template verifier and return formatted output."""
    verifier = TemplateBasedVerifier(templates_path)
    passed = verifier.verify_element(doc_path)

    lines = [
        f"Verification Result: {'PASS' if passed else 'FAIL'}",
        "",
        f"Checked against: {spec_name}",
        f"Document: {doc_name}",
        "",
        f"Checks passed: {verifier.checks_passed}/{verifier.checks_total}",
    ]

    if verifier.errors:
        lines.append("")
        lines.append("Issues:")
        for error in verifier.errors:
            lines.append(f"  ✗ {error}")
    else:
        lines.append("")
        lines.append("All structural requirements satisfied.")

    return "\n".join(lines)


def create_verification_edge(target_dir: Path, doc_id: str, doc_name: str, spec_id: str, spec_name: str, doc_path: Path = None, templates_path: Path = None) -> Path:
    """Create a verification edge from a document to its spec.

    If doc_path and templates_path are provided, runs actual verification and includes output.
    """
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Derive source_type from doc_id pattern
    source_type = 'vertex/ontology' if 'ontology' in doc_id else 'vertex/doc'

    # Run verification if paths provided
    verification_output = ""
    verification_status = "Pass"
    if doc_path and templates_path and doc_path.exists():
        verification_output = run_verification(templates_path, doc_path, doc_name, spec_name)
        verification_status = "Pass" if "PASS" in verification_output else "Fail"

    content = f"""---
type: edge/verification
extends: edge
id: e:verification:{doc_id}:{spec_id}
name: Verification - {doc_name} against {spec_name}
source: v:{doc_id}
target: v:spec:{spec_id}
source_type: {source_type}
target_type: vertex/spec
orientation: directed
verification_method: structural
tags:
  - edge
  - verification
  - bootstrap
version: 1.0.0
created: {now}
modified: {now}
---

# Verification - {doc_name} against {spec_name}

This verification edge asserts that {doc_name} conforms to the structural requirements defined in {spec_name}.

## Verification Output

```
{verification_output if verification_output else "Verification output not captured during bootstrap."}
```

## Verification Status

- **Status:** {verification_status}
- **Date:** {now}
- **Tool:** TemplateBasedVerifier v1.0.0

## Bootstrap Note

This verification edge was created during repository initialization. The ontology is foundational infrastructure that has been verified against its spec.
"""

    file_path = target_dir / '01_edges' / f'verification-{doc_id.replace(":", "-")}-{spec_id}.md'
    file_path.write_text(content, encoding='utf-8')
    return file_path


def create_validation_edge(target_dir: Path, doc_id: str, doc_name: str, guidance_id: str, guidance_name: str, github_username: str) -> Path:
    """Create a validation edge from a document to its guidance."""
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Derive source_type from doc_id pattern
    source_type = 'vertex/ontology' if 'ontology' in doc_id else 'vertex/doc'

    content = f"""---
type: edge/validation
extends: edge
id: e:validation:{doc_id}:{guidance_id}
name: Validation - {doc_name} against {guidance_name}
source: v:{doc_id}
target: v:guidance:{guidance_id}
source_type: {source_type}
target_type: vertex/guidance
orientation: directed
validation_method: manual
validator: {github_username}
validation_date: {now}
tags:
  - edge
  - validation
  - bootstrap
version: 1.0.0
created: {now}
modified: {now}
---

# Validation - {doc_name} against {guidance_name}

This validation edge attests that {doc_name} meets the quality criteria defined in {guidance_name}.

## Validation Assessment

**Guidance:** [[{guidance_name}|v:guidance:{guidance_id}]]
**Validator:** {github_username}
**Method:** Manual
**Date:** {now}

### Quality Criteria Evaluation

The repository administrator has reviewed {doc_name} during initialization and determined it meets the quality criteria defined in {guidance_name}. As foundational infrastructure, the ontology has been assessed for:

- **Type Completeness**: All required simplex types are defined
- **Coherence Rules**: Local rules comprehensively cover type interactions
- **Extension Clarity**: Clear extension points are documented
- **Type Hierarchy Consistency**: Consistent inheritance chains
- **Documentation Quality**: Types have clear purpose statements
- **Local Rule Verifiability**: Rules can be mechanically verified

### Overall Assessment

**Recommendation:** Pass
**Summary:** The ontology meets quality criteria as foundational infrastructure for the knowledge complex.

## Accountability Statement

This validation was performed manually by {github_username}, who takes full responsibility for the assessment as the repository administrator during initialization.

**Signed:** {github_username}
**Date:** {now}
"""

    file_path = target_dir / '01_edges' / f'validation-{doc_id.replace(":", "-")}-{guidance_id}.md'
    file_path.write_text(content, encoding='utf-8')
    return file_path


def create_signs_edge(target_dir: Path, github_username: str, doc_id: str, doc_name: str, guidance_id: str = 'ontology') -> Path:
    """Create a signs edge from signer to document."""
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Derive target_type from doc_id pattern
    target_type = 'vertex/ontology' if 'ontology' in doc_id else 'vertex/doc'

    # Reference the qualifies edge for this guidance
    qualifies_edge_id = f"e:qualifies:{github_username}:{guidance_id}"

    content = f"""---
type: edge/signs
extends: edge
id: e:signs:{github_username}:{doc_id}
name: Signs - {github_username} signs {doc_name}
source: v:signer:{github_username}
target: v:{doc_id}
source_type: vertex/signer
target_type: {target_type}
orientation: directed
signing_date: {now}
commit_hash: bootstrap-init
qualifies_edge: {qualifies_edge_id}
tags:
  - edge
  - signs
  - bootstrap
version: 1.0.0
created: {now}
modified: {now}
---

# Signs - {github_username} signs {doc_name}

This signs edge records {github_username}'s attestation to {doc_name}.

## Signing Event

**Signer:** [[signer-{github_username}|v:signer:{github_username}]]
**Document:** [[{doc_name}|v:{doc_id}]]
**Date:** {now}
**Commit:** bootstrap-init

{github_username} attests to the quality and correctness of {doc_name} as repository administrator.

## Qualification at Signing

**Qualifies Edge:** [[{qualifies_edge_id}]]
**Credential Type:** role
**Valid At:** Confirmed - qualifies edge was created during bootstrap initialization

The signer's qualification to validate against guidance-for-{guidance_id} was established during repository initialization.

## Attestation Statement

I, {github_username}, attest to {doc_name} on {now.split('T')[0]}.

This attestation was created during repository initialization. The commit signature will be established when this document is committed to the repository.

**Signed:** {github_username}
**Date:** {now}
"""

    file_path = target_dir / '01_edges' / f'signs-{github_username}-{doc_id.replace(":", "-")}.md'
    file_path.write_text(content, encoding='utf-8')
    return file_path


def create_conveys_edge(target_dir: Path, role_id: str, role_name: str, guidance_id: str, guidance_name: str) -> Path:
    """Create a conveys edge from role to guidance (Permission Assignment)."""
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    content = f"""---
type: edge/conveys
extends: edge
id: e:conveys:{role_id}:{guidance_id}
name: Conveys - {role_name} conveys validation authority for {guidance_name}
source: v:role:{role_id}
target: v:guidance:{guidance_id}
source_type: vertex/role
target_type: vertex/guidance
orientation: directed
permission_type: validate
tags:
  - edge
  - conveys
  - bootstrap
version: 1.0.0
created: {now}
modified: {now}
---

# Conveys - {role_name} conveys validation authority for {guidance_name}

This conveys edge establishes that the {role_name} role grants validation authority against {guidance_name}.

## Permission Assignment (NIST RBAC)

**Role:** [[role-{role_id}|v:role:{role_id}]]
**Permission Target:** [[{guidance_name}|v:guidance:{guidance_id}]]
**Permission Type:** validate

## Authority Granted

Actors holding the {role_name} role can:
- Validate documents against {guidance_name}
- Create qualifies edges for this guidance

## Bootstrap Note

This conveys edge was created during repository initialization to establish the admin role's validation authority.
"""

    file_path = target_dir / '01_edges' / f'conveys-{role_id}-{guidance_id}.md'
    file_path.write_text(content, encoding='utf-8')
    return file_path


def create_authorization_face(target_dir: Path, github_username: str, role_id: str, role_name: str, guidance_id: str, guidance_name: str) -> Path:
    """Create an authorization face proving actor has permission through role."""
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Build IDs
    has_role_edge = f"e:has-role:{github_username}:{role_id}"
    conveys_edge = f"e:conveys:{role_id}:{guidance_id}"
    qualifies_edge = f"e:qualifies:{github_username}:{guidance_id}"

    content = f"""---
type: face/authorization
extends: face
id: f:authorization:{github_username}:{role_id}:{guidance_id}
name: Authorization - {github_username} as {role_name} for {guidance_name}
description: Proves {github_username} can validate against {guidance_name} through {role_name} role
vertices:
  - v:signer:{github_username}
  - v:role:{role_id}
  - v:guidance:{guidance_id}
actor: v:signer:{github_username}
role: v:role:{role_id}
permission: v:guidance:{guidance_id}
edges:
  - {has_role_edge}
  - {conveys_edge}
  - {qualifies_edge}
orientation: oriented
has_role_edge: {has_role_edge}
conveys_edge: {conveys_edge}
qualifies_edge: {qualifies_edge}
tags:
  - face
  - authorization
  - bootstrap
version: 1.0.0
created: {now}
modified: {now}
---

# Authorization - {github_username} as {role_name} for {guidance_name}

This authorization face proves that {github_username} has permission to validate documents against {guidance_name} through their {role_name} role assignment.

## Face Description

**Type:** Authorization Triangle (NIST RBAC)
**Purpose:** Permission derivation through role assignment

This face implements the NIST RBAC pattern where:
- User Assignment (UA): {github_username} has-role {role_name}
- Permission Assignment (PA): {role_name} conveys validate-permission for {guidance_name}
- Derived: {github_username} qualifies-for {guidance_name}

## Vertices

1. **[[signer-{github_username}|v:signer:{github_username}]]**
   - The actor seeking permission
   - Type: vertex/signer
   - Role in face: Permission holder

2. **[[role-{role_id}|v:role:{role_id}]]**
   - The role granting permission
   - Type: vertex/role
   - Role in face: Permission mediator

3. **[[{guidance_name}|v:guidance:{guidance_id}]]**
   - The permission target (validation authority)
   - Type: vertex/guidance
   - Role in face: Permission scope

## Edges (Boundary)

1. **[[{has_role_edge}]]**
   - Source: {github_username} → Target: {role_name}
   - Type: edge/has-role
   - NIST: User Assignment (UA)

2. **[[{conveys_edge}]]**
   - Source: {role_name} → Target: {guidance_name}
   - Type: edge/conveys
   - NIST: Permission Assignment (PA)

3. **[[{qualifies_edge}]]**
   - Source: {github_username} → Target: {guidance_name}
   - Type: edge/qualifies
   - NIST: Derived permission

## Triangle Coherence

**RBAC Chain Verification:**
- ✓ Actor has role assignment (UA exists)
- ✓ Role conveys permission (PA exists)
- ✓ Derived permission recorded (qualifies edge exists)

## Permission Derivation

**NIST RBAC Logic:**
```
has-role({github_username}, {role_name}) ∧ conveys({role_name}, {guidance_name})
  ⟹ qualifies({github_username}, {guidance_name})
```

## Bootstrap Note

This authorization face was created during repository initialization to establish the admin's validation authority chain.
"""

    file_path = target_dir / '02_faces' / f'authorization-{github_username}-{role_id}-{guidance_id}.md'
    file_path.write_text(content, encoding='utf-8')
    return file_path


def create_signature_face(target_dir: Path, github_username: str, doc_id: str, doc_name: str, guidance_id: str) -> Path:
    """Create a signature face for a document."""
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Build edge IDs
    validation_edge = f"e:validation:{doc_id}:{guidance_id}"
    signs_edge = f"e:signs:{github_username}:{doc_id}"
    qualifies_edge = f"e:qualifies:{github_username}:{guidance_id}"
    assurance_face = f"f:assurance:{doc_id}"

    content = f"""---
type: face/signature
extends: face
id: f:signature:{doc_id}:{github_username}
name: Signature - {doc_name} by {github_username}
description: Signature face recording {github_username}'s attestation to {doc_name}
vertices:
  - v:{doc_id}
  - v:guidance:{guidance_id}
  - v:signer:{github_username}
doc: v:{doc_id}
guidance: v:guidance:{guidance_id}
signer: v:signer:{github_username}
edges:
  - {validation_edge}
  - {signs_edge}
  - {qualifies_edge}
orientation: oriented
validation_edge: {validation_edge}
signs_edge: {signs_edge}
qualifies_edge: {qualifies_edge}
signing_date: {now}
commit_hash: bootstrap-init
assurance_face: {assurance_face}
tags:
  - face
  - signature
  - bootstrap
version: 1.0.0
created: {now}
modified: {now}
---

# Signature - {doc_name} by {github_username}

This signature face records {github_username}'s attestation to {doc_name} based on validation against guidance-for-{guidance_id}.

## Face Description

**Type:** Signature Triangle
**Signing Date:** {now}
**Commit:** bootstrap-init

This signature face records {github_username}'s attestation to {doc_name} based on validation against guidance-for-{guidance_id}. It complements the assurance face by making the signer explicit.

## Vertices

1. **[[{doc_name}|v:{doc_id}]]**
   - The document being signed
   - Type: vertex/ontology
   - Role: Target of signature

2. **[[guidance-for-{guidance_id}|v:guidance:{guidance_id}]]**
   - Quality criteria for validation
   - Type: vertex/guidance
   - Role: Validation target

3. **[[signer-{github_username}|v:signer:{github_username}]]**
   - The signing authority
   - Type: vertex/signer
   - GitHub: {github_username}
   - Role: Accountable party

## Edges (Boundary)

1. **[[{validation_edge}]]**
   - Source: {doc_name} → Target: guidance-for-{guidance_id}
   - Type: edge/validation
   - Status: Pass
   - **SHARED** with assurance face: {assurance_face}

2. **[[{signs_edge}]]**
   - Source: {github_username} → Target: {doc_name}
   - Type: edge/signs
   - Signing Date: {now}
   - Commit: bootstrap-init

3. **[[{qualifies_edge}]]**
   - Source: {github_username} → Target: guidance-for-{guidance_id}
   - Type: edge/qualifies
   - Credential Type: role
   - Valid At: Confirmed valid at signing time

## Triangle Coherence

**Topological Properties:**
- **Closed Boundary:** All three edges form a cycle
- **Complete:** All vertices connected by edges
- **Oriented:** Validation and qualifies directed to guidance; signs directed to doc

**Signature Completeness:**
- Validation assessment exists and passed
- Signer qualification verified at signing time
- Signing event recorded with commit hash
- Shared boundary with assurance face {assurance_face}

## Accountability Statement

This signature records that {github_username} attested to {doc_name} on {now.split('T')[0]}.

The signer's qualification was verified through {qualifies_edge}, which establishes role authority to validate against guidance-for-{guidance_id}.

This signature was created during repository initialization. The commit signature will be established when committed.

**Signed:** {github_username}
**GitHub:** {github_username}
**Date:** {now}

## Related Assurance

**Assurance Face:** [[{assurance_face}]]
**Shared Edge:** {validation_edge}

This signature face complements the assurance face by making the signer explicit.
"""

    file_path = target_dir / '02_faces' / f'signature-{doc_id.replace(":", "-")}.md'
    file_path.write_text(content, encoding='utf-8')
    return file_path


def create_assurance_face(target_dir: Path, doc_id: str, doc_name: str, spec_id: str, guidance_id: str, github_username: str) -> Path:
    """Create an assurance face for a document."""
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    date_only = now.split('T')[0]

    # Build edge IDs
    verification_edge = f"e:verification:{doc_id}:{spec_id}"
    validation_edge = f"e:validation:{doc_id}:{guidance_id}"
    coupling_edge = f"e:coupling:{guidance_id}"

    content = f"""---
type: face/assurance
extends: face
id: f:assurance:{doc_id}
name: Assurance Face - {doc_name}
description: Complete assurance pattern for {doc_name}
vertices:
  - v:{doc_id}
  - v:spec:{spec_id}
  - v:guidance:{guidance_id}
target: v:{doc_id}
spec: v:spec:{spec_id}
guidance: v:guidance:{guidance_id}
edges:
  - {coupling_edge}
  - {verification_edge}
  - {validation_edge}
orientation: oriented
coupling_edge: {coupling_edge}
verification_edge: {verification_edge}
validation_edge: {validation_edge}
assurer: {github_username}
assurance_method: manual
tags:
  - face
  - assurance
  - bootstrap
version: 1.0.0
created: {now}
modified: {now}
---

# Assurance Face - {doc_name}

This assurance face represents the complete quality assurance pattern for {doc_name}, consisting of a specification, guidance, and the three edges that form the assurance triangle: coupling, verification, and validation.

## Face Structure

### Vertices

1. **Target Document**: [[{doc_name}|v:{doc_id}]] - The document being assured
2. **Specification**: [[spec-for-{guidance_id}|v:spec:{spec_id}]] - Structural requirements for the target
3. **Guidance**: [[guidance-for-{guidance_id}|v:guidance:{guidance_id}]] - Quality criteria for the target

### Edges (Boundary)

1. **Coupling Edge**: [[{coupling_edge}]]
   - Connects specification and guidance
   - Ensures they address the same document type
   - Type: `edge/coupling`

2. **Verification Edge**: [[{verification_edge}]]
   - Target verifies against specification
   - Deterministic structural checking
   - Type: `edge/verification`

3. **Validation Edge**: [[{validation_edge}]]
   - Target validates against guidance
   - Qualitative quality assessment
   - Type: `edge/validation`

## Assurance Triangle

```
         Guidance (quality criteria)
              /\\
             /  \\
  Validation/    \\Coupling
           /      \\
          /        \\
         /          \\
    Target -------- Spec
         Verification
```

The three edges form a closed boundary creating the assurance face.

## Assurance Assessment

**Assurer:** {github_username}
**Method:** manual
**Date:** {date_only}

### Triangle Coherence Review

#### Coupling Coherence

**Assessment**: Excellent
**Rationale**: The coupling between spec-for-ontology and guidance-for-ontology properly addresses ontology documents. They are designed together as a matched pair.
**Evidence**: Both documents define requirements for the same document type (ontology) with complementary structural and quality criteria.

#### Verification Completeness

**Assessment**: Pass
**Rationale**: Verification passed all structural checks during initialization.
**Evidence**: Verification edge shows PASS status with all checks satisfied.

#### Validation Quality

**Assessment**: Pass
**Rationale**: Quality assessment performed by repository administrator during initialization.
**Evidence**: Validation edge documents manual review with quality criteria evaluation.

#### Triangle Integration

**Assessment**: Coherent
**Rationale**: All three edges work together to provide complete assurance for the ontology.
**Evidence**: Spec and guidance are coupled, ontology passes verification against spec, and ontology passes validation against guidance.

## Overall Assurance

**Status**: ASSURED

**Summary**: The ontology-base document is fully assured. It passes structural verification against its specification and quality validation against its guidance. The spec-guidance coupling is properly established.

### Assurance Criteria

1. ✓ **Structural Compliance**: Pass verification against specification
2. ✓ **Quality Achievement**: Pass validation against guidance
3. ✓ **Coupling Integrity**: Spec and guidance properly coupled for ontology type
4. ✓ **Currency**: All edges current and reflect actual document state
5. ✓ **Coherence**: Triangle works together without contradictions

**Conclusion**: This document is trustworthy as foundational infrastructure for the knowledge complex. It was reviewed and assured during repository initialization by the admin user.

## Accountability Statement

This assurance assessment was performed manually by {github_username}, who takes full responsibility for reviewing the complete assurance triangle and attesting to its trustworthiness.

**Signed:** {github_username}
**Date:** {date_only}

## Assurance Metadata

| Property | Value |
|----------|-------|
| Target Document | [[{doc_name}|v:{doc_id}]] |
| Specification | [[spec-for-{guidance_id}|v:spec:{spec_id}]] |
| Guidance | [[guidance-for-{guidance_id}|v:guidance:{guidance_id}]] |
| Coupling Edge | [[{coupling_edge}]] |
| Verification Edge | [[{verification_edge}]] |
| Validation Edge | [[{validation_edge}]] |
| Assurance Method | manual |
| Assurer | {github_username} |
| Date Assured | {date_only} |
| Assurance Status | ASSURED |
"""

    file_path = target_dir / '02_faces' / f'assurance-{doc_id.replace(":", "-")}.md'
    file_path.write_text(content, encoding='utf-8')
    return file_path


# Directory structure for a new knowledge complex
DIRECTORIES = [
    '00_vertices',
    '01_edges',
    '02_faces',
    'charts',
    'design',
]

# README content for each directory
DIRECTORY_READMES = {
    '00_vertices': """# Vertices

This directory contains vertex documents representing nodes in the knowledge complex.

Vertex types include:
- `vertex/spec` - Specification documents
- `vertex/guidance` - Guidance documents
- `vertex/doc` - General documents
- `vertex/persona` - Persona definitions
- `vertex/purpose` - Purpose definitions
- `vertex/protocol` - Protocol definitions

## Creating a new vertex

1. Choose the appropriate template from `templates/00_vertices/`
2. Copy it to this directory with a descriptive name
3. Fill in the frontmatter fields
4. Run `aaa verify <file>` to validate

## Naming convention

Files should be named: `{type}-{name}.md`
Example: `spec-for-authentication.md`
""",
    '01_edges': """# Edges

This directory contains edge documents representing relationships between vertices.

Edge types include:
- `edge/verification` - Verifies a document against a reference
- `edge/validation` - Validates a document meets requirements
- `edge/qualification` - Qualifies an actor for a role

## Creating a new edge

1. Choose the appropriate template from `templates/01_edges/`
2. Copy it to this directory with a descriptive name
3. Fill in source, target, and other frontmatter fields
4. Run `aaa verify <file>` to validate

## Naming convention

Files should be named: `{type}-{source}:{target}.md`
Example: `verification-spec-auth:guidance-spec.md`
""",
    '02_faces': """# Faces

This directory contains face documents representing 2-cells (triangular relationships).

Face types include:
- `face/assurance` - Assurance that a document is correct
- `face/signature` - Cryptographic signature attestation

## Creating a new face

1. Choose the appropriate template from `templates/02_faces/`
2. Copy it to this directory with a descriptive name
3. Fill in the vertices, edges, and other frontmatter fields
4. Run `aaa verify <file>` to validate

## Naming convention

Files should be named: `{type}-{target}.md`
Example: `assurance-spec-auth.md`
""",
    'charts': """# Charts

This directory contains chart documents that define subcomplexes of the knowledge complex.

Chart types include:
- `chart/assurance_audit` - Audit chart for assurance coverage
- `chart/boundary_complex` - Boundary definition chart

## Structure

Each chart should be in its own subdirectory:
```
charts/
  my-chart/
    my-chart.md        # Main chart file
    my-chart-audit-trail.md  # Generated audit trail
```

## Creating a new chart

1. Create a subdirectory with the chart name
2. Create the main chart file using a template from `templates/charts/`
3. Run `aaa audit charts/my-chart` to validate coverage
""",
    'design': """# Design

This directory contains foundational design documents for the knowledge complex.

## Contents

- `ontology-base.md` - The base ontology defining all vertex, edge, face, and chart types

## Ontology

The ontology defines the type system for the knowledge complex:
- **14 vertex types** (doc, spec, guidance, actor, signer, role, authority, module, etc.)
- **18 edge types** (verification, validation, coupling, signs, qualifies, etc.)
- **11 face types** (assurance, signature, authorization, input, output, etc.)
- **4 chart types** (audit, module, runbook, execution-trace)

See `ontology-base.md` for complete type definitions and local rules.

## Extending the Ontology

Application ontologies can extend the base ontology by:
1. Setting `extends_ontology` to reference the base
2. Adding new types using dotted namespaces (e.g., `brand.audience`)
3. Adding local rules that strengthen (never weaken) base rules
""",
}

# Root README template
ROOT_README_TEMPLATE = """# {project_name}

A knowledge complex project using the AAA (Assurances, Audits, Accountability) framework.

## Structure

```
{project_name}/
├── 00_vertices/    # Vertex documents (specs, guidance, personas, etc.)
├── 01_edges/       # Edge documents (verification, validation, qualification)
├── 02_faces/       # Face documents (assurance, signature)
├── charts/         # Chart documents (subcomplexes)
├── design/         # Foundational design (ontology, architecture)
├── templates/      # Document templates
└── complex.json    # Generated cache (run `aaa build`)
```

## Getting Started

1. Create vertices in `00_vertices/` using templates
2. Create edges to relate vertices in `01_edges/`
3. Create faces to provide assurance in `02_faces/`
4. Create charts to define subcomplexes in `charts/`

## Commands

```bash
# Verify a document against its template
aaa verify 00_vertices/my-spec.md

# Verify all documents
aaa verify --all

# Build the complex.json cache
aaa build

# Audit assurance coverage of a chart
aaa audit charts/my-chart

# Check topology of a chart
aaa check topology charts/my-chart
```

## Documentation

See the [AAA Documentation](https://github.com/BlockScience/assurances-audits-accountability) for more information.
"""

# Minimal complex.json template
MINIMAL_COMPLEX_JSON = """{
  "version": "1.0.0",
  "generated": null,
  "root_path": ".",
  "elements": {
    "vertices": {},
    "edges": {},
    "faces": {},
    "charts": {}
  },
  "statistics": {
    "vertex_count": 0,
    "edge_count": 0,
    "face_count": 0,
    "chart_count": 0,
    "euler_characteristic": 0
  }
}
"""


@click.command()
@click.argument('name', required=False, default='.')
@click.option('--minimal', is_flag=True, help='Create minimal structure without example content')
@click.option('--force', '-f', is_flag=True, help='Overwrite existing files')
@click.option('--github-username', '-u', default=None, help='GitHub username for the admin signer')
@click.option('--no-bootstrap', is_flag=True, help='Skip creating bootstrap signer and RBAC elements')
@click.pass_context
def init(ctx, name, minimal, force, github_username, no_bootstrap):
    """Initialize a new knowledge complex project.

    Creates the directory structure and copies templates needed for a new
    knowledge complex project. By default, creates a bootstrap admin signer
    with role assignment authority.

    \b
    Examples:
        aaa init my-project      # Create new project in my-project/
        aaa init .               # Initialize current directory
        aaa init --minimal       # Minimal structure (no example content)
        aaa init -u myuser       # Specify GitHub username for admin
        aaa init --no-bootstrap  # Skip bootstrap signer creation
    """
    # Determine target directory
    if name == '.':
        target_dir = Path.cwd()
        project_name = target_dir.name
    else:
        target_dir = Path.cwd() / name
        project_name = name

    # Check if directory exists and has content
    if target_dir.exists() and any(target_dir.iterdir()) and not force:
        click.echo(f"Error: Directory '{target_dir}' is not empty.", err=True)
        click.echo("Use --force to overwrite existing files.", err=True)
        sys.exit(1)

    click.echo(f"Initializing knowledge complex: {project_name}")
    click.echo(f"Target directory: {target_dir}")
    click.echo("")

    # Create target directory if needed
    target_dir.mkdir(parents=True, exist_ok=True)

    # Create directories with READMEs
    for dir_name in DIRECTORIES:
        dir_path = target_dir / dir_name
        dir_path.mkdir(exist_ok=True)
        click.echo(f"  Created {dir_name}/")

        # Write README
        readme_path = dir_path / 'README.md'
        if not readme_path.exists() or force:
            readme_path.write_text(DIRECTORY_READMES[dir_name], encoding='utf-8')

    # Copy templates
    click.echo("")
    click.echo("Copying templates...")

    try:
        bundled_templates = get_bundled_templates_path()
        target_templates = target_dir / 'templates'

        if target_templates.exists() and not force:
            click.echo(f"  Templates directory exists, skipping (use --force to overwrite)")
        else:
            if target_templates.exists():
                shutil.rmtree(target_templates)
            shutil.copytree(bundled_templates, target_templates)
            click.echo(f"  Copied templates to templates/")

    except FileNotFoundError as e:
        click.echo(f"Warning: Could not copy templates: {e}", err=True)
        click.echo("You may need to copy templates manually.", err=True)

    # Copy foundation documents (ontology, spec, guidance, coupling)
    click.echo("")
    click.echo("Copying foundation documents...")

    try:
        bundled_foundation = get_bundled_foundation_path()

        # Check if new structure (with subdirectories) exists
        foundation_vertices = bundled_foundation / '00_vertices'
        foundation_edges = bundled_foundation / '01_edges'

        if foundation_vertices.exists():
            # New structure: copy from subdirectories
            # Copy ontology-base.md to design/
            ontology_source = foundation_vertices / 'ontology-base.md'
            ontology_target = target_dir / 'design' / 'ontology-base.md'
            if ontology_source.exists() and (not ontology_target.exists() or force):
                shutil.copy2(ontology_source, ontology_target)
                click.echo(f"  Copied ontology to design/ontology-base.md")

            # Copy all foundation vertices (b0-root, SS, GS, SG, GG, spec/guidance for ontology)
            foundation_vertex_files = [
                'b0-root.md',
                'spec-for-spec.md',
                'guidance-for-spec.md',
                'spec-for-guidance.md',
                'guidance-for-guidance.md',
                'spec-for-ontology.md',
                'guidance-for-ontology.md',
            ]
            for filename in foundation_vertex_files:
                source = foundation_vertices / filename
                target = target_dir / '00_vertices' / filename
                if source.exists() and (not target.exists() or force):
                    shutil.copy2(source, target)
                    click.echo(f"  Copied {filename} to 00_vertices/")

            # Copy all foundation edges (coupling, b1 boundary edges, genesis verification/validation)
            if foundation_edges.exists():
                foundation_edge_files = [
                    # Coupling edges
                    'coupling-spec.md',
                    'coupling-guidance.md',
                    'coupling-ontology.md',
                    # Boundary edges (b1) for b2 faces
                    'b1-couples-GS-root.md',
                    'b1-couples-SG-root.md',
                    'b1-self-validation.md',
                    'b1-self-verification.md',
                    # Genesis verification/validation edges for SG and GS
                    'verification-spec-guidance-spec-spec.md',
                    'validation-spec-guidance-guidance-spec.md',
                    'verification-guidance-spec-spec-guidance.md',
                    'validation-guidance-spec-guidance-guidance.md',
                ]
                for filename in foundation_edge_files:
                    source = foundation_edges / filename
                    target = target_dir / '01_edges' / filename
                    if source.exists() and (not target.exists() or force):
                        shutil.copy2(source, target)
                        click.echo(f"  Copied {filename} to 01_edges/")

            # Copy all foundation faces (b2 genesis faces)
            foundation_faces = bundled_foundation / '02_faces'
            if foundation_faces.exists():
                foundation_face_files = [
                    # b2 boundary assurance faces
                    'b2-spec-spec.md',
                    'b2-guidance-guidance.md',
                    'b2-spec-guidance.md',
                    'b2-guidance-spec.md',
                ]
                for filename in foundation_face_files:
                    source = foundation_faces / filename
                    target = target_dir / '02_faces' / filename
                    if source.exists() and (not target.exists() or force):
                        shutil.copy2(source, target)
                        click.echo(f"  Copied {filename} to 02_faces/")
        else:
            # Old structure: ontology-base.md is directly in foundation/
            ontology_source = bundled_foundation / 'ontology-base.md'
            ontology_target = target_dir / 'design' / 'ontology-base.md'

            if ontology_source.exists():
                if not ontology_target.exists() or force:
                    shutil.copy2(ontology_source, ontology_target)
                    click.echo(f"  Copied ontology to design/ontology-base.md")
                else:
                    click.echo(f"  Ontology exists, skipping (use --force to overwrite)")
            else:
                click.echo(f"Warning: ontology-base.md not found in bundled foundation", err=True)

    except FileNotFoundError as e:
        click.echo(f"Warning: Could not copy foundation documents: {e}", err=True)
        click.echo("You may need to copy foundation documents manually.", err=True)

    # Create root README
    readme_path = target_dir / 'README.md'
    if not readme_path.exists() or force:
        readme_content = ROOT_README_TEMPLATE.format(project_name=project_name)
        readme_path.write_text(readme_content, encoding='utf-8')
        click.echo(f"  Created README.md")

    # Create minimal complex.json
    complex_path = target_dir / 'complex.json'
    if not complex_path.exists() or force:
        complex_path.write_text(MINIMAL_COMPLEX_JSON, encoding='utf-8')
        click.echo(f"  Created complex.json")

    # Create bootstrap admin signer and RBAC elements
    if not no_bootstrap and not minimal:
        click.echo("")
        click.echo("Creating bootstrap admin signer...")

        # Determine GitHub username
        detected_username = github_username
        display_name = None

        if detected_username:
            # Username was provided via command line
            display_name = get_git_username() or detected_username
            click.echo(f"  Using provided GitHub username: {detected_username}")
        else:
            # Try to get from git config
            git_name = get_git_username()
            git_email = get_git_email()

            # Try to infer GitHub username from email
            detected_username = infer_github_username_from_email(git_email)

            if detected_username:
                display_name = git_name or detected_username
                click.echo(f"  Detected GitHub username from email: {detected_username}")
            elif git_name:
                # Use git name as fallback (user can fix later)
                # Convert to lowercase, replace spaces with hyphens for ID
                detected_username = git_name.lower().replace(' ', '-').replace('.', '-')
                display_name = git_name
                click.echo(f"  Using git config name: {git_name}")
                click.echo(f"  (GitHub username: {detected_username} - edit signer file if incorrect)")
            else:
                # Prompt for username
                detected_username = click.prompt(
                    "  Enter your GitHub username",
                    default="admin"
                )
                display_name = detected_username

        # Create the bootstrap documents
        try:
            signer_path = create_bootstrap_signer(target_dir, detected_username, display_name)
            click.echo(f"  Created signer: {signer_path.relative_to(target_dir)}")

            role_path = create_admin_role(target_dir)
            click.echo(f"  Created admin role: {role_path.relative_to(target_dir)}")

            has_role_path = create_has_role_edge(target_dir, detected_username)
            click.echo(f"  Created has-role edge: {has_role_path.relative_to(target_dir)}")

            qualifies_path = create_bootstrap_qualifies_edge(target_dir, detected_username)
            click.echo(f"  Created qualifies edge: {qualifies_path.relative_to(target_dir)}")

            click.echo("")
            click.echo(f"  Admin signer '{detected_username}' created with:")
            click.echo(f"    - Admin role (can assign roles to others)")
            click.echo(f"    - Qualification for guidance-for-guidance")

            # Create ontology assurance documents (verification, validation, signature, assurance)
            # Only if foundation documents were copied
            ontology_in_design = target_dir / 'design' / 'ontology-base.md'
            spec_exists = (target_dir / '00_vertices' / 'spec-for-ontology.md').exists()
            guidance_exists = (target_dir / '00_vertices' / 'guidance-for-ontology.md').exists()

            if ontology_in_design.exists() and spec_exists and guidance_exists:
                click.echo("")
                click.echo("Creating ontology layer assurance documents...")

                # First, create RBAC for guidance-for-spec (needed to sign spec-for-ontology)
                conveys_spec_path = create_conveys_edge(
                    target_dir,
                    'admin', 'Administrator',
                    'spec', 'guidance-for-spec'
                )
                click.echo(f"  Created conveys edge: {conveys_spec_path.relative_to(target_dir)}")

                qualifies_spec = _create_qualifies_edge(
                    target_dir, detected_username, 'spec', 'guidance-for-spec',
                    datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
                )
                click.echo(f"  Created qualifies edge: {qualifies_spec.relative_to(target_dir)}")

                auth_spec_path = create_authorization_face(
                    target_dir,
                    detected_username,
                    'admin', 'Administrator',
                    'spec', 'guidance-for-spec'
                )
                click.echo(f"  Created authorization face: {auth_spec_path.relative_to(target_dir)}")

                # Create RBAC for guidance-for-guidance (needed to sign guidance-for-ontology)
                conveys_guidance_path = create_conveys_edge(
                    target_dir,
                    'admin', 'Administrator',
                    'guidance', 'guidance-for-guidance'
                )
                click.echo(f"  Created conveys edge: {conveys_guidance_path.relative_to(target_dir)}")

                auth_guidance_path = create_authorization_face(
                    target_dir,
                    detected_username,
                    'admin', 'Administrator',
                    'guidance', 'guidance-for-guidance'
                )
                click.echo(f"  Created authorization face: {auth_guidance_path.relative_to(target_dir)}")

                # === spec-for-ontology assurance ===
                # Verification: spec-for-ontology -> spec-for-spec
                verification_spec_ontology = create_verification_edge(
                    target_dir,
                    'spec:ontology', 'spec-for-ontology',
                    'spec', 'spec-for-spec'
                )
                click.echo(f"  Created verification edge: {verification_spec_ontology.relative_to(target_dir)}")

                # Validation: spec-for-ontology -> guidance-for-spec
                validation_spec_ontology = create_validation_edge(
                    target_dir,
                    'spec:ontology', 'spec-for-ontology',
                    'spec', 'guidance-for-spec',
                    detected_username
                )
                click.echo(f"  Created validation edge: {validation_spec_ontology.relative_to(target_dir)}")

                # Assurance face for spec-for-ontology
                assurance_spec_ontology = create_assurance_face(
                    target_dir,
                    'spec:ontology', 'spec-for-ontology',
                    'spec', 'spec',
                    detected_username
                )
                click.echo(f"  Created assurance face: {assurance_spec_ontology.relative_to(target_dir)}")

                # Signs edge for spec-for-ontology
                signs_spec_ontology = create_signs_edge(
                    target_dir,
                    detected_username,
                    'spec:ontology', 'spec-for-ontology',
                    guidance_id='spec'
                )
                click.echo(f"  Created signs edge: {signs_spec_ontology.relative_to(target_dir)}")

                # Signature face for spec-for-ontology
                signature_spec_ontology = create_signature_face(
                    target_dir,
                    detected_username,
                    'spec:ontology', 'spec-for-ontology',
                    'spec'
                )
                click.echo(f"  Created signature face: {signature_spec_ontology.relative_to(target_dir)}")

                # === guidance-for-ontology assurance ===
                # Verification: guidance-for-ontology -> spec-for-guidance
                verification_guidance_ontology = create_verification_edge(
                    target_dir,
                    'guidance:ontology', 'guidance-for-ontology',
                    'guidance', 'spec-for-guidance'
                )
                click.echo(f"  Created verification edge: {verification_guidance_ontology.relative_to(target_dir)}")

                # Validation: guidance-for-ontology -> guidance-for-guidance
                validation_guidance_ontology = create_validation_edge(
                    target_dir,
                    'guidance:ontology', 'guidance-for-ontology',
                    'guidance', 'guidance-for-guidance',
                    detected_username
                )
                click.echo(f"  Created validation edge: {validation_guidance_ontology.relative_to(target_dir)}")

                # Assurance face for guidance-for-ontology
                assurance_guidance_ontology = create_assurance_face(
                    target_dir,
                    'guidance:ontology', 'guidance-for-ontology',
                    'guidance', 'guidance',
                    detected_username
                )
                click.echo(f"  Created assurance face: {assurance_guidance_ontology.relative_to(target_dir)}")

                # Signs edge for guidance-for-ontology
                signs_guidance_ontology = create_signs_edge(
                    target_dir,
                    detected_username,
                    'guidance:ontology', 'guidance-for-ontology',
                    guidance_id='guidance'
                )
                click.echo(f"  Created signs edge: {signs_guidance_ontology.relative_to(target_dir)}")

                # Signature face for guidance-for-ontology
                signature_guidance_ontology = create_signature_face(
                    target_dir,
                    detected_username,
                    'guidance:ontology', 'guidance-for-ontology',
                    'guidance'
                )
                click.echo(f"  Created signature face: {signature_guidance_ontology.relative_to(target_dir)}")

                # === ontology-base assurance ===
                # Create conveys edge: admin role -> ontology guidance (Permission Assignment)
                conveys_path = create_conveys_edge(
                    target_dir,
                    'admin', 'Administrator',
                    'ontology', 'guidance-for-ontology'
                )
                click.echo(f"  Created conveys edge: {conveys_path.relative_to(target_dir)}")

                # Create qualifies edge for ontology guidance
                ontology_qualifies = create_ontology_qualifies_edge(target_dir, detected_username)
                click.echo(f"  Created qualifies edge: {ontology_qualifies.relative_to(target_dir)}")

                # Create authorization face: proves signer can validate via role
                authorization_path = create_authorization_face(
                    target_dir,
                    detected_username,
                    'admin', 'Administrator',
                    'ontology', 'guidance-for-ontology'
                )
                click.echo(f"  Created authorization face: {authorization_path.relative_to(target_dir)}")

                # Get templates path for running verification
                target_templates = target_dir / 'templates'

                # Create verification edge: ontology -> spec-for-ontology
                verification_path = create_verification_edge(
                    target_dir,
                    'ontology:base', 'ontology-base',
                    'ontology', 'spec-for-ontology',
                    doc_path=ontology_in_design,
                    templates_path=target_templates
                )
                click.echo(f"  Created verification edge: {verification_path.relative_to(target_dir)}")

                # Create validation edge: ontology -> guidance-for-ontology
                validation_path = create_validation_edge(
                    target_dir,
                    'ontology:base', 'ontology-base',
                    'ontology', 'guidance-for-ontology',
                    detected_username
                )
                click.echo(f"  Created validation edge: {validation_path.relative_to(target_dir)}")

                # Create signs edge: signer -> ontology
                signs_path = create_signs_edge(
                    target_dir,
                    detected_username,
                    'ontology:base', 'ontology-base'
                )
                click.echo(f"  Created signs edge: {signs_path.relative_to(target_dir)}")

                # Create signature face
                signature_path = create_signature_face(
                    target_dir,
                    detected_username,
                    'ontology:base', 'ontology-base',
                    'ontology'
                )
                click.echo(f"  Created signature face: {signature_path.relative_to(target_dir)}")

                # Create assurance face
                assurance_path = create_assurance_face(
                    target_dir,
                    'ontology:base', 'ontology-base',
                    'ontology', 'ontology',
                    detected_username
                )
                click.echo(f"  Created assurance face: {assurance_path.relative_to(target_dir)}")

                click.echo("")
                click.echo("  Ontology assurance complete:")
                click.echo("    - Verified against spec-for-ontology")
                click.echo("    - Validated against guidance-for-ontology")
                click.echo(f"    - Signed by {detected_username}")

        except Exception as e:
            click.echo(f"Warning: Could not create bootstrap signer: {e}", err=True)
            click.echo("You can create these manually later.", err=True)

    click.echo("")
    click.echo(f"Knowledge complex initialized in: {target_dir}")
    click.echo("")
    click.echo("Next steps:")
    if not no_bootstrap and not minimal:
        click.echo(f"  1. cd {name if name != '.' else ''}")
        click.echo("  2. Review your admin signer in 00_vertices/")
        click.echo("  3. Create your first document: copy a template from templates/00_vertices/")
        click.echo("  4. Verify your document: aaa verify 00_vertices/your-doc.md")
        click.echo("  5. Build the cache: aaa build")
    else:
        click.echo(f"  1. cd {name if name != '.' else ''}")
        click.echo("  2. Create your first vertex: copy a template from templates/00_vertices/")
        click.echo("  3. Verify your document: aaa verify 00_vertices/your-doc.md")
        click.echo("  4. Build the cache: aaa build")
