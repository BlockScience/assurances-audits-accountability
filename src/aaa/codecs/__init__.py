"""
AAA Codec registry.

Each AAA element type has a Pydantic-backed Codec that handles:
  decompile(uri) -> dict   — parse YAML frontmatter + validate with Pydantic
  compile(element) -> None — write attrs back to frontmatter

Unknown types fall back to DocCodec (graceful degradation during migration).
"""

from .assurance import AssuranceCodec, AssuranceModel
from .chart import ChartCodec, ChartModel
from .doc import DocCodec, DocModel
from .doctype import DocTypeCodec, DocTypeModel
from .guidance import GuidanceCodec, GuidanceModel
from .spec import SpecCodec, SpecModel
from .validation import ValidationCodec, ValidationModel
from .verification import VerificationCodec, VerificationModel

# Map canonical type strings (as they appear in YAML frontmatter) to Codec instances.
# Accepts both short names and full "vertex/<type>" / "edge/<type>" / "face/<type>" forms.
_CODEC_MAP: dict[str, object] = {
    # Vertices
    "doc": DocCodec(),
    "vertex/doc": DocCodec(),
    "spec": SpecCodec(),
    "vertex/spec": SpecCodec(),
    "guidance": GuidanceCodec(),
    "vertex/guidance": GuidanceCodec(),
    "chart": ChartCodec(),
    "vertex/chart": ChartCodec(),
    "assurance_audit": ChartCodec(),
    "vertex/assurance_audit": ChartCodec(),
    # Edges
    "coupling": DocCodec(),
    "edge/coupling": DocCodec(),
    "verification": VerificationCodec(),
    "edge/verification": VerificationCodec(),
    "validation": ValidationCodec(),
    "edge/validation": ValidationCodec(),
    "doctype": DocTypeCodec(),
    "DocType": DocTypeCodec(),
    "edge/doctype": DocTypeCodec(),
    "edge/DocType": DocTypeCodec(),
    # Faces
    "assurance": AssuranceCodec(),
    "face/assurance": AssuranceCodec(),
}

_FALLBACK = DocCodec()


def codec_for_type(type_name: str):
    """Return the Codec for the given type name.  Falls back to DocCodec."""
    return _CODEC_MAP.get(type_name, _FALLBACK)


# Short type name → KC dimension, for routing to add_vertex/add_edge/add_face
_VERTEX_TYPES = {
    "doc",
    "vertex/doc",
    "spec",
    "vertex/spec",
    "guidance",
    "vertex/guidance",
    "chart",
    "vertex/chart",
    "assurance_audit",
    "vertex/assurance_audit",
}
_EDGE_TYPES = {
    "coupling",
    "edge/coupling",
    "verification",
    "edge/verification",
    "validation",
    "edge/validation",
    "doctype",
    "edge/doctype",
    "DocType",
    "edge/DocType",
}
_FACE_TYPES = {
    "assurance",
    "face/assurance",
}


def dimension_for_type(type_name: str) -> str:
    """Return 'vertex', 'edge', or 'face' for the given type name."""
    if type_name in _VERTEX_TYPES:
        return "vertex"
    if type_name in _EDGE_TYPES:
        return "edge"
    if type_name in _FACE_TYPES:
        return "face"
    # Infer from prefix
    if type_name.startswith("vertex/"):
        return "vertex"
    if type_name.startswith("edge/"):
        return "edge"
    if type_name.startswith("face/"):
        return "face"
    # Default: treat as vertex
    return "vertex"


def short_type(type_name: str) -> str:
    """Strip 'vertex/', 'edge/', 'face/' prefix to get the KC type name."""
    for prefix in ("vertex/", "edge/", "face/"):
        if type_name.startswith(prefix):
            return type_name[len(prefix) :]
    return type_name


__all__ = [
    "DocCodec",
    "DocModel",
    "SpecCodec",
    "SpecModel",
    "GuidanceCodec",
    "GuidanceModel",
    "ChartCodec",
    "ChartModel",
    "VerificationCodec",
    "VerificationModel",
    "ValidationCodec",
    "ValidationModel",
    "DocTypeCodec",
    "DocTypeModel",
    "AssuranceCodec",
    "AssuranceModel",
    "codec_for_type",
    "dimension_for_type",
    "short_type",
]
