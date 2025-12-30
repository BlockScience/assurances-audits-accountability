---
type: edge/transitions-to
source: v:student:intermediate-learner
target: v:student:compositional-learner
source_type: vertex/student
target_type: vertex/student
orientation: directed
id: e:transitions-to:intermediate-learner:compositional-learner
name: intermediate-learner transitions-to compositional-learner
description: Edge representing student state transition from intermediate-learner to compositional-learner through Module 3 completion
tags:
  - edge
  - transitions-to
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# intermediate-learner transitions-to compositional-learner

## Purpose

This edge represents the student state transition from intermediate-learner to compositional-learner, which occurs upon successful completion of Module 3. This is the third state transition in the learning journey.

## Source

**Vertex:** [[v:student:intermediate-learner]]

**Type:** student

**Role:** The student state before Module 3, possessing 2 skills

## Target

**Vertex:** [[v:student:compositional-learner]]

**Type:** student

**Role:** The student state after Module 3, possessing 3 skills

## Relationship Semantics

This transitions-to edge represents a discrete learning state change. The transition is characterized by:

**Entry state (intermediate-learner):**
- Skills: {simplicial-complex-fundamentals, typed-simplicial-complexes}
- Cardinality: 2 skills

**Exit state (compositional-learner):**
- Skills: {simplicial-complex-fundamentals, typed-simplicial-complexes, composing-typed-simplicial-complexes}
- Cardinality: 3 skills

**Supermodular constraint satisfied:** |compositional-learner| = 3 ≥ |intermediate-learner| = 2

## Type Constraints

- **Source type:** MUST be `student`
- **Target type:** MUST be `student`
- **Semantic constraint:** Target must have all source skills plus at least one new skill

## Related Edges

- [[e:studies:intermediate-learner:composing-typed-simplicial-complexes]] - The module study that enables this transition
- [[e:advances:composing-typed-simplicial-complexes:compositional-learner]] - The module that causes advancement
- [[e:has-skill:compositional-learner:composing-typed-simplicial-complexes]] - New skill acquired in target state

---

**Note:** This edge participates in the completion face that represents the Module 3 completion process and state transition.
