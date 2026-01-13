---
type: vertex/signer
extends: actor
id: v:signer:admin
name: Bootstrap Administrator Signer
description: Placeholder signer for foundation - replaced by actual admin during aaa init
github_username: ADMIN_USERNAME
tags:
  - vertex
  - actor
  - signer
  - admin
  - genesis
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
dependencies: []
---

# Bootstrap Administrator Signer

## Purpose

This is a placeholder signer vertex for the foundation. During `aaa init`, this is replaced with an actual signer vertex using the provided GitHub username.

## Genesis Context

This signer is part of the foundation infrastructure:

- Created at system initialization
- Placeholder for the first human administrator
- Signs foundational ontology documents

## Capabilities

1. **Sign Foundation Documents**: Authority to sign ontology layer documents
2. **Bootstrap Authority**: Initial authority before user-specific signers are created

## Note

The `ADMIN_USERNAME` placeholder is replaced during `aaa init` with the actual GitHub username of the administrator.
