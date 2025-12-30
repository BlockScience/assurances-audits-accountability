---
type: vertex/actor/team
extends: vertex/actor
id: v:actor:team:product
name: Product Team
description: Product development team responsible for building and testing application features
tags:
  - vertex
  - actor
  - team
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
members:
  - v:actor:staff:dana
  - v:actor:staff:evan
responsibilities:
  - Build application features
  - Write and run tests
  - Create deployment packages
---

# Product Team

## Identity

The Product Team is an organizational unit responsible for application development. This team builds features, writes tests, and prepares code for deployment.

## Capabilities

The Product Team can:
- Develop new application features
- Write unit and integration tests
- Build deployment packages
- Review code changes
- Coordinate with Platform Team for deployments

## Constraints

- Must pass all tests before merging
- Code requires peer review
- Must coordinate with Platform Team for production deployments

## Structure

| Member | Role | Primary Responsibility |
|--------|------|----------------------|
| Dana | Senior Developer | Feature development, code review |
| Evan | Developer | Feature development, testing |

## Relationships

- **Parent:** Engineering Division
- **Collaborates with:** Platform Team, QA Team
- **Hands off to:** Platform Team (deployment packages)
