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

from aaa.core import get_bundled_templates_path, get_bundled_foundation_path


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

    content = f"""---
type: edge/qualifies
extends: edge
id: e:qualifies:{github_username}:guidance
name: Qualifies - {github_username} qualified for guidance-for-guidance
source: v:signer:{github_username}
target: v:guidance:guidance
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

# Qualifies - {github_username} qualified for guidance-for-guidance

This qualifies edge establishes that {github_username} is qualified to validate documents against guidance-for-guidance.

## Qualification Description

**Signer:** [[signer-{github_username}|v:signer:{github_username}]]
**Guidance:** [[guidance-for-guidance|v:guidance:guidance]]
**Credential Type:** role

As the repository administrator, {github_username} has bootstrap authority to validate guidance documents. This qualification is granted by virtue of the admin role.

## Credential Evidence

- **Role**: Administrator of this knowledge complex
- **Bootstrap Authority**: Established during repository initialization
- **Responsibility**: Accountable for initial guidance quality standards

## Scope and Limitations

**Scope:** This qualification covers validation of any document against guidance-for-guidance, establishing the foundation for the guidance quality chain.

**Bootstrap Note:** This is a bootstrap qualification. In a mature knowledge complex, qualifications would be established through formal validation chains. The admin's initial qualification enables the system to bootstrap.

## Propagation Rule

When a signer validates a guidance document against guidance-for-guidance, they demonstrate competence in guidance quality assessment. This can serve as evidence for granting qualifies edges to other guidance documents they author or review.
"""

    file_path = target_dir / '01_edges' / f'qualifies-{github_username}-guidance.md'
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

    # Copy ontology
    click.echo("")
    click.echo("Copying ontology...")

    try:
        bundled_foundation = get_bundled_foundation_path()
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
        click.echo(f"Warning: Could not copy ontology: {e}", err=True)
        click.echo("You may need to copy ontology-base.md manually.", err=True)

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
