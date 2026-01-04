---
type: edge/dependency
extends: edge
id: e:dependency:program-memo-bfe:program-plan-bfe
name: Dependency Edge - program-memo-bfe requires program-plan-bfe
description: The program memo summarizes and authorizes the program plan
source: v:doc:program-memo-bus-electrification
target: v:doc:program-plan-bus-electrification
orientation: directed
dependency_type: structural
rationale: Program memo must accurately summarize program plan for executive authorization
tags:
  - edge
  - dependency
  - program-development
version: 1.0.0
created: 2026-01-04T23:00:00Z
modified: 2026-01-04T23:00:00Z
---

# Dependency Edge - program-memo-bfe requires program-plan-bfe

This edge represents the dependency relationship where the program memo document for bus electrification requires the program plan document.

## Dependency Details

**Source**: [[program-memo-bus-electrification]]
**Target**: [[program-plan-bus-electrification]]
**Type**: Structural dependency

## Rationale

The program memo depends on the complete program plan:
- Executive summary must accurately reflect plan content
- Budget and timeline come from program plan analysis
- Risk summary drawn from program plan risk register
- Authorization scope defined by plan deliverables

The program memo is the authorization wrapper for the program plan.
