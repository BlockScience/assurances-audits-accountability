---
type: face/prerequisite
vertices:
  - v:student:knowledge-complex-learner
  - v:skill:sets-and-graphs
  - v:learning-module:simplicial-complex-fundamentals
edges:
  - e:has-skill:knowledge-complex-learner:sets-and-graphs
  - e:requires-skill:simplicial-complex-fundamentals:sets-and-graphs
  - e:studies:knowledge-complex-learner:simplicial-complex-fundamentals
orientation: oriented
id: f:prerequisite:knowledge-complex-learner:sets-and-graphs:simplicial-complex-fundamentals
name: Prerequisite triangle - knowledge-complex-learner with sets-and-graphs for simplicial-complex-fundamentals
description: knowledge-complex-learner possessing sets-and-graphs can study simplicial-complex-fundamentals which requires that skill
tags:
  - face
  - prerequisite
  - triangle
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Prerequisite Triangle: knowledge-complex-learner with sets-and-graphs for simplicial-complex-fundamentals

Validates that student has first prerequisite skill for the module.

**Boundary edges:**
1. has-skill: knowledge-complex-learner → sets-and-graphs
2. requires-skill: simplicial-complex-fundamentals → sets-and-graphs  
3. studies: knowledge-complex-learner → simplicial-complex-fundamentals

**Validation:** Student has required skill ✓
