---
type: vertex/actor/staff
extends: vertex/actor
id: v:actor:staff:bob
name: Bob
description: SRE on Platform Team
tags:
  - vertex
  - actor
  - staff
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
roles:
  - v:actor:role:sre
team: v:actor:team:platform
---

# Bob - SRE

## Identity

Bob is a staff member serving as Site Reliability Engineer on the Platform Team. He is responsible for monitoring and incident response.

## Capabilities

Bob can:
- Configure monitoring systems
- Respond to incidents
- Execute deployments (with approval)
- Automate operational tasks

## Constraints

- Requires Tech Lead approval for production changes
- On-call rotation
- Must document incidents
