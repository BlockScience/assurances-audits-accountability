---
type: edge/has-skill
source: v:student:compositional-learner
target: v:skill:composing-typed-simplicial-complexes
source_type: vertex/student
target_type: vertex/skill
orientation: directed
id: e:has-skill:compositional-learner:composing-typed-simplicial-complexes
name: compositional-learner has-skill composing-typed-simplicial-complexes
description: Edge representing that compositional-learner students possess the composing-typed-simplicial-complexes skill (newly acquired from Module 3)
tags:
  - edge
  - has-skill
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# compositional-learner has-skill composing-typed-simplicial-complexes

## Purpose

This edge represents that students in the compositional-learner state possess the composing-typed-simplicial-complexes skill, acquired by completing Module 3. This is the new skill that distinguishes compositional-learner from intermediate-learner.

## Source

**Vertex:** [[v:student:compositional-learner]]

**Type:** student

**Role:** The student state after completing Module 3

## Target

**Vertex:** [[v:skill:composing-typed-simplicial-complexes]]

**Type:** skill

**Role:** The composition skill developed in Module 3 through identification/pasting operations

## Relationship Semantics

This has-skill edge indicates that compositional-learner students possess the ability to:

- Identify shared elements across multiple charts
- Perform set union operations while avoiding duplication
- Verify type consistency across composition boundaries
- Calculate topology for composed structures
- Create composite charts from modular components

This skill is:

- Developed in Module 3
- The distinguishing skill of the compositional-learner state
- Foundational for modular chart design and advanced compositional reasoning

## Type Constraints

- **Source type:** MUST be `student`
- **Target type:** MUST be `skill`
- **Semantic constraint:** Source student must have completed Module 3

## Related Edges

- [[e:develops-skill:composing-typed-simplicial-complexes:composing-typed-simplicial-complexes]] - The module that develops this skill
- [[e:transitions-to:intermediate-learner:compositional-learner]] - The state transition that enables skill acquisition

---

**Note:** This edge participates in the skill-gain face showing that Module 3 completion causes acquisition of the composition skill.
