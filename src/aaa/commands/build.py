"""
aaa build - Build the complex.json cache.

Examples:
    aaa build
    aaa build --output custom.json
"""

import click
import sys
from pathlib import Path


@click.command()
@click.option('--output', '-o', default='complex.json', help='Output file path')
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.pass_context
def build(ctx, output, verbose):
    """Build the complex.json cache from markdown files.

    Scans the repository for vertices, edges, faces, and charts,
    parses them, and generates a JSON cache file.

    \b
    Examples:
        aaa build                   # Build cache
        aaa build -o my-cache.json  # Custom output path
    """
    repo_root = ctx.obj.get('repo_root', Path.cwd())

    # Add scripts directory to path
    scripts_dir = repo_root / 'scripts'
    sys.path.insert(0, str(scripts_dir))

    # Change to repo root for the script
    import os
    original_cwd = os.getcwd()
    os.chdir(repo_root)

    try:
        from build_cache import build_cache as do_build_cache, calculate_euler_characteristic

        output_path = repo_root / output

        # build_cache already prints progress and writes the file
        cache_data = do_build_cache(repo_root, output_path)

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

    except ImportError as e:
        click.echo(f"Error: Could not import build_cache module: {e}", err=True)
        sys.exit(1)

    except Exception as e:
        click.echo(f"Error building cache: {e}", err=True)
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

    finally:
        os.chdir(original_cwd)
