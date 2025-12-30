---
type: face/prerequisite
vertices:
  - v:student:verification-learner
  - v:skill:verification-validation
  - v:learning-module:assurance-audits
edges:
  - e:has-skill:verification-learner:verification-validation
  - e:requires-skill:assurance-audits:verification-validation
  - e:studies:verification-learner:assurance-audits
orientation: oriented
id: f:prerequisite:verification-learner:verification-validation:assurance-audits
name: Prerequisite triangle - verification-learner with verification-validation for assurance-audits
description: verification-learner possessing verification-validation can study assurance-audits which requires that skill
tags:
  - face
  - prerequisite
  - triangle
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Prerequisite Triangle: verification-learner with verification-validation for assurance-audits

Validates that student has prerequisite skill for Module 05.

**Boundary edges:**
1. has-skill: verification-learner → verification-validation
2. requires-skill: assurance-audits → verification-validation
3. studies: verification-learner → assurance-audits

**Validation:** Student has required quality assurance skill ✓
