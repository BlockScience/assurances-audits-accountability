---
type: face/prerequisite
extends: face
id: f:prerequisite:intermediate-learner:typed-simplicial-complexes:composing-typed-simplicial-complexes
name: prerequisite intermediate-learner typed-simplicial-complexes composing-typed-simplicial-complexes
description: Prerequisite face validating that intermediate-learner students have typed-simplicial-complexes required by Module 3
vertices:
  - v:student:intermediate-learner
  - v:skill:typed-simplicial-complexes
  - v:learning-module:composing-typed-simplicial-complexes
edges:
  - e:has-skill:intermediate-learner:typed-simplicial-complexes
  - e:requires-skill:composing-typed-simplicial-complexes:typed-simplicial-complexes
  - e:studies:intermediate-learner:composing-typed-simplicial-complexes
orientation: oriented
tags:
  - face
  - prerequisite
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# prerequisite intermediate-learner typed-simplicial-complexes composing-typed-simplicial-complexes

## Purpose

This prerequisite face validates that intermediate-learner students possess the typed-simplicial-complexes skill required by Module 3. The face encodes the constraint: "to study Module 3, you must understand semantic types and type constraints."

## Vertices

1. **[[v:student:intermediate-learner]]** (type: student) - The student state entering Module 3
2. **[[v:skill:typed-simplicial-complexes]]** (type: skill) - The typing skill from Module 2
3. **[[v:learning-module:composing-typed-simplicial-complexes]]** (type: learning-module) - Module 3

## Boundary Edges

This face has three boundary edges forming a closed triangle:

1. **[[e:has-skill:intermediate-learner:typed-simplicial-complexes]]**
   - From: v:student:intermediate-learner
   - To: v:skill:typed-simplicial-complexes
   - Semantics: Student HAS the prerequisite skill

2. **[[e:requires-skill:composing-typed-simplicial-complexes:typed-simplicial-complexes]]**
   - From: v:learning-module:composing-typed-simplicial-complexes
   - To: v:skill:typed-simplicial-complexes
   - Semantics: Module REQUIRES the skill

3. **[[e:studies:intermediate-learner:composing-typed-simplicial-complexes]]**
   - From: v:student:intermediate-learner
   - To: v:learning-module:composing-typed-simplicial-complexes
   - Semantics: Student STUDIES the module

## Validation Logic

This face validates the prerequisite constraint:

```
IF student.studies(module) AND module.requires(skill)
THEN student.has(skill) MUST be true
```

For this specific instance:

- intermediate-learner studies composing-typed-simplicial-complexes ✓
- composing-typed-simplicial-complexes requires typed-simplicial-complexes ✓
- intermediate-learner has typed-simplicial-complexes ✓

**Conclusion:** Prerequisite satisfied. Student has the typing knowledge needed for type-safe composition.

## Type Consistency

All vertices and edges have consistent types:

- Vertex types: (student, skill, learning-module) ✓
- Edge types match prerequisite pattern ✓
- Boundary edges form closed triangle ✓

## Related Faces

- [[f:prerequisite:intermediate-learner:simplicial-complex-fundamentals:composing-typed-simplicial-complexes]] - Module 3's other prerequisite (foundational skill)
- [[f:completion:intermediate-learner:composing-typed-simplicial-complexes:compositional-learner]] - Completion face after both prerequisites are satisfied

---

**Note:** This is the second of two prerequisite faces for Module 3, validating the typing skill prerequisite.
