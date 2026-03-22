"""Codec for vertex/chart elements."""

from __future__ import annotations

from pydantic import field_validator

from .base import parse_frontmatter, write_frontmatter
from .doc import DocModel


def _is_valid_sparql(query: str) -> bool:
    """Basic SPARQL syntax check — verifies SELECT/CONSTRUCT/ASK/DESCRIBE keyword."""
    upper = query.strip().upper()
    return any(upper.startswith(kw) for kw in ("SELECT", "CONSTRUCT", "ASK", "DESCRIBE", "PREFIX"))


class ChartModel(DocModel):
    """Pydantic model for vertex/chart."""

    query: str

    @field_validator("query")
    @classmethod
    def query_looks_like_sparql(cls, v: str) -> str:
        if not _is_valid_sparql(v):
            raise ValueError(
                "chart 'query' field must contain valid SPARQL "
                "(must start with SELECT, CONSTRUCT, ASK, DESCRIBE, or PREFIX)"
            )
        return v


class ChartCodec:
    def decompile(self, uri: str) -> dict:
        fm, _body = parse_frontmatter(uri)
        ChartModel(**fm)
        return fm

    def compile(self, element: dict) -> None:
        path_uri = element.get("uri", "")
        if not path_uri:
            raise ValueError("element has no uri")
        fm = {k: v for k, v in element.items() if k != "uri"}
        write_frontmatter(path_uri, fm)
