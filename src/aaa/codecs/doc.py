"""Codec for vertex/doc elements."""

from __future__ import annotations

from .base import AAABaseModel, parse_frontmatter, write_frontmatter


class DocModel(AAABaseModel):
    """Pydantic model for vertex/doc (and all doc subtypes)."""

    extends: str | None = None


class DocCodec:
    """Codec for doc vertices (and fallback for unknown doc subtypes)."""

    def decompile(self, uri: str) -> dict:
        fm, _body = parse_frontmatter(uri)
        DocModel(**fm)  # raises ValidationError if invalid
        return fm

    def compile(self, element: dict) -> None:
        path_uri = element.get("uri", "")
        if not path_uri:
            raise ValueError("element has no uri — cannot compile to file")
        fm = {k: v for k, v in element.items() if k != "uri"}
        write_frontmatter(path_uri, fm)
