---
type: vertex/role
extends: property
id: v:role:admin
name: Administrator
description: Role with authority to assign other roles and manage the knowledge complex
tags:
  - vertex
  - property
  - role
  - admin
version: 1.0.0
created: 2026-01-13T00:20:00Z
modified: 2026-01-13T00:20:00Z
dependencies: []
---

# Administrator Role

## Purpose

The Administrator role grants authority to manage the knowledge complex, including the ability to assign roles to other actors and establish qualification credentials.

## Responsibilities

- Assign roles to new team members
- Establish initial qualifications for signers
- Manage knowledge complex structure and policies
- Approve foundational changes to the framework

## Authority Granted

This role conveys the following permissions:

- **can-assign**: Authority to assign any role to any actor
- **validate-guidance**: Authority to validate documents against any guidance
- **bootstrap-authority**: Initial authority before formal RBAC chains are established

## Qualification Requirements

This role is typically held by:
- Repository founders/owners
- Organization leadership
- Designated knowledge complex administrators
