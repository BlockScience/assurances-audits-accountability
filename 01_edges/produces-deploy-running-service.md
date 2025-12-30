---
type: edge/produces
extends: edge
id: e:produces:deploy:running-service
name: Deploy produces Running Service
description: Deploy function produces running service as output
tags:
  - edge
  - produces
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:function:deploy
target: v:resource:running-service
source_type: vertex/function
target_type: vertex/resource
orientation: directed
---

# Deploy produces Running Service

## Relationship

The Deploy function produces Running Service as its output.

## Edge Properties

- **Type:** Resource production
- **Source:** Deploy (Function)
- **Target:** Running Service (Resource)

## Pipeline Terminus

This production edge represents the **terminal output** of the deployment pipeline. The running service is the end goal.
