---
type: edge/advances
source: v:learning-module:assurance-audits
target: v:student:assurance-learner
source_type: vertex/learning-module
target_type: vertex/student
orientation: directed
id: e:advances:assurance-audits:assurance-learner
name: assurance-audits advances assurance-learner
description: Edge representing that Module 05 advances students to the assurance-learner state
tags:
  - edge
  - advances
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# assurance-audits advances assurance-learner

## Purpose

This edge represents that Module 05 advances students to the assurance-learner state. Successful completion of this module causes the state transition from verification-learner to assurance-learner.

## Source

**Vertex:** [[v:learning-module:assurance-audits]]

**Type:** learning-module

**Role:** Module 05, which teaches assurance networks and boundary complex

## Target

**Vertex:** [[v:student:assurance-learner]]

**Type:** student

**Role:** The student state achieved after completing Module 05 (fork point for advanced modules)

## Relationship Semantics

This advances edge indicates that Module 05 causes student advancement to the assurance-learner state. Upon completion, students:

- Acquire the assurance-audits skill
- Transition from 3-skill state to 4-skill state
- Understand complete assurance networks and boundary complex
- Reach fork point: can proceed to Module 06 (document-composition) or Module 07 (reference-reuse)

## Type Constraints

- **Source type:** MUST be `learning-module`
- **Target type:** MUST be `student`
- **Semantic constraint:** Target student state must include the skill developed by source module

## Related Edges

- [[e:develops-skill:assurance-audits:assurance-audits]] - The skill developed that enables advancement
- [[e:transitions-to:verification-learner:assurance-learner]] - The state transition caused by this module
- [[e:studies:verification-learner:assurance-audits]] - Student engagement with the module

---

**Note:** This edge participates in the completion face that encodes the causal relationship between module completion and state advancement. The assurance-learner state is significant as the fork point for two parallel advanced paths.
