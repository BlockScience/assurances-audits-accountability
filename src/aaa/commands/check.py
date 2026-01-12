"""
aaa check - Various checking commands.

Examples:
    aaa check accountability document.md
    aaa check topology charts/my-chart
    aaa check ontology
"""

import click
import sys
from pathlib import Path

from aaa.core import (
    TemplateBasedVerifier,
    get_templates_path,
    get_bundled_foundation_path,
    check_validation_edge_accountability,
    find_holes,
)


@click.group()
@click.pass_context
def check(ctx):
    """Run various checks on documents and the repository.

    \b
    Available checks:
        aaa check accountability <file>  - Check accountability statements
        aaa check topology <chart>       - Check topological properties
        aaa check ontology               - Verify ontology integrity
    """
    pass


@check.command()
@click.argument('file', required=True, type=click.Path(exists=True))
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.pass_context
def accountability(ctx, file, verbose):
    """Check accountability statements in a document.

    Verifies that the document has proper accountability fields
    (signs edges, qualifies edges, etc.)

    \b
    Example:
        aaa check accountability 01_edges/validation-my-doc.md
    """
    repo_root = ctx.obj.get('repo_root', Path.cwd())

    file_path = Path(file)
    if not file_path.is_absolute():
        file_path = repo_root / file_path

    try:
        click.echo(f"Checking accountability: {file_path.name}")

        # Use the core accountability check
        passed, message = check_validation_edge_accountability(
            file_path,
            author="",  # Empty for file-based check (not commit-time)
            committer="",
            github_actor=""
        )

        if passed:
            click.echo("Accountability check passed")
            if verbose:
                click.echo(f"  {message}")
        else:
            click.echo("Accountability check failed", err=True)
            click.echo(f"  {message}", err=True)
            sys.exit(1)

    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


@check.command()
@click.argument('chart', required=True, type=click.Path())
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.pass_context
def topology(ctx, chart, verbose):
    """Check topological properties of a chart.

    Verifies Euler characteristic and other topological invariants.

    \b
    Example:
        aaa check topology charts/incose-paper-assurance
    """
    repo_root = ctx.obj.get('repo_root', Path.cwd())

    # Resolve chart path
    chart_path = Path(chart)
    if not chart_path.is_absolute():
        chart_path = repo_root / chart_path

    # If directory, look for chart file
    if chart_path.is_dir():
        chart_name = chart_path.name
        chart_file = chart_path / f"{chart_name}.md"
        if chart_file.exists():
            chart_path = chart_file

    if not chart_path.exists():
        click.echo(f"Error: Chart file not found: {chart_path}", err=True)
        sys.exit(1)

    try:
        click.echo(f"Checking topology: {chart_path.name}")

        # Use the core topology module
        analysis = find_holes(chart_path, repo_root)

        stats = analysis['statistics']
        click.echo(f"\nVertices (V): {stats['vertices']}")
        click.echo(f"Edges (E):    {stats['edges']}")
        click.echo(f"Faces (F):    {stats['faces']}")
        click.echo(f"\nEuler characteristic: X = V - E + F = {stats['euler_characteristic']}")

        click.echo(f"\nPotential faces (triangles): {stats['potential_faces']}")
        click.echo(f"Actual faces:                {stats['faces']}")
        click.echo(f"Holes (missing faces):       {stats['holes']}")

        if analysis['holes']:
            click.echo(f"\nDetected {len(analysis['holes'])} topological hole(s):")
            for i, hole in enumerate(analysis['holes'][:5], 1):
                click.echo(f"  {i}. Missing face: {hole}")
            if len(analysis['holes']) > 5:
                click.echo(f"  ... and {len(analysis['holes']) - 5} more")
        else:
            click.echo("\nNo holes detected - chart is a complete simplicial complex")

    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


@check.command()
@click.option('--templates', default=None, help='Path to templates directory')
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.pass_context
def ontology(ctx, templates, verbose):
    """Verify ontology integrity.

    Checks that the ontology files are valid and consistent.

    \b
    Example:
        aaa check ontology
    """
    repo_root = ctx.obj.get('repo_root', Path.cwd())

    click.echo("Checking ontology integrity...")

    # Find ontology files - check both design/ and 00_vertices/
    ontology_files = []
    design_dir = repo_root / 'design'
    vertices_dir = repo_root / '00_vertices'

    if design_dir.exists():
        ontology_files.extend(design_dir.glob('ontology-*.md'))
    if vertices_dir.exists():
        ontology_files.extend(vertices_dir.glob('ontology-*.md'))

    if not ontology_files:
        # Try to fall back to bundled ontology
        try:
            bundled_foundation = get_bundled_foundation_path()
            bundled_ontology = bundled_foundation / 'ontology-base.md'
            if bundled_ontology.exists():
                ontology_files = [bundled_ontology]
                click.echo("  (Using bundled ontology - no local ontology found)")
        except FileNotFoundError:
            pass

    if not ontology_files:
        click.echo("Warning: No ontology files found", err=True)
        click.echo("Run 'aaa init --force' to copy the bundled ontology to your project.", err=True)
        sys.exit(1)

    all_valid = True

    if TemplateBasedVerifier is None:
        click.echo("Error: Could not import verification module.", err=True)
        sys.exit(1)

    # Resolve templates path
    if templates:
        templates_path = Path(templates)
        if not templates_path.is_absolute():
            templates_path = repo_root / templates_path
    else:
        local_templates = repo_root / 'templates'
        if local_templates.exists():
            templates_path = local_templates
        else:
            try:
                templates_path = get_templates_path()
            except FileNotFoundError as e:
                click.echo(f"Error: {e}", err=True)
                sys.exit(1)

    verifier = TemplateBasedVerifier(templates_path)

    for ont_file in ontology_files:
        click.echo(f"\n  Checking: {ont_file.name}")

        passed = verifier.verify_element(ont_file)
        if passed:
            click.echo(f"    Valid")
        else:
            click.echo(f"    Invalid", err=True)
            all_valid = False

    if all_valid:
        click.echo(f"\nAll ontology files valid ({len(ontology_files)} checked)")
    else:
        click.echo(f"\nSome ontology files invalid", err=True)
        sys.exit(1)
