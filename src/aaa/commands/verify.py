"""
aaa verify - Validate a single markdown file via its Pydantic Codec.

Performs single-document structural validation (required fields, field types,
controlled vocabulary values). Does NOT run SHACL graph-level checks — use
`aaa audit` for that.

Examples:
    aaa verify docs/my-spec.md
    aaa verify 01_edges/e:verification:foo.md
"""

import sys
from pathlib import Path

import click
from pydantic import ValidationError

from aaa.codecs import codec_for_type, dimension_for_type


def _read_type(path: Path) -> str | None:
    import re

    import yaml

    try:
        text = path.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
        if not m:
            return None
        fm = yaml.safe_load(m.group(1)) or {}
        return fm.get("type")
    except Exception:
        return None


@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--verbose", "-v", is_flag=True, help="Show full validation details.")
def verify(file, verbose):
    """Verify FILE against its Pydantic model (single-document check)."""
    path = Path(file)
    type_name = _read_type(path)

    if type_name is None:
        click.echo(f"[ERROR] {path}: no YAML frontmatter or missing 'type' field.", err=True)
        sys.exit(1)

    codec = codec_for_type(type_name)

    try:
        attrs = codec.decompile(path.resolve().as_uri())
    except ValidationError as exc:
        click.echo(f"[FAIL]  {path}")
        click.echo(f"        type: {type_name}")
        for err in exc.errors():
            loc = ".".join(str(x) for x in err["loc"])
            click.echo(f"        {loc}: {err['msg']}")
        sys.exit(1)
    except (ValueError, FileNotFoundError) as exc:
        click.echo(f"[ERROR] {path}: {exc}", err=True)
        sys.exit(1)

    dim = dimension_for_type(type_name)
    elem_id = attrs.get("id", "?")
    name = attrs.get("name", "?")

    click.echo(f"[OK]    {path}")
    if verbose:
        click.echo(f"        id:   {elem_id}")
        click.echo(f"        type: {type_name} ({dim})")
        click.echo(f"        name: {name}")
