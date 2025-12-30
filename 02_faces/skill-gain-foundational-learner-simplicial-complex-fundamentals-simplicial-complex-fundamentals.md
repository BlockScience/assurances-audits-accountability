---
type: face/skill-gain
vertices:
  - v:student:foundational-learner
  - v:learning-module:simplicial-complex-fundamentals
  - v:skill:simplicial-complex-fundamentals
edges:
  - e:advances:simplicial-complex-fundamentals:foundational-learner
  - e:has-skill:foundational-learner:simplicial-complex-fundamentals
  - e:develops-skill:simplicial-complex-fundamentals:simplicial-complex-fundamentals
orientation: oriented
id: f:skill-gain:foundational-learner:simplicial-complex-fundamentals:simplicial-complex-fundamentals
name: Skill-gain triangle - foundational-learner gains simplicial-complex-fundamentals from simplicial-complex-fundamentals
description: foundational-learner gains simplicial-complex-fundamentals through completing simplicial-complex-fundamentals
tags:
  - face
  - skill-gain
  - acquisition
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Skill-Gain Triangle: foundational-learner gains simplicial-complex-fundamentals from simplicial-complex-fundamentals

Represents the causal skill acquisition - completing simplicial-complex-fundamentals module causes foundational-learner to gain simplicial-complex-fundamentals skill.

**Boundary edges:**
1. advances: simplicial-complex-fundamentals → foundational-learner (module advances to new state)
2. has-skill: foundational-learner → simplicial-complex-fundamentals (student possesses skill)
3. develops-skill: simplicial-complex-fundamentals → simplicial-complex-fundamentals (module develops skill)

**Causality:** Module completion → Skill acquisition

**Validation:**
- Module develops this skill? ✓ (develops-skill edge exists)
- Module advances to this student? ✓ (advances edge exists from completion face)
- Student has this skill? ✓ (has-skill edge exists)
- Causal relationship valid? ✓
