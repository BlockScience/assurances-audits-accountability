---
type: edge/advances
source: v:learning-module:verification-validation
target: v:student:verification-learner
source_type: vertex/learning-module
target_type: vertex/student
orientation: directed
id: e:advances:verification-validation:verification-learner
name: verification-validation advances verification-learner
description: Edge representing that Module 04 advances students to the verification-learner state
tags:
  - edge
  - advances
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# verification-validation advances verification-learner

## Purpose

This edge represents that Module 04 advances students to the verification-learner state. Successful completion of this module causes the state transition from intermediate-learner to verification-learner.

## Source

**Vertex:** [[v:learning-module:verification-validation]]

**Type:** learning-module

**Role:** Module 04, which teaches quality assurance fundamentals

## Target

**Vertex:** [[v:student:verification-learner]]

**Type:** student

**Role:** The student state achieved after completing Module 04

## Relationship Semantics

This advances edge indicates that Module 04 causes student advancement to the verification-learner state. Upon completion, students:

- Acquire the verification-validation skill
- Transition from 2-skill state to 3-skill state
- Understand structural verification and qualitative validation
- Become ready for assurance network construction (Module 05)

## Type Constraints

- **Source type:** MUST be `learning-module`
- **Target type:** MUST be `student`
- **Semantic constraint:** Target student state must include the skill developed by source module

## Related Edges

- [[e:develops-skill:verification-validation:verification-validation]] - The skill developed that enables advancement
- [[e:transitions-to:intermediate-learner:verification-learner]] - The state transition caused by this module
- [[e:studies:intermediate-learner:verification-validation]] - Student engagement with the module

---

**Note:** This edge participates in the completion face that encodes the causal relationship between module completion and state advancement.
