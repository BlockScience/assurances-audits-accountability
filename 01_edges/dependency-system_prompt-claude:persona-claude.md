---
type: edge/dependency
extends: edge
id: e:dependency:system_prompt-claude:persona-claude
name: Dependency - System Prompt Claude uses Persona Claude
description: System prompt for Claude assistant includes persona-claude-assistant as its Persona subsection
source: v:system_prompt:claude-assistant
target: v:persona:claude-assistant
source_type: vertex/system_prompt
target_type: vertex/persona
orientation: directed
dependency_type: compositional
subsection_field: persona
required: true
tags:
  - edge
  - dependency
version: 1.0.0
created: 2025-12-28T00:10:00Z
modified: 2025-12-28T00:10:00Z
---

# Dependency - System Prompt Claude uses Persona Claude

This dependency edge tracks that the system_prompt-claude-assistant document includes persona-claude-assistant as its Persona subsection using Obsidian embed syntax.

## Dependency Relationship

**Dependent:** [system_prompt-claude-assistant](../00_vertices/system_prompt-claude-assistant.md) - Complete AI model configuration
**Dependency:** [persona-claude-assistant](../00_vertices/persona-claude-assistant.md) - WHO the AI is
**Relationship:** system_prompt includes persona (compositional)

**Usage:** The system_prompt document has a `## Persona` section that embeds the persona-claude-assistant document using Obsidian's `![[persona-claude-assistant]]` syntax. This creates a compositional dependency where the system prompt is built FROM the persona component.

**Assurance Note:** This dependency edge tracks instance-level composition and is separate from both:
- Spec-level dependencies (v:spec:system_prompt → v:spec:persona)
- Assurance DAG (system_prompt-claude → spec:system_prompt verification)

## Dependency Usage

**Structural Usage:**
- The system_prompt document contains a `## Persona` section at level 2
- This section embeds `persona-claude-assistant.md` using `![[persona-claude-assistant]]`
- The embedded content appears inline when viewed in Obsidian
- The standalone persona document remains the canonical source

**Field/Subsection:** `## Persona` section
**Required:** Yes - system prompts MUST have a persona component per PPP framework
**Cardinality:** Exactly one persona per system prompt

## Compositional Justification

**Why Composition:** The PPP (Persona-Purpose-Protocol) framework requires system prompts to be composed of three distinct components. Using separate documents with embeds provides:
- **Single source of truth:** Persona is defined once in persona-claude-assistant.md
- **Reusability:** The same persona could be used in different system prompts
- **Independent assurance:** Persona can be verified and validated separately
- **Clear modularity:** Each component has its own lifecycle and quality checks

**Not Inheritance:** This is not "is-a" - system_prompt is not a specialized persona. It CONTAINS a persona as a component.

**Not Assurance:** This dependency doesn't prove quality. The persona must still be verified (structural) and validated (quality) independently.

## Obsidian Integration

The embed syntax `![[persona-claude-assistant]]` allows:
- Viewing complete content in Obsidian without opening separate file
- Maintaining single source of truth (persona document is canonical)
- Graph view showing compositional relationships
- Link tracking and refactoring support

## Compilation

For deployment or use outside Obsidian, a compiled version can be generated that expands all embeds into a single markdown file. The compiled version is cached and can be regenerated whenever dependencies change.

---

**Note:** This is an instance-level dependency (document → document), distinct from the spec-level dependencies (v:spec:system_prompt → v:spec:persona) that define the compositional pattern.
