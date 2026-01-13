# Domain Packs Implementation Plan

This document tracks the implementation of the domain pack system for AAA-docware.

## Overview

The pack system organizes content into self-contained domain packs with their own ontologies, rules, and demo charts. Each pack declares dependencies on other packs.

## Dependency Hierarchy

```text
boundary (Tier 0) - Genesis bootstrap        ─┐
    │               SS, SG, GS, GG            │ Auto-builds on
    │                                         │ `aaa init`
    └── foundation (Tier 1) - Ontology layer  │
            │                                 │
            └── meta (Tier 2) - Infrastructure─┘
                    │           chart, assurance-audit, runbook
                    │
                    ├── ppp (Tier 3) ────────── Persona, Purpose, Protocol
                    │
                    ├── rbac (Tier 3) ───────── Signers, roles, signatures
                    │
                    ├── learning (Tier 3) ───── Students, skills, modules
                    │
                    ├── architecture (Tier 3) ─ Field-survey → physical
                    │
                    └── planning (Tier 4) ───── Lifecycle, program-plan
                                                (depends on architecture)
```

## Pack Requirements

Each pack requires:

| Component | Description |
|-----------|-------------|
| README.md | Pack overview, dependencies, vertex/edge/face types |
| pack.yaml | Manifest with name, tier, dependencies, vertex/edge/face types |
| ontology.md | Formal type definitions extending base ontology |
| rules.py | Python module with domain-specific verification rules |
| examples/ | Usage examples demonstrating pack features |
| charts/ | Demo charts that pass all ontology checks |

## Implementation Status

### Tier 0: Boundary Pack

| Task | Status | Notes |
|------|--------|-------|
| README.md | ⬜ Pending | Genesis bootstrap documentation |
| pack.yaml | ⬜ Pending | Manifest with SS, SG, GS, GG types |
| ontology.md | ⬜ Pending | Bootstrap type definitions |
| rules.py | ⬜ Pending | Self-reference validation rules |
| examples/ | ⬜ Pending | Bootstrap usage example |
| demo chart | ⬜ Pending | boundary-complex chart |

### Tier 1: Foundation Pack

| Task | Status | Notes |
|------|--------|-------|
| README.md | ⬜ Pending | Ontology layer documentation |
| pack.yaml | ⬜ Pending | Manifest with ontology types |
| ontology.md | ⬜ Pending | spec, guidance, doc type definitions |
| rules.py | ⬜ Pending | Coupling, verification, validation rules |
| examples/ | ⬜ Pending | Basic V&V example |
| demo chart | ⬜ Pending | foundation-types chart |

### Tier 2: Meta Pack

| Task | Status | Notes |
|------|--------|-------|
| README.md | ✅ Done | |
| pack.yaml | ✅ Done | |
| ontology.md | ⬜ Pending | chart, assurance-audit, runbook types |
| rules.py | ⬜ Pending | Chart completeness rules |
| examples/ | ⬜ Pending | Assurance audit example |
| demo chart | ⬜ Pending | demo-assurance-audit chart |

### Tier 3: PPP Pack

| Task | Status | Notes |
|------|--------|-------|
| README.md | ✅ Done | |
| pack.yaml | ✅ Done | |
| ontology.md | ⬜ Pending | persona, purpose, protocol types |
| rules.py | ⬜ Pending | PPP triad validation rules |
| examples/ | ⬜ Pending | LLM specialization example |
| demo chart | ⬜ Pending | demo-ppp-triad chart |

### Tier 3: RBAC Pack

| Task | Status | Notes |
|------|--------|-------|
| README.md | ✅ Done | |
| pack.yaml | ✅ Done | |
| ontology.md | ⬜ Pending | signer, role, signature types |
| rules.py | ⬜ Pending | Signature adjacency rules (key!) |
| examples/ | ⬜ Pending | Authorization chain example |
| demo chart | ⬜ Pending | demo-authorization-chain chart |

### Tier 3: Learning Pack

| Task | Status | Notes |
|------|--------|-------|
| README.md | ✅ Done | |
| pack.yaml | ✅ Done | |
| ontology.md | ⬜ Pending | student, skill, syllabus types |
| rules.py | ⬜ Pending | Prerequisite validation rules |
| examples/ | ⬜ Pending | Course completion example |
| demo chart | ⬜ Pending | demo-course-completion chart |

### Tier 3: Architecture Pack

| Task | Status | Notes |
|------|--------|-------|
| README.md | ✅ Done | |
| pack.yaml | ✅ Done | |
| ontology.md | ⬜ Pending | Architecture stack types |
| rules.py | ⬜ Pending | Stack ordering rules |
| examples/ | ⬜ Pending | Architecture stack example |
| demo chart | ⬜ Pending | demo-architecture-stack chart |

### Tier 4: Planning Pack

| Task | Status | Notes |
|------|--------|-------|
| README.md | ✅ Done | |
| pack.yaml | ✅ Done | |
| ontology.md | ⬜ Pending | lifecycle, program-plan types |
| rules.py | ⬜ Pending | Lifecycle precedence rules |
| examples/ | ⬜ Pending | Program lifecycle example |
| demo chart | ⬜ Pending | demo-program-lifecycle chart |

### Infrastructure

| Task | Status | Notes |
|------|--------|-------|
| src/aaa/core/packs.py | ⬜ Pending | Pack loader infrastructure |
| Update rules.py | ⬜ Pending | Load pack rules dynamically |
| CLI: aaa pack list | ⬜ Pending | List available packs |
| CLI: aaa pack check | ⬜ Pending | Validate pack rules |
| CLI: aaa pack deps | ⬜ Pending | Show dependency tree |
| Move packs to src/aaa/ | ⬜ Pending | Final pack location |

## Working Together

### How to Collaborate

1. **Pick a pack**: Start with Tier 0 (boundary) since all other packs depend on it. Work up through the tiers.

2. **For each pack, work through components in order**:
   - README.md first (establishes context)
   - pack.yaml (formal manifest)
   - ontology.md (type definitions)
   - rules.py (validation logic)
   - examples/ (usage demonstration)
   - demo chart (validates everything works)

3. **Verify as you go**:
   ```bash
   # After creating/modifying any document
   uv run aaa verify <file>

   # After creating demo charts
   uv run aaa check rules
   uv run aaa audit <chart>

   # Run full test suite periodically
   uv run pytest tests/ -v
   ```

### Rule Factoring Guidance

**Important**: Rules are factored across packs. A rule should live in the pack that introduces the concept it validates.

| Rule | Pack | Rationale |
|------|------|-----------|
| Verification edge endpoints | foundation | Core V&V concept |
| Coupling uniqueness | foundation | Core V&V concept |
| Assurance face boundary | foundation | Core V&V concept |
| Chart correctness | meta | Charts allow rule checking |
| Factory produces | meta | creates input-output relations|
| Runbook composes factories | meta | facilitates workflow|
| PPP triad completeness | ppp | PPP factory for system prompt |
| Signature adjacency | rbac | RBAC introduces signatures |
| Authorization chain | rbac | RBAC introduces authorization |
| Architecture stack order | architecture | runbook for design documents|
| Lifecycle precedence | planning | Planning introduces lifecycle |
| Program Plan | planning | augments lifecycle with resources

**Key insight**: Assurances without RBAC cannot require signature adjacency. That rule is introduced in the RBAC pack, not in foundation or meta.

### Request Format

When asking for help with a specific task, include:

1. **Which pack** you're working on
2. **Which component** (README, ontology, rules, etc.)
3. **Any specific requirements** or constraints
4. **Related existing content** to reference

Example:
> "I need help with the RBAC pack's rules.py. It should include the signature adjacency rule that requires signature faces to be adjacent to assurance faces. Reference the existing rules in src/aaa/core/rules.py for the pattern."

### Verification Commands

```bash
# Verify single document
uv run aaa verify 00_vertices/my-spec.md

# Verify all documents
uv run aaa verify --all

# Build cache and validate
uv run aaa build

# Check ontology rules
uv run aaa check rules

# Audit a chart
uv run aaa audit charts/my-chart

# Check topology
uv run aaa check topology charts/my-chart

# Run tests
uv run pytest tests/ -v
```

## Priority Order

1. **Boundary pack** (Tier 0) - Everything depends on this
2. **Foundation pack** (Tier 1) - Core ontology types
3. **Meta pack** (Tier 2) - Infrastructure specs
4. **RBAC pack** (Tier 3) - Signature rules are key
5. **PPP pack** (Tier 3) - LLM specialization
6. **Architecture pack** (Tier 3) - Design documentation
7. **Planning pack** (Tier 4) - Program management
8. **Learning pack** (Tier 3) - Educational content
9. **Infrastructure** - Pack loader and CLI commands

## Notes

- All packs will eventually live in `src/aaa/` as Python submodules
- Tier 0-2 packs auto-build on `aaa init`
- Tier 3-4 packs are optional, installed on request
- Demo charts must pass `aaa check rules` before a pack is complete