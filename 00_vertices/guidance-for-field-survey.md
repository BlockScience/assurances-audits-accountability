---
type: vertex/guidance
extends: doc
id: v:guidance:field-survey
name: Guidance for Field Survey Documents
description: Quality criteria and best practices for creating effective field surveys that map stakeholders, resources, and relationships before architecture work
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-01-04T23:00:00Z
modified: 2025-01-04T23:00:00Z
dependencies: []
criteria:
  - scope-clarity
  - actor-completeness
  - resource-completeness
  - relationship-accuracy
  - boundary-precision
  - executive-accessibility
---

# Guidance for Field Survey Documents

**This guidance helps authors create high-quality field surveys that effectively map stakeholders (actors), resources, and their relationships to establish context before architecture work begins.**

## Purpose

While spec-for-field-survey defines what structural elements must be present, this guidance helps authors assess **how well** a field survey serves its purpose. Great field surveys provide clear, complete context that enables informed architecture decisions by documenting what exists before defining what will be built.

## Document Overview

### What This Guidance Covers

Field surveys establish the foundational context for any intervention:
- **Animating Purpose** frames why this survey matters
- **Actors** identify all relevant stakeholders
- **Resources** inventory what the system produces or depends on
- **Relationships** map how actors and resources connect (bipartite graph)
- **Scope Boundaries** define what's in and out of consideration

This guidance supports authors in creating surveys that:
- Capture the full picture within defined scope
- Describe actors and resources clearly and concisely
- Map relationships accurately without forcing connections
- Define boundaries explicitly and justify them
- Remain accessible to non-technical stakeholders

### Best Use Cases

1. **Pre-Architecture Discovery:** Understanding the landscape before designing solutions
2. **Stakeholder Mapping:** Identifying all parties who must be considered
3. **Resource Inventory:** Cataloging technologies, data, and infrastructure
4. **Dependency Analysis:** Understanding how actors rely on resources
5. **Scope Definition:** Establishing clear boundaries for subsequent work

### When NOT to Use

- When you already have a complete architecture (the survey comes first)
- When you need to design solutions (that's architecture work)
- When scope is already well-understood and documented elsewhere
- When a quick stakeholder list is sufficient (survey is more comprehensive)
- When detailed technical specifications are needed (wrong document type)

## Quality Criteria

### 1. Scope Clarity

**Excellent:**
- Animating purpose is immediately clear to any reader
- Scope statement is specific and bounded
- Key questions are insightful and answerable
- Reader understands exactly what this survey covers and why
- Purpose connects to subsequent architecture work

**Good:**
- Purpose is understandable
- Scope is defined
- Key questions present
- General clarity on coverage

**Needs Improvement:**
- Purpose is vague or buried
- Scope is unclear or unbounded
- Key questions are generic or missing
- Reader unsure what the survey is about
- No connection to subsequent work

### 2. Actor Completeness

**Excellent:**
- All significant stakeholders within scope are identified
- No obvious actors missing that affect the system
- Actor types are correctly classified
- Descriptions are clear, concise, and differentiated
- Accountabilities are specific and non-overlapping
- Reader could identify and contact each actor class

**Good:**
- Major stakeholders identified
- Most actor types correct
- Descriptions adequate
- Accountabilities mostly clear

**Needs Improvement:**
- Significant actors missing
- Misclassified actor types
- Vague or duplicative descriptions
- Unclear or overlapping accountabilities
- "Everyone" or "all users" without specificity

### 3. Resource Completeness

**Excellent:**
- All significant resources within scope are identified
- Types correctly classify each resource
- Descriptions explain what the resource is and does
- Status accurately reflects current state
- No obvious resources missing that actors depend on
- Resources include both produced and consumed items

**Good:**
- Major resources identified
- Most types correct
- Descriptions adequate
- Status noted

**Needs Improvement:**
- Significant resources missing
- Misclassified resource types
- Vague descriptions
- Missing or incorrect status
- Only includes technology (misses data, capital, etc.)

### 4. Relationship Accuracy

**Excellent:**
- Relationships accurately reflect real actor-resource connections
- Relationship types correctly describe the nature of connection
- No forced relationships (sparse graph is appropriate)
- All significant dependencies are captured
- Diagram (if present) clearly shows bipartite structure
- Key dependencies are highlighted and explained

**Good:**
- Most relationships accurate
- Types mostly correct
- Sparse where appropriate
- Diagram understandable

**Needs Improvement:**
- Relationships forced to fill matrix
- Incorrect relationship types
- Missing critical dependencies
- Diagram confusing or wrong
- Actor-to-actor or resource-to-resource edges (not bipartite)

### 5. Boundary Precision

**Excellent:**
- In-scope items are specific and comprehensive
- Out-of-scope items clearly exclude relevant alternatives
- Boundary rationale is logical and well-justified
- Geographical/jurisdictional/functional limits are explicit
- No ambiguity about what's included or excluded
- Boundaries enable focused architecture work

**Good:**
- In-scope defined
- Out-of-scope noted
- Some rationale provided
- Boundaries mostly clear

**Needs Improvement:**
- Vague in-scope statements ("relevant stakeholders")
- Missing out-of-scope section
- No rationale for boundaries
- Ambiguous edge cases
- Boundaries too broad or too narrow for purpose

### 6. Executive Accessibility

**Excellent:**
- Non-technical readers can understand the survey completely
- No unexplained jargon or acronyms
- Tables are scannable and informative
- Key findings are actionable
- Implications for architecture are clear to decision-makers
- Survey can serve as briefing document

**Good:**
- Mostly accessible
- Limited jargon
- Tables usable
- Findings present

**Needs Improvement:**
- Requires technical background
- Heavy jargon
- Dense, unscannable tables
- Findings unclear or missing
- Cannot serve non-technical audiences

## Section-by-Section Guidance

### Animating Purpose

**Purpose:** Frame why this survey matters and what it aims to discover

**Tips:**

- Lead with the problem or opportunity motivating the survey
- Keep scope statement to 1-2 sentences maximum
- Key questions should be specific to this domain, not generic
- Connect to subsequent architecture work explicitly
- Answer: "Why are we mapping this system?"

**Anti-patterns:**

- ❌ Starting with methodology instead of purpose
- ❌ Generic scope like "understand the system"
- ❌ Boilerplate questions ("Who are the stakeholders?")
- ❌ No connection to what comes next

**Preferred:**

- ✅ "We need to understand [domain] because [motivation], before designing [intervention]"
- ✅ Scope: "This survey covers [specific boundary], excluding [explicit exclusions]"
- ✅ Questions: "How does [specific actor] currently [specific activity]?"

### Actors (Stakeholders)

**Purpose:** Provide complete inventory of relevant stakeholders

**Tips:**

- Use consistent ID format (A1, A2, etc.) for cross-referencing
- Actor types help categorize but don't force-fit
- Descriptions should differentiate actors from each other
- Accountability should be specific, not "responsible for various things"
- Expanded definitions only where table entry is insufficient
- Think: organizations, roles, user classes, external parties

**Anti-patterns:**

- ❌ "All employees" without specificity
- ❌ Overlapping accountabilities between actors
- ❌ Descriptions that could apply to multiple actors
- ❌ Missing external parties or affected classes
- ❌ Every actor expanded (defeats table purpose)

**Preferred:**

- ✅ Specific actor classes: "Field technicians (50-100 staff)"
- ✅ Clear accountability: "Owns data quality for sensor readings"
- ✅ Differentiated descriptions: Actor A does X; Actor B does Y

### Resources

**Purpose:** Provide complete inventory of relevant resources

**Tips:**

- Resource types: Technology, Data, Infrastructure, Service, Capital, Process
- Status should be accurate: Active, Planned, Legacy, Deprecated
- Include both produced resources and consumed/dependent resources
- Descriptions explain what it is, not just its name
- Think beyond technology: data assets, capital flows, services consumed

**Anti-patterns:**

- ❌ Only listing technologies (missing data, capital, etc.)
- ❌ Vague status like "in use" (be specific)
- ❌ Descriptions that just repeat the name
- ❌ Missing resources that actors clearly depend on
- ❌ Future-state resources (survey is current state)

**Preferred:**

- ✅ Diverse types: "R1: Sensor data (Data), R2: AWS cloud (Infrastructure)"
- ✅ Specific status: "Active - deployed Q3 2024" or "Legacy - scheduled for retirement"
- ✅ Clear descriptions: "Real-time telemetry from 500 field sensors"

### Relationships (Bipartite Graph)

**Purpose:** Map how actors and resources are actually connected

**Tips:**

- This is a sparse graph—don't force connections
- Relationship types: Produces, Consumes, Maintains, Depends On, Governs, Funds
- Each relationship should be meaningful and verifiable
- Mermaid diagram helps but isn't required
- Key dependencies section should highlight critical paths
- Remember: only actor-to-resource edges (bipartite structure)

**Anti-patterns:**

- ❌ Every actor related to every resource (not realistic)
- ❌ Actor-to-actor relationships (not bipartite)
- ❌ Resource-to-resource relationships (not bipartite)
- ❌ Generic relationship types ("uses")
- ❌ Missing critical dependencies

**Preferred:**

- ✅ Sparse and accurate: only real connections
- ✅ Specific types: "A1 Produces R3" not "A1 uses R3"
- ✅ Key dependencies: "Failure of R2 would affect A1, A3, A4"

### Scope Boundaries

**Purpose:** Define explicit limits on survey coverage

**Tips:**

- In-scope should be specific enough to verify completeness
- Out-of-scope should address likely questions about exclusions
- Rationale should explain why these boundaries make sense
- Boundaries can be geographical, jurisdictional, functional, or organizational
- Test: Could someone verify what's in/out of scope?

**Anti-patterns:**

- ❌ Vague in-scope: "relevant stakeholders and systems"
- ❌ Missing out-of-scope (implies everything is in scope)
- ❌ No rationale (boundaries seem arbitrary)
- ❌ Boundaries inconsistent with actors/resources listed

**Preferred:**

- ✅ Specific: "North American operations only"
- ✅ Explicit exclusions: "Excludes partner integrations (covered in separate survey)"
- ✅ Justified: "Limited to production systems; development environment covered separately"

### Key Findings

**Purpose:** Synthesize observations that inform architecture work

**Tips:**

- Summary observations should be insights, not inventory restatement
- Gaps identify what's missing (actor, resource, or relationship)
- Tensions identify conflicts (competing accountabilities, resource contention)
- Implications should directly inform architecture decisions
- This section is the "so what" of the survey

**Anti-patterns:**

- ❌ Just restating actor/resource counts
- ❌ Generic findings: "System is complex"
- ❌ Missing implications for architecture
- ❌ Findings not traceable to survey content

**Preferred:**

- ✅ Insight: "Three actors independently maintain overlapping data sets"
- ✅ Gap: "No actor currently accountable for data quality"
- ✅ Implication: "Architecture should address single source of truth"

## Workflow Guidance

### Recommended Authoring Sequence

1. **Define Scope First** (30 min)
   - Draft animating purpose
   - Set clear boundaries before inventorying
   - Identify key questions to answer
   - Test: Can you explain scope in one sentence?

2. **Inventory Actors** (1-2 hours)
   - Brainstorm all stakeholder classes
   - Classify by type (Organization, Role, User Class, External Party)
   - Write clear descriptions and accountabilities
   - Check: Any obvious actors missing?

3. **Inventory Resources** (1-2 hours)
   - Identify technologies, data, infrastructure, services, capital
   - Classify by type and status
   - Write clear descriptions
   - Check: Any resources that actors depend on missing?

4. **Map Relationships** (1-2 hours)
   - For each actor, identify resource connections
   - Use appropriate relationship types
   - Don't force connections—sparse is expected
   - Create diagram if helpful
   - Identify key dependencies

5. **Refine Boundaries** (30 min)
   - Review in-scope list against inventory
   - Ensure out-of-scope is explicit
   - Write boundary rationale
   - Check: Boundaries consistent with content?

6. **Synthesize Findings** (1 hour)
   - Identify patterns and insights
   - Note gaps and tensions
   - Write implications for architecture
   - Check: Findings actionable?

7. **Quality Review** (30 min)
   - Check against quality criteria
   - Test executive accessibility
   - Verify counts in frontmatter match content
   - Confirm all IDs are consistent

**Total estimated time:** 5-8 hours for comprehensive field survey

### Quality Checkpoints

- **After step 1:** Can you explain the scope in one sentence?
- **After step 3:** Does the inventory feel complete within scope?
- **After step 4:** Are relationships sparse (not every actor to every resource)?
- **After step 6:** Would findings inform architecture decisions?
- **After step 7:** Would a non-technical reader understand this?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Scope Creep** | Survey keeps expanding | Return to scope statement; move items to out-of-scope |
| **Forced Relationships** | Matrix is too dense | Remove speculative connections; sparse is correct |
| **Generic Actors** | "Users" without specificity | Break into specific classes with distinct accountabilities |
| **Technology Bias** | Only tech resources listed | Add data, capital, services, processes |
| **Missing Dependencies** | Key relationships absent | Ask "what does each actor need to function?" |
| **Jargon Heavy** | Non-technical readers lost | Replace acronyms; explain domain terms |
| **No Insights** | Findings just restate inventory | Ask "what surprised me?" and "what's missing?" |
| **Inconsistent IDs** | A1 in actors but Actor1 in relationships | Standardize ID format throughout |
| **Future State Mix** | Planned resources mixed with current | Clearly mark status; survey is current state |

## Best Practices

1. **Survey Before Architecture** - Always understand what exists before designing what will be built
2. **Sparse is Good** - Don't force relationships; real systems have sparse connection matrices
3. **Describe, Don't Prescribe** - Survey documents current state, not desired state
4. **Be Specific About Actors** - "Operations team" beats "employees"; specificity enables action
5. **Include Non-Technical Resources** - Data, capital, services matter as much as technology
6. **Justify Boundaries** - If someone asks "why not X?" your rationale should answer
7. **Connect to Architecture** - Findings should directly inform subsequent design decisions
8. **Test with Outsiders** - Someone unfamiliar should understand the landscape after reading
9. **Use Consistent IDs** - A1, A2, R1, R2 format enables clear cross-referencing
10. **Update When Reality Changes** - Surveys become stale; version and date everything

## Validation vs. Verification

**Verification** (deterministic, against spec-for-field-survey):
- Are all required sections present?
- Do counts in frontmatter match content?
- Are all relationship IDs valid?
- Are minimums met (≥2 actors, ≥2 resources, ≥3 relationships)?

**Validation** (qualitative, against this guidance):
- Is the scope clear and well-bounded?
- Are actors and resources complete within scope?
- Are relationships accurate and appropriately sparse?
- Are boundaries precise and justified?
- Is it accessible to non-technical readers?

This guidance document supports **validation** - assessing fitness-for-purpose.

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

- **Scope Clarity:** Clear purpose statement and defined coverage
- **Actor Completeness:** Addresses authors creating field surveys
- **Resource Completeness:** Covers all aspects of field survey creation
- **Relationship Accuracy:** Connects criteria to specific sections
- **Boundary Precision:** Clear about what this guidance covers and doesn't
- **Executive Accessibility:** Written for practical use by document authors

## Document Metadata

| Property | Value |
|----------|-------|
| Specification | [[spec-for-field-survey]] |
| Guidance Version | 1.0.0 |
| Specification Version | 1.0.0 |
| Prerequisites | None (field survey is the first step) |
| Target Users | Authors establishing context before architecture work |

---

**Note:** This guidance is coupled with [[spec-for-field-survey]] via a coupling edge. Field surveys establish the foundation for architecture work by documenting "what exists" before architecture defines "what will be built."
