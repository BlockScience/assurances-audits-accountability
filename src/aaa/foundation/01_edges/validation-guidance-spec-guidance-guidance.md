---
type: edge/validation
extends: edge
id: e:validation:guidance-spec:guidance-guidance
name: Validation - guidance-for-spec against guidance-for-guidance
description: Guidance-for-spec validates quality against guidance-for-guidance
source: v:guidance:spec
target: v:guidance:guidance
source_type: vertex/guidance
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

# Validation - guidance-for-spec against guidance-for-guidance

This validation edge establishes that guidance-for-spec (GS) validates its quality against guidance-for-guidance (GG).

## Validation Relationship

**Source:** `v:guidance:spec` (GS - the document being validated)
**Target:** `v:guidance:guidance` (GG - the guidance it validates against)

GS is a guidance document, so it must validate against the guidance for guidance documents (GG).

## Genesis Context

This validation edge is part of the genesis infrastructure:

- Created at system initialization
- Part of b2:guidance-spec boundary face
- Enables GS to achieve genesis assurance status

## Quality Assessment

GG assesses guidance documents for:

- Empathy and clarity
- Actionability of advice
- Comprehensiveness of criteria
- Usability of workflow
- Specificity of practices

GS meets all these quality criteria as a well-formed guidance document.
