---
type: face/skill-gain
vertices:
  - v:student:management-architect
  - v:learning-module:resource-management
  - v:skill:resource-management
edges:
  - e:has-skill:management-architect:resource-management
  - e:develops-skill:resource-management:resource-management
  - e:advances:resource-management:management-architect
orientation: oriented
id: f:skill-gain:management-architect:resource-management:resource-management
name: Skill-gain triangle - management-architect gains resource-management from resource-management module
description: management-architect possesses resource-management skill developed by resource-management module
tags:
  - face
  - skill-gain
  - triangle
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Skill-Gain Triangle: management-architect gains resource-management

Represents causal relationship between module completion and skill possession.

**Boundary edges:**
1. has-skill: management-architect → resource-management
2. develops-skill: resource-management → resource-management
3. advances: resource-management → management-architect

**Causal chain:**
- Module develops the skill (develops-skill edge)
- Module advances student to new state (advances edge)
- Student in new state possesses the skill (has-skill edge)

**Attribution:** resource-management skill is attributed to Module 09 completion ✓
