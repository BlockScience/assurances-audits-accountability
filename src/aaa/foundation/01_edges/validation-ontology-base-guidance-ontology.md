---
type: edge/validation
extends: edge
id: e:validation:ontology-base:guidance-ontology
name: Validation - ontology-base against guidance-for-ontology
description: Ontology-base validates against guidance-for-ontology quality criteria
source: v:ontology:base
target: v:guidance:ontology
source_type: vertex/ontology
target_type: vertex/guidance
orientation: directed
validator: genesis
validation_method: manual
tags:
  - edge
  - validation
  - foundation
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Validation - ontology-base against guidance-for-ontology

This validation edge establishes that ontology-base has been assessed against guidance-for-ontology quality criteria.

## Validation Relationship

**Source:** `v:ontology:base` (the document being validated)
**Target:** `v:guidance:ontology` (the guidance it validates against)

Ontology-base is an ontology document, so it validates against the guidance for ontology documents.

## Validation Assessment

Guidance-for-ontology criteria assess:

- Type completeness
- Coherence rules
- Extension clarity
- Type hierarchy consistency
- Documentation quality
- Local rule verifiability
- Chart design quality
- Assurance completeness

Ontology-base meets these quality criteria.

## Accountability

This validation was performed as part of foundation bootstrap. The admin signer attests to this validation through the signature face.

**Signed:** genesis
**Date:** 2026-01-13T00:00:00Z
