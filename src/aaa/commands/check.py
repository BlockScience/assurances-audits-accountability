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

from aaa.core import TemplateBasedVerifier


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

    # Add scripts directory to path for check_accountability
    # (not yet in core module)
    scripts_dir = repo_root / 'scripts'
    sys.path.insert(0, str(scripts_dir))

    file_path = Path(file)
    if not file_path.is_absolute():
        file_path = repo_root / file_path

    try:
        from check_accountability import check_accountability as do_check
    except ImportError as e:
        click.echo(f"Error: Could not import accountability module: {e}", err=True)
        sys.exit(1)

    try:
        click.echo(f"Checking accountability: {file_path.name}")

        result = do_check(file_path)

        if result.get('valid', False):
            click.echo("✓ Accountability check passed")
            if verbose and 'details' in result:
                for detail in result['details']:
                    click.echo(f"  - {detail}")
        else:
            click.echo("✗ Accountability check failed", err=True)
            if 'errors' in result:
                for error in result['errors']:
                    click.echo(f"  - {error}", err=True)
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

    # Add scripts directory to path for topology module
    scripts_dir = repo_root / 'scripts'
    sys.path.insert(0, str(scripts_dir))

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
        from topology import main as topology_main

        click.echo(f"Checking topology: {chart_path.name}")

        # Run topology check
        # The topology script outputs directly, so we just call it
        import os
        original_cwd = os.getcwd()
        os.chdir(repo_root)

        try:
            # Simulate running the script
            sys.argv = ['topology', str(chart_path)]
            topology_main()
        finally:
            os.chdir(original_cwd)

    except ImportError as e:
        click.echo(f"Error: Could not import topology module: {e}", err=True)
        sys.exit(1)
    except SystemExit as e:
        # topology script may call sys.exit
        if e.code != 0:
            sys.exit(e.code)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


@check.command()
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.pass_context
def ontology(ctx, verbose):
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
        click.echo("Warning: No ontology files found", err=True)
        sys.exit(1)

    all_valid = True

    if TemplateBasedVerifier is None:
        click.echo("Error: Could not import verification module.", err=True)
        sys.exit(1)

    templates_path = repo_root / 'templates'
    verifier = TemplateBasedVerifier(templates_path)

    for ont_file in ontology_files:
        click.echo(f"\n  Checking: {ont_file.name}")

        passed = verifier.verify_element(ont_file)
        if passed:
            click.echo(f"    ✓ Valid")
        else:
            click.echo(f"    ✗ Invalid", err=True)
            all_valid = False

    if all_valid:
        click.echo(f"\n✓ All ontology files valid ({len(ontology_files)} checked)")
    else:
        click.echo(f"\n✗ Some ontology files invalid", err=True)
        sys.exit(1)
