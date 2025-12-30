---
type: vertex/resource
extends: vertex
id: v:resource:built-artifact
name: Built Artifact
description: Compiled application artifact ready for testing
tags:
  - vertex
  - resource
  - artifact
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
resource_type: artifact
owner: v:actor:team:product
---

# Built Artifact Resource

## Definition

Compiled and packaged application artifact, output of the Build function.

## Resource Type

**Artifact** - A versioned digital asset

## Owner

Product Team

## Properties

- Container image or binary
- Versioned with build metadata
- Stored in artifact registry
- Intermediate pipeline stage
