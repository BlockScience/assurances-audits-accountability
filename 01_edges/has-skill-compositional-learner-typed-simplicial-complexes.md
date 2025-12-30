---
type: edge/has-skill
source: v:student:compositional-learner
target: v:skill:typed-simplicial-complexes
source_type: vertex/student
target_type: vertex/skill
orientation: directed
id: e:has-skill:compositional-learner:typed-simplicial-complexes
name: compositional-learner has-skill typed-simplicial-complexes
description: Edge representing that compositional-learner students possess the typed-simplicial-complexes skill (carried over from intermediate-learner state)
tags:
  - edge
  - has-skill
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# compositional-learner has-skill typed-simplicial-complexes

## Purpose

This edge represents that students in the compositional-learner state possess the typed-simplicial-complexes skill, acquired in Module 2 and carried forward through Module 3. This demonstrates skill preservation through state transitions.

## Source

**Vertex:** [[v:student:compositional-learner]]

**Type:** student

**Role:** The student state after completing Modules 1, 2, and 3

## Target

**Vertex:** [[v:skill:typed-simplicial-complexes]]

**Type:** skill

**Role:** The typing skill from Module 2, preserved in compositional-learner state

## Relationship Semantics

This has-skill edge indicates that compositional-learner students retain the ability to work with typed simplicial complexes (semantic types, type constraints, validation). This skill is:

- Developed in Module 2
- Required for Module 3 (type consistency validation during composition)
- Preserved in compositional-learner state
- Foundational for advanced verification and assurance work

## Type Constraints

- **Source type:** MUST be `student`
- **Target type:** MUST be `skill`
- **Semantic constraint:** Source student must have completed Module 2 (directly or transitively)

## Related Edges

- [[e:develops-skill:typed-simplicial-complexes:typed-simplicial-complexes]] - The module that developed this skill
- [[e:has-skill:intermediate-learner:typed-simplicial-complexes]] - First acquisition of this skill
- [[e:has-skill:compositional-learner:typed-simplicial-complexes]] - Skill carried forward

---

**Note:** This edge demonstrates skill accumulation: compositional-learner has 3 skills (fundamentals + typing + composition).
