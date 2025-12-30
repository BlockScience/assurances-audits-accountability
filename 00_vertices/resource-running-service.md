---
type: vertex/resource
extends: vertex
id: v:resource:running-service
name: Running Service
description: Live application running in production environment
tags:
  - vertex
  - resource
  - infrastructure
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
resource_type: infrastructure
owner: v:actor:team:platform
---

# Running Service Resource

## Definition

Live application instance running in the production environment.

## Resource Type

**Infrastructure** - A deployed operational resource

## Owner

Platform Team

## Properties

- Production deployment
- Subject to monitoring
- SLA-bound
- Terminal output of deployment pipeline
