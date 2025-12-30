---
type: face/skill-gain
vertices:
  - v:student:chief-engineer
  - v:learning-module:organizational-topology
  - v:skill:topological-data-analysis
edges:
  - e:has-skill:chief-engineer:topological-data-analysis
  - e:develops-skill:organizational-topology:topological-data-analysis
  - e:advances:organizational-topology:chief-engineer
orientation: oriented
id: f:skill-gain:chief-engineer:organizational-topology:topological-data-analysis
name: Skill-gain triangle - chief-engineer gains topological-data-analysis from organizational-topology module
description: chief-engineer possesses topological-data-analysis skill developed by organizational-topology module
tags:
  - face
  - skill-gain
  - triangle
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---

# Skill-Gain Triangle: chief-engineer gains topological-data-analysis

Represents causal relationship between module completion and first skill possession.

**Boundary edges:**
1. has-skill: chief-engineer → topological-data-analysis
2. develops-skill: organizational-topology → topological-data-analysis
3. advances: organizational-topology → chief-engineer

**Causal chain:**
- Module develops the skill (develops-skill edge)
- Module advances student to new state (advances edge)
- Student in new state possesses the skill (has-skill edge)

**Attribution:** topological-data-analysis skill is attributed to Module 10 completion ✓

**Note:** This is one of TWO skill-gain faces for Module 10 (the only module that develops 2 skills).
