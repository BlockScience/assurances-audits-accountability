---
type: vertex/guidance
extends: doc
id: v:guidance:organization
name: Guidance for Organization Charts
description: Quality criteria and best practices for creating excellent organization chart documents
tags:
  - vertex
  - doc
  - guidance
  - chart-type
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
dependencies: []
---

# Guidance for Organization Charts

**This guidance defines quality criteria and best practices for creating excellent organization chart documents.**

## Purpose

While spec-for-organization defines what structural elements must be present, this guidance helps authors assess **how well** an organization chart serves its analytical purpose. Great organization charts are purposeful, accurate, well-scoped, and actionable.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating organization charts by providing:
- Quality assessment criteria for organizational modeling
- Best practices for coordination, management, and composed charts
- Common pitfalls in organizational topology and solutions
- Section-by-section authoring advice
- Workflow recommendations for chart creation

### Best Use Cases

Use this guidance when:
- Creating a new organization chart to document team structure
- Building RACI matrices as typed simplicial complexes
- Modeling resource flows and operational dependencies
- Composing coordination and management views into unified charts
- Reviewing existing organization charts for quality and accuracy
- Teaching others how to model organizational structure

## Quality Criteria

### 1. Organizational Accuracy

**Excellent:**
- Chart reflects actual organizational structure
- All team members correctly represented
- Roles and responsibilities accurately captured
- Resource flows match real operational reality
- Changes tracked and dated

**Good:**
- Generally accurate with minor omissions
- Most relationships captured
- Core structure correct

**Needs Improvement:**
- Outdated or inaccurate structure
- Missing key relationships
- Doesn't reflect reality

### 2. Purpose Clarity

**Excellent:**
- Clear statement of what organizational question is answered
- Explicit audience (managers, team leads, auditors)
- Success criteria stated
- Scope boundaries well-defined

**Good:**
- General purpose clear
- Audience can be inferred
- Some scope definition

**Needs Improvement:**
- Purpose vague ("show the org")
- No clear audience
- Unbounded scope

### 3. RACI Completeness (Coordination Charts)

**Excellent:**
- Every responsibility has exactly one Accountable
- At least one Responsible per responsibility
- Consulted and Informed relationships documented
- No orphan roles or unassigned responsibilities
- RACI coverage explicitly stated

**Good:**
- Core RACI relationships present
- Minor gaps in C/I assignments
- Main accountabilities clear

**Needs Improvement:**
- Multiple or missing Accountables
- Unclear responsibility assignments
- Orphan roles

### 4. Resource Flow Coherence (Management Charts)

**Excellent:**
- All resources have clear producers
- Consumption dependencies explicit
- Cross-team handoffs documented
- Critical path identified
- No circular dependencies (or cycles documented if intentional)

**Good:**
- Main flows captured
- Most dependencies documented
- Core path clear

**Needs Improvement:**
- Orphan resources (no producer)
- Hidden dependencies
- Undocumented handoffs
- Unidentified cycles

### 5. Composition Quality (Composed Charts)

**Excellent:**
- Source charts clearly identified
- Shared vertices (teams) consistent across sources
- Emergent relationships documented and explained
- No conflicting edges
- Clear value proposition for composition

**Good:**
- Sources identified
- Most consistency maintained
- Core emergent edges noted

**Needs Improvement:**
- Unclear what was composed
- Inconsistent shared vertices
- Conflicting information
- No explanation of value

### 6. Topological Awareness

**Excellent:**
- Euler characteristic computed and interpreted
- Connectivity analyzed (islands identified)
- Holes/gaps identified and explained
- Topology connected to organizational meaning
- Bottlenecks visible in structure

**Good:**
- Basic topology computed
- Major structural features noted
- Some interpretation

**Needs Improvement:**
- No topological analysis
- Structure not interpreted
- Patterns missed

### 7. Actionability

**Excellent:**
- Clear implications for organizational decisions
- Gaps and issues highlighted
- Recommendations included
- Supports actual use (onboarding, planning, audit)
- Living document with update process

**Good:**
- Some implications noted
- Major issues visible
- Generally useful

**Needs Improvement:**
- No actionable insights
- Just lists elements
- Not useful for decisions

### 8. Maintainability

**Excellent:**
- Clear ownership and update responsibility
- Version history documented
- Change triggers defined (reorg, new hire, role change)
- Verification commands provided
- Freshness indicators (last verified date)

**Good:**
- Owner identifiable
- Version tracked
- Basic verification

**Needs Improvement:**
- No owner
- No versioning
- Cannot verify currency

## Section-by-Section Guidance

### Organization Structure Section

**Purpose:** Provide clear categorization of all organizational elements

**Tips:**
- Separate actors (who) from properties (what) clearly
- For coordination: staff → roles → responsibilities chain
- For management: teams → functions → resources chain
- Use consistent naming conventions
- Link to vertex definitions where helpful

**Anti-patterns:**
- ❌ Mixing staff and roles without distinction
- ✅ Clear hierarchy: Team contains Staff who hold Roles
- ❌ Resources without owners
- ✅ Every resource has owner team

### Organizational Analysis Section

**Purpose:** Extract actionable insights from structure

**Tips:**
- Start with high-level counts (how many teams, staff, functions)
- Identify critical relationships (who is accountable for what)
- Note structural patterns (centralized vs distributed)
- Connect topology to organizational health

**Anti-patterns:**
- ❌ "The organization has teams" (obvious)
- ✅ "Platform Team is single point of failure for deployments (all flows pass through)"
- ❌ Just counting elements
- ✅ Interpreting what counts mean

### Constraint Validation Section

**Purpose:** Verify organizational rules are satisfied

**Tips:**
- For RACI: Check single-accountable rule explicitly
- For flows: Check for orphans and cycles
- Document any intentional violations with rationale
- Make constraints checkable (provide verification)

**Anti-patterns:**
- ❌ "Constraints satisfied" (no detail)
- ✅ "✓ Deploy responsibility: Alice (A), Bob (R), Charlie (I) - single accountable confirmed"
- ❌ Ignoring violations
- ✅ "⚠️ Monitoring has no Accountable - flagged for resolution"

## Workflow Guidance

### Creating a Coordination Chart

1. **Identify Teams** (15 min)
   - List all teams in scope
   - Define team boundaries
   - Note team relationships (parent/child)

2. **Map Staff to Teams** (30 min)
   - List all staff in scope
   - Create member edges (staff → team)
   - Verify no one is orphaned

3. **Define Roles** (30 min)
   - List roles within teams
   - Create includes edges (team → role)
   - Create holds-role edges (staff → role)

4. **Assign Responsibilities** (45 min)
   - List all responsibilities
   - For each: identify R, A, C, I
   - Create assignment faces
   - Verify single-accountable

5. **Verify RACI** (15 min)
   - Check every responsibility has A
   - Check every responsibility has R
   - Document gaps

### Creating a Management Chart

1. **Identify Teams** (15 min)
   - Same teams as coordination (for composition)
   - Note operational responsibilities

2. **Define Functions** (30 min)
   - List operational functions per team
   - Create operates edges (team → function)
   - Document inputs/outputs

3. **Map Resources** (30 min)
   - List all resources (artifacts, infrastructure, capabilities)
   - Assign owners (team → owns → resource)
   - Categorize by type

4. **Define Flows** (45 min)
   - Create produces edges (function → resource)
   - Create consumes edges (function → resource)
   - Mark blocking dependencies

5. **Identify Cross-Team Dependencies** (30 min)
   - Find handoff points
   - Create dependency faces
   - Document critical path

### Creating a Composed Chart

1. **Select Source Charts** (15 min)
   - Choose coordination and management charts
   - Verify they share team vertices

2. **Validate Shared Vertices** (30 min)
   - Compare team definitions
   - Resolve any inconsistencies
   - Document merge decisions

3. **Combine Elements** (30 min)
   - Union of all vertices
   - Union of all edges
   - Union of all faces

4. **Discover Emergent Relationships** (45 min)
   - Look for new meaningful connections
   - Staff → operates (via team) → function
   - Role → requires → skill → function
   - Document discoveries

5. **Analyze Composed Topology** (30 min)
   - Compute combined χ
   - Identify structural insights
   - Note integration points

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Multiple Accountables** | RACI violation | Review responsibility, split if truly different aspects, or designate single A |
| **Missing Accountable** | Responsibility gap | Assign A or escalate to manager |
| **Orphan Resource** | No producer | Identify source or mark as external input |
| **Circular Dependency** | Flow deadlock | Identify cycle, break with external trigger or redesign |
| **Inconsistent Teams** | Composition conflict | Establish canonical team definition, update source charts |
| **Stale Chart** | Outdated structure | Establish update triggers, assign owner, schedule reviews |
| **Too Complex** | Unreadable chart | Split into focused subcharts, compose programmatically |

## Best Practices

### Organizational Accuracy

1. **Validate with stakeholders** - Review chart with actual team members
2. **Date your sources** - Note when information was gathered
3. **Track changes** - Document what changed and when
4. **Distinguish formal vs informal** - Capture both where relevant
5. **Note assumptions** - Explicit about what you inferred

### RACI Excellence

6. **One A, always** - Never compromise on single accountable
7. **At least one R** - Work must be done by someone
8. **C/I are optional** - Don't force them if not meaningful
9. **Review with owners** - Accountables should confirm assignments
10. **Gap analysis** - Actively look for missing assignments

### Resource Flow Clarity

11. **Name resources specifically** - "Deployment Package" not "artifact"
12. **Identify blocking dependencies** - Mark with `blocking: true`
13. **Document cross-team flows** - These are integration points
14. **Critical path analysis** - What must happen in sequence?
15. **Look for bottlenecks** - Single points of failure

### Composition Success

16. **Start with shared vocabulary** - Teams must match
17. **Document merge decisions** - How conflicts were resolved
18. **Discover emergent value** - Why compose? What's revealed?
19. **Maintain source links** - Track provenance
20. **Update atomically** - Change sources, recompose

## Examples

### Excellent Coordination Chart Example

A coordination chart would demonstrate:
- ✓ Clear team → staff → role hierarchy
- ✓ Complete RACI for all responsibilities
- ✓ Single accountable per responsibility
- ✓ No orphan roles or staff
- ✓ Actionable insights about coverage gaps

### Excellent Management Chart Example

A management chart would demonstrate:
- ✓ Clear team → function → resource flows
- ✓ All resources have producers
- ✓ Cross-team dependencies documented
- ✓ Critical path identified
- ✓ Bottlenecks highlighted

### Excellent Composed Chart Example

A composed chart would demonstrate:
- ✓ Teams consistent across coordination and management views
- ✓ Emergent relationships documented
- ✓ Staff-to-function paths visible
- ✓ Complete organizational picture
- ✓ Integration points clear

## Validation vs. Verification

**Verification** (deterministic, against spec-for-organization):
- All required frontmatter fields present
- All required sections present
- Element counts match
- Valid simplicial complex
- Constraint rules satisfied structurally

**Validation** (qualitative, against this guidance):
- Organizational accuracy
- Purpose clarity
- RACI completeness
- Flow coherence
- Actionability
- Overall fitness-for-purpose

## Tooling Support

### Verification Commands

```bash
# Verify chart structure
python scripts/verify_chart.py charts/<org-chart>/<org-chart>.md

# Analyze topology
python scripts/topology.py charts/<org-chart>/<org-chart>.md

# Export for analysis
python scripts/export_chart_direct.py charts/<org-chart>/<org-chart>.md

# Hodge analysis (for complex charts)
python scripts/hodge_analysis.py charts/<org-chart>/<org-chart>.json
```

### Validation Support

Organization chart validation is primarily manual review against the quality criteria above. Key validation questions:

- Does this chart reflect the actual organization?
- Is RACI complete and valid?
- Are resource flows accurate?
- Can someone use this chart for real decisions?
- Is the chart maintainable?

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

✓ **Purpose Clarity:** Clear statement of helping authors create excellent organization charts
✓ **Organizational Accuracy:** Based on actual organizational modeling patterns
✓ **Actionability:** Provides concrete workflows and checklists
✓ **Maintainability:** Versioned, timestamped, with clear ownership

---

**Note:** This guidance pairs with spec-for-organization via a coupling edge. The spec defines structure; this guidance defines quality. Together they enable full assurance (verification + validation) for organization chart documents.
