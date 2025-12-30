---
type: face/prerequisite
vertices:
  - v:student:assurance-learner
  - v:skill:assurance-audits
  - v:learning-module:document-composition
edges:
  - e:has-skill:assurance-learner:assurance-audits
  - e:requires-skill:document-composition:assurance-audits
  - e:studies:assurance-learner:document-composition
orientation: oriented
id: f:prerequisite:assurance-learner:assurance-audits:document-composition
name: Prerequisite triangle - assurance-learner with assurance-audits for document-composition
description: assurance-learner possessing assurance-audits can study document-composition which requires that skill (prerequisite 1 of 2)
tags:
  - face
  - prerequisite
  - triangle
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Prerequisite Triangle: assurance-learner with assurance-audits for document-composition

Validates that student has first prerequisite skill for Module 06 (dual prerequisites required).

**Boundary edges:**
1. has-skill: assurance-learner → assurance-audits
2. requires-skill: document-composition → assurance-audits
3. studies: assurance-learner → document-composition

**Validation:** Student has required assurance network skill ✓ (prerequisite 1 of 2)
