---
type: edge/dependency
extends: edge
id: e:dependency:program-memo-digital-transformation:program-plan-digital-transformation
name: Dependency - Program Memo requires Program Plan
description: Program memo depends on program plan for Execution Summary section
source: v:doc:program-memo-digital-transformation
target: v:doc:program-plan-digital-transformation
source_type: vertex/doc
target_type: vertex/doc
orientation: directed
dependency_type: execution_source
required: true
tags:
  - edge
  - dependency
  - program-development
version: 1.0.0
created: 2026-01-05T12:00:00Z
modified: 2026-01-05T12:00:00Z
---

# Dependency - Program Memo requires Program Plan

**The program memo for digital transformation depends on the program plan for the Execution Summary section.**

## Dependency Relationship

**Dependent:** `v:doc:program-memo-digital-transformation` (Program Memo - Digital Transformation Program)
**Dependency:** `v:doc:program-plan-digital-transformation` (Program Plan - Digital Transformation Program)
**Relationship:** Program memo requires program plan (execution source)

**Usage:** The program memo's Execution Summary section synthesizes timeline, resources, and top risks from the program plan document.

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Field/Subsection** | `program_plan_ref` in program memo metadata |
| **Required** | Yes - program plan MUST exist before program memo |
| **Cardinality** | One program plan per program memo document |

### Consistency Checks Enabled

| Check | Description |
|-------|-------------|
| C1.1 | Timeline milestones must match program plan milestones |
| C1.2 | Resource summary must align with program plan budget |
| C1.3 | Top risks must be selected from program plan risk register |

---

**Note:** This dependency is part of the program development documentation chain: Field Survey → Architecture → Lifecycle → Program Plan → Program Memo.
