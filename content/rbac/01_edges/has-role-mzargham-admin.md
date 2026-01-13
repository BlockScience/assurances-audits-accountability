---
type: edge/has-role
extends: edge
id: e:has-role:mzargham:admin
name: Has Role - mzargham has admin role
source: v:signer:mzargham
target: v:role:admin
source_type: vertex/signer
target_type: vertex/role
orientation: directed
granted_by: system
granted_date: 2026-01-13T00:20:00Z
tags:
  - edge
  - has-role
  - bootstrap
version: 1.0.0
created: 2026-01-13T00:20:00Z
modified: 2026-01-13T00:20:00Z
---

# Has Role - mzargham has admin role

This edge establishes that mzargham holds the Administrator role.

## Role Assignment

**Actor:** [[signer-mzargham|v:signer:mzargham]]
**Role:** [[role-admin|v:role:admin]]
**Granted By:** System (bootstrap during repository initialization)
**Granted Date:** 2026-01-13T00:20:00Z

## Authority Chain

This role assignment was created during repository initialization. The founding user automatically receives the admin role, establishing the root of the RBAC authority chain.

## Scope

This role assignment grants mzargham full administrative authority over this knowledge complex, including:
- Assigning roles to other actors
- Establishing qualification credentials
- Managing framework structure
