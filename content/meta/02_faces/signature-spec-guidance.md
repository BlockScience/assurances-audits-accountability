---
type: face/signature
extends: face
id: f:signature:spec-guidance
name: Signature Face - spec-for-guidance
vertices:
  - v:spec:guidance
  - v:guidance:spec
  - b0:root
doc: v:spec:guidance
guidance: v:guidance:spec
signer: b0:root
edges:
  - e:validation:spec-guidance:guidance-spec
  - e:signs:root:spec-guidance
  - e:qualifies:root:guidance-spec
validation_edge: e:validation:spec-guidance:guidance-spec
signs_edge: e:signs:root:spec-guidance
qualifies_edge: e:qualifies:root:guidance-spec
signing_date: 2025-12-27T00:00:00Z
commit_hash: genesis
assurance_face: f:assurance:spec-guidance
orientation: oriented
tags:
  - face
  - signature
  - boundary-complex
version: 1.0.0
created: 2025-12-27T00:00:00Z
modified: 2025-12-30T00:00:00Z
---

# Signature Face - spec-for-guidance

Accountability triangle for spec-for-guidance assurance, signed by root.

**Signed:** root
**Date:** 2025-12-27T00:00:00Z

## Significance

This signature face establishes accountability for the foundational spec-for-guidance assurance. Root serves as the bootstrap authority that anchors the system with this assurance in place.
