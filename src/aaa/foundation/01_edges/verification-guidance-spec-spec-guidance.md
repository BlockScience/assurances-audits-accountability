---
type: edge/verification
extends: edge
id: e:verification:guidance-spec:spec-guidance
name: Verification - guidance-for-spec against spec-for-guidance
description: Guidance-for-spec verifies structural compliance against spec-for-guidance
source: v:guidance:spec
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

# Verification - guidance-for-spec against spec-for-guidance

This verification edge establishes that guidance-for-spec (GS) verifies its structural compliance against spec-for-guidance (SG).

## Verification Relationship

**Source:** `v:guidance:spec` (GS - the document being verified)
**Target:** `v:spec:guidance` (SG - the specification it verifies against)

GS is a guidance document, so it must verify against the specification for guidance documents (SG).

## Genesis Context

This verification edge is part of the genesis infrastructure:

- Created at system initialization
- Part of b2:guidance-spec boundary face
- Enables GS to achieve genesis assurance status

## Verification Checks

SG requires guidance documents to have:

- Purpose section
- Quality criteria (minimum 3)
- Leveled assessment
- Section-by-section guidance
- Workflow guidance

GS conforms to all these requirements as a valid guidance document.
