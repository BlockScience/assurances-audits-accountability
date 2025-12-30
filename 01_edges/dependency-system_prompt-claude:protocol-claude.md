---
type: edge/dependency
extends: edge
id: e:dependency:system_prompt-claude:protocol-claude
name: Dependency - System Prompt Claude uses Protocol Claude
description: System prompt for Claude assistant includes protocol-claude-assistant as its Protocol subsection
source: v:system_prompt:claude-assistant
target: v:protocol:claude-assistant
source_type: vertex/system_prompt
target_type: vertex/protocol
orientation: directed
dependency_type: compositional
subsection_field: protocol
required: true
tags:
  - edge
  - dependency
version: 1.0.0
created: 2025-12-28T00:10:00Z
modified: 2025-12-28T00:10:00Z
---

# Dependency - System Prompt Claude uses Protocol Claude

This dependency edge tracks that the system_prompt-claude-assistant document includes protocol-claude-assistant as its Protocol subsection using Obsidian embed syntax.

## Dependency Relationship

**Dependent:** [system_prompt-claude-assistant](../00_vertices/system_prompt-claude-assistant.md) - Complete AI model configuration
**Dependency:** [protocol-claude-assistant](../00_vertices/protocol-claude-assistant.md) - HOW the AI works
**Relationship:** system_prompt includes protocol (compositional)

**Usage:** The system_prompt document has a `## Protocol` section that embeds the protocol-claude-assistant document using Obsidian's `![[protocol-claude-assistant]]` syntax. This creates a compositional dependency where the system prompt is built FROM the protocol component.

**Assurance Note:** This dependency edge tracks instance-level composition and is separate from both:
- Spec-level dependencies (v:spec:system_prompt → v:spec:protocol)
- Assurance DAG (system_prompt-claude → spec:system_prompt verification)

## Dependency Usage

**Structural Usage:**
- The system_prompt document contains a `## Protocol` section at level 2
- This section embeds `protocol-claude-assistant.md` using `![[protocol-claude-assistant]]`
- The embedded content appears inline when viewed in Obsidian
- The standalone protocol document remains the canonical source

**Field/Subsection:** `## Protocol` section
**Required:** Yes - system prompts MUST have a protocol component per PPP framework
**Cardinality:** Exactly one protocol per system prompt

## Compositional Justification

**Why Composition:** The PPP framework requires protocol to be designed LAST (to integrate persona and purpose). Using a separate protocol document with embed provides:
- **Design order enforcement:** Protocol is designed after purpose and persona
- **Integration clarity:** Protocol explicitly integrates persona's approach with purpose's objectives
- **Independent assurance:** Protocol can be verified and validated separately
- **Operational focus:** Protocol defines HOW to operationalize purpose through persona

**Not Inheritance:** This is not "is-a" - system_prompt is not a specialized protocol. It CONTAINS a protocol as a component.

**Not Assurance:** This dependency doesn't prove quality. The protocol must still be verified (structural) and validated (quality) independently.

## Obsidian Integration

The embed syntax `![[protocol-claude-assistant]]` allows:
- Viewing complete content in Obsidian without opening separate file
- Maintaining single source of truth (protocol document is canonical)
- Graph view showing compositional relationships
- Link tracking and refactoring support

## Compilation

For deployment or use outside Obsidian, a compiled version can be generated that expands all embeds into a single markdown file. The compiled version is cached and can be regenerated whenever dependencies change.

---

**Note:** This is an instance-level dependency (document → document), distinct from the spec-level dependencies (v:spec:system_prompt → v:spec:protocol) that define the compositional pattern. Protocol is designed LAST in PPP to integrate persona and purpose.
