---
type: vertex/function
extends: vertex
id: v:function:build
name: Build Service
description: Function that compiles code and creates deployment artifacts
tags:
  - vertex
  - function
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
operated_by: v:actor:team:product
inputs:
  - v:resource:source-code
outputs:
  - v:resource:built-artifact
---

# Build Service Function

## Definition

The Build function compiles application source code and creates deployment-ready artifacts.

## Inputs

- **Source Code:** Raw application code from version control

## Outputs

- **Built Artifact:** Compiled, packaged application ready for testing

## Operation

Operated by the Product Team (specifically developers).

## Constraints

- Requires all tests to pass
- Artifacts must be versioned
- Build logs must be retained
