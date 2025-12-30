---
type: edge/dependency
extends: edge
id: e:dependency:system_prompt-claude:purpose-claude
name: Dependency - System Prompt Claude uses Purpose Claude
description: System prompt for Claude assistant includes purpose-claude-assistant as its Purpose subsection
source: v:system_prompt:claude-assistant
target: v:purpose:claude-assistant
source_type: vertex/system_prompt
target_type: vertex/purpose
orientation: directed
dependency_type: compositional
subsection_field: purpose
required: true
tags:
  - edge
  - dependency
version: 1.0.0
created: 2025-12-28T00:10:00Z
modified: 2025-12-28T00:10:00Z
---

# Dependency - System Prompt Claude uses Purpose Claude

This dependency edge tracks that the system_prompt-claude-assistant document includes purpose-claude-assistant as its Purpose subsection using Obsidian embed syntax.

## Dependency Relationship

**Dependent:** [system_prompt-claude-assistant](../00_vertices/system_prompt-claude-assistant.md) - Complete AI model configuration
**Dependency:** [purpose-claude-assistant](../00_vertices/purpose-claude-assistant.md) - WHAT the AI does
**Relationship:** system_prompt includes purpose (compositional)

**Usage:** The system_prompt document has a `## Purpose` section that embeds the purpose-claude-assistant document using Obsidian's `![[purpose-claude-assistant]]` syntax. This creates a compositional dependency where the system prompt is built FROM the purpose component.

**Note on Header Collision:** The system_prompt has TWO `## Purpose` sections - one meta-statement about the system_prompt itself, and one typed subsection containing the AI's purpose. The typed subsection embeds the purpose document.

**Assurance Note:** This dependency edge tracks instance-level composition and is separate from both:
- Spec-level dependencies (v:spec:system_prompt → v:spec:purpose)
- Assurance DAG (system_prompt-claude → spec:system_prompt verification)

## Dependency Usage

**Structural Usage:**
- The system_prompt document contains a `## Purpose` section at level 2 (the typed subsection, not the meta-statement)
- This section embeds `purpose-claude-assistant.md` using `![[purpose-claude-assistant]]`
- The embedded content appears inline when viewed in Obsidian
- The standalone purpose document remains the canonical source

**Field/Subsection:** `## Purpose` section (typed subsection)
**Required:** Yes - system prompts MUST have a purpose component per PPP framework
**Cardinality:** Exactly one purpose per system prompt

## Compositional Justification

**Why Composition:** The PPP framework requires purpose to be designed FIRST (the anchor). Using a separate purpose document with embed provides:
- **Design order enforcement:** Purpose exists independently, designed before persona/protocol
- **Reusability:** The same purpose could inform different system prompts
- **Independent assurance:** Purpose can be verified and validated separately
- **Clear value proposition:** Purpose defines WHAT value is delivered

**Not Inheritance:** This is not "is-a" - system_prompt is not a specialized purpose. It CONTAINS a purpose as a component.

**Not Assurance:** This dependency doesn't prove quality. The purpose must still be verified (structural) and validated (quality) independently.

## Obsidian Integration

The embed syntax `![[purpose-claude-assistant]]` allows:
- Viewing complete content in Obsidian without opening separate file
- Maintaining single source of truth (purpose document is canonical)
- Graph view showing compositional relationships
- Link tracking and refactoring support

## Compilation

For deployment or use outside Obsidian, a compiled version can be generated that expands all embeds into a single markdown file. The compiled version is cached and can be regenerated whenever dependencies change.

---

**Note:** This is an instance-level dependency (document → document), distinct from the spec-level dependencies (v:spec:system_prompt → v:spec:purpose) that define the compositional pattern. Purpose is the anchor of PPP design.
