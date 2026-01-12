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


@click.command()
@click.argument('file', required=False, type=click.Path(exists=True))
@click.option('--all', 'verify_all', is_flag=True, help='Verify all documents in the repository')
@click.option('--templates', default='templates', help='Path to templates directory')
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

    # Add scripts directory to path so we can import the verification logic
    scripts_dir = repo_root / 'scripts'
    sys.path.insert(0, str(scripts_dir))

    try:
        from verify_template_based import TemplateBasedVerifier
    except ImportError as e:
        click.echo(f"Error: Could not import verification module: {e}", err=True)
        click.echo("Make sure you're running from the repository root.", err=True)
        sys.exit(1)

    templates_path = repo_root / templates

    if not templates_path.exists():
        click.echo(f"Error: Templates directory not found: {templates_path}", err=True)
        sys.exit(1)

    verifier = TemplateBasedVerifier(templates_path)

    if verify_all:
        # Verify all documents
        all_passed = True
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

        if all_passed:
            click.echo("\n✓ All documents passed verification")
            sys.exit(0)
        else:
            click.echo("\n✗ Some documents failed verification", err=True)
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
