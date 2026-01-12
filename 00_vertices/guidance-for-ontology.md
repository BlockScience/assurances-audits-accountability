---
type: vertex/guidance
extends: doc
id: v:guidance:ontology
name: Guidance for Ontology Documents
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2026-01-11T00:00:00Z
modified: 2026-01-11T00:00:00Z
description: Quality criteria for evaluating knowledge complex ontology documents
criteria:
  - Type Completeness
  - Coherence Rules
  - Extension Clarity
  - Type Hierarchy Consistency
  - Documentation Quality
  - Local Rule Verifiability
  - Chart Design Quality
  - Assurance Completeness
rubric: excellent/good/needs-improvement
---

# Guidance for Ontology Documents

## Purpose Statement

This guidance helps authors create high-quality ontology documents and helps reviewers evaluate them. An ontology is foundational infrastructure - errors propagate to every document in the knowledge complex. This guidance ensures ontologies are complete, coherent, extensible, and well-documented.

## Document Overview

### What This Guidance Covers

Ontology documents that define the type system for a knowledge complex:

- **Vertex types**: Documents, actors, roles, authorities
- **Edge types**: Relationships between vertices with endpoint constraints
- **Face types**: Triangular structures with boundary requirements
- **Chart types**: Vertices containing simplex collections (construction scaffolds and analytical views)
- **Local rules**: Constraints on topologically adjacent simplices

### Best Use Cases

1. **Creating a new knowledge complex** - Start with the base ontology, extend as needed
2. **Extending for a domain** - Add application-specific types to base ontology
3. **Reviewing ontology changes** - Evaluate proposed type additions or modifications
4. **Debugging coherence failures** - Trace errors back to type definitions
5. **Planning system capabilities** - Understand what relationships can be expressed

## Quality Criteria

### Type Completeness

**Excellent:** All required simplex types are defined with clear semantics. Every type needed to express the domain is present. No placeholders or "TBD" types. Type counts in frontmatter match actual definitions.

**Good:** Core types are defined and functional. Some optional or edge-case types may be missing but can be added later without breaking changes. Minor gaps in coverage.

**Needs Improvement:** Critical types are missing or incomplete. The ontology cannot express required relationships. Type counts do not match definitions.

### Coherence Rules

**Excellent:** Local rules comprehensively cover type interactions. Every face type has explicit boundary requirements. Edge endpoint constraints prevent invalid connections. Rules are mutually consistent - no conflicts.

**Good:** Key local rules are defined covering primary use cases. Some edge cases may lack explicit rules but fail safely. Minor ambiguities in rule interactions.

**Needs Improvement:** Local rules are missing or inconsistent. Faces can be constructed with invalid boundaries. Edges can connect incompatible vertex types. Rules conflict with each other.

### Extension Clarity

**Excellent:** Clear extension points are documented with examples for application ontologies. Reserved prefixes are defined. Inheritance rules are explicit. An application developer can extend the ontology without reading the full document.

**Good:** Extension mechanism is documented but examples are limited. Some ambiguity about what can be extended vs. what is fixed. Application developers may need to study the full ontology first.

**Needs Improvement:** Unclear how to extend the base ontology. No reserved prefixes. Extension attempts break existing types or rules.

### Type Hierarchy Consistency

**Excellent:** Consistent inheritance chains with no orphan types. Every type's `extends` field points to a valid parent. Tag arrays correctly reflect full inheritance path. ID prefixes match type categories.

**Good:** Mostly consistent hierarchy with minor gaps. Some types may have incomplete tag arrays but are functionally correct. ID patterns are mostly followed.

**Needs Improvement:** Inconsistent inheritance - types extend non-existent parents. Tag arrays missing inheritance chain entries. ID prefixes don't match type categories.

### Documentation Quality

**Excellent:** Every type has a clear purpose statement, complete field definitions, and illustrative examples. Constraints are explained, not just listed. A reader unfamiliar with the domain can understand each type's role.

**Good:** Core types are well-documented. Peripheral types have minimal but adequate documentation. Some constraints lack explanation. Reader can understand with some domain knowledge.

**Needs Improvement:** Types are defined without explanation. Field tables are incomplete. Constraints are cryptic or missing. Reader cannot understand type purposes.

### Local Rule Verifiability

**Excellent:** All local rules can be mechanically verified by examining topologically adjacent simplices. Rule expressions are unambiguous. Verification procedures are documented. Rules compose - checking each locally guarantees global coherence.

**Good:** Most rules are verifiable with clear procedures. Some rules require judgment but have documented criteria. Rules mostly compose with documented exceptions.

**Needs Improvement:** Rules are ambiguous or require global context to verify. Verification procedures are missing. Rules don't compose - local satisfaction doesn't guarantee global coherence.

### Chart Design Quality

**Excellent:** Chart types serve clear dual purposes (construction and analysis). Membership constraints precisely specify allowed simplex types. Coherence requirements ensure charts form valid sub-complexes. Charts enable both safe addition of new simplices and meaningful inspection of existing structure. Use cases are concrete and actionable. For module/runbook charts, exit criteria are explicit: all output documents must have assurance faces (validated by qualified signers).

**Good:** Chart types have defined purposes and constraints. Some membership constraints are loose but don't allow invalid configurations. Coherence requirements are present but may lack edge cases. Construction and analysis use cases are documented. Exit criteria are present but may lack precision.

**Needs Improvement:** Chart types lack clear purpose. Membership constraints are missing or too permissive. Coherence requirements don't ensure valid sub-complexes. Use cases are vague or missing. Charts don't enable either safe construction or meaningful analysis. Module/runbook charts lack exit criteria, leaving iteration termination ambiguous.

### Assurance Completeness

**Excellent:** Every document vertex is covered by at least one assurance face. All assurance chains terminate at b2 anchors. No gaps in critical paths. The ontology enables complete traceability from any document to its trust roots.

**Good:** Core documents are assured. Some peripheral documents may lack assurance faces but are identified as technical debt. Most assurance chains are complete.

**Needs Improvement:** Significant documents lack assurance. Assurance chains don't trace to b2 anchors. Critical paths have gaps that prevent trust verification.

## Section-by-Section Guidance

### Purpose Section

**Purpose:** Establish the domain scope and rationale for this ontology.

**Tips:**
- State what domain or problem space this ontology addresses
- Explain why a new ontology (or extension) is needed
- Reference parent ontology if extending

**Anti-patterns:**
- "This ontology defines types" - too generic, says nothing
- Copying purpose from another ontology without adapting

### Vertex Types Section

**Purpose:** Define all 0-simplex types in the ontology.

**Tips:**
- Organize by category (documents, actors, organizational, structural)
- Start with abstract base types, then concrete subtypes
- Include complete field tables for each type
- Document constraints in prose, not just bullets

**Anti-patterns:**
- Defining types without explaining their purpose
- Missing inheritance chain in tags
- Inconsistent ID patterns across types
- Fields without type specifications

### Edge Types Section

**Purpose:** Define all 1-simplex types with endpoint constraints.

**Tips:**
- Group by semantic category (assurance, accountability, I/O, etc.)
- Always specify source_type and target_type constraints
- Indicate direction (directed vs undirected)
- Document when edges are required vs optional

**Anti-patterns:**
- Edges without endpoint constraints
- Missing direction specification
- Edges that can connect incompatible types

### Face Types Section

**Purpose:** Define all 2-simplex types with boundary specifications.

**Tips:**
- Specify all three boundary edges and their types
- Document which vertices compose the face
- List all local rules for this face type
- Show the triangle diagram if helpful

**Anti-patterns:**
- Faces without explicit boundary edge requirements
- Missing local rules
- Boundary that doesn't close (edges don't form triangle)

### Chart Types Section

**Purpose:** Define chart types that serve as construction scaffolds and analytical views.

**Tips:**

- Document both construction and analysis use cases for each chart type
- Specify membership constraints with cardinality (min..max)
- Include coherence requirements ensuring valid sub-complex
- Define chart-specific local rules
- Show how the chart connects to existing simplices legally
- Explain what insights the chart provides when used for analysis
- **For module and runbook charts: document exit criteria** - specify when execution is complete (typically: all output documents have assurance faces, validated by qualified signers)

**Anti-patterns:**

- Charts without clear dual purpose (construction AND analysis)
- Missing membership constraints allowing arbitrary simplices
- No coherence requirements (chart could be incoherent)
- Charts that duplicate existing types instead of composing them
- Isolated charts that don't connect to the broader complex
- **Module/runbook charts without exit criteria** - leaves termination conditions ambiguous, especially for iterative modules

### Local Rules Section

**Purpose:** Define constraints on topologically adjacent simplices.

**Tips:**
- Organize by rule type (edge-endpoint, face-boundary, face-adjacency, star)
- Provide concrete examples for each rule
- Document verification procedure
- Explain why each rule exists

**Anti-patterns:**
- Rules without clear scope
- Unverifiable rules
- Rules that conflict with each other
- Rules without rationale

### Extension Points Section

**Purpose:** Enable application ontologies to extend safely.

**Tips:**
- Document reserved prefixes explicitly
- Provide extension examples
- Explain what cannot be changed in extensions
- Show how to add types without breaking compatibility

**Anti-patterns:**
- No reserved prefix scheme
- Unclear what can vs cannot be extended
- Missing extension examples

## Workflow Guidance

### Creating a New Ontology

1. **Determine scope**: What domain does this ontology cover?
2. **Identify parent**: Extend base ontology or create root?
3. **List required types**: What vertices, edges, faces are needed?
4. **Design hierarchy**: How do types inherit?
5. **Define local rules**: What constraints ensure coherence?
6. **Document thoroughly**: Purpose, fields, constraints for each type
7. **Test with examples**: Can you create valid instances?
8. **Review for completeness**: Check all quality criteria

### Extending an Existing Ontology

1. **Study parent**: Understand existing types and rules
2. **Identify gaps**: What types are missing for your domain?
3. **Design extensions**: New types that complement (not conflict)
4. **Preserve rules**: Cannot weaken parent local rules
5. **Use app prefixes**: `v:app:`, `e:app:`, `f:app:`
6. **Document extensions**: Reference parent for inherited types

## Common Issues and Solutions

| Issue | Symptom | Solution |
|-------|---------|----------|
| Orphan types | Type extends non-existent parent | Check extends field, ensure parent exists |
| Broken tag chain | Verification fails on tags | Include full inheritance path in tags array |
| Invalid edges | Edges connect wrong types | Add endpoint constraints to edge type |
| Unclosed faces | Face verification fails | Ensure boundary edges form closed triangle |
| Rule conflicts | Local rules contradict | Review rules together, resolve ambiguity |
| Missing extension points | Apps can't extend safely | Add reserved prefixes, document inheritance |
| Type count mismatch | Frontmatter doesn't match body | Count types in body, update frontmatter |
| No exit criteria | Unclear when iterative modules complete | Add exit criteria: all outputs must have assurance faces |

## Best Practices

1. **Start minimal**: Define only types you need now; extend later
2. **Inherit aggressively**: Reuse parent types instead of redefining
3. **Document the "why"**: Explain purposes, not just structures
4. **Test locally**: Verify each local rule independently
5. **Reserve prefixes**: Prevent extension conflicts before they happen
6. **Version carefully**: Semantic versioning reflects compatibility
7. **Review holistically**: Check quality criteria together, not in isolation
8. **Example everything**: Concrete instances clarify abstract definitions
9. **Compose rules**: Ensure local satisfaction implies global coherence
10. **Fail explicitly**: Rules should reject invalid structures, not silently accept

## Appendices

### Appendix A: Visualization Guidelines

#### Visual Notation Convention

When creating diagrams of ontology structures:

**Vertex Symbols:**

- Documents (doc, spec, guidance): Rectangles
- Actors (actor, signer): Ovals
- Organizational (role, authority): Diamonds
- Modules: Hexagons
- Charts: Rounded rectangles with dashed borders

**Edge Notation:**

- Directed edges: Solid arrows
- Undirected edges: Solid lines (no arrows)
- Derived edges: Dashed arrows

**Face Shading:**

- Assurance faces: Light blue fill
- Signature faces: Light green fill
- B2 bootstrap faces: Gold fill
- RBAC faces: Light purple fill
- Module I/O faces: Light orange fill

**Color Coding by Constraint Class:**

- Syntactic constraints: Blue annotations
- Semantic constraints: Red annotations

#### Diagram Best Practices

1. **Show face boundaries explicitly** - draw the triangle with all three edges
2. **Label vertices with type:name** - e.g., "doc:my-spec"
3. **Group related simplices** - cluster RBAC, assurance, module regions
4. **Indicate chart membership** - use containing rectangles or color coding
5. **Mark b2 anchors prominently** - these are trust roots

### Appendix B: Typed Guidance Criteria

Guidance criteria can be typed as predicates for formal evaluation:

| Criterion Type | Signature | Example |
|----------------|-----------|---------|
| Completeness | `Doc → Bool` | "All required sections present" |
| Consistency | `Doc × Doc → Bool` | "No contradictions between sections" |
| Clarity | `Doc → Rating` | "Reader can understand without domain expertise" |
| Measurable | `Doc → Metric` | "Cyclomatic complexity < 10" |

Typed criteria enable:

- Automated partial evaluation (completeness checks)
- Structured review checklists (consistency matrices)
- Quantitative quality tracking (metric dashboards)

Application ontologies may extend these criterion types for domain-specific quality dimensions.

### Appendix C: Homological Completeness (Advanced)

For formal analysis, assurance completeness can be interpreted homologically:

- **H₁ = 0**: All edges are covered by faces (complete assurance)
- **H₁ ≠ 0**: Uncovered edges exist (gaps in assurance network)

The simplicial complex structure admits boundary operator analysis:

- **∂₂**: Maps faces to their edge boundaries
- **∂₁**: Maps edges to their vertex boundaries
- **ker(∂₁)/im(∂₂)**: First homology group detecting coverage gaps

This interpretation enables automated gap detection in assurance networks.

---

**Note:** This guidance is coupled to [[spec-for-ontology]] which defines the structural requirements for ontology documents.
