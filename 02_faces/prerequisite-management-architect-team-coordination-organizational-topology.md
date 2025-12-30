---
type: face/prerequisite
vertices:
  - v:student:management-architect
  - v:skill:team-coordination
  - v:learning-module:organizational-topology
edges:
  - e:has-skill:management-architect:team-coordination
  - e:requires-skill:organizational-topology:team-coordination
  - e:studies:management-architect:organizational-topology
orientation: oriented
id: f:prerequisite:management-architect:team-coordination:organizational-topology
name: Prerequisite triangle - management-architect with team-coordination for organizational-topology
description: management-architect possessing team-coordination can study organizational-topology which requires that skill
tags:
  - face
  - prerequisite
  - triangle
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Prerequisite Triangle: management-architect with team-coordination for organizational-topology

Validates first of three prerequisite skills for Module 10 (capstone has 3 prerequisites).

**Boundary edges:**
1. has-skill: management-architect → team-coordination
2. requires-skill: organizational-topology → team-coordination
3. studies: management-architect → organizational-topology

**Validation:** Student has required coordination chart skill ✓
