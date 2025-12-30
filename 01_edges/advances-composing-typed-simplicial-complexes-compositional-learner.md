---
type: edge/advances
source: v:learning-module:composing-typed-simplicial-complexes
target: v:student:compositional-learner
source_type: vertex/learning-module
target_type: vertex/student
orientation: directed
id: e:advances:composing-typed-simplicial-complexes:compositional-learner
name: composing-typed-simplicial-complexes advances compositional-learner
description: Edge representing that Module 3 advances students to the compositional-learner state
tags:
  - edge
  - advances
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# composing-typed-simplicial-complexes advances compositional-learner

## Purpose

This edge represents that Module 3 advances students to the compositional-learner state. Successful completion of this module causes the state transition from intermediate-learner to compositional-learner.

## Source

**Vertex:** [[v:learning-module:composing-typed-simplicial-complexes]]

**Type:** learning-module

**Role:** Module 3, which teaches composition through identification

## Target

**Vertex:** [[v:student:compositional-learner]]

**Type:** student

**Role:** The student state achieved after completing Module 3

## Relationship Semantics

This advances edge indicates that Module 3 causes student advancement to the compositional-learner state. Upon completion, students:

- Acquire the composing-typed-simplicial-complexes skill
- Transition from 2-skill state to 3-skill state
- Complete the foundational trilogy of modules
- Become ready for advanced work in verification, validation, and assurance

## Type Constraints

- **Source type:** MUST be `learning-module`
- **Target type:** MUST be `student`
- **Semantic constraint:** Target student state must include the skill developed by source module

## Related Edges

- [[e:develops-skill:composing-typed-simplicial-complexes:composing-typed-simplicial-complexes]] - The skill developed that enables advancement
- [[e:transitions-to:intermediate-learner:compositional-learner]] - The state transition caused by this module
- [[e:studies:intermediate-learner:composing-typed-simplicial-complexes]] - Student engagement with the module

---

**Note:** This edge participates in the completion face that encodes the causal relationship between module completion and state advancement.
