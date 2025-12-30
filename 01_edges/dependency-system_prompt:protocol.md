---
type: edge/dependency
extends: edge
id: e:dependency:system_prompt:protocol
name: Dependency - System Prompt uses Protocol
description: System prompts have a protocol subsection that must conform to protocol spec (typed subsection)
source: v:spec:system_prompt
target: v:spec:protocol
source_type: vertex/spec
target_type: vertex/spec
orientation: directed
dependency_type: typed_subsection
subsection_field: protocol
required: true
version: 1.0.0
created: 2025-12-27T23:00:00Z
modified: 2025-12-27T23:00:00Z
tags:
  - edge
  - dependency
  - typed-subsection
---

# Dependency - System Prompt uses Protocol

This dependency edge tracks that system_prompt specs use protocol specs as a typed subsection. System prompts are **compositional documents** built from persona, purpose, and protocol components.

## Dependency Relationship

**Dependent:** `v:spec:system_prompt` (Specification for System Prompt Documents)
**Dependency:** `v:spec:protocol` (Specification for Protocol Documents)
**Relationship:** system_prompt uses protocol (typed subsection)

**Direction:** System prompt depends on protocol (system_prompt → protocol)

**Usage:** System prompts have a `## Protocol` section that must conform to `v:spec:protocol`. This subsection defines HOW the AI works - its operational workflow, behavioral guidelines, error handling, and quality standards.

**Assurance Note:** This dependency edge tracks composition and is **separate from the assurance DAG**. For assurance purposes, both system_prompt and protocol verify against v:spec:spec (because both are spec documents), not against each other.

## Dependency Usage

### Structural Usage

System prompts include a Protocol section:

```markdown
## Protocol

### Operational Workflow
[Sequential workflow, as required by v:spec:protocol]

### Behavioral Guidelines
[≥3 guidelines, as required by v:spec:protocol]

### Error Handling
[Error scenarios and responses, as required by v:spec:protocol]

### Quality Standards
[Quality criteria, as required by v:spec:protocol]
```

### Requirements

- **Required:** Yes - system prompts MUST have a protocol subsection
- **Cardinality:** Exactly one protocol per system prompt
- **Conformance:** Protocol subsection MUST satisfy all requirements from `v:spec:protocol`
- **Declared:** Listed in `dependencies` field of system_prompt frontmatter

### Verification

When verifying a system_prompt document:
1. Check it has a `## Protocol` section
2. Extract that subsection
3. Verify extracted subsection conforms to `v:spec:protocol`
4. Report subsection verification results

## Compositional Justification

### Why Composition Not Inheritance

**System prompts are NOT protocols** (they don't extend protocol). System prompts are composite documents that **contain** a protocol component.

- ❌ **Not inheritance:** system_prompt doesn't "is-a" protocol
- ✅ **Composition:** system_prompt "has-a" protocol (plus persona and purpose)

### Why Typed Subsections

The typed subsection pattern enables:

1. **Modularity:** Protocols can be designed and verified independently
2. **Reusability:** Same protocol spec can be used across multiple system prompts
3. **Type Safety:** Subsections have defined structure and can be mechanically verified
4. **Clear Separation:** Protocol focuses on HOW, system_prompt integrates WHO + WHAT + HOW

### Relationship to PPP Framework

In the PPP (Persona-Purpose-Protocol) framework:
- **Persona:** WHO the AI is
- **Purpose:** WHAT the AI does
- **Protocol:** HOW the AI works

System prompts integrate all three into a complete AI model configuration. Each component is defined by its own spec, and the system_prompt spec defines how they compose.

**Design Order:** Protocol should be designed LAST (after purpose and persona), because:
- Protocol operationalizes purpose objectives
- Protocol workflow reflects persona approach
- Protocol is the integration layer that makes persona + purpose work together

### Relationship to Assurance

**Separate Assurance Paths:**

```
Compositional dependency:
  v:spec:system_prompt --depends-on--> v:spec:protocol

Assurance for system_prompt:
  v:spec:system_prompt --verifies--> v:spec:spec
  v:spec:system_prompt --validates--> v:guidance:spec

Assurance for protocol:
  v:spec:protocol --verifies--> v:spec:spec
  v:spec:protocol --validates--> v:guidance:spec
```

Both are assured independently. The dependency edge just tracks that system_prompt uses protocol structurally.

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
