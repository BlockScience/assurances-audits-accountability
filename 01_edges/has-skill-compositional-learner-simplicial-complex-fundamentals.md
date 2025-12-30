---
type: edge/has-skill
source: v:student:compositional-learner
target: v:skill:simplicial-complex-fundamentals
source_type: vertex/student
target_type: vertex/skill
orientation: directed
id: e:has-skill:compositional-learner:simplicial-complex-fundamentals
name: compositional-learner has-skill simplicial-complex-fundamentals
description: Edge representing that compositional-learner students possess the simplicial-complex-fundamentals skill (carried over from previous states)
tags:
  - edge
  - has-skill
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# compositional-learner has-skill simplicial-complex-fundamentals

## Purpose

This edge represents that students in the compositional-learner state possess the simplicial-complex-fundamentals skill, originally acquired in Module 1 and carried forward through all subsequent learning states. This demonstrates supermodular skill accumulation.

## Source

**Vertex:** [[v:student:compositional-learner]]

**Type:** student

**Role:** The student state after completing Modules 1, 2, and 3

## Target

**Vertex:** [[v:skill:simplicial-complex-fundamentals]]

**Type:** skill

**Role:** The foundational skill from Module 1, preserved through all state transitions

## Relationship Semantics

This has-skill edge indicates that compositional-learner students retain the fundamental skill of understanding vertices, edges, faces, and the Euler characteristic. This skill is:

- Developed in Module 1
- Preserved through intermediate-learner state (Module 2 transition)
- Preserved through compositional-learner state (Module 3 transition)
- Foundational for all subsequent advanced work

## Type Constraints

- **Source type:** MUST be `student`
- **Target type:** MUST be `skill`
- **Semantic constraint:** Source student must have completed Module 1 (directly or transitively)

## Related Edges

- [[e:develops-skill:simplicial-complex-fundamentals:simplicial-complex-fundamentals]] - The module that originally developed this skill
- [[e:has-skill:foundational-learner:simplicial-complex-fundamentals]] - First acquisition of this skill
- [[e:has-skill:intermediate-learner:simplicial-complex-fundamentals]] - Skill carried to intermediate state
- [[e:has-skill:compositional-learner:simplicial-complex-fundamentals]] - Skill carried to compositional state

---

**Note:** This edge demonstrates the supermodular constraint: skills accumulate and are never lost through state transitions.
