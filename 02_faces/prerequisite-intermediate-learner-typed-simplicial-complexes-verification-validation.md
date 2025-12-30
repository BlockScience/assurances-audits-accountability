---
type: face/prerequisite
vertices:
  - v:student:intermediate-learner
  - v:skill:typed-simplicial-complexes
  - v:learning-module:verification-validation
edges:
  - e:has-skill:intermediate-learner:typed-simplicial-complexes
  - e:requires-skill:verification-validation:typed-simplicial-complexes
  - e:studies:intermediate-learner:verification-validation
orientation: oriented
id: f:prerequisite:intermediate-learner:typed-simplicial-complexes:verification-validation
name: Prerequisite triangle - intermediate-learner with typed-simplicial-complexes for verification-validation
description: intermediate-learner possessing typed-simplicial-complexes can study verification-validation which requires that skill
tags:
  - face
  - prerequisite
  - triangle
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Prerequisite Triangle: intermediate-learner with typed-simplicial-complexes for verification-validation

Validates that student has prerequisite skill for Module 04.

**Boundary edges:**
1. has-skill: intermediate-learner → typed-simplicial-complexes
2. requires-skill: verification-validation → typed-simplicial-complexes
3. studies: intermediate-learner → verification-validation

**Validation:** Student has required type system skill ✓
