"""Codec for vertex/spec elements."""

from __future__ import annotations
from .base import parse_frontmatter, write_frontmatter
from .doc import DocModel


class SpecModel(DocModel):
    """Pydantic model for vertex/spec."""
    # Specs may carry additional structured fields; extra fields allowed via base.
    pass


class SpecCodec:
    def decompile(self, uri: str) -> dict:
        fm, _body = parse_frontmatter(uri)
        SpecModel(**fm)
        return fm

    def compile(self, element: dict) -> None:
        path_uri = element.get("uri", "")
        if not path_uri:
            raise ValueError("element has no uri")
        fm = {k: v for k, v in element.items() if k != "uri"}
        write_frontmatter(path_uri, fm)
