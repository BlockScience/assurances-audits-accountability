---
type: vertex/skill
extends: vertex/property
id: v:skill:organizational-design-analysis
name: Organizational Design & Analysis
description: Understanding how to compose organizational charts and interpret their combined structure for comprehensive organizational modeling
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

# Organizational Design & Analysis

## Purpose

This skill defines the capability to compose and analyze complete organizational models by combining coordination charts (staff, team, role) with management charts (resource, function, team). It represents mastery of chart composition, semantic edge/face discovery, and holistic organizational interpretation.

## Property Definition

An **organizational design & analysis** understanding is a learnable capability encompassing:
- **Chart composition:** Pasting coordination and management charts together via shared team vertices
- **Semantic discovery:** Finding new meaningful edges and faces in the composed structure
- **Holistic modeling:** Understanding how people, responsibilities, functions, and resources interact
- **Complexity navigation:** Working with dense organizational structures
- **Design patterns:** Recognizing common organizational patterns and anti-patterns
- **Iterative refinement:** Evolving organizational models based on analysis insights
- **Chief engineer perspective:** Comprehensive view of organizational architecture

This skill is abstract until possessed by an actor (student), at which point it represents concrete knowledge and capability.

## Acquisition

This skill is **learned** through study and practice:
- Completing the [[v:learning-module:organizational-topology]] module
- Composing coordination and management charts via team vertex identification
- Exploring the composed chart for new semantic relationships
- Identifying edges and faces that span the coordination-management boundary
- Interpreting what the combined topology reveals about organizational structure
- Using visualization and algebraic tools together for comprehensive analysis

## Applicable Actors

This skill can be possessed by:
- **`vertex/student`**: Students engaged in knowledge complex education
- **`vertex/actor`**: Any actor learning about organizational architecture and design

Rationale: This is an advanced learnable capability appropriate for actors who have mastered both coordination and resource flow modeling and need to synthesize them into complete organizational models.

## Learning Outcomes

After acquiring this skill, a learner can:

1. **Compose charts** (paste coordination and management charts via shared vertices)
2. **Discover new edges** (find semantically meaningful relationships in composed structure)
3. **Discover new faces** (find higher-order relationships spanning chart types)
4. **Interpret holistically** (understand how all organizational elements interact)
5. **Navigate complexity** (work effectively with dense, composed structures)
6. **Recognize patterns** (identify common organizational patterns and anti-patterns)
7. **Design organizations** (create organizational models that satisfy constraints)
8. **Communicate findings** (explain organizational structure to stakeholders)

## Prerequisite Skills

**Required:**
- [[v:skill:resource-management]] - Must understand management charts before composing them
- [[v:skill:team-coordination]] - Must understand coordination charts before composing them
- [[v:skill:composing-typed-simplicial-complexes]] - Must understand composition operations

**Background (helpful but not required):**
- Organizational design experience
- Systems thinking
- Management consulting exposure

## Enables

Possessing this skill enables:

- **Organizational architecture**: Can design complete organizational structures
- **Cross-functional analysis**: Can understand how coordination and operations interact
- **Strategic insight**: Can connect people structures to operational flows
- **Chief Engineer capability**: Combined with topological-data-analysis, enables full organizational modeling mastery

## Assessment Methods

Skill possession can be assessed through:

1. **Chart Composition:** Compose coordination and management charts correctly
2. **Edge Discovery:** Identify 3+ new meaningful edges in composed structure
3. **Face Discovery:** Identify 2+ new meaningful faces spanning chart types
4. **Holistic Interpretation:** Write analysis of how the composed structure reveals organizational dynamics
5. **Pattern Recognition:** Identify organizational patterns (silos, bottlenecks, redundancy)
6. **Design Exercise:** Create organizational model satisfying given constraints
7. **Stakeholder Communication:** Present organizational analysis to non-technical audience

**Standard:** 80% accuracy on exercises and assessments demonstrates skill possession.

## Examples

**Students possessing this skill:**
- `v:student:chief-engineer` - Has completed organizational-topology module

**Usage in prerequisite faces:**
```yaml
type: face/prerequisite
vertices:
  - v:student:management-architect  # has team-coordination skill
  - v:skill:team-coordination  # prerequisite
  - v:learning-module:organizational-topology  # requires this skill
```

**Usage in skill-gain faces:**
```yaml
type: face/skill-gain
vertices:
  - v:student:chief-engineer  # possesses this skill after completion
  - v:learning-module:organizational-topology  # develops this skill
  - v:skill:organizational-design-analysis  # this skill
```

## Constraints

- Must be acquired through learning (not inherent)
- Requires resource-management, team-coordination, and composing-typed-simplicial-complexes as prerequisites
- Cannot be possessed without completing learning process (module or equivalent study)
- Should be validated through assessment before considering possessed
- Best developed through practice with real organizational structures

## Real-World Applications

This skill enables understanding of:

- **Organizational design**: Creating effective team and resource structures
- **Restructuring analysis**: Understanding impacts of organizational changes
- **M&A integration**: Analyzing how organizations can be combined
- **Process improvement**: Finding inefficiencies in organizational flows
- **Role definition**: Understanding how roles connect people to functions

---

**Note:** This skill is one of two capstone skills developed in Module 10. Combined with topological-data-analysis, it represents the full chief-engineer capability for designing and analyzing complex organizational structures. While TDA provides the mathematical rigor, this skill provides the semantic interpretation and design capability.
