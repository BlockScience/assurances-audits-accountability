"""Codec for face/assurance elements."""

from __future__ import annotations
from typing import Literal
from .base import AAABaseModel, parse_frontmatter, write_frontmatter


class AssuranceModel(AAABaseModel):
    """
    Pydantic model for face/assurance.

    Assurance faces are metadata aggregators: they roll up key facts from
    the three boundary edges (verification, validation, DocType) into a
    single addressable record, enabling audit without dereferencing docs.

    SHACL (in the RDF graph) additionally validates that doc_name and
    signed_by are consistent with the actual boundary element attributes.
    """
    edges: list[str]          # exactly 3 edge IDs forming the boundary
    doc_name: str             # name of the document being assured
    signed_by: str            # party who signed the validation
    status: Literal["assured", "pending", "failed"]
    validation_date: str | None = None
    verification_date: str | None = None

    def model_post_init(self, __context: object) -> None:
        if len(self.edges) != 3:
            raise ValueError(
                f"assurance face must have exactly 3 boundary edges, got {len(self.edges)}"
            )


class AssuranceCodec:
    def decompile(self, uri: str) -> dict:
        fm, _body = parse_frontmatter(uri)
        AssuranceModel(**fm)
        return fm

    def compile(self, element: dict) -> None:
        path_uri = element.get("uri", "")
        if not path_uri:
            raise ValueError("element has no uri")
        fm = {k: v for k, v in element.items() if k != "uri"}
        write_frontmatter(path_uri, fm)
