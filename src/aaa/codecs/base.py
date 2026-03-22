"""
Base utilities and models for AAA codecs.

parse_frontmatter(uri)  — read a file:// URI, extract YAML frontmatter
write_frontmatter(uri, data, body)  — write YAML frontmatter back to file
AAABaseModel  — common Pydantic fields shared by all AAA element types
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml
from pydantic import BaseModel, field_validator

# ---------------------------------------------------------------------------
# File I/O helpers
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)", re.DOTALL)


def _uri_to_path(uri: str) -> Path:
    """Convert a file:// URI to a Path. Accepts plain paths too."""
    parsed = urlparse(uri)
    if parsed.scheme == "file":
        return Path(parsed.path)
    return Path(uri)


def _normalize(value: Any) -> Any:
    """Recursively normalize YAML-parsed values to JSON-compatible types.

    YAML parses ISO 8601 timestamps as datetime objects; we convert them back
    to ISO strings so all Pydantic models always receive plain strings.
    """
    import datetime as dt

    if isinstance(value, (dt.datetime, dt.date)):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: _normalize(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_normalize(v) for v in value]
    return value


def parse_frontmatter(uri: str) -> tuple[dict[str, Any], str]:
    """
    Read a markdown file and return (frontmatter_dict, body_str).

    Datetime fields in YAML frontmatter are normalized to ISO 8601 strings
    so that all Pydantic models receive consistent str inputs.

    Raises:
        FileNotFoundError: if the file does not exist.
        ValueError: if the file has no YAML frontmatter.
    """
    path = _uri_to_path(uri)
    content = path.read_text(encoding="utf-8")
    match = _FM_RE.match(content)
    if not match:
        raise ValueError(f"No YAML frontmatter found in {path}")
    fm_str, body = match.groups()
    fm = yaml.safe_load(fm_str) or {}
    return _normalize(fm), body.strip()


def write_frontmatter(uri: str, data: dict[str, Any], body: str = "") -> None:
    """Write frontmatter dict + body back to the file at uri."""
    path = _uri_to_path(uri)
    fm_str = yaml.dump(data, allow_unicode=True, default_flow_style=False)
    path.write_text(f"---\n{fm_str}---\n\n{body}\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Base Pydantic model
# ---------------------------------------------------------------------------


class AAABaseModel(BaseModel):
    """Fields common to all AAA markdown elements (vertices, edges, faces)."""

    model_config = {"extra": "allow"}

    id: str
    name: str
    type: str

    # Optional fields present on most elements
    tags: list[str] = []
    version: str | None = None
    created: str | None = None
    modified: str | None = None
    description: str | None = None
    axiomatic: bool = False

    @field_validator("id")
    @classmethod
    def id_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("id must not be empty")
        return v

    @field_validator("name")
    @classmethod
    def name_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("name must not be empty")
        return v
