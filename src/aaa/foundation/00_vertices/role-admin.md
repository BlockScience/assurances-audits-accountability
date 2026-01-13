---
type: vertex/role
extends: property
id: v:role:admin
name: Administrator
description: Bootstrap administrator role with authority to manage the knowledge complex
tags:
  - vertex
  - property
  - role
  - admin
  - genesis
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
dependencies: []
---

# Administrator Role

## Purpose

The Administrator role is the bootstrap authority for the foundation. It grants authority to manage the knowledge complex, sign foundational documents, and establish the initial RBAC chain.

## Genesis Context

This role is part of the foundation infrastructure:

- Created at system initialization
- Held by the first admin signer
- Enables signing of ontology layer documents

## Authority Granted

This role conveys authority to:

- Sign validation edges for foundational documents
- Establish qualifications for other signers
- Manage knowledge complex structure

## Qualification Requirements

This role is assigned to the repository administrator during `aaa init`.
