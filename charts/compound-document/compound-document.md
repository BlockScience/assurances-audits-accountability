---
type: chart/standard
extends: chart
id: c:compound-document
name: Compound Document - PPP Framework Demonstration
description: Complete demonstration of document composition using the Persona-Purpose-Protocol (PPP) framework, showing how a system_prompt is composed from three component documents with full quality infrastructure

# Chart construction metadata
constructed_by: "claude-assistant"
construction_method: assisted
construction_date: 2025-12-29T00:00:00Z

# Chart purpose
purpose: Demonstrate document composition pattern where system_prompt embeds persona, purpose, and protocol documents via Obsidian embeds, then compiles to standalone document
scope: 13 vertices (4 specs, 4 guidances, 4 concrete docs, 1 compiled), 16 edges, 4 assurance faces

# Elements comprising this chart
elements:
  vertices:
    # Specifications - define structure for each document type
    - v:spec:persona
    - v:spec:purpose
    - v:spec:protocol
    - v:spec:system_prompt
    # Guidances - quality criteria for each document type
    - v:guidance:persona
    - v:guidance:purpose
    - v:guidance:protocol
    - v:guidance:system_prompt
    # Concrete documents - the actual PPP implementation
    - v:persona:claude-assistant
    - v:purpose:claude-assistant
    - v:protocol:claude-assistant
    - v:system_prompt:claude-assistant
    # Compiled output - standalone deployable document
    - v:system_prompt:claude-assistant-compiled
  edges:
    # Coupling edges - link spec to guidance for each document type
    - e:coupling:persona
    - e:coupling:purpose
    - e:coupling:protocol
    - e:coupling:system_prompt
    # Dependency edges - system_prompt composition dependencies
    - e:dependency:system_prompt-claude:persona-claude
    - e:dependency:system_prompt-claude:purpose-claude
    - e:dependency:system_prompt-claude:protocol-claude
    # Compilation edge - compositional to compiled
    - e:compilation:system_prompt-compiled:system_prompt-reference
    # Verification edges - automated checks against specs
    - e:verification:persona-claude:spec
    - e:verification:purpose-claude:spec
    - e:verification:protocol-claude:spec
    - e:verification:system_prompt-compiled:spec
    # Validation edges - human review against guidances
    - e:validation:persona-claude:guidance
    - e:validation:purpose-claude:guidance
    - e:validation:protocol-claude:guidance
    - e:validation:system_prompt-compiled:guidance
  faces:
    # Assurance triangles - complete quality attestation
    - f:assurance:persona-claude
    - f:assurance:purpose-claude
    - f:assurance:protocol-claude
    - f:assurance:system_prompt-compiled

tags:
  - chart
  - standard
  - compound-document
  - ppp
  - composition
  - system_prompt
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
---

# Compound Document - PPP Framework Demonstration

This chart demonstrates the **Persona-Purpose-Protocol (PPP) framework** for creating compound documents. It shows how a `system_prompt` document is composed from three component documents (`persona`, `purpose`, `protocol`), each with their own specifications, guidances, and quality assurance.

## Document Composition Pattern

The PPP framework follows a specific design order:

1. **Purpose** (designed FIRST) - Establishes what value is delivered
2. **Persona** (designed second) - Matches expertise to purpose
3. **Protocol** (designed LAST) - Integrates persona and purpose into operational workflow

The `system_prompt` document then composes these three via Obsidian-style embeds:

```markdown
## Persona
![[persona-claude-assistant]]

## Purpose
![[purpose-claude-assistant]]

## Protocol
![[protocol-claude-assistant]]
```

## Chart Structure

### Vertices (13)

| Category | Vertices | Role |
|----------|----------|------|
| **Specs** | persona, purpose, protocol, system_prompt | Define valid structure |
| **Guidances** | persona, purpose, protocol, system_prompt | Define quality criteria |
| **Concrete Docs** | persona-claude, purpose-claude, protocol-claude, system_prompt-claude | Actual content |
| **Compiled** | system_prompt-compiled | Standalone deployment |

### Edges (16)

| Type | Count | Role |
|------|-------|------|
| **Coupling** | 4 | Link spec ↔ guidance for each type |
| **Dependency** | 3 | System_prompt depends on components |
| **Verification** | 4 | Automated checks against specs |
| **Validation** | 4 | Human review against guidances |

### Faces (4)

Each concrete document has a complete **assurance triangle**:
- `f:assurance:persona-claude`
- `f:assurance:purpose-claude`
- `f:assurance:protocol-claude`
- `f:assurance:system_prompt-compiled`

## Visual Structure

```
    ┌─────────────────────────────────────────────────────────────┐
    │                    TYPE LAYER (specs + guidances)            │
    │  [spec:persona] ←→ [guidance:persona]                       │
    │  [spec:purpose] ←→ [guidance:purpose]                       │
    │  [spec:protocol] ←→ [guidance:protocol]                     │
    │  [spec:system_prompt] ←→ [guidance:system_prompt]           │
    └─────────────────────────────────────────────────────────────┘
                    ↓ verify              ↓ validate
    ┌─────────────────────────────────────────────────────────────┐
    │                    INSTANCE LAYER (concrete docs)           │
    │                                                             │
    │      [persona:claude] ←──┐                                  │
    │      [purpose:claude] ←──┼── depends ── [system_prompt]     │
    │      [protocol:claude] ←─┘                                  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
                              │
                              ↓ compile
    ┌─────────────────────────────────────────────────────────────┐
    │                    OUTPUT LAYER                             │
    │              [system_prompt-compiled]                       │
    │         (standalone document with embeds expanded)          │
    └─────────────────────────────────────────────────────────────┘
```

## Key Relationships

### Composition Dependencies

The system_prompt document declares dependencies on its component documents:

- `e:dependency:system_prompt-claude:persona-claude` - embeds persona
- `e:dependency:system_prompt-claude:purpose-claude` - embeds purpose
- `e:dependency:system_prompt-claude:protocol-claude` - embeds protocol

### Quality Assurance Triangles

Each assurance face represents a complete quality triangle:

```
         [coupling]
    spec ←────────→ guidance
      \             /
       \           /
   verify\       /validate
         \     /
          \   /
           ↓ ↓
        [document]
           ↓
      [assurance face]
```

## Compilation Process

The `compile_document.py` script transforms the compositional document:

```bash
python scripts/compile_document.py \
    00_vertices/system_prompt-claude-assistant.md \
    00_vertices/system_prompt-claude-assistant-compiled.md
```

This expands `![[...]]` embeds into inline content, creating a standalone document suitable for deployment.

## Use Cases

1. **AI System Configuration**: Creating complete model configurations with clear separation of concerns
2. **Role Documentation**: Defining personas with associated purposes and protocols
3. **Workflow Specification**: Documenting systematic processes with quality assurance
4. **Template-Based Generation**: Using specs and guidances to guide document creation

## Related Charts

- `charts/boundary-complex/` - Foundational spec/guidance relationships
- `charts/chart-types-audit/` - Doc-kit registry patterns