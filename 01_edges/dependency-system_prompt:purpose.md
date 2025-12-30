---
type: edge/dependency
extends: edge
id: e:dependency:system_prompt:purpose
name: Dependency - System Prompt uses Purpose
description: System prompts have a purpose subsection that must conform to purpose spec (typed subsection)
source: v:spec:system_prompt
target: v:spec:purpose
source_type: vertex/spec
target_type: vertex/spec
orientation: directed
dependency_type: typed_subsection
subsection_field: purpose
required: true
version: 1.0.0
created: 2025-12-27T23:00:00Z
modified: 2025-12-27T23:00:00Z
tags:
  - edge
  - dependency
  - typed-subsection
---

# Dependency - System Prompt uses Purpose

This dependency edge tracks that system_prompt specs use purpose specs as a typed subsection. System prompts are **compositional documents** built from persona, purpose, and protocol components.

## Dependency Relationship

**Dependent:** `v:spec:system_prompt` (Specification for System Prompt Documents)
**Dependency:** `v:spec:purpose` (Specification for Purpose Documents)
**Relationship:** system_prompt uses purpose (typed subsection)

**Direction:** System prompt depends on purpose (system_prompt → purpose)

**Usage:** System prompts have a `## Purpose` section that must conform to `v:spec:purpose`. This subsection defines WHAT the AI does - its objectives, success criteria, constraints, and outputs.

**Assurance Note:** This dependency edge tracks composition and is **separate from the assurance DAG**. For assurance purposes, both system_prompt and purpose verify against v:spec:spec (because both are spec documents), not against each other.

## Dependency Usage

### Structural Usage

System prompts include a Purpose section:

```markdown
## Purpose

### Core Objectives
[3-5 objectives, as required by v:spec:purpose]

### Success Criteria
[≥3 items, as required by v:spec:purpose]

### Constraints and Boundaries
[≥3 items, as required by v:spec:purpose]

### Expected Outputs
[Description, as required by v:spec:purpose]
```

### Requirements

- **Required:** Yes - system prompts MUST have a purpose subsection
- **Cardinality:** Exactly one purpose per system prompt
- **Conformance:** Purpose subsection MUST satisfy all requirements from `v:spec:purpose`
- **Declared:** Listed in `dependencies` field of system_prompt frontmatter

### Verification

When verifying a system_prompt document:
1. Check it has a `## Purpose` section
2. Extract that subsection
3. Verify extracted subsection conforms to `v:spec:purpose`
4. Report subsection verification results

## Compositional Justification

### Why Composition Not Inheritance

**System prompts are NOT purposes** (they don't extend purpose). System prompts are composite documents that **contain** a purpose component.

- ❌ **Not inheritance:** system_prompt doesn't "is-a" purpose
- ✅ **Composition:** system_prompt "has-a" purpose (plus persona and protocol)

### Why Typed Subsections

The typed subsection pattern enables:

1. **Modularity:** Purposes can be designed and verified independently
2. **Reusability:** Same purpose spec can be used across multiple system prompts
3. **Type Safety:** Subsections have defined structure and can be mechanically verified
4. **Clear Separation:** Purpose focuses on WHAT, system_prompt integrates WHO + WHAT + HOW

### Relationship to PPP Framework

In the PPP (Persona-Purpose-Protocol) framework:
- **Persona:** WHO the AI is
- **Purpose:** WHAT the AI does
- **Protocol:** HOW the AI works

System prompts integrate all three into a complete AI model configuration. Each component is defined by its own spec, and the system_prompt spec defines how they compose.

**Design Order:** Purpose should be designed FIRST (before persona and protocol), because:
- Persona expertise must enable purpose objectives
- Protocol workflow must operationalize purpose through persona

### Relationship to Assurance

**Separate Assurance Paths:**

```
Compositional dependency:
  v:spec:system_prompt --depends-on--> v:spec:purpose

Assurance for system_prompt:
  v:spec:system_prompt --verifies--> v:spec:spec
  v:spec:system_prompt --validates--> v:guidance:spec

Assurance for purpose:
  v:spec:purpose --verifies--> v:spec:spec
  v:spec:purpose --validates--> v:guidance:spec
```

Both are assured independently. The dependency edge just tracks that system_prompt uses purpose structurally.

## Notes

This dependency is part of a set of three:
```
v:spec:system_prompt --depends-on--> v:spec:persona
v:spec:system_prompt --depends-on--> v:spec:purpose
v:spec:system_prompt --depends-on--> v:spec:protocol
```

Together, these dependencies define the PPP framework's compositional structure.

---

**Version:** 1.0.0
**Type:** Dependency Edge
**Last Modified:** 2025-12-27
