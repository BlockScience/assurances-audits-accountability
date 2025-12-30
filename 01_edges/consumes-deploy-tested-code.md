---
type: edge/consumes
extends: edge
id: e:consumes:deploy:tested-code
name: Deploy consumes Tested Code
description: Deploy function consumes tested code as input
tags:
  - edge
  - consumes
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:function:deploy
target: v:resource:tested-code
source_type: vertex/function
target_type: vertex/resource
orientation: directed
blocking: true
---

# Deploy consumes Tested Code

## Relationship

The Deploy function consumes Tested Code as its input.

## Edge Properties

- **Type:** Resource consumption
- **Source:** Deploy (Function)
- **Target:** Tested Code (Resource)
- **Blocking:** Yes - Deploy cannot proceed without tested code

## Cross-Team Handoff

This consumption edge represents the **critical handoff** from Product Team to Platform Team. Product produces tested code; Platform consumes it for deployment.
