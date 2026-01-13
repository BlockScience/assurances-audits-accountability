# PPP Domain Pack - Persona-Purpose-Protocol Framework

## Overview

The PPP (Persona-Purpose-Protocol) framework provides a structured approach to defining AI assistant configurations. It separates concerns into three coupled document types:

- **Persona**: Who the assistant is (identity, expertise, communication style)
- **Purpose**: What the assistant does (objectives, deliverables, success criteria)
- **Protocol**: How the assistant operates (procedures, workflows, tool usage)

## Dependencies

- **boundary**: Genesis bootstrap (SS, SG, GS, GG)
- **foundation**: Ontology layer
- **meta**: Infrastructure specs (charts, factories)

## Vertex Types

### persona
Defines the AI assistant's identity and character.

| Field | Description |
|-------|-------------|
| role | Primary role/function |
| expertise | Domain knowledge areas |
| tone | Communication style |
| boundaries | What the persona will/won't do |

### purpose
Defines what value the assistant provides.

| Field | Description |
|-------|-------------|
| problem_statement | What problem is being solved |
| objectives | Specific goals |
| deliverables | What the assistant produces |
| success_criteria | How to measure success |

### protocol
Defines operational procedures.

| Field | Description |
|-------|-------------|
| phases | Workflow phases |
| tools | Available tools and when to use them |
| validation_points | User interaction checkpoints |
| error_handling | How to handle failures |

### actor
A named entity that can perform actions. Broader than persona - can represent humans, systems, or AI assistants.

### system-prompt
A compiled document combining persona + purpose + protocol into a single system prompt for deployment.

## Edge Types

Uses standard edge types from foundation:
- `edge/coupling` - Links persona ↔ purpose ↔ protocol
- `edge/verification` - Structural compliance checking
- `edge/validation` - Quality assessment

## Face Types

Uses standard face types from foundation:
- `face/assurance` - Complete assurance triangle
- `face/signature` - Human accountability

## Domain Rules

### ppp_triad_completeness
**Severity:** warning

A persona document should have corresponding purpose and protocol documents to form a complete triad. Incomplete triads may indicate work-in-progress.

### system_prompt_sources
**Severity:** warning

System prompt documents should reference their source persona, purpose, and protocol documents to maintain traceability.

## Demo Chart

See `charts/demo-ppp-triad.md` for an example of a complete PPP triad with full assurance.

## Usage

1. Create a persona document defining the assistant's identity
2. Create a purpose document defining objectives
3. Create a protocol document defining procedures
4. Create coupling edges between all three
5. Create verification/validation edges for each
6. Create assurance faces to complete the quality chain
7. Optionally compile into a system-prompt document

## Related Packs

- **meta**: Provides chart and assurance-audit types used to organize PPP documents
- **rbac**: Provides signer/role types for signing validations
