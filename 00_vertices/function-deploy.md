---
type: vertex/function
extends: vertex
id: v:function:deploy
name: Deploy Service
description: Function that deploys validated artifacts to production environment
tags:
  - vertex
  - function
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
operated_by: v:actor:team:platform
inputs:
  - v:resource:tested-code
outputs:
  - v:resource:running-service
---

# Deploy Service Function

## Definition

The Deploy function takes validated artifacts and deploys them to the production environment.

## Inputs

- **Tested Code:** Validated artifact from Test function

## Outputs

- **Running Service:** Live application in production

## Operation

Operated by the Platform Team (SREs with Tech Lead approval).

## Constraints

- Requires Tech Lead approval
- Must occur during change windows (except emergencies)
- Rollback plan required
