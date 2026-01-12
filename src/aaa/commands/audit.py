"""
aaa audit - Audit assurance coverage of charts.

Examples:
    aaa audit charts/incose-paper-assurance/incose-paper-assurance.md
    aaa audit charts/incose-paper-assurance
    aaa audit --topology charts/boundary-complex/boundary-complex.md
"""

import click
import sys
from pathlib import Path


@click.command()
@click.argument('chart', required=True, type=click.Path())
@click.option('--topology', is_flag=True, help='Also check topological properties')
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.pass_context
def audit(ctx, chart, topology, verbose):
    """Audit assurance coverage of a chart.

    Verifies that all vertices in a chart are properly assured,
    checks trace to root, and validates the V - F = 1 invariant.

    \b
    Examples:
        aaa audit charts/incose-paper-assurance/incose-paper-assurance.md
        aaa audit charts/incose-paper-assurance  # Auto-finds chart file
        aaa audit --topology charts/boundary-complex
    """
    repo_root = ctx.obj.get('repo_root', Path.cwd())

    # Add scripts directory to path
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
        else:
            # Try to find any .md file that looks like a chart
            md_files = list(chart_path.glob('*.md'))
            chart_files = [f for f in md_files if f.name != 'README.md' and 'audit-trail' not in f.name]
            if len(chart_files) == 1:
                chart_path = chart_files[0]
            else:
                click.echo(f"Error: Could not find chart file in {chart_path}", err=True)
                click.echo(f"Found files: {[f.name for f in md_files]}", err=True)
                sys.exit(1)

    if not chart_path.exists():
        click.echo(f"Error: Chart file not found: {chart_path}", err=True)
        sys.exit(1)

    try:
        from audit_assurance_chart import audit_chart
    except ImportError as e:
        click.echo(f"Error: Could not import audit module: {e}", err=True)
        sys.exit(1)

    # Change to repo root
    import os
    original_cwd = os.getcwd()
    os.chdir(repo_root)

    try:
        click.echo(f"Auditing: {chart_path.relative_to(repo_root)}")
        click.echo("=" * 60)

        result = audit_chart(chart_path)

        if result.get('passed', False):
            click.echo(f"\n✓ Audit PASSED")
            if 'coverage' in result:
                click.echo(f"  Coverage: {result['coverage']}")
            if 'vertices_assured' in result:
                click.echo(f"  Vertices assured: {result['vertices_assured']}")
        else:
            click.echo(f"\n✗ Audit FAILED", err=True)
            if 'errors' in result:
                for error in result['errors']:
                    click.echo(f"  - {error}", err=True)
            sys.exit(1)

        # Topology check if requested
        if topology:
            click.echo("\n" + "=" * 60)
            click.echo("Topology Check:")

            try:
                from topology import check_topology
                topo_result = check_topology(chart_path)

                if topo_result.get('valid', False):
                    click.echo(f"  ✓ Topology valid")
                    click.echo(f"  Euler characteristic: χ = {topo_result.get('euler', 'N/A')}")
                else:
                    click.echo(f"  ✗ Topology invalid", err=True)
                    sys.exit(1)

            except ImportError:
                click.echo("  Warning: topology module not available", err=True)
            except Exception as e:
                click.echo(f"  Error checking topology: {e}", err=True)

    except Exception as e:
        click.echo(f"Error during audit: {e}", err=True)
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

    finally:
        os.chdir(original_cwd)
