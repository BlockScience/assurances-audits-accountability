---
type: face/skill-gain
vertices:
  - v:student:coordination-architect
  - v:learning-module:team-coordination
  - v:skill:team-coordination
edges:
  - e:has-skill:coordination-architect:team-coordination
  - e:develops-skill:team-coordination:team-coordination
  - e:advances:team-coordination:coordination-architect
orientation: oriented
id: f:skill-gain:coordination-architect:team-coordination:team-coordination
name: Skill-gain triangle - coordination-architect gains team-coordination from team-coordination module
description: coordination-architect possesses team-coordination skill developed by team-coordination module
tags:
  - face
  - skill-gain
  - triangle
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Skill-Gain Triangle: coordination-architect gains team-coordination

Represents causal relationship between module completion and skill possession.

**Boundary edges:**
1. has-skill: coordination-architect → team-coordination
2. develops-skill: team-coordination → team-coordination
3. advances: team-coordination → coordination-architect

**Causal chain:**
- Module develops the skill (develops-skill edge)
- Module advances student to new state (advances edge)
- Student in new state possesses the skill (has-skill edge)

**Attribution:** team-coordination skill is attributed to Module 08 completion ✓
