# Planning Domain Pack

This pack provides document types for program planning and lifecycle management, building on architecture documentation.

## Pack Info

- **Dependencies:** boundary, foundation, meta, architecture
- **Manifest:** [pack.yaml](pack.yaml)

## Vertex Types

| Type | Description |
|------|-------------|
| lifecycle | Lifecycle stage definitions and transitions |
| program-plan | High-level program objectives and milestones |
| program-memo | Status updates and decision records |
| implementation-plan | Detailed implementation steps |

## Planning Workflow

```text
lifecycle → program-plan → program-memo → implementation-plan
                 ↓
           architecture (dependency)
```

Planning documents build on architecture by referencing architecture documents as dependencies.

## Edge Types

| Type | Source → Target | Description |
|------|-----------------|-------------|
| dependency | planning doc → planning/architecture doc | One doc depends on another |

Plus standard edges from foundation for verification and validation.

## Domain Rules

### lifecycle_precedes_plan
**Severity:** warning

Program plans should reference a lifecycle definition to establish the context for planning.

### memo_references_plan
**Severity:** warning

Program memos should reference their parent plan to maintain traceability.

## Directory Structure

```text
content/planning/
├── 00_vertices/     # Specs and guidances for planning types
├── 01_edges/        # Coupling, verification, validation, dependency edges
├── 02_faces/        # Assurance faces
└── impl-plans/      # Implementation plan instances
```

## Related Packs

- **architecture**: Planning docs depend on architecture docs
- **ppp**: Can be combined with ppp for program personas and purposes
- **rbac**: Can be combined with rbac for plan approval signatures
