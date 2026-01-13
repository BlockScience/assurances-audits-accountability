---
type: face/signature
extends: face
id: f:signature:guidance-ontology
name: Signature Face - guidance-for-ontology
description: Admin signature for guidance-for-ontology validation
vertices:
  - v:guidance:ontology
  - v:guidance:guidance
  - v:signer:admin
doc: v:guidance:ontology
guidance: v:guidance:guidance
signer: v:signer:admin
edges:
  - e:validation:guidance-ontology:guidance-guidance
  - e:qualifies:admin:guidance-guidance
  - e:signs:admin:guidance-ontology
validation_edge: e:validation:guidance-ontology:guidance-guidance
qualifies_edge: e:qualifies:admin:guidance-guidance
signs_edge: e:signs:admin:guidance-ontology
signing_date: 2026-01-13T00:00:00Z
commit_hash: foundation
assurance_face: f:assurance:guidance-ontology
orientation: oriented
tags:
  - face
  - signature
  - foundation
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Signature Face - guidance-for-ontology

This is a **signature face** providing accountability for the guidance-for-ontology validation.

## Face Structure

**Vertices:**
1. `v:guidance:ontology` - The document being validated
2. `v:guidance:guidance` - The quality criteria
3. `v:signer:admin` - The qualified validator

**Edges:**
1. `e:validation:guidance-ontology:guidance-guidance` - SHARED with assurance face
2. `e:qualifies:admin:guidance-guidance` - SHARED with authorization face
3. `e:signs:admin:guidance-ontology` - The signature attestation

## Accountability Chain

This signature face shares:
- The validation edge with `f:assurance:guidance-ontology`
- The qualifies edge with `f:authorization:admin:guidance-guidance`

This creates complete accountability linking human approval to document assurance.
