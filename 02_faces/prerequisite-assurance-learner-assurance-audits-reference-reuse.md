---
type: face/prerequisite
vertices:
  - v:student:assurance-learner
  - v:skill:assurance-audits
  - v:learning-module:reference-reuse
edges:
  - e:has-skill:assurance-learner:assurance-audits
  - e:requires-skill:reference-reuse:assurance-audits
  - e:studies:assurance-learner:reference-reuse
orientation: oriented
id: f:prerequisite:assurance-learner:assurance-audits:reference-reuse
name: Prerequisite triangle - assurance-learner with assurance-audits for reference-reuse
description: assurance-learner possessing assurance-audits can study reference-reuse which requires that skill
tags:
  - face
  - prerequisite
  - triangle
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Prerequisite Triangle: assurance-learner with assurance-audits for reference-reuse

Validates that student has prerequisite skill for Module 07 (single prerequisite, simpler than Module 06).

**Boundary edges:**
1. has-skill: assurance-learner → assurance-audits
2. requires-skill: reference-reuse → assurance-audits
3. studies: assurance-learner → reference-reuse

**Validation:** Student has required assurance network skill ✓
