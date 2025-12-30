---
type: vertex/function
extends: vertex
id: v:function:test
name: Test Service
description: Function that executes tests and validates build artifacts
tags:
  - vertex
  - function
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
operated_by: v:actor:team:product
inputs:
  - v:resource:built-artifact
outputs:
  - v:resource:tested-code
---

# Test Service Function

## Definition

The Test function executes automated tests against build artifacts to validate correctness.

## Inputs

- **Built Artifact:** Compiled application from Build function

## Outputs

- **Tested Code:** Validated artifact ready for deployment

## Operation

Operated by the Product Team.

## Constraints

- All tests must pass for output
- Test results must be recorded
- Coverage requirements must be met
