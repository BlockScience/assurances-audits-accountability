"""Codec for vertex/guidance elements."""

from __future__ import annotations

from .base import parse_frontmatter, write_frontmatter
from .doc import DocModel


class GuidanceModel(DocModel):
    """Pydantic model for vertex/guidance."""

    pass


class GuidanceCodec:
    def decompile(self, uri: str) -> dict:
        fm, _body = parse_frontmatter(uri)
        GuidanceModel(**fm)
        return fm

    def compile(self, element: dict) -> None:
        path_uri = element.get("uri", "")
        if not path_uri:
            raise ValueError("element has no uri")
        fm = {k: v for k, v in element.items() if k != "uri"}
        write_frontmatter(path_uri, fm)
