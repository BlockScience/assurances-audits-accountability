---
type: edge/transitions-to
source: v:student:assurance-learner
target: v:student:document-architect
source_type: vertex/student
target_type: vertex/student
orientation: directed
id: e:transitions-to:assurance-learner:document-architect
name: assurance-learner transitions-to document-architect
description: Edge representing student state transition from assurance-learner to document-architect through Module 06 or Module 07 completion
tags:
  - edge
  - transitions-to
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# assurance-learner transitions-to document-architect

## Purpose

This edge represents the student state transition from assurance-learner to document-architect, which occurs upon successful completion of Module 06 (document-composition) OR Module 07 (reference-reuse). This is the convergence point where two parallel paths merge.

## Source

**Vertex:** [[v:student:assurance-learner]]

**Type:** student

**Role:** The student state before advanced modules (fork point), possessing 4 skills

## Target

**Vertex:** [[v:student:document-architect]]

**Type:** student

**Role:** The final student state after completing advanced module(s), possessing 5-7 skills

## Relationship Semantics

This transitions-to edge represents a discrete learning state change. The transition is characterized by:

**Entry state (assurance-learner):**
- Skills: {simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation, assurance-audits}
- Cardinality: 4 skills
- Optional: +composing-typed-simplicial-complexes if Module 03 taken (5 skills)

**Exit state (document-architect):**
- Skills: 4 core skills + at least one of {document-composition, reference-reuse}
- Cardinality: 5-7 skills depending on path taken
- Path 1 (Module 06): +composing-typed-simplicial-complexes, +document-composition (6 skills)
- Path 2 (Module 07): +reference-reuse (5 skills)
- Both paths: +composing-typed-simplicial-complexes, +document-composition, +reference-reuse (7 skills)

**Supermodular constraint satisfied:** |document-architect| ≥ |assurance-learner| always

## Type Constraints

- **Source type:** MUST be `student`
- **Target type:** MUST be `student`
- **Semantic constraint:** Target must have all source skills plus at least one new skill

## Related Edges

- [[e:studies:assurance-learner:document-composition]] - Module 06 study path (requires composing skill)
- [[e:studies:assurance-learner:reference-reuse]] - Module 07 study path (assurance-audits only)
- [[e:advances:document-composition:document-architect]] - Module 06 causes advancement
- [[e:advances:reference-reuse:document-architect]] - Module 07 causes advancement

---

**Note:** This edge participates in completion faces from BOTH Module 06 and Module 07, as both modules advance students to the same terminal state (convergence point).
