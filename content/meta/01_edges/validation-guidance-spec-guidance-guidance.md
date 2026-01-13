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
validation_method: manual
validator: genesis-system
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

## Validation Assessment

**Guidance:** [[guidance-for-guidance|v:guidance:guidance]]
**Validator:** genesis-system
**Method:** Manual
**Date:** 2025-12-27T22:00:00Z

### Quality Criteria Evaluation

#### Empathy and Clarity

**Level:** Excellent
**Rationale:** GS clearly communicates with its intended audience (specification authors) and provides actionable guidance.
**Evidence:** Quality criteria are written from the perspective of helping authors succeed.

#### Actionability of Advice

**Level:** Excellent
**Rationale:** Each quality criterion includes specific, actionable recommendations.
**Evidence:** Section-by-section guidance provides concrete steps for improvement.

#### Comprehensiveness of Criteria

**Level:** Good
**Rationale:** Covers the key aspects of specification quality with appropriate depth.
**Evidence:** Five quality criteria address purpose, completeness, testability, consistency, and examples.

#### Usability of Workflow

**Level:** Good
**Rationale:** The guidance can be followed as a checklist during specification authoring.
**Evidence:** Workflow guidance section provides a clear sequence of activities.

#### Specificity of Practices

**Level:** Good
**Rationale:** Practices are specific enough to apply consistently across specifications.
**Evidence:** Leveled assessment provides clear distinctions between quality levels.

### Overall Assessment

**Recommendation:** Pass
**Summary:** Guidance-for-spec meets all quality criteria established by guidance-for-guidance. It is a well-formed guidance document that provides valuable assistance to specification authors.

### Strengths

- Clear quality criteria with specific examples
- Empathetic tone that guides rather than criticizes
- Actionable workflow recommendations

### Areas for Improvement

- Could provide more templates for common specification patterns

## Accountability Statement

This validation was performed during genesis initialization. The assessment represents the foundational quality baseline for guidance documents.

**Signed:** genesis-system
**Date:** 2025-12-27T22:00:00Z
