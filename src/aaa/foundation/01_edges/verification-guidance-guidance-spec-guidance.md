---
type: edge/verification
extends: edge
id: e:verification:guidance-guidance:spec-guidance
name: Verification - guidance-for-guidance against spec-for-guidance
description: Guidance-for-guidance verifies structural compliance against spec-for-guidance
source: v:guidance:guidance
target: v:spec:guidance
source_type: vertex/guidance
target_type: vertex/spec
orientation: directed
tags:
  - edge
  - verification
  - genesis
version: 1.0.0
created: 2025-12-27T22:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Verification - guidance-for-guidance against spec-for-guidance

This verification edge establishes that guidance-for-guidance (GG) verifies its structural compliance against spec-for-guidance (SG).

## Verification Relationship

**Source:** `v:guidance:guidance` (GG - the document being verified)
**Target:** `v:spec:guidance` (SG - the specification it verifies against)

GG is a guidance document, so it must verify against the specification for guidance documents (SG).

## Genesis Context

This verification edge is part of the genesis infrastructure:

- Created at system initialization
- Part of b2:guidance-guidance boundary face
- Enables GG to achieve genesis assurance status

## Verification Output

```text
Verification Result: PASS

Checked against: v:spec:guidance (Specification for Guidance Documents)
Document: v:guidance:guidance (Guidance for Guidance Documents)

Required Fields:
✓ type: vertex/guidance
✓ extends: doc
✓ id: v:guidance:guidance
✓ name: present
✓ tags: [vertex, doc, guidance]
✓ version: present
✓ created: present
✓ modified: present

Required Body Sections:
✓ Purpose
✓ Quality Criteria (5 criteria found)
✓ Leveled Assessment
✓ Section-by-Section Guidance
✓ Workflow Guidance

All structural requirements satisfied.
```

## Verification Status

- **Status:** Pass
- **Date:** 2025-12-27T22:00:00Z
- **Tool:** genesis-verification v1.0.0

## Verification Checks

SG requires guidance documents to have:

- Purpose section
- Quality criteria (minimum 3)
- Leveled assessment
- Section-by-section guidance
- Workflow guidance

GG conforms to all these requirements as a valid guidance document.
