---
type: edge/member
extends: edge
id: e:member:platform:bob
name: Bob is member of Platform Team
description: Membership relationship between Bob and Platform Team
tags:
  - edge
  - member
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:actor:staff:bob
target: v:actor:team:platform
source_type: vertex/actor/staff
target_type: vertex/actor/team
orientation: directed
---

# Bob is member of Platform Team

## Relationship

Bob is a member of the Platform Team, serving as SRE.

## Edge Properties

- **Type:** Membership
- **Source:** Bob (Staff)
- **Target:** Platform Team (Team)
- **Direction:** Staff → Team
