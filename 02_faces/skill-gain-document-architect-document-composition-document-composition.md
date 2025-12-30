---
type: face/skill-gain
extends: face
id: f:skill-gain:document-architect:document-composition:document-composition
name: skill-gain document-architect document-composition document-composition
description: Skill-gain face attributing document-composition skill to Module 06 completion
vertices:
  - v:student:document-architect
  - v:learning-module:document-composition
  - v:skill:document-composition
edges:
  - e:has-skill:document-architect:document-composition
  - e:develops-skill:document-composition:document-composition
  - e:advances:document-composition:document-architect
orientation: oriented
tags:
  - face
  - skill-gain
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# skill-gain document-architect document-composition document-composition

## Purpose

This skill-gain face establishes the causal relationship between Module 06 completion and acquisition of the document-composition skill. The face encodes: "document-architect has this skill BECAUSE they completed Module 06."

## Vertices

1. **[[v:student:document-architect]]** (type: student) - The terminal student state (convergence point)
2. **[[v:learning-module:document-composition]]** (type: learning-module) - Module 06
3. **[[v:skill:document-composition]]** (type: skill) - The compositional architecture skill developed

## Boundary Edges

This face has three boundary edges forming a closed triangle:

1. **[[e:has-skill:document-architect:document-composition]]**
   - From: v:student:document-architect
   - To: v:skill:document-composition
   - Semantics: Student HAS the new skill

2. **[[e:develops-skill:document-composition:document-composition]]**
   - From: v:learning-module:document-composition
   - To: v:skill:document-composition
   - Semantics: Module DEVELOPS the skill

3. **[[e:advances:document-composition:document-architect]]**
   - From: v:learning-module:document-composition
   - To: v:student:document-architect
   - Semantics: Module ADVANCES student (who gains the skill)

## Causality Semantics

This face establishes skill attribution:

```
IF module.develops(skill) AND module.advances(student_state)
THEN student_state.has(skill) MUST be true
```

For this specific instance:

- document-composition develops document-composition skill ✓
- document-composition advances document-architect ✓
- document-architect has document-composition skill ✓

**Conclusion:** Skill gain is properly attributed. The document-architect possesses this skill specifically because they completed Module 06.

## Skill Optionality

This skill is **optional** for the document-architect state (convergence allows multiple paths):

- assurance-learner does NOT have this skill (0/1)
- document-architect MAY have this skill (1/1 if Module 06 taken, 0/1 if only Module 07 taken)
- This is one of two distinguishing skills for document-architect (the other being reference-reuse)

## Type Consistency

All vertices and edges have consistent types:

- Vertex types: (student, learning-module, skill) ✓
- Edge types match skill-gain pattern ✓
- Boundary edges form closed triangle ✓

## Related Faces

- [[f:completion:assurance-learner:document-composition:document-architect]] - Completion face that enables this skill gain
- [[f:prerequisite:assurance-learner:assurance-audits:document-composition]] - Prerequisite 1 for the module that develops this skill
- [[f:prerequisite:assurance-learner:composing-typed-simplicial-complexes:document-composition]] - Prerequisite 2 for the module that develops this skill

---

**Note:** This skill-gain face is significant as it represents one of two paths to the terminal document-architect state. Students may reach this state via Module 06 (gaining document-composition), Module 07 (gaining reference-reuse), or both.
