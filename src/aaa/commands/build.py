"""
aaa build - Build the complex.json cache.

Examples:
    aaa build
    aaa build --output custom.json
    aaa build examples/incose-paper  # Build cache for example
"""

import click
import sys
from pathlib import Path

from aaa.core import build_cache as do_build_cache, calculate_euler_characteristic


@click.command()
@click.argument('path', required=False, type=click.Path(exists=True))
@click.option('--output', '-o', default='complex.json', help='Output file path')
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.pass_context
def build(ctx, path, output, verbose):
    """Build the complex.json cache from markdown files.

    Scans the specified path (or repository root) for vertices, edges, faces,
    and charts, parses them, and generates a JSON cache file.

    \b
    Examples:
        aaa build                        # Build cache for repo root
        aaa build -o my-cache.json       # Custom output path
        aaa build examples/incose-paper  # Build cache for example
    """
    repo_root = ctx.obj.get('repo_root', Path.cwd())

    # Determine build root
    if path:
        build_root = Path(path)
        if not build_root.is_absolute():
            build_root = repo_root / build_root
    else:
        build_root = repo_root

    if do_build_cache is None:
        click.echo("Error: Could not import build_cache module.", err=True)
        sys.exit(1)

    # Change to build root for the script
    import os
    original_cwd = os.getcwd()
    os.chdir(build_root)

    try:

        output_path = build_root / output

        # build_cache already prints progress and writes the file
        cache_data = do_build_cache(build_root, output_path)

        if cache_data:
            # Print summary
            vertices = cache_data.get('vertices', [])
            edges = cache_data.get('edges', [])
            faces = cache_data.get('faces', [])

            euler = calculate_euler_characteristic(vertices, edges, faces)
            click.echo(f"Euler characteristic: χ = {euler}")
        else:
            click.echo("Error: Failed to build cache", err=True)
            sys.exit(1)

    except Exception as e:
        click.echo(f"Error building cache: {e}", err=True)
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

    finally:
        os.chdir(original_cwd)
