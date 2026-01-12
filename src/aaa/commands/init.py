"""
aaa init - Initialize a new knowledge complex project.

Examples:
    aaa init my-project      # Create a new project in my-project/
    aaa init .               # Initialize current directory
    aaa init --minimal       # Minimal structure (no example content)
"""

import click
import sys
import shutil
from pathlib import Path

from aaa.core import get_bundled_templates_path, get_bundled_foundation_path


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
@click.pass_context
def init(ctx, name, minimal, force):
    """Initialize a new knowledge complex project.

    Creates the directory structure and copies templates needed for a new
    knowledge complex project.

    \b
    Examples:
        aaa init my-project      # Create new project in my-project/
        aaa init .               # Initialize current directory
        aaa init --minimal       # Minimal structure (no example content)
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

    click.echo("")
    click.echo(f"Knowledge complex initialized in: {target_dir}")
    click.echo("")
    click.echo("Next steps:")
    click.echo(f"  1. cd {name if name != '.' else ''}")
    click.echo("  2. Create your first vertex: copy a template from templates/00_vertices/")
    click.echo("  3. Verify your document: aaa verify 00_vertices/your-doc.md")
    click.echo("  4. Build the cache: aaa build")
