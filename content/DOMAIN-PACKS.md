# Domain Packs - Design Document

This document outlines the plan for organizing content into self-contained domain packs with their own ontologies, rules, and demo charts.

## Overview

Each domain pack is a self-contained extension to the knowledge complex that:
1. Has its own README documenting the domain
2. Defines an ontology (vertex types, edge types, face types)
3. Provides rules for validating domain-specific constraints
4. Includes at least one demo chart showing the domain in action
5. Declares dependencies on other domain packs

## Domain Pack Structure

```
content/<domain>/
├── README.md           # Domain documentation
├── ontology.md         # Domain ontology (extends base ontology)
├── rules.py            # Domain-specific validation rules
├── charts/             # Demo charts for this domain
│   └── demo-<domain>.md
├── 00_vertices/        # Domain vertices (specs, guidances, instances)
├── 01_edges/           # Domain edges
└── 02_faces/           # Domain faces
```

## Dependency Graph

```
boundary (Tier 0) - Genesis bootstrap
    │               SS, SG, GS, GG (spec/guidance combinations)
    │
    └── foundation (Tier 1) - Ontology layer
            │                 spec:ontology, guidance:ontology, ontology:base
            │
            └── meta (Tier 2) - Infrastructure specs
                    │           chart, assurance-audit, runbook, factory,
                    │           organization, repository-policy
                    │
                    ├── ppp (Tier 3) ────────── Persona, Purpose, Protocol, system-prompt
                    │
                    ├── rbac (Tier 3) ───────── signers, signatures, roles, authorization
                    │
                    ├── learning (Tier 3) ───── student, skill, syllabus, learning-module
                    │
                    ├── architecture (Tier 3) ─ field-survey, conceptual, functional,
                    │                           logical, physical, requirements-trace
                    │
                    └── planning (Tier 4) ← architecture
                                            lifecycle, program-plan, program-memo,
                                            implementation-plan
```

**Key Design Decisions:**
- Boundary is truly primitive - just the four spec/guidance combinations
- Foundation adds the ontology layer (how to define types)
- Meta adds infrastructure for organizing content (charts, factories)
- Domain packs (Tier 3) are peers - all require boundary + foundation + meta
- Only planning has a cross-domain dependency (on architecture)

## Domain Packs

### Tier 0: Boundary (bundled)

- **Location:** `src/aaa/boundary/`
- **Dependencies:** None (genesis bootstrap)
- **Provides:** SS, SG, GS, GG (spec/guidance combinations)
- **Rules:** Structural only (documents exist, have frontmatter)

### Tier 1: Foundation (bundled)

- **Location:** `src/aaa/foundation/`
- **Dependencies:** boundary
- **Provides:** spec:ontology, guidance:ontology, ontology:base
- **Rules:** Ontology rules (types are valid, extend correctly)

### Tier 2: Meta (bundled)

- **Dependencies:** boundary, foundation
- **Provides:**
  - Vertex types: chart, assurance-audit, runbook, factory, organization, repository-policy
  - Edge types: (standard verification/validation/coupling)
  - Face types: assurance (structural only, no signature requirement)
- **Rules:** Chart rules (topology, completeness)
- **Demo chart:** Assurance audit chart

### Tier 3: Domain Packs (peers)

#### ppp (Persona-Purpose-Protocol)

- **Dependencies:** boundary, foundation, meta
- **Provides:**
  - Vertex types: persona, purpose, protocol, system-prompt
  - Edge types: (standard)
  - Face types: (standard assurance)
- **Demo chart:** PPP triad showing persona + purpose + protocol assured together

#### rbac (Role-Based Access Control)

- **Dependencies:** boundary, foundation, meta
- **Provides:**
  - Vertex types: signer, role
  - Edge types: signs, qualifies, has-role, conveys
  - Face types: signature, authorization
- **Rules:** Signature adjacency (assurance requires signature)
- **Demo chart:** Multi-signer authorization chain

#### learning (Educational Content)

- **Dependencies:** boundary, foundation, meta
- **Provides:**
  - Vertex types: student, skill, syllabus, learning-module
  - Edge types: studies, has-skill, requires-skill, inherits
  - Face types: prerequisite, skill-gain, completion
- **Demo chart:** Course completion (student gains skills through modules)

#### architecture

- **Dependencies:** boundary, foundation, meta
- **Provides:**
  - Vertex types: architecture, conceptual-architecture, functional-architecture, logical-architecture, physical-architecture, field-survey, novel-contributions, requirements-trace
  - Edge types: dependency (between architecture docs)
  - Face types: (standard assurance)
- **Demo chart:** Architecture stack (conceptual → functional → logical → physical)

### Tier 4: Planning

#### planning

- **Dependencies:** boundary, foundation, meta, architecture
- **Provides:**
  - Vertex types: lifecycle, program-plan, program-memo, implementation-plan
  - Edge types: dependency (between planning docs)
  - Face types: (standard assurance)
- **Demo chart:** Program lifecycle (lifecycle → plan → memo → impl-plan)

## Implementation Plan

### Phase 1: Infrastructure
- [ ] Create domain pack template files
- [ ] Add `pack.yaml` manifest format
- [ ] Update `registry.yaml` to track pack dependencies
- [ ] Create pack loader in `rules.py`

### Phase 2: Core Packs (Tier 1)
- [ ] ppp pack: README, ontology, rules, demo chart
- [ ] meta pack: README, ontology, rules, demo chart
- [ ] rbac pack: README, ontology, rules, demo chart

### Phase 3: Domain Packs (Tier 2)
- [ ] architecture pack: README, ontology, rules, demo chart
- [ ] planning pack: README, ontology, rules, demo chart

### Phase 4: Specialized Packs (Tier 3)
- [ ] learning pack: README, ontology, rules, demo chart

### Phase 5: Tooling
- [ ] `aaa pack list` - list available packs
- [ ] `aaa pack check <pack>` - validate pack rules
- [ ] `aaa pack deps <pack>` - show dependency tree
- [ ] Update `aaa check rules` to load pack rules

## Pack Manifest Format (pack.yaml)

```yaml
name: ppp
version: 1.0.0
description: Persona-Purpose-Protocol framework for AI system documentation
dependencies:
  - foundation

ontology:
  vertex_types:
    - persona
    - purpose
    - protocol
    - actor
    - system-prompt
  edge_types: []  # uses standard types
  face_types: []  # uses standard types

rules:
  - ppp_triad_completeness  # persona must have purpose and protocol
  - actor_has_persona       # actors must reference a persona

demo_charts:
  - charts/demo-ppp.md
```

## Rules Extension Format

Each domain pack can provide a `rules.py` that exports:

```python
# content/ppp/rules.py

VERTEX_TYPES = {
    'vertex/persona': {...},
    'vertex/purpose': {...},
    'vertex/protocol': {...},
}

EDGE_RULES = {
    # edge type: (allowed_sources, allowed_targets)
}

FACE_RULES = {
    # face type: boundary requirements
}

def check_ppp_triad(chart_data):
    """Check that PPP documents form complete triads."""
    errors = []
    # ... validation logic
    return errors

LOCAL_RULES = [
    check_ppp_triad,
]
```

## Next Steps

1. Create `content/ppp/pack.yaml` as first example
2. Extract PPP-specific rules from main `rules.py`
3. Create `content/ppp/README.md` documenting the framework
4. Build demo chart for PPP triad
5. Repeat for other domain packs

## Notes

- The foundation pack is special - bundled with the package, not in content/
- Packs can be disabled/enabled via registry.yaml
- Pack rules are additive - they extend, not replace, foundation rules
- Demo charts serve as both documentation and regression tests
