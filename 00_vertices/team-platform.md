---
type: vertex/actor/team
extends: vertex/actor
id: v:actor:team:platform
name: Platform Team
description: Infrastructure and platform engineering team responsible for deployment, monitoring, and infrastructure
tags:
  - vertex
  - actor
  - team
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
members:
  - v:actor:staff:alice
  - v:actor:staff:bob
  - v:actor:staff:charlie
responsibilities:
  - Deploy to production
  - Monitor services
  - Maintain infrastructure
---

# Platform Team

## Identity

The Platform Team is an organizational unit responsible for infrastructure and platform engineering. This team ensures reliable deployment pipelines, service monitoring, and infrastructure management.

## Capabilities

The Platform Team can:
- Deploy applications to production environments
- Configure and maintain monitoring systems
- Provision and manage infrastructure resources
- Respond to incidents and outages
- Support development teams with platform tooling

## Constraints

- Must maintain 99.9% uptime SLA
- Changes require approval from Tech Lead
- Production deployments only during change windows (except emergencies)

## Structure

| Member | Role | Primary Responsibility |
|--------|------|----------------------|
| Alice | Tech Lead | Deployment approval, architecture decisions |
| Bob | SRE | Monitoring, incident response |
| Charlie | SRE | Infrastructure automation |

## Relationships

- **Parent:** Engineering Division
- **Collaborates with:** Product Team, QA Team
- **Depends on:** Security Team (for compliance reviews)
