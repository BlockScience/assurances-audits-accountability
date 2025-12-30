---
type: face/skill-gain
extends: face
id: f:skill-gain:document-architect:reference-reuse:reference-reuse
name: skill-gain document-architect reference-reuse reference-reuse
description: Skill-gain face attributing reference-reuse skill to Module 07 completion
vertices:
  - v:student:document-architect
  - v:learning-module:reference-reuse
  - v:skill:reference-reuse
edges:
  - e:has-skill:document-architect:reference-reuse
  - e:develops-skill:reference-reuse:reference-reuse
  - e:advances:reference-reuse:document-architect
orientation: oriented
tags:
  - face
  - skill-gain
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# skill-gain document-architect reference-reuse reference-reuse

## Purpose

This skill-gain face establishes the causal relationship between Module 07 completion and acquisition of the reference-reuse skill. The face encodes: "document-architect has this skill BECAUSE they completed Module 07."

## Vertices

1. **[[v:student:document-architect]]** (type: student) - The terminal student state (convergence point)
2. **[[v:learning-module:reference-reuse]]** (type: learning-module) - Module 07
3. **[[v:skill:reference-reuse]]** (type: skill) - The doc-kit pattern library skill developed

## Boundary Edges

This face has three boundary edges forming a closed triangle:

1. **[[e:has-skill:document-architect:reference-reuse]]**
   - From: v:student:document-architect
   - To: v:skill:reference-reuse
   - Semantics: Student HAS the new skill

2. **[[e:develops-skill:reference-reuse:reference-reuse]]**
   - From: v:learning-module:reference-reuse
   - To: v:skill:reference-reuse
   - Semantics: Module DEVELOPS the skill

3. **[[e:advances:reference-reuse:document-architect]]**
   - From: v:learning-module:reference-reuse
   - To: v:student:document-architect
   - Semantics: Module ADVANCES student (who gains the skill)

## Causality Semantics

This face establishes skill attribution:

```
IF module.develops(skill) AND module.advances(student_state)
THEN student_state.has(skill) MUST be true
```

For this specific instance:

- reference-reuse develops reference-reuse skill ✓
- reference-reuse advances document-architect ✓
- document-architect has reference-reuse skill ✓

**Conclusion:** Skill gain is properly attributed. The document-architect possesses this skill specifically because they completed Module 07.

## Skill Optionality

This skill is **optional** for the document-architect state (convergence allows multiple paths):

- assurance-learner does NOT have this skill (0/1)
- document-architect MAY have this skill (1/1 if Module 07 taken, 0/1 if only Module 06 taken)
- This is one of two distinguishing skills for document-architect (the other being document-composition)

## Type Consistency

All vertices and edges have consistent types:

- Vertex types: (student, learning-module, skill) ✓
- Edge types match skill-gain pattern ✓
- Boundary edges form closed triangle ✓

## Related Faces

- [[f:completion:assurance-learner:reference-reuse:document-architect]] - Completion face that enables this skill gain
- [[f:prerequisite:assurance-learner:assurance-audits:reference-reuse]] - Prerequisite for the module that develops this skill

---

**Note:** This skill-gain face is significant as it represents the second of two paths to the terminal document-architect state. Students may reach this state via Module 06 (gaining document-composition), Module 07 (gaining reference-reuse), or both (complete skill set).
