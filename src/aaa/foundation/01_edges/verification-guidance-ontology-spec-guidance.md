---
type: edge/verification
extends: edge
id: e:verification:guidance-ontology:spec-guidance
name: Verification - guidance-for-ontology against spec-for-guidance
description: Guidance-for-ontology verifies structural compliance against spec-for-guidance
source: v:guidance:ontology
target: v:spec:guidance
source_type: vertex/guidance
target_type: vertex/spec
orientation: directed
tags:
  - edge
  - verification
  - foundation
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Verification - guidance-for-ontology against spec-for-guidance

This verification edge establishes that guidance-for-ontology verifies its structural compliance against spec-for-guidance.

## Verification Relationship

**Source:** `v:guidance:ontology` (the document being verified)
**Target:** `v:spec:guidance` (the specification it verifies against)

Guidance-for-ontology is a guidance document, so it must verify against the specification for guidance (SG).

## Verification Output

```text
Verification Result: PASS

Checked against: v:spec:guidance (Specification for Guidance Documents)
Document: v:guidance:ontology (Guidance for Ontology Documents)

Required Fields:
✓ type: vertex/guidance
✓ extends: doc
✓ id: v:guidance:ontology
✓ name: present
✓ tags: [vertex, doc, guidance]
✓ version: present
✓ created: present
✓ modified: present

Required Body Sections:
✓ Purpose
✓ Quality Criteria (8 criteria found)
✓ Leveled Assessment
✓ Section-by-Section Guidance
✓ Workflow Guidance

All structural requirements satisfied.
```

## Verification Status

- **Status:** Pass
- **Date:** 2026-01-13T00:00:00Z
- **Tool:** genesis-verification v1.0.0

## Verification Checks

SG requires guidance documents to have:

- Purpose section
- Quality criteria (minimum 3)
- Leveled assessment
- Section-by-section guidance
- Workflow guidance

Guidance-for-ontology conforms to all these requirements.
