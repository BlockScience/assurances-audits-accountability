"""
aaa init — scaffold a new knowledge complex project.

Creates a project directory with the standard AAA structure,
copies foundation documents, and optionally initializes git.
"""

import importlib.resources
import subprocess
import sys
from pathlib import Path

import click


@click.command()
@click.argument("name")
@click.option(
    "--no-git",
    is_flag=True,
    default=False,
    help="Skip git init.",
)
def init(name, no_git):
    """Initialize a new AAA knowledge complex project.

    Creates a project directory NAME with the standard simplicial complex
    structure, copies foundation documents, and optionally initializes git.

    \b
    Example:
        aaa init my-project
        cd my-project
        aaa build
    """
    target = Path(name).resolve()

    if target.exists():
        click.echo(f"[ERROR] Directory already exists: {target}", err=True)
        sys.exit(1)

    click.echo(f"Creating project: {target.name}")

    # Create directory structure
    dirs = [
        "00_vertices",
        "01_edges",
        "02_faces",
        "charts",
    ]
    for d in dirs:
        (target / d).mkdir(parents=True, exist_ok=True)

    # Copy foundation files
    _copy_package_data("aaa.foundation", target)

    # Create .gitignore
    gitignore = target / ".gitignore"
    gitignore.write_text(
        "# Python\n"
        "__pycache__/\n"
        "*.py[cod]\n"
        ".venv/\n"
        "\n"
        "# AAA build outputs\n"
        "complex.json\n"
        "graph.ttl\n"
        "graph.jsonld\n"
        "\n"
        "# IDE\n"
        ".vscode/\n"
        ".idea/\n"
        "\n"
        "# OS\n"
        ".DS_Store\n"
    )

    # Create a minimal README
    readme = target / "README.md"
    readme.write_text(
        f"# {name}\n\n"
        "A knowledge complex project built with "
        "[aaa-docware](https://github.com/BlockScience/assurances-audits-accountability).\n\n"
        "## Quick Start\n\n"
        "```bash\n"
        "# Verify a document\n"
        "aaa verify 00_vertices/my-doc.md\n\n"
        "# Build the RDF graph\n"
        "aaa build\n\n"
        "# Audit assurance coverage\n"
        "aaa audit charts/my-chart\n"
        "```\n"
    )

    # Initialize git
    if not no_git:
        try:
            subprocess.run(
                ["git", "init"],
                cwd=target,
                capture_output=True,
                check=True,
            )
            click.echo("  Initialized git repository")
        except (subprocess.CalledProcessError, FileNotFoundError):
            click.echo("  [WARN] git init failed — skipping")

    click.echo()
    click.echo(f"Project created: {target}")
    click.echo()
    click.echo("Next steps:")
    click.echo(f"  cd {name}")
    click.echo("  aaa build              # Build the knowledge complex")
    click.echo("  aaa verify <file>      # Verify a document")
    click.echo("  aaa audit <chart>      # Audit assurance coverage")


def _copy_package_data(package_name: str, target: Path) -> None:
    """Copy package data files into the target directory, preserving structure."""
    try:
        data_root = importlib.resources.files(package_name)
    except (ModuleNotFoundError, TypeError):
        click.echo(f"  [WARN] Could not locate {package_name} data — skipping", err=True)
        return

    count = 0
    for item in data_root.iterdir():
        count += _copy_resource(item, target)

    click.echo(f"  Copied {count} foundation files")


def _copy_resource(resource, target: Path) -> int:
    """Recursively copy a resource (file or directory) to target. Returns file count."""
    if resource.is_file():
        dest = target / resource.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(resource.read_bytes())
        return 1
    elif resource.is_dir():
        count = 0
        dest_dir = target / resource.name
        dest_dir.mkdir(parents=True, exist_ok=True)
        for child in resource.iterdir():
            count += _copy_resource(child, dest_dir)
        return count
    return 0
