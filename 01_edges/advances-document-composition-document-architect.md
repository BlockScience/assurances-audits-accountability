---
type: edge/advances
source: v:learning-module:document-composition
target: v:student:document-architect
source_type: vertex/learning-module
target_type: vertex/student
orientation: directed
id: e:advances:document-composition:document-architect
name: document-composition advances document-architect
description: Edge representing that Module 06 advances students to the document-architect state
tags:
  - edge
  - advances
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# document-composition advances document-architect

## Purpose

This edge represents that Module 06 advances students to the document-architect state. Successful completion of this module causes the state transition from assurance-learner to document-architect (one of two paths to this terminal state).

## Source

**Vertex:** [[v:learning-module:document-composition]]

**Type:** learning-module

**Role:** Module 06, which teaches compositional document architecture

## Target

**Vertex:** [[v:student:document-architect]]

**Type:** student

**Role:** The final student state achieved after completing advanced module (convergence point)

## Relationship Semantics

This advances edge indicates that Module 06 causes student advancement to the document-architect state. Upon completion, students:

- Acquire the document-composition skill
- Transition from 4-5 skill state to 5-6 skill state
- Understand compositional document architecture with systematic assurance
- Reach terminal state (can also take Module 07 for complete skill set)

## Type Constraints

- **Source type:** MUST be `learning-module`
- **Target type:** MUST be `student`
- **Semantic constraint:** Target student state must include the skill developed by source module

## Related Edges

- [[e:develops-skill:document-composition:document-composition]] - The skill developed that enables advancement
- [[e:transitions-to:assurance-learner:document-architect]] - The state transition caused by this module (shared with Module 07)
- [[e:studies:assurance-learner:document-composition]] - Student engagement with the module

---

**Note:** This edge participates in the completion face that encodes the causal relationship between Module 06 completion and state advancement. The document-architect state is a convergence point where Module 06 and Module 07 paths merge.
