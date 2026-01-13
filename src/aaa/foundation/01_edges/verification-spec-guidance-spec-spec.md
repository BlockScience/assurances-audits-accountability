---
type: edge/verification
extends: edge
id: e:verification:spec-guidance:spec-spec
name: Verification - spec-for-guidance against spec-for-spec
description: Spec-for-guidance verifies structural compliance against spec-for-spec
source: v:spec:guidance
target: v:spec:spec
source_type: vertex/spec
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

# Verification - spec-for-guidance against spec-for-spec

This verification edge establishes that spec-for-guidance (SG) verifies its structural compliance against spec-for-spec (SS).

## Verification Relationship

**Source:** `v:spec:guidance` (SG - the document being verified)
**Target:** `v:spec:spec` (SS - the specification it verifies against)

SG is a specification document, so it must verify against the specification for specifications (SS).

## Genesis Context

This verification edge is part of the genesis infrastructure:

- Created at system initialization
- Part of b2:spec-guidance boundary face
- Enables SG to achieve genesis assurance status

## Verification Output

```text
Verification Result: PASS

Checked against: v:spec:spec (Specification for Specifications)
Document: v:spec:guidance (Specification for Guidance Documents)

Required Fields:
✓ type: vertex/spec
✓ extends: doc
✓ id: v:spec:guidance
✓ name: present
✓ tags: [vertex, doc, spec]
✓ version: present
✓ created: present
✓ modified: present

Required Body Sections:
✓ Purpose
✓ Required Frontmatter Fields
✓ Required Body Sections

All structural requirements satisfied.
```

## Verification Status

- **Status:** Pass
- **Date:** 2025-12-27T22:00:00Z
- **Tool:** genesis-verification v1.0.0

## Verification Checks

SS requires specifications to have:

- Purpose section
- Required fields table
- Schema definition
- Validation rules
- Examples

SG conforms to all these requirements as a valid specification document.
