"""Codec for edge/verification elements."""

from __future__ import annotations
from typing import Literal
from pydantic import model_validator
from .base import AAABaseModel, parse_frontmatter, write_frontmatter


_VALID_STATUS = {"passing", "failing", "pending"}


class VerificationModel(AAABaseModel):
    """Pydantic model for edge/verification."""
    source: str  # doc vertex id
    target: str  # spec vertex id
    status: Literal["passing", "failing", "pending"]

    @model_validator(mode="after")
    def source_target_differ(self) -> "VerificationModel":
        if self.source == self.target:
            raise ValueError("verification edge source and target must differ")
        return self


class VerificationCodec:
    def decompile(self, uri: str) -> dict:
        fm, _body = parse_frontmatter(uri)
        VerificationModel(**fm)
        return fm

    def compile(self, element: dict) -> None:
        path_uri = element.get("uri", "")
        if not path_uri:
            raise ValueError("element has no uri")
        fm = {k: v for k, v in element.items() if k != "uri"}
        write_frontmatter(path_uri, fm)
