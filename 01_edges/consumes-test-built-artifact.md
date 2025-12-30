---
type: edge/consumes
extends: edge
id: e:consumes:test:built-artifact
name: Test consumes Built Artifact
description: Test function consumes built artifact as input
tags:
  - edge
  - consumes
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:function:test
target: v:resource:built-artifact
source_type: vertex/function
target_type: vertex/resource
orientation: directed
blocking: true
---

# Test consumes Built Artifact

## Relationship

The Test function consumes Built Artifact as its input.

## Edge Properties

- **Type:** Resource consumption
- **Source:** Test (Function)
- **Target:** Built Artifact (Resource)
- **Blocking:** Yes - Test cannot proceed without built artifact
