---
type: edge/operates
extends: edge
id: e:operates:product:test
name: Product Team operates Test
description: Operational control of Test function by Product Team
tags:
  - edge
  - operates
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:actor:team:product
target: v:function:test
source_type: vertex/actor/team
target_type: vertex/function
orientation: directed
---

# Product Team operates Test

## Relationship

The Product Team has operational control of the Test function.

## Edge Properties

- **Type:** Operational control
- **Source:** Product Team (Team)
- **Target:** Test (Function)
- **Direction:** Team → Function
