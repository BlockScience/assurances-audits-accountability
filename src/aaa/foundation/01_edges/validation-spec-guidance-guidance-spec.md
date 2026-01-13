---
type: edge/validation
extends: edge
id: e:validation:spec-guidance:guidance-spec
name: Validation - spec-for-guidance against guidance-for-spec
description: Spec-for-guidance validates quality against guidance-for-spec
source: v:spec:guidance
target: v:guidance:spec
source_type: vertex/spec
target_type: vertex/guidance
orientation: directed
tags:
  - edge
  - validation
  - genesis
version: 1.0.0
created: 2025-12-27T22:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Validation - spec-for-guidance against guidance-for-spec

This validation edge establishes that spec-for-guidance (SG) validates its quality against guidance-for-spec (GS).

## Validation Relationship

**Source:** `v:spec:guidance` (SG - the document being validated)
**Target:** `v:guidance:spec` (GS - the guidance it validates against)

SG is a specification document, so it must validate against the guidance for specifications (GS).

## Genesis Context

This validation edge is part of the genesis infrastructure:

- Created at system initialization
- Part of b2:spec-guidance boundary face
- Enables SG to achieve genesis assurance status

## Quality Assessment

GS assesses specifications for:

- Clarity of purpose
- Completeness of requirements
- Testability of schema
- Consistency of rules
- Quality of examples

SG meets all these quality criteria as a well-formed specification document.
