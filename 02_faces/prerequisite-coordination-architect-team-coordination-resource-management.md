---
type: face/prerequisite
vertices:
  - v:student:coordination-architect
  - v:skill:team-coordination
  - v:learning-module:resource-management
edges:
  - e:has-skill:coordination-architect:team-coordination
  - e:requires-skill:resource-management:team-coordination
  - e:studies:coordination-architect:resource-management
orientation: oriented
id: f:prerequisite:coordination-architect:team-coordination:resource-management
name: Prerequisite triangle - coordination-architect with team-coordination for resource-management
description: coordination-architect possessing team-coordination can study resource-management which requires that skill
tags:
  - face
  - prerequisite
  - triangle
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Prerequisite Triangle: coordination-architect with team-coordination for resource-management

Validates that student has prerequisite skill for Module 09 (single prerequisite pattern).

**Boundary edges:**
1. has-skill: coordination-architect → team-coordination
2. requires-skill: resource-management → team-coordination
3. studies: coordination-architect → resource-management

**Validation:** Student has required coordination chart skill ✓
