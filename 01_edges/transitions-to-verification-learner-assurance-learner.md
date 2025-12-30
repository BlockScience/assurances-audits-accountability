---
type: edge/transitions-to
source: v:student:verification-learner
target: v:student:assurance-learner
source_type: vertex/student
target_type: vertex/student
orientation: directed
id: e:transitions-to:verification-learner:assurance-learner
name: verification-learner transitions-to assurance-learner
description: Edge representing student state transition from verification-learner to assurance-learner through Module 05 completion
tags:
  - edge
  - transitions-to
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# verification-learner transitions-to assurance-learner

## Purpose

This edge represents the student state transition from verification-learner to assurance-learner, which occurs upon successful completion of Module 05. This is the fourth state transition in the learning journey.

## Source

**Vertex:** [[v:student:verification-learner]]

**Type:** student

**Role:** The student state before Module 05, possessing 3 skills

## Target

**Vertex:** [[v:student:assurance-learner]]

**Type:** student

**Role:** The student state after Module 05, possessing 4 skills (fork point for Modules 06/07)

## Relationship Semantics

This transitions-to edge represents a discrete learning state change. The transition is characterized by:

**Entry state (verification-learner):**
- Skills: {simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation}
- Cardinality: 3 skills

**Exit state (assurance-learner):**
- Skills: {simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation, assurance-audits}
- Cardinality: 4 skills

**Supermodular constraint satisfied:** |assurance-learner| = 4 ≥ |verification-learner| = 3

## Type Constraints

- **Source type:** MUST be `student`
- **Target type:** MUST be `student`
- **Semantic constraint:** Target must have all source skills plus at least one new skill

## Related Edges

- [[e:studies:verification-learner:assurance-audits]] - The module study that enables this transition
- [[e:advances:assurance-audits:assurance-learner]] - The module that causes advancement
- [[e:has-skill:assurance-learner:assurance-audits]] - New skill acquired in target state

---

**Note:** This edge participates in the completion face that represents the Module 05 completion process and state transition. The assurance-learner state is a fork point where students can proceed to Module 06 or Module 07.
