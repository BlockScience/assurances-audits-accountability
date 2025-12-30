---
type: face/skill-gain
vertices:
  - v:student:intermediate-learner
  - v:learning-module:typed-simplicial-complexes
  - v:skill:typed-simplicial-complexes
edges:
  - e:advances:typed-simplicial-complexes:intermediate-learner
  - e:has-skill:intermediate-learner:typed-simplicial-complexes
  - e:develops-skill:typed-simplicial-complexes:typed-simplicial-complexes
orientation: oriented
id: f:skill-gain:intermediate-learner:typed-simplicial-complexes:typed-simplicial-complexes
name: Skill-gain triangle - intermediate-learner gains typed-simplicial-complexes from typed-simplicial-complexes
description: intermediate-learner gains typed-simplicial-complexes through completing typed-simplicial-complexes module
tags:
  - face
  - skill-gain
  - acquisition
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Skill-Gain Triangle: intermediate-learner gains typed-simplicial-complexes from typed-simplicial-complexes

Represents the causal skill acquisition - completing typed-simplicial-complexes module causes intermediate-learner to gain typed-simplicial-complexes skill.

**Boundary edges:**
1. advances: typed-simplicial-complexes → intermediate-learner (module advances to new state)
2. has-skill: intermediate-learner → typed-simplicial-complexes (student possesses skill)
3. develops-skill: typed-simplicial-complexes → typed-simplicial-complexes (module develops skill)

**Causality:** Module 2 completion → Type system skill acquisition

**Validation:**
- Module develops this skill? ✓ (develops-skill edge exists)
- Module advances to this student? ✓ (advances edge exists from completion face)
- Student has this skill? ✓ (has-skill edge exists)
- Causal relationship valid? ✓
