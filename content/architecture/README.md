# Design Documents

This directory contains the design documentation for the AAA (Assurances, Audits, Accountability) framework.

## Contents

### Architecture Documents

The framework follows a 4-layer architecture pattern (conceptual, functional, logical, physical):

| Document | Description |
|----------|-------------|
| [field-survey-knowledge-complex-refactor.md](field-survey-knowledge-complex-refactor.md) | Initial survey and problem analysis |
| [conceptual-architecture-knowledge-complex-refactor.md](conceptual-architecture-knowledge-complex-refactor.md) | High-level concepts and stakeholder concerns |
| [functional-architecture-knowledge-complex-refactor.md](functional-architecture-knowledge-complex-refactor.md) | Functional decomposition and capabilities |
| [logical-architecture-knowledge-complex-refactor.md](logical-architecture-knowledge-complex-refactor.md) | Logical structure and component relationships |
| [physical-architecture-knowledge-complex-refactor.md](physical-architecture-knowledge-complex-refactor.md) | Concrete implementation elements |
| [architecture-knowledge-complex-refactor.md](architecture-knowledge-complex-refactor.md) | Architecture overview and summary |

### Requirements Traceability

| Document | Description |
|----------|-------------|
| [requirements-trace-knowledge-complex-refactor.md](requirements-trace-knowledge-complex-refactor.md) | Requirements traceability matrix |
| [doc-requirements-trace-knowledge-complex-refactor.md](doc-requirements-trace-knowledge-complex-refactor.md) | Requirements documentation |

### Ontology

| Document | Description |
|----------|-------------|
| [ontology-base.md](ontology-base.md) | Core type system and ontology definitions |

### Implementation Plans

| Document | Description |
|----------|-------------|
| [impl-plans/doc-impl-plan-physical-architecture-refactor.md](impl-plans/doc-impl-plan-physical-architecture-refactor.md) | Physical architecture implementation plan |

## Usage

These documents are reference material for understanding the framework's design. They are not part of the runtime system but inform the implementation of:

- The type system in `templates/`
- The verification scripts in `scripts/`
- The CLI in `src/aaa/`

## Relationship to Framework

The design documents describe *how* the framework works. The framework itself (specs, guidance, templates) describes *what* documents should contain. This separation allows:

1. Design evolution without breaking verified documents
2. Clear distinction between framework development and framework usage
3. Implementation plans to be tracked separately from the framework they implement
