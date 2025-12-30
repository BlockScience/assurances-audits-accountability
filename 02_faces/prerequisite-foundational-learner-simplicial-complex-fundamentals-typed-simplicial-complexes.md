---
type: face/prerequisite
vertices:
  - v:student:foundational-learner
  - v:skill:simplicial-complex-fundamentals
  - v:learning-module:typed-simplicial-complexes
edges:
  - e:has-skill:foundational-learner:simplicial-complex-fundamentals
  - e:requires-skill:typed-simplicial-complexes:simplicial-complex-fundamentals
  - e:studies:foundational-learner:typed-simplicial-complexes
orientation: oriented
id: f:prerequisite:foundational-learner:simplicial-complex-fundamentals:typed-simplicial-complexes
name: Prerequisite triangle - foundational-learner with simplicial-complex-fundamentals for typed-simplicial-complexes
description: foundational-learner possessing simplicial-complex-fundamentals can study typed-simplicial-complexes which requires that skill
tags:
  - face
  - prerequisite
  - triangle
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Prerequisite Triangle: foundational-learner with simplicial-complex-fundamentals for typed-simplicial-complexes

Validates that student has prerequisite skill for Module 2.

**Boundary edges:**
1. has-skill: foundational-learner → simplicial-complex-fundamentals
2. requires-skill: typed-simplicial-complexes → simplicial-complex-fundamentals
3. studies: foundational-learner → typed-simplicial-complexes

**Validation:** Student has required foundational topology skill ✓
