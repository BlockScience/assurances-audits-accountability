"""Codec for edge/validation elements."""

from __future__ import annotations
from typing import Literal
from pydantic import model_validator
from .base import AAABaseModel, parse_frontmatter, write_frontmatter


class ValidationModel(AAABaseModel):
    """Pydantic model for edge/validation."""
    source: str  # doc vertex id
    target: str  # guidance vertex id
    status: Literal["approved", "rejected", "pending"]
    rationale: str | None = None
    signed_by: str | None = None

    @model_validator(mode="after")
    def source_target_differ(self) -> "ValidationModel":
        if self.source == self.target:
            raise ValueError("validation edge source and target must differ")
        return self


class ValidationCodec:
    def decompile(self, uri: str) -> dict:
        fm, _body = parse_frontmatter(uri)
        ValidationModel(**fm)
        return fm

    def compile(self, element: dict) -> None:
        path_uri = element.get("uri", "")
        if not path_uri:
            raise ValueError("element has no uri")
        fm = {k: v for k, v in element.items() if k != "uri"}
        write_frontmatter(path_uri, fm)
