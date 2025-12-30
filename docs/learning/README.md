# Knowledge Complex Learning Path

Welcome to the Knowledge Complex learning journey. This guide walks you through 10 progressive modules that build your expertise from foundational concepts to organizational topology mastery.

**Total journey**: 10 modules, ~6-8 hours of hands-on learning

---

## How to Use This Guide

1. **Follow modules in order** - Each builds on previous concepts
2. **Do the exercises** - Hands-on practice solidifies understanding
3. **Use Obsidian** - Open this repo as a vault for easy navigation
4. **Run the tools** - Verify your understanding with actual commands
5. **Build your own** - Apply concepts to your own documentation

---

## Learning Philosophy

This knowledge complex uses **typed simplicial complexes** to represent structured knowledge. You'll learn:

- **Topology** - Vertices, edges, faces, and how they form valid structures
- **Type Systems** - Semantic meaning layered on topological structure
- **Quality Frameworks** - Verification, validation, and assurance
- **Composition** - Building complex documents from reusable components
- **Organizational Modeling** - Teams, resources, and coordination patterns
- **Algebraic Topology** - Hodge decomposition and structural analysis

**Core Insight:** Documentation quality can be represented as **topological properties** - making it verifiable, traceable, and maintainable.

---

## The Complete Syllabus

The full learning journey is itself a knowledge complex chart:

- **Location**: [charts/learning-journey-full/](../../charts/learning-journey-full/)
- **Visualization**: [learning-journey-full.html](../../charts/learning-journey-full/learning-journey-full.html)
- **Topology**: V=32, E=70, F=35, χ=-3

---

## Module Overview

### Foundations (Modules 01-03)

| Module | Topic | Prerequisites | Develops |
|--------|-------|---------------|----------|
| **01** | [Simplicial Complex Fundamentals](../../charts/learning-journey-module-01/) | sets-and-graphs | simplicial-complex-fundamentals |
| **02** | [Typed Simplicial Complexes](../../charts/learning-journey-module-02/) | simplicial-complex-fundamentals | typed-simplicial-complexes |
| **03** | [Composing Typed Simplicial Complexes](../../charts/learning-journey-module-03/) | simplicial-complex-fundamentals, typed-simplicial-complexes | composing-typed-simplicial-complexes |

**What you'll learn:**

- Vertices, edges, and faces as mathematical objects
- Euler characteristic (χ = V - E + F) and topological holes
- Adding semantic types to structure
- Composing charts via identification (pasting)

### Quality Assurance (Modules 04-05)

| Module | Topic | Prerequisites | Develops |
|--------|-------|---------------|----------|
| **04** | [Verification & Validation](../../charts/learning-journey-module-04/) | typed-simplicial-complexes | verification-validation |
| **05** | [Assurance & Audits](../../charts/learning-journey-module-05/) | verification-validation | assurance-audits |

**What you'll learn:**

- Verification edges (document → spec)
- Validation edges (document → guidance)
- Coupling edges (spec ↔ guidance)
- Assurance triangles as complete quality coverage
- Audit tools for systematic verification

### Document Architecture (Modules 06-07)

| Module | Topic | Prerequisites | Develops |
|--------|-------|---------------|----------|
| **06** | [Document Composition](../../charts/learning-journey-module-06/) | assurance-audits, composing-typed-simplicial-complexes | document-composition |
| **07** | [Reference & Reuse via Doc-Kits](../../charts/learning-journey-module-07/) | assurance-audits | reference-reuse |

**What you'll learn:**

- Compositional documents with typed subsections
- Obsidian embeds and compilation
- Doc-kit pattern (spec + guidance + example)
- Template-driven documentation

**Note:** Module 06 is optional but recommended. Both paths lead to document-architect state.

### Organizational Modeling (Modules 08-10)

| Module | Topic | Prerequisites | Develops |
|--------|-------|---------------|----------|
| **08** | [Team Coordination](../../charts/learning-journey-module-08/) | reference-reuse | team-coordination |
| **09** | [Resource Management](../../charts/learning-journey-module-09/) | team-coordination | resource-management |
| **10** | [Organizational Topology](../../charts/learning-journey-module-10/) | team-coordination, resource-management, composing-typed-simplicial-complexes | topological-data-analysis, organizational-design-analysis |

**What you'll learn:**

- Actor, team, role, staff vertex types
- RACI patterns and role assignments
- Resource and function modeling
- Cross-team resource flows
- Chart composition for organizational analysis
- Hodge decomposition and edge PageRank
- Analysis at scale beyond visualization

---

## Learning States

As you progress through modules, your skill set grows:

| State | After Module | Skills |
|-------|--------------|--------|
| knowledge-complex-learner | (entry) | sets-and-graphs |
| foundational-learner | 01 | +simplicial-complex-fundamentals |
| intermediate-learner | 02 | +typed-simplicial-complexes |
| compositional-learner | 03 | +composing-typed-simplicial-complexes |
| verification-learner | 04 | +verification-validation |
| assurance-learner | 05 | +assurance-audits |
| document-architect | 06/07 | +document-composition (optional), +reference-reuse |
| coordination-architect | 08 | +team-coordination |
| management-architect | 09 | +resource-management |
| **chief-engineer** | 10 | +topological-data-analysis, +organizational-design-analysis |

**Supermodular property**: Skills only accumulate - you never lose skills as you progress.

---

## Quick Start Path

If you're short on time, here's the minimal path to understand the core concepts:

1. **Module 01**: Simplicial Complex Fundamentals (~45 min)
2. **Module 04**: Verification & Validation (~45 min)
3. **Module 05**: Assurance & Audits (~45 min)

**Total**: ~2.5 hours for core quality assurance concepts

---

## Full Journey Path

For complete mastery:

1. Modules 01-03: Foundations (~2 hours)
2. Modules 04-05: Quality (~1.5 hours)
3. Module 07: Doc-Kits (~45 min) - skip 06 if short on time
4. Modules 08-10: Organizations (~2 hours)

**Total**: ~6-8 hours depending on exercises

---

## Tools You'll Use

Throughout the journey, you'll use these scripts:

```bash
# Build element cache (run first)
python scripts/build_cache.py

# Verify chart structure
python scripts/verify_chart.py charts/<chart>/<chart>.md

# Analyze topology
python scripts/topology.py charts/<chart>/<chart>.md --root .

# Export and visualize
python scripts/export_chart_direct.py charts/<chart>/<chart>.md output.json --root .
python scripts/visualize_chart.py output.json

# Verify documents against templates
python scripts/verify_template_based.py <document>.md --templates templates

# Audit assurance coverage
python scripts/audit_assurance_chart.py charts/<chart>/<chart>.md
```

---

## Success Criteria

You've mastered the knowledge complex when you can:

- Calculate Euler characteristic and explain topological holes
- Design typed simplicial complexes for your domain
- Create verification, validation, and assurance edges
- Build compositional documents with templates
- Model organizational structures as charts
- Compose charts via identification
- Apply algebraic topology to structural analysis
- Navigate complexity beyond what visualization can show

---

## Additional Resources

### Documentation

- [README.md](../../README.md) - Repository overview and quick start
- [docs/concepts/](../concepts/) - Reference documentation
- [docs/use-cases/](../use-cases/) - Practical examples

### Charts

- [test-tetrahedron](../../charts/test-tetrahedron/) - Minimal example (4V, 6E, 3F)
- [boundary-complex](../../charts/boundary-complex/) - Self-referential foundation
- [learning-journey-full](../../charts/learning-journey-full/) - Complete syllabus

### Module Charts

Each module has its own chart in `charts/learning-journey-module-XX/`:

- Markdown definition (`.md`)
- JSON export (`.json`)
- HTML visualization (`.html`)

---

## What's Next?

After completing the learning journey:

1. **Build your own knowledge complex** - Start with your documentation domain
2. **Create custom vertex types** - Extend templates for your needs
3. **Design assurance charts** - Systematic quality tracking
4. **Model your organization** - Teams, resources, coordination
5. **Apply at scale** - Use algebraic topology when visualization fails

**Welcome to the knowledge complex!**
