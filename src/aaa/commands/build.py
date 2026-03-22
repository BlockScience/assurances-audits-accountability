"""
aaa build - Walk markdown files and build an RDF graph via KnowledgeComplex.

Reads all .md files with YAML frontmatter, decompiles each via its Codec
(Pydantic validation), inserts into a KnowledgeComplex, runs SHACL at the end,
and serialises to RDF (Turtle by default, or JSON-LD).

Replaces the old complex.json cache with a formal RDF graph.

Examples:
    aaa build
    aaa build --output graph.ttl
    aaa build --output graph.jsonld --format json-ld
    aaa build --strict          # fail fast on any Pydantic error
    aaa build tests/fixtures/   # build from a specific directory
"""

import click
import sys
from pathlib import Path
from typing import Iterator

from knowledgecomplex import KnowledgeComplex
from knowledgecomplex.io import save_graph
from knowledgecomplex.exceptions import ValidationError as KCValidationError, SchemaError
from pydantic import ValidationError as PydanticValidationError

from aaa.schema import build_aaa_schema
from aaa.codecs import codec_for_type, dimension_for_type, short_type


# Directories to scan for markdown files (relative to the repo root or given path)
_SCAN_DIRS = [
    "00_vertices",
    "01_edges",
    "02_faces",
    "charts",
    "content",
    "src/aaa/foundation",
]

# Directories to always skip
_SKIP_DIRS = {".git", ".venv", "archive", "__pycache__", ".pytest_cache", "node_modules"}


def _walk_markdown(root: Path) -> Iterator[Path]:
    """Yield all .md files under root, skipping ignored directories."""
    for path in root.rglob("*.md"):
        if any(part in _SKIP_DIRS for part in path.parts):
            continue
        yield path


def _read_type(path: Path) -> str | None:
    """Quickly read the 'type' field from YAML frontmatter without full parse."""
    try:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            return None
        import yaml, re
        m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
        if not m:
            return None
        fm = yaml.safe_load(m.group(1)) or {}
        return fm.get("type")
    except Exception:
        return None


def _insert_element(kc: KnowledgeComplex, path: Path, attrs: dict, type_name: str) -> None:
    """Insert a decompiled element into kc based on its dimension."""
    dim = dimension_for_type(type_name)
    kc_type = short_type(type_name)
    uri = path.as_uri()
    elem_id = attrs.get("id", path.stem)

    if dim == "vertex":
        vertex_attrs = {
            k: v for k, v in attrs.items()
            if k not in ("id", "type", "uri")
        }
        kc.add_vertex(elem_id, type=kc_type, uri=uri, **vertex_attrs)

    elif dim == "edge":
        source = attrs.get("source", "")
        target = attrs.get("target", "")
        if not source or not target:
            raise ValueError(f"Edge {path} missing 'source' or 'target' field")
        edge_attrs = {
            k: v for k, v in attrs.items()
            if k not in ("id", "type", "uri", "source", "target")
        }
        kc.add_edge(elem_id, type=kc_type, vertices={source, target}, uri=uri, **edge_attrs)

    elif dim == "face":
        edges = attrs.get("edges", [])
        if not edges:
            raise ValueError(f"Face {path} missing 'edges' field")
        face_attrs = {
            k: v for k, v in attrs.items()
            if k not in ("id", "type", "uri", "edges")
        }
        kc.add_face(elem_id, type=kc_type, boundary=list(edges), uri=uri, **face_attrs)


@click.command()
@click.argument("path", required=False, type=click.Path(exists=True))
@click.option("--output", "-o", default="graph.ttl", show_default=True,
              help="Output RDF file path.")
@click.option("--format", "fmt", default="turtle", show_default=True,
              type=click.Choice(["turtle", "json-ld", "n-triples"]),
              help="RDF serialisation format.")
@click.option("--strict", is_flag=True,
              help="Fail immediately on any Pydantic validation error.")
def build(path, output, fmt, strict):
    """Build an RDF graph from markdown files in PATH (default: current directory)."""
    root = Path(path).resolve() if path else Path.cwd()
    schema = build_aaa_schema()
    kc = KnowledgeComplex(schema=schema)

    errors: list[str] = []
    skipped = 0
    inserted = 0

    # Collect files, separating into vertex/edge/face so we insert in order
    # (vertices first, then edges, then faces) to satisfy boundary requirements.
    vertices: list[tuple[Path, str]] = []
    edges: list[tuple[Path, str]] = []
    faces: list[tuple[Path, str]] = []

    for md_path in _walk_markdown(root):
        type_name = _read_type(md_path)
        if type_name is None:
            skipped += 1
            continue
        dim = dimension_for_type(type_name)
        if dim == "vertex":
            vertices.append((md_path, type_name))
        elif dim == "edge":
            edges.append((md_path, type_name))
        else:
            faces.append((md_path, type_name))

    ordered = vertices + edges + faces

    with kc.deferred_verification():
        for md_path, type_name in ordered:
            codec = codec_for_type(type_name)
            try:
                attrs = codec.decompile(md_path.as_uri())
                _insert_element(kc, md_path, attrs, type_name)
                inserted += 1
            except PydanticValidationError as exc:
                msg = f"  {md_path}: Pydantic validation failed — {exc}"
                errors.append(msg)
                if strict:
                    click.echo(f"[ERROR] {msg}", err=True)
                    sys.exit(1)
                else:
                    click.echo(f"[WARN]  {msg}", err=True)
            except (ValueError, KeyError, FileNotFoundError, SchemaError) as exc:
                msg = f"  {md_path}: {exc}"
                errors.append(msg)
                if strict:
                    click.echo(f"[ERROR] {msg}", err=True)
                    sys.exit(1)
                else:
                    click.echo(f"[WARN]  {msg}", err=True)

    # SHACL validation
    try:
        kc.verify()
    except KCValidationError as exc:
        click.echo(f"[ERROR] SHACL validation failed:\n{exc}", err=True)
        sys.exit(1)

    # Serialise
    out_path = Path(output)
    save_graph(kc, out_path, format=fmt)

    click.echo(
        f"Built: {inserted} elements inserted, {skipped} files skipped, "
        f"{len(errors)} warnings → {out_path}"
    )
