---
type: edge/dependency
extends: edge
id: e:dependency:system_prompt:persona
name: Dependency - System Prompt uses Persona
description: System prompts have a persona subsection that must conform to persona spec (typed subsection)
source: v:spec:system_prompt
target: v:spec:persona
source_type: vertex/spec
target_type: vertex/spec
orientation: directed
dependency_type: typed_subsection
subsection_field: persona
required: true
version: 1.0.0
created: 2025-12-27T23:00:00Z
modified: 2025-12-27T23:00:00Z
tags:
  - edge
  - dependency
  - typed-subsection
---

# Dependency - System Prompt uses Persona

This dependency edge tracks that system_prompt specs use persona specs as a typed subsection. System prompts are **compositional documents** built from persona, purpose, and protocol components.

## Dependency Relationship

**Dependent:** `v:spec:system_prompt` (Specification for System Prompt Documents)
**Dependency:** `v:spec:persona` (Specification for Persona Documents)
**Relationship:** system_prompt uses persona (typed subsection)

**Direction:** System prompt depends on persona (system_prompt → persona)

**Usage:** System prompts have a `## Persona` section that must conform to `v:spec:persona`. This subsection defines WHO the AI is - its professional identity, domain expertise, thinking approach, communication style, and explicit boundaries.

**Assurance Note:** This dependency edge tracks composition and is **separate from the assurance DAG**. For assurance purposes, both system_prompt and persona verify against v:spec:spec (because both are spec documents), not against each other.

## Dependency Usage

### Structural Usage

System prompts include a Persona section:

```markdown
## Persona

### Role and Identity
[Content conforming to v:spec:persona requirements]

### Domain Expertise
[2-4 specific areas, as required by v:spec:persona]

### Approach and Methodology
[Behavioral approach, as required by v:spec:persona]

### Communication Tone
[Tone specification, as required by v:spec:persona]

### Boundaries and Limitations
[≥3 items, as required by v:spec:persona]
```

### Requirements

- **Required:** Yes - system prompts MUST have a persona subsection
- **Cardinality:** Exactly one persona per system prompt
- **Conformance:** Persona subsection MUST satisfy all requirements from `v:spec:persona`
- **Declared:** Listed in `dependencies` field of system_prompt frontmatter

### Verification

When verifying a system_prompt document:
1. Check it has a `## Persona` section
2. Extract that subsection
3. Verify extracted subsection conforms to `v:spec:persona`
4. Report subsection verification results

## Compositional Justification

### Why Composition Not Inheritance

**System prompts are NOT personas** (they don't extend persona). System prompts are composite documents that **contain** a persona component.

- ❌ **Not inheritance:** system_prompt doesn't "is-a" persona
- ✅ **Composition:** system_prompt "has-a" persona (plus purpose and protocol)

### Why Typed Subsections

The typed subsection pattern enables:

1. **Modularity:** Personas can be designed and verified independently
2. **Reusability:** Same persona spec can be used across multiple system prompts
3. **Type Safety:** Subsections have defined structure and can be mechanically verified
4. **Clear Separation:** Persona focuses on WHO, system_prompt integrates WHO + WHAT + HOW

### Relationship to PPP Framework

In the PPP (Persona-Purpose-Protocol) framework:
- **Persona:** WHO the AI is
- **Purpose:** WHAT the AI does
- **Protocol:** HOW the AI works

System prompts integrate all three into a complete AI model configuration. Each component is defined by its own spec, and the system_prompt spec defines how they compose.

### Relationship to Assurance

**Separate Assurance Paths:**

```
Compositional dependency:
  v:spec:system_prompt --depends-on--> v:spec:persona

Assurance for system_prompt:
  v:spec:system_prompt --verifies--> v:spec:spec
  v:spec:system_prompt --validates--> v:guidance:spec

Assurance for persona:
  v:spec:persona --verifies--> v:spec:spec
  v:spec:persona --validates--> v:guidance:spec
```

Both are assured independently. The dependency edge just tracks that system_prompt uses persona structurally.

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
