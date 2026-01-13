"""
aaa verify - Verify documents against their templates.

Examples:
    aaa verify document.md
    aaa verify 00_vertices/spec-for-spec.md
    aaa verify --all
"""

import click
import sys
from pathlib import Path

from aaa.core import TemplateBasedVerifier, get_templates_path


@click.command()
@click.argument('file', required=False, type=click.Path(exists=True))
@click.option('--all', 'verify_all', is_flag=True, help='Verify all documents in the repository')
@click.option('--templates', default=None, help='Path to templates directory (uses bundled if not specified)')
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.pass_context
def verify(ctx, file, verify_all, templates, verbose):
    """Verify a document against its template.

    \b
    Examples:
        aaa verify 00_vertices/spec-for-spec.md
        aaa verify --all
    """
    repo_root = ctx.obj.get('repo_root', Path.cwd())

    if TemplateBasedVerifier is None:
        click.echo("Error: Could not import verification module.", err=True)
        sys.exit(1)

    # Resolve templates path: use custom, local, or bundled
    if templates:
        templates_path = Path(templates)
        if not templates_path.is_absolute():
            templates_path = repo_root / templates_path
        if not templates_path.exists():
            click.echo(f"Error: Templates directory not found: {templates_path}", err=True)
            sys.exit(1)
    else:
        # Try local templates first, then fall back to bundled
        local_templates = repo_root / 'templates'
        if local_templates.exists():
            templates_path = local_templates
        else:
            try:
                templates_path = get_templates_path()
            except FileNotFoundError as e:
                click.echo(f"Error: {e}", err=True)
                sys.exit(1)

    if verbose:
        click.echo(f"Using templates from: {templates_path}")

    verifier = TemplateBasedVerifier(templates_path)

    if verify_all:
        # Verify all documents
        all_passed = True
        failed_files = []
        dirs_to_check = ['00_vertices', '01_edges', '02_faces']

        for dir_name in dirs_to_check:
            dir_path = repo_root / dir_name
            if not dir_path.exists():
                continue

            for md_file in dir_path.glob('*.md'):
                if md_file.name == 'README.md':
                    continue

                passed = verifier.verify_element(md_file)
                if not passed:
                    all_passed = False
                    failed_files.append((md_file.relative_to(repo_root), verifier.errors.copy()))

        if all_passed:
            click.echo("\n✓ All documents passed verification")
            sys.exit(0)
        else:
            click.echo("\n✗ Some documents failed verification", err=True)
            click.echo("")
            for file_path, errors in failed_files:
                click.echo(f"FAILED: {file_path}", err=True)
                for error in errors:
                    click.echo(f"  - {error}", err=True)
            click.echo("")
            click.echo(f"Total: {len(failed_files)} file(s) failed", err=True)
            sys.exit(1)

    elif file:
        # Verify single file
        file_path = Path(file)
        if not file_path.is_absolute():
            file_path = repo_root / file_path

        passed = verifier.verify_element(file_path)

        if passed:
            sys.exit(0)
        else:
            sys.exit(1)

    else:
        click.echo("Error: Specify a file to verify or use --all", err=True)
        click.echo("Usage: aaa verify <file> or aaa verify --all", err=True)
        sys.exit(1)
