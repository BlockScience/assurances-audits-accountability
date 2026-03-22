"""Codec for edge/DocType elements."""

from __future__ import annotations

from pydantic import model_validator

from .base import AAABaseModel, parse_frontmatter, write_frontmatter


class DocTypeModel(AAABaseModel):
    """
    Pydantic model for edge/DocType.

    A DocType edge connects a spec vertex to a guidance vertex and defines
    a document type. The edge itself is a first-class addressable element
    carrying data about the type (name, description, commonly_used_for).
    """

    source: str  # spec vertex id
    target: str  # guidance vertex id
    # name is inherited from AAABaseModel (required)
    commonly_used_for: str | None = None

    @model_validator(mode="after")
    def source_target_differ(self) -> DocTypeModel:
        if self.source == self.target:
            raise ValueError("DocType edge source and target must differ")
        return self


class DocTypeCodec:
    def decompile(self, uri: str) -> dict:
        fm, _body = parse_frontmatter(uri)
        DocTypeModel(**fm)
        return fm

    def compile(self, element: dict) -> None:
        path_uri = element.get("uri", "")
        if not path_uri:
            raise ValueError("element has no uri")
        fm = {k: v for k, v in element.items() if k != "uri"}
        write_frontmatter(path_uri, fm)
