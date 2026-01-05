---
type: edge/dependency
extends: edge
id: e:dependency:program-memo-digital-transformation:field-survey-digital-transformation
name: Dependency - Program Memo requires Field Survey
description: Program memo depends on field survey for context and stakeholder information
source: v:doc:program-memo-digital-transformation
target: v:doc:field-survey-digital-transformation
source_type: vertex/doc
target_type: vertex/doc
orientation: directed
dependency_type: contextual_source
required: true
tags:
  - edge
  - dependency
  - program-development
version: 1.0.0
created: 2026-01-05T12:00:00Z
modified: 2026-01-05T12:00:00Z
---

# Dependency - Program Memo requires Field Survey

**The program memo for digital transformation depends on the field survey for context and stakeholder information.**

## Dependency Relationship

**Dependent:** `v:doc:program-memo-digital-transformation` (Program Memo - Digital Transformation Program)
**Dependency:** `v:doc:field-survey-digital-transformation` (Field Survey - Digital Transformation Program)
**Relationship:** Program memo requires field survey (contextual source)

**Usage:** The program memo's Program Overview section draws context from the field survey, including problem statement drivers, stakeholder identification, and current state assessment.

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Field/Subsection** | `field_survey_ref` in program memo metadata |
| **Required** | Yes - field survey MUST exist before program memo |
| **Cardinality** | One field survey per program memo document |

### Consistency Checks Enabled

| Check | Description |
|-------|-------------|
| C1.1 | Problem statement must align with field survey pain points |
| C1.2 | Stakeholder references must be traceable to field survey actors |
| C1.3 | Constraints mentioned must reflect field survey constraints |

---

**Note:** This dependency is part of the program development documentation chain: Field Survey → Architecture → Lifecycle → Program Plan → Program Memo.
