"""
AAA CLI - Main entry point.

Usage:
    aaa verify <file>           Verify a document against its template
    aaa build                   Build the complex.json cache
    aaa audit <chart>           Audit assurance coverage of a chart
    aaa check accountability    Check accountability statements
    aaa check topology          Check topological properties
"""

import click
import sys
from pathlib import Path

from aaa.commands import verify, build, audit, check, init


@click.group()
@click.version_option(version="1.0.0", prog_name="aaa")
@click.pass_context
def main(ctx):
    """AAA - Assurances, Audits & Accountability Framework

    A command-line tool for verifying, validating, and auditing
    documents in a typed simplicial complex knowledge framework.

    \b
    Quick start:
        aaa verify document.md      # Verify a single document
        aaa build                   # Build the complex.json cache
        aaa audit charts/my-chart   # Audit assurance coverage
    """
    # Ensure ctx.obj exists for passing data between commands
    ctx.ensure_object(dict)

    # Find repository root (look for pyproject.toml or .git)
    ctx.obj['repo_root'] = find_repo_root()


def find_repo_root() -> Path:
    """Find the repository root by looking for pyproject.toml or .git."""
    current = Path.cwd()

    for parent in [current] + list(current.parents):
        if (parent / 'pyproject.toml').exists() or (parent / '.git').exists():
            return parent

    # Fall back to current directory
    return current


# Register command groups
main.add_command(verify.verify)
main.add_command(build.build)
main.add_command(audit.audit)
main.add_command(check.check)
main.add_command(init.init)


if __name__ == '__main__':
    main()
