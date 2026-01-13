"""
aaa check - Various checking commands.

Examples:
    aaa check accountability document.md
    aaa check topology charts/my-chart
    aaa check ontology [chart]           # Check ontology type rules
    aaa check rules [chart]              # Check both topology AND ontology rules
"""

import click
import json
import sys
from pathlib import Path

from aaa.core import (
    TemplateBasedVerifier,
    get_templates_path,
    get_bundled_foundation_path,
    check_validation_edge_accountability,
    find_holes,
    check_ontology_rules,
    load_cache,
    Severity,
    parse_chart,
    ParseError,
)


@click.group()
@click.pass_context
def check(ctx):
    """Run various checks on documents and the repository.

    \b
    Available checks:
        aaa check accountability <file>  - Check accountability statements
        aaa check topology <chart>       - Check topological properties (structural)
        aaa check ontology [chart]       - Check ontology type rules
        aaa check rules [chart]          - Comprehensive check (topology + ontology)
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

    Verifies structural simplicial complex properties:
    - Euler characteristic (χ = V - E + F)
    - Hole detection (missing faces)
    - Boundary completeness

    This checks STRUCTURAL rules, not type rules.
    Use 'aaa check ontology' for type rules or 'aaa check rules' for both.

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
        click.echo(f"\nEuler characteristic: χ = V - E + F = {stats['euler_characteristic']}")

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


def _resolve_chart_path(chart: str, repo_root: Path) -> Path:
    """Resolve chart argument to a file path."""
    chart_path = Path(chart)
    if not chart_path.is_absolute():
        chart_path = repo_root / chart_path

    # If directory, look for chart file
    if chart_path.is_dir():
        chart_name = chart_path.name
        chart_file = chart_path / f"{chart_name}.md"
        if chart_file.exists():
            chart_path = chart_file

    return chart_path


def _filter_cache_for_chart(cache: dict, chart_path: Path) -> dict:
    """Filter cache to only include elements in the specified chart."""
    try:
        chart = parse_chart(chart_path)
    except ParseError as e:
        raise ValueError(f"Failed to parse chart: {e}")

    chart_vertices = set(chart['elements']['vertices'])
    chart_edges = set(chart['elements']['edges'])
    chart_faces = set(chart['elements']['faces'])

    filtered = {
        'elements': {
            'vertices': {
                vid: vdata for vid, vdata in cache['elements']['vertices'].items()
                if vid in chart_vertices
            },
            'edges': {
                eid: edata for eid, edata in cache['elements']['edges'].items()
                if eid in chart_edges
            },
            'faces': {
                fid: fdata for fid, fdata in cache['elements']['faces'].items()
                if fid in chart_faces
            },
        },
        'statistics': {
            'vertices': len(chart_vertices),
            'edges': len(chart_edges),
            'faces': len(chart_faces),
        }
    }
    return filtered


def _run_ontology_checks(cache: dict, verbose: bool, json_output: bool, warnings: bool) -> int:
    """Run ontology type rule checks. Returns exit code."""
    violations = check_ontology_rules(cache)

    # Filter warnings if requested
    if not warnings:
        violations = [v for v in violations if v.severity == Severity.ERROR]

    # Count by severity
    errors = [v for v in violations if v.severity == Severity.ERROR]
    warns = [v for v in violations if v.severity == Severity.WARNING]

    if json_output:
        output = {
            'status': 'pass' if not errors else 'fail',
            'errors': len(errors),
            'warnings': len(warns),
            'violations': [
                {
                    'rule': v.rule_name,
                    'type': v.rule_type.value,
                    'severity': v.severity.value,
                    'element_id': v.element_id,
                    'element_type': v.element_type,
                    'message': v.message,
                    'details': v.details
                }
                for v in violations
            ]
        }
        click.echo(json.dumps(output, indent=2))
    else:
        if not violations:
            click.echo("All ontology rules passed!")
        else:
            # Group by rule name for cleaner output
            by_rule = {}
            for v in violations:
                if v.rule_name not in by_rule:
                    by_rule[v.rule_name] = []
                by_rule[v.rule_name].append(v)

            for rule_name, rule_violations in by_rule.items():
                click.echo(f"\n{rule_name} ({len(rule_violations)} violation(s)):")

                for v in rule_violations[:10]:
                    severity_marker = "ERROR" if v.severity == Severity.ERROR else "WARN"
                    click.echo(f"  [{severity_marker}] {v.element_id}")
                    click.echo(f"    {v.message}")

                    if verbose and v.details:
                        for key, value in v.details.items():
                            click.echo(f"    {key}: {value}")

                if len(rule_violations) > 10:
                    click.echo(f"  ... and {len(rule_violations) - 10} more")

            click.echo(f"\nSummary: {len(errors)} error(s), {len(warns)} warning(s)")

    return 1 if errors else 0


@check.command()
@click.argument('chart', required=False, type=click.Path())
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.option('--json-output', '-j', is_flag=True, help='Output results as JSON')
@click.option('--warnings/--no-warnings', default=True, help='Include warnings (default: yes)')
@click.pass_context
def ontology(ctx, chart, verbose, json_output, warnings):
    """Check ontology type rules.

    Verifies that elements conform to ontology local rules:
    - Edge endpoint type constraints (verification: doc→spec, etc.)
    - Vertex degree constraints (spec couples to exactly one guidance)
    - Face boundary closure (3 vertices, 3 edges)
    - Signature/assurance face adjacency requirements
    - Module qualification cascade
    - Execution trace DAG requirements

    If CHART is specified, only check elements in that chart.
    If omitted, check the entire knowledge complex.

    IMPORTANT: This is verification (deterministic type checking),
    not validation (human judgment of fitness for purpose).

    \b
    Examples:
        aaa check ontology                    # Check entire complex
        aaa check ontology charts/my-chart    # Check specific chart
        aaa check ontology -v                 # Verbose output
        aaa check ontology --json             # JSON output for CI/CD
    """
    repo_root = ctx.obj.get('repo_root', Path.cwd())

    # Load cache
    try:
        cache = load_cache(repo_root)
    except FileNotFoundError:
        click.echo("Error: complex.json not found. Run 'aaa build' first.", err=True)
        sys.exit(1)

    # Filter to chart if specified
    if chart:
        chart_path = _resolve_chart_path(chart, repo_root)
        if not chart_path.exists():
            click.echo(f"Error: Chart file not found: {chart_path}", err=True)
            sys.exit(1)

        try:
            cache = _filter_cache_for_chart(cache, chart_path)
            if not json_output:
                click.echo(f"Checking ontology rules for chart: {chart_path.name}")
        except ValueError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)
    else:
        if not json_output:
            click.echo("Checking ontology rules for entire complex...")

    if not json_output:
        stats = cache.get('statistics', {})
        click.echo(f"  Vertices: {stats.get('vertex_count', stats.get('vertices', 0))}")
        click.echo(f"  Edges: {stats.get('edge_count', stats.get('edges', 0))}")
        click.echo(f"  Faces: {stats.get('face_count', stats.get('faces', 0))}")
        click.echo("")

    exit_code = _run_ontology_checks(cache, verbose, json_output, warnings)
    if exit_code:
        sys.exit(exit_code)


@check.command()
@click.argument('chart', required=False, type=click.Path())
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.option('--json-output', '-j', is_flag=True, help='Output results as JSON')
@click.option('--warnings/--no-warnings', default=True, help='Include warnings (default: yes)')
@click.pass_context
def rules(ctx, chart, verbose, json_output, warnings):
    """Comprehensive rule check (topology + ontology).

    Runs BOTH topology and ontology checks:

    TOPOLOGY (structural):
    - Euler characteristic (χ = V - E + F)
    - Hole detection (missing faces)
    - Boundary completeness

    ONTOLOGY (type rules):
    - Edge endpoint type constraints
    - Vertex degree constraints
    - Face boundary closure
    - Face adjacency requirements
    - DAG requirements for execution traces

    If CHART is specified, only check that chart.
    If omitted, check the entire knowledge complex.

    \b
    Examples:
        aaa check rules                    # Check entire complex
        aaa check rules charts/my-chart    # Check specific chart
        aaa check rules -v                 # Verbose output
        aaa check rules --json             # JSON output for CI/CD
    """
    repo_root = ctx.obj.get('repo_root', Path.cwd())
    has_errors = False

    # Load cache
    try:
        cache = load_cache(repo_root)
    except FileNotFoundError:
        click.echo("Error: complex.json not found. Run 'aaa build' first.", err=True)
        sys.exit(1)

    # Determine scope
    if chart:
        chart_path = _resolve_chart_path(chart, repo_root)
        if not chart_path.exists():
            click.echo(f"Error: Chart file not found: {chart_path}", err=True)
            sys.exit(1)
        scope_name = chart_path.name
    else:
        chart_path = None
        scope_name = "entire complex"

    if not json_output:
        click.echo(f"Comprehensive rule check for: {scope_name}")
        click.echo("=" * 50)

    # ===== TOPOLOGY CHECK =====
    if chart_path:
        if not json_output:
            click.echo("\n## Topology Check (Structural)")
            click.echo("-" * 30)

        try:
            analysis = find_holes(chart_path, repo_root)
            stats = analysis['statistics']

            if not json_output:
                click.echo(f"Vertices (V): {stats['vertices']}")
                click.echo(f"Edges (E):    {stats['edges']}")
                click.echo(f"Faces (F):    {stats['faces']}")
                click.echo(f"Euler characteristic: χ = {stats['euler_characteristic']}")
                click.echo(f"Holes: {stats['holes']}")

                if analysis['holes']:
                    click.echo(f"\n  {len(analysis['holes'])} topological hole(s) detected:")
                    for i, hole in enumerate(analysis['holes'][:10], 1):
                        click.echo(f"    {i}. {hole}")
                    if len(analysis['holes']) > 10:
                        click.echo(f"    ... and {len(analysis['holes']) - 10} more")
                    # Holes are valid topological features, not errors
                else:
                    click.echo("\n  ✓ No topological holes")

        except Exception as e:
            click.echo(f"Topology check error: {e}", err=True)
            has_errors = True
    else:
        # For whole complex, report overall Euler characteristic from cache
        if not json_output:
            click.echo("\n## Topology Check (Structural)")
            click.echo("-" * 30)
            stats = cache.get('statistics', {})
            V = stats.get('vertex_count', stats.get('vertices', 0))
            E = stats.get('edge_count', stats.get('edges', 0))
            F = stats.get('face_count', stats.get('faces', 0))
            euler = stats.get('euler_characteristic', V - E + F)
            click.echo(f"Vertices (V): {V}")
            click.echo(f"Edges (E):    {E}")
            click.echo(f"Faces (F):    {F}")
            click.echo(f"Euler characteristic: χ = {euler}")
            click.echo("\n  (Use 'aaa check topology <chart>' for chart-specific hole detection)")

    # ===== ONTOLOGY CHECK =====
    if not json_output:
        click.echo("\n## Ontology Check (Type Rules)")
        click.echo("-" * 30)

    # Filter cache if chart specified
    if chart_path:
        try:
            filtered_cache = _filter_cache_for_chart(cache, chart_path)
        except ValueError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)
    else:
        filtered_cache = cache

    if not json_output:
        stats = filtered_cache.get('statistics', {})
        click.echo(f"Checking {stats.get('vertices', 0)} vertices, {stats.get('edges', 0)} edges, {stats.get('faces', 0)} faces")
        click.echo("")

    # Run ontology checks
    violations = check_ontology_rules(filtered_cache)

    if not warnings:
        violations = [v for v in violations if v.severity == Severity.ERROR]

    errors = [v for v in violations if v.severity == Severity.ERROR]
    warns = [v for v in violations if v.severity == Severity.WARNING]

    if json_output:
        # Combined JSON output
        output = {
            'scope': scope_name,
            'topology': {
                'euler_characteristic': stats.get('euler_characteristic', None) if chart_path else (V - E + F),
                'holes': len(analysis['holes']) if chart_path else None,
            } if 'stats' in dir() or chart_path is None else None,
            'ontology': {
                'status': 'pass' if not errors else 'fail',
                'errors': len(errors),
                'warnings': len(warns),
                'violations': [
                    {
                        'rule': v.rule_name,
                        'type': v.rule_type.value,
                        'severity': v.severity.value,
                        'element_id': v.element_id,
                        'element_type': v.element_type,
                        'message': v.message,
                        'details': v.details
                    }
                    for v in violations
                ]
            }
        }
        click.echo(json.dumps(output, indent=2))
    else:
        if not violations:
            click.echo("  ✓ All ontology rules passed!")
        else:
            by_rule = {}
            for v in violations:
                if v.rule_name not in by_rule:
                    by_rule[v.rule_name] = []
                by_rule[v.rule_name].append(v)

            for rule_name, rule_violations in by_rule.items():
                click.echo(f"\n{rule_name} ({len(rule_violations)} violation(s)):")

                for v in rule_violations[:5]:
                    severity_marker = "ERROR" if v.severity == Severity.ERROR else "WARN"
                    click.echo(f"  [{severity_marker}] {v.element_id}")
                    click.echo(f"    {v.message}")

                    if verbose and v.details:
                        for key, value in v.details.items():
                            click.echo(f"    {key}: {value}")

                if len(rule_violations) > 5:
                    click.echo(f"  ... and {len(rule_violations) - 5} more")

        # ===== SUMMARY =====
        click.echo("\n" + "=" * 50)
        click.echo("## Summary")

        if errors:
            has_errors = True

        if has_errors:
            click.echo(f"FAILED: {len(errors)} ontology error(s), {len(warns)} warning(s)")
        else:
            click.echo(f"PASSED: {len(warns)} warning(s)")

    if has_errors or errors:
        sys.exit(1)
