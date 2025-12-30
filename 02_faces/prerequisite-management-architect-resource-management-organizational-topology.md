---
type: face/prerequisite
vertices:
  - v:student:management-architect
  - v:skill:resource-management
  - v:learning-module:organizational-topology
edges:
  - e:has-skill:management-architect:resource-management
  - e:requires-skill:organizational-topology:resource-management
  - e:studies:management-architect:organizational-topology
orientation: oriented
id: f:prerequisite:management-architect:resource-management:organizational-topology
name: Prerequisite triangle - management-architect with resource-management for organizational-topology
description: management-architect possessing resource-management can study organizational-topology which requires that skill
tags:
  - face
  - prerequisite
  - triangle
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Prerequisite Triangle: management-architect with resource-management for organizational-topology

Validates second of three prerequisite skills for Module 10 (capstone has 3 prerequisites).

**Boundary edges:**
1. has-skill: management-architect → resource-management
2. requires-skill: organizational-topology → resource-management
3. studies: management-architect → organizational-topology

**Validation:** Student has required management chart skill ✓
