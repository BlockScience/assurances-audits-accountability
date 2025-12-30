---
type: vertex/skill
extends: vertex/property
id: v:skill:topological-data-analysis
name: Topological Data Analysis
description: Understanding Hodge decomposition, edge PageRank, and algebraic topology methods for analyzing complex organizational structures
tags:
  - vertex
  - property
  - skill
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
domain: knowledge-complexes
level: advanced
---

# Topological Data Analysis

## Purpose

This skill defines the capability to apply algebraic topology methods to analyze complex organizational structures. It represents mastery of Hodge decomposition, edge PageRank, and the semantic interpretation of topological features in organizational charts.

## Property Definition

A **topological data analysis** understanding is a learnable capability encompassing:
- **Hodge decomposition:** Decomposing edge flows into harmonic, gradient, and curl components
- **Harmonic term:** Edges on the boundary of topological holes (cycles that don't bound)
- **Gradient term:** Edges along structural bridges (flow from source to sink)
- **Curl term:** Edges in confluence/circulation patterns
- **Edge PageRank:** Identifying structurally important edges in the complex
- **Semantic interpretation:** Understanding what topological features mean organizationally
- **Scale resilience:** Using algebra when visualization becomes unwieldy
- **Compositional analysis:** Analyzing charts composed from multiple sub-charts

This skill is abstract until possessed by an actor (student), at which point it represents concrete knowledge and capability.

## Acquisition

This skill is **learned** through study and practice:
- Completing the [[v:learning-module:organizational-topology]] module
- Composing coordination and management charts
- Running Hodge analysis scripts on composed charts
- Interpreting harmonic, gradient, and curl components
- Running edge PageRank to identify critical edges
- Connecting topological features to organizational meaning
- Analyzing charts too complex for visual inspection

## Applicable Actors

This skill can be possessed by:
- **`vertex/student`**: Students engaged in knowledge complex education
- **`vertex/actor`**: Any actor learning about algebraic topology applied to organizational analysis

Rationale: This is an advanced learnable capability appropriate for actors who have mastered coordination and resource flow modeling and need rigorous analytical tools for complex structures.

## Learning Outcomes

After acquiring this skill, a learner can:

1. **Apply Hodge decomposition** (decompose edge flows into three components)
2. **Interpret harmonic edges** (identify topological holes and their organizational meaning)
3. **Interpret gradient edges** (identify structural bridges and flow paths)
4. **Interpret curl edges** (identify circulation and confluence patterns)
5. **Run edge PageRank** (identify structurally important edges)
6. **Analyze at scale** (use algebraic methods when visualization fails)
7. **Connect to semantics** (explain what topological features mean for the organization)
8. **Validate compositions** (verify composed charts maintain expected properties)

## Prerequisite Skills

**Required:**
- [[v:skill:resource-management]] - Must understand management charts before composing them
- [[v:skill:team-coordination]] - Must understand coordination charts before composing them
- [[v:skill:composing-typed-simplicial-complexes]] - Must understand composition operations

**Background (helpful but not required):**
- Linear algebra fundamentals
- Graph theory basics
- Experience with network analysis

## Enables

Possessing this skill enables:

- **Complex organizational analysis**: Can analyze structures too large for visual inspection
- **Rigorous topology**: Can apply mathematical methods to organizational data
- **Pattern recognition**: Can identify holes, bridges, and circulation in org structures
- **Chief Engineer capability**: Combined with organizational-design-analysis, enables full organizational modeling mastery

## Assessment Methods

Skill possession can be assessed through:

1. **Hodge Decomposition:** Run decomposition on a composed chart, explain components
2. **Harmonic Interpretation:** Identify what organizational patterns create harmonic edges
3. **Gradient Interpretation:** Trace flow paths through gradient edges
4. **Curl Interpretation:** Identify circulation patterns and their meaning
5. **PageRank Analysis:** Run edge PageRank, identify top-ranked edges, explain significance
6. **Scale Analysis:** Analyze a chart with 20+ vertices using algebraic methods
7. **Semantic Connection:** Write report connecting topological features to org insights

**Standard:** 80% accuracy on exercises and assessments demonstrates skill possession.

## Examples

**Students possessing this skill:**
- `v:student:chief-engineer` - Has completed organizational-topology module

**Usage in prerequisite faces:**
```yaml
type: face/prerequisite
vertices:
  - v:student:management-architect  # has resource-management skill
  - v:skill:resource-management  # prerequisite
  - v:learning-module:organizational-topology  # requires this skill
```

**Usage in skill-gain faces:**
```yaml
type: face/skill-gain
vertices:
  - v:student:chief-engineer  # possesses this skill after completion
  - v:learning-module:organizational-topology  # develops this skill
  - v:skill:topological-data-analysis  # this skill
```

## Constraints

- Must be acquired through learning (not inherent)
- Requires resource-management, team-coordination, and composing-typed-simplicial-complexes as prerequisites
- Cannot be possessed without completing learning process (module or equivalent study)
- Should be validated through assessment before considering possessed
- Requires computational tools (Hodge analysis scripts) for practical application

## Real-World Applications

This skill enables understanding of:

- **Network analysis**: Applying algebraic topology to any network structure
- **Organizational diagnostics**: Finding structural issues in large organizations
- **Complexity management**: Handling structures too complex for intuition
- **Flow analysis**: Understanding how resources, information, or authority flow
- **Bottleneck identification**: Finding critical paths and constraints

---

**Note:** This skill is one of two capstone skills developed in Module 10. Combined with organizational-design-analysis, it represents the full chief-engineer capability for analyzing and designing complex organizational structures using rigorous mathematical methods.
