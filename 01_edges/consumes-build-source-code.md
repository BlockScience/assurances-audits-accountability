---
type: edge/consumes
extends: edge
id: e:consumes:build:source-code
name: Build consumes Source Code
description: Build function consumes source code as input
tags:
  - edge
  - consumes
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:function:build
target: v:resource:source-code
source_type: vertex/function
target_type: vertex/resource
orientation: directed
blocking: true
---

# Build consumes Source Code

## Relationship

The Build function consumes Source Code as its input.

## Edge Properties

- **Type:** Resource consumption
- **Source:** Build (Function)
- **Target:** Source Code (Resource)
- **Blocking:** Yes - Build cannot proceed without source code
