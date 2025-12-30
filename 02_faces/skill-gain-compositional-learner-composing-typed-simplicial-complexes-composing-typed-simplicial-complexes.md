---
type: face/skill-gain
extends: face
id: f:skill-gain:compositional-learner:composing-typed-simplicial-complexes:composing-typed-simplicial-complexes
name: skill-gain compositional-learner composing-typed-simplicial-complexes composing-typed-simplicial-complexes
description: Skill-gain face attributing composing-typed-simplicial-complexes skill to Module 3 completion
vertices:
  - v:student:compositional-learner
  - v:learning-module:composing-typed-simplicial-complexes
  - v:skill:composing-typed-simplicial-complexes
edges:
  - e:has-skill:compositional-learner:composing-typed-simplicial-complexes
  - e:develops-skill:composing-typed-simplicial-complexes:composing-typed-simplicial-complexes
  - e:advances:composing-typed-simplicial-complexes:compositional-learner
orientation: oriented
tags:
  - face
  - skill-gain
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# skill-gain compositional-learner composing-typed-simplicial-complexes composing-typed-simplicial-complexes

## Purpose

This skill-gain face establishes the causal relationship between Module 3 completion and acquisition of the composing-typed-simplicial-complexes skill. The face encodes: "compositional-learner has this skill BECAUSE they completed Module 3."

## Vertices

1. **[[v:student:compositional-learner]]** (type: student) - The student state after Module 3
2. **[[v:learning-module:composing-typed-simplicial-complexes]]** (type: learning-module) - Module 3
3. **[[v:skill:composing-typed-simplicial-complexes]]** (type: skill) - The composition skill developed

## Boundary Edges

This face has three boundary edges forming a closed triangle:

1. **[[e:has-skill:compositional-learner:composing-typed-simplicial-complexes]]**
   - From: v:student:compositional-learner
   - To: v:skill:composing-typed-simplicial-complexes
   - Semantics: Student HAS the new skill

2. **[[e:develops-skill:composing-typed-simplicial-complexes:composing-typed-simplicial-complexes]]**
   - From: v:learning-module:composing-typed-simplicial-complexes
   - To: v:skill:composing-typed-simplicial-complexes
   - Semantics: Module DEVELOPS the skill

3. **[[e:advances:composing-typed-simplicial-complexes:compositional-learner]]**
   - From: v:learning-module:composing-typed-simplicial-complexes
   - To: v:student:compositional-learner
   - Semantics: Module ADVANCES student (who gains the skill)

## Causality Semantics

This face establishes skill attribution:

```
IF module.develops(skill) AND module.advances(student_state)
THEN student_state.has(skill) MUST be true
```

For this specific instance:

- composing-typed-simplicial-complexes develops composing-typed-simplicial-complexes skill ✓
- composing-typed-simplicial-complexes advances compositional-learner ✓
- compositional-learner has composing-typed-simplicial-complexes skill ✓

**Conclusion:** Skill gain is properly attributed. The compositional-learner possesses this skill specifically because they completed Module 3.

## Skill Uniqueness

This skill is **unique** to the compositional-learner state:

- intermediate-learner does NOT have this skill (0/1)
- compositional-learner DOES have this skill (1/1)
- This is the distinguishing skill of the compositional-learner state

## Type Consistency

All vertices and edges have consistent types:

- Vertex types: (student, learning-module, skill) ✓
- Edge types match skill-gain pattern ✓
- Boundary edges form closed triangle ✓

## Related Faces

- [[f:completion:intermediate-learner:composing-typed-simplicial-complexes:compositional-learner]] - Completion face that enables this skill gain
- [[f:prerequisite:intermediate-learner:simplicial-complex-fundamentals:composing-typed-simplicial-complexes]] - Prerequisite for the module that develops this skill
- [[f:prerequisite:intermediate-learner:typed-simplicial-complexes:composing-typed-simplicial-complexes]] - Other prerequisite for the module

---

**Note:** This is the third skill-gain face in the learning journey, attributing the composition skill to Module 3. With this skill, students complete the foundational trilogy and are ready for advanced work.
