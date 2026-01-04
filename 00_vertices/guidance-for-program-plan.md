---
type: vertex/guidance
extends: doc
id: v:guidance:program-plan
name: Guidance for Program Plan Documents
description: Quality criteria and best practices for creating effective program plans that secure stakeholder confidence in delivery
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-01-04T12:00:00Z
modified: 2025-01-04T12:00:00Z
dependencies:
  - v:guidance:architecture
  - v:guidance:lifecycle
criteria:
  - stakeholder-confidence
  - traceability
  - realism
  - risk-awareness
  - accountability-clarity
  - operational-readiness
---

# Guidance for Program Plan Documents

**This guidance helps authors create high-quality program plan documents that secure stakeholder confidence by demonstrating a credible path from architecture through lifecycle to delivered capability.**

## Purpose

While spec-for-program-plan defines what structural elements must be present, this guidance helps authors assess **how well** a program plan serves its purpose. Great program plans convince funders and stakeholders that the team is ready and able to deliver on time and on budget. They make the path from current state to goal state tangible, with honest treatment of risks and clear accountability.

## Document Overview

### What This Guidance Covers

Program plans operationalize the architecture → lifecycle progression:
- **Architecture** defines the goal state (what we're building)
- **Lifecycle** defines the algorithm (how we build it)
- **Program Plan** equips the path (who, when, with what resources, what could go wrong)

This guidance supports authors in creating plans that:
- Build confidence with funders and stakeholders
- Provide realistic schedules and resource estimates
- Identify and manage risks proactively
- Establish clear accountability for execution
- Enable effective program governance

### Best Use Cases

1. **Securing Funding:** Convincing sponsors that investment will yield results
2. **Stakeholder Alignment:** Getting all parties to agree on approach and expectations
3. **Execution Guidance:** Providing teams with clear direction and milestones
4. **Risk Management:** Identifying and preparing for what could go wrong
5. **Governance Framework:** Establishing how the program will be monitored and controlled

### Strategic vs. Tactical Plans

This guidance applies to both strategic and tactical plans, with differences in granularity:

| Aspect | Strategic Plan | Tactical Plan |
|--------|---------------|---------------|
| **Scope** | Program/portfolio level | Project/sprint level |
| **Timeline** | Quarters to years | Weeks to months |
| **Activities** | Phases and milestones | Tasks and work packages |
| **Teams** | Organizations and teams | Individuals and roles |
| **Audience** | Executives, funders | Project managers, team leads |
| **Update Frequency** | Quarterly | Weekly/bi-weekly |

## Quality Criteria

### 1. Stakeholder Confidence

**Excellent:**
- Executive summary clearly communicates value, approach, and confidence
- Non-technical stakeholders can understand the plan without technical background
- Risk treatment is honest but demonstrates preparedness
- Resource requests are justified and reasonable
- Confidence statements are supported by evidence

**Good:**
- Summary is understandable
- Most stakeholders can follow the plan
- Risks acknowledged
- Resources specified

**Needs Improvement:**
- Technical jargon alienates stakeholders
- Oversells or undersells—either unrealistic optimism or excessive hedging
- Risks hidden or minimized
- Resource requests unjustified
- Confidence asserted without basis

### 2. Traceability

**Excellent:**
- Every objective traces explicitly to architecture elements
- Execution approach references and summarizes lifecycle
- Deliverables trace to objectives and architecture
- Activities trace to lifecycle phases
- Clear thread from stakeholder value → objectives → activities → deliverables

**Good:**
- Major elements are traceable
- Architecture and lifecycle referenced
- Most deliverables connected to objectives

**Needs Improvement:**
- Plan seems disconnected from architecture and lifecycle
- Objectives don't trace to architecture
- Deliverables appear without connection to objectives
- Cannot answer "why are we doing this activity?"

### 3. Realism

**Excellent:**
- Schedule estimates based on comparable work or expert judgment (stated)
- Confidence levels honestly assessed (not everything is "high confidence")
- Dependencies and critical path accurately identified
- Resource estimates include basis and assumptions
- Contingency appropriately sized for risk level

**Good:**
- Estimates seem reasonable
- Confidence generally appropriate
- Major dependencies identified
- Contingency present

**Needs Improvement:**
- Schedule is wishful thinking
- Everything is high confidence (red flag)
- Dependencies incomplete or wrong
- No contingency or inadequate contingency
- Estimates have no stated basis

### 4. Risk Awareness

**Excellent:**
- Risks are specific and actionable (not generic)
- Probability and impact honestly assessed
- Mitigations are concrete and feasible
- Contingency plans exist for high-impact risks
- Risk ownership is clear and appropriate
- Risk register reflects actual program risks, not boilerplate

**Good:**
- Major risks identified
- Mitigations specified
- Ownership assigned
- Reasonable P/I assessment

**Needs Improvement:**
- Generic risks ("schedule might slip")
- No mitigation strategies
- Ownership unclear or absent
- P/I assessment inconsistent or unrealistic
- Obvious risks missing

### 5. Accountability Clarity

**Excellent:**
- Every activity has a clear owner
- RACI matrix is complete and consistent
- Governance structure has clear decision authority
- Escalation paths are defined
- External dependencies have named contacts
- No orphan activities or shared ownership without clarity

**Good:**
- Most activities have owners
- RACI present and mostly complete
- Governance defined
- Major escalation paths clear

**Needs Improvement:**
- Activities without owners
- RACI incomplete or inconsistent
- Governance vague
- "The team" owns things (no individual accountability)
- External dependencies unnamed

### 6. Operational Readiness

**Excellent:**
- Governance structure is actionable (meeting schedules, decision processes)
- Reporting cadence and content supports oversight needs
- Performance metrics are measurable and relevant
- Change management process is clear and proportionate
- Plan could be executed starting tomorrow

**Good:**
- Governance structure present
- Reporting defined
- Key metrics identified
- Change process exists

**Needs Improvement:**
- Governance is theoretical
- Reporting not defined or unrealistic
- Metrics unmeasurable or irrelevant
- No change management process
- Plan requires significant clarification before execution

## Section-by-Section Guidance

### Executive Summary

**Purpose:** Enable stakeholders to understand the plan's essence without reading details

**Tips:**
- Lead with value: what capability will be delivered?
- Keep to 2-4 paragraphs maximum
- Include: deliverable, timeline, budget, key risks, confidence
- Write this section LAST (after everything else is complete)
- Use language appropriate for funders, not engineers

**Anti-patterns:**
- ❌ Starting with technical details
- ❌ Omitting risks (creates mistrust when discovered later)
- ❌ "We're confident we can deliver" without basis
- ✅ "Based on team experience and comparable projects, we assess medium-high confidence in the proposed timeline"

### Scope and Objectives

**Purpose:** Define what the program will achieve, traced to architecture

**Tips:**
- Objectives should be SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- Explicitly state what is OUT of scope (prevents scope creep)
- Architecture trace shows objectives aren't arbitrary
- Constraints and assumptions surface hidden dependencies

**Anti-patterns:**
- ❌ "Implement the system" (too vague)
- ✅ "Deliver functional verification capability for 4-layer architecture documents by Q3"
- ❌ Objectives with no success criteria
- ❌ Missing constraints that will later block work

### Execution Approach

**Purpose:** Show how lifecycle translates to this program

**Tips:**
- Reference lifecycle document—don't duplicate
- Summarize phases with expected durations
- V&V strategy should connect to lifecycle gates
- This section bridges lifecycle (generic) to program plan (specific)

**Anti-patterns:**
- ❌ Copy-pasting lifecycle content
- ❌ No reference to lifecycle document
- ❌ V&V mentioned but not connected to lifecycle

### Work Breakdown

**Purpose:** Decompose work into manageable, trackable activities

**Strategic Plans:**
- Activities at phase/milestone level
- Dependencies between phases
- Effort in person-months or FTE-months

**Tactical Plans:**
- Activities at task/work-package level
- Dependencies between tasks
- Effort in person-days or story points

**Tips:**
- Every activity needs an ID for reference
- Dependencies should form a DAG (no cycles)
- Critical path identification shows schedule risk concentration
- Gantt chart should be readable (not 200 rows)

**Anti-patterns:**
- ❌ Activities without dependencies (implies no critical path)
- ❌ All activities in parallel (unrealistic)
- ❌ Gantt chart that's unreadable
- ❌ Critical path not identified

### Teams and Responsibilities

**Purpose:** Establish who does what

**Strategic Plans:**
- Teams/organizations as units
- Leads by role (e.g., "Technical Lead")

**Tactical Plans:**
- Named individuals
- Specific role assignments

**Tips:**
- RACI should cover all activities
- Exactly one "R" (Responsible) per activity
- External dependencies are risks—treat them accordingly
- Team structure should support communication needs

**Anti-patterns:**
- ❌ Multiple "R"s for one activity (diluted accountability)
- ❌ Activities with no assignment
- ❌ "TBD" in team leads
- ❌ External dependencies without mitigation plan

### Timeline and Milestones

**Purpose:** Establish checkpoints and timeline

**Tips:**
- Milestones should be verifiable (clear pass/fail)
- Schedule confidence should reflect actual uncertainty
- Visual timeline helps stakeholders understand sequencing
- Include decision milestones (go/no-go points)

**Strategic Plans:**
- Quarterly or monthly milestones
- Major phase transitions

**Tactical Plans:**
- Weekly or bi-weekly milestones
- Sprint/iteration boundaries

**Anti-patterns:**
- ❌ Milestones without criteria ("Phase 1 complete")
- ✅ "Architecture document verified against spec, validated by chief engineer"
- ❌ All milestones in final month (back-loaded)
- ❌ Schedule confidence always "high"

### Resource Requirements

**Purpose:** Specify what's needed to execute

**Tips:**
- Personnel by role, not just headcount
- Budget breakdown enables trade-off discussions
- Confidence levels should vary (some estimates are better than others)
- Infrastructure needs often forgotten—include early

**Anti-patterns:**
- ❌ Single-number budget with no breakdown
- ❌ All estimates "high confidence" (red flag)
- ❌ Personnel without skills specified
- ❌ No basis for estimates

### Risks and Mitigations

**Purpose:** Demonstrate preparedness for what could go wrong

**Tips:**
- Risks should be specific to THIS program
- Mitigations should be actionable (not "hope it doesn't happen")
- Risk matrix helps prioritize attention
- Contingency plans for high-impact risks are essential
- Update risk register throughout execution

**Anti-patterns:**
- ❌ Generic risks ("requirements may change")
- ✅ "Key SME availability limited in Q2 due to competing project"
- ❌ Mitigations that are just restated risks
- ❌ No contingency for high-impact risks
- ❌ Risk owner is "the team"

### Deliverables and Acceptance

**Purpose:** Define what gets delivered and how acceptance works

**Tips:**
- Deliverables should trace to architecture/objectives
- Acceptance criteria enable unambiguous sign-off
- Acceptance process should name who approves
- Map deliverables to milestones for tracking

**Anti-patterns:**
- ❌ Deliverables without acceptance criteria
- ❌ Acceptance criteria that are subjective ("high quality")
- ❌ No clear acceptance authority

### Operations and Assessment

**Purpose:** Establish how the program will be governed

**Tips:**
- Governance should enable decisions, not create bureaucracy
- Reporting cadence should match stakeholder needs
- Metrics should be leading indicators (not just lagging)
- Change management prevents scope creep while enabling adaptation
- Lessons learned capture enables continuous improvement

**Anti-patterns:**
- ❌ Governance meeting weekly for strategic plan (overkill)
- ❌ Monthly reporting for tactical plan (too slow)
- ❌ Metrics that can't be measured
- ❌ No change management (invites scope creep)
- ❌ Lessons learned "at the end" (too late to apply)

## Workflow Guidance

### Recommended Authoring Sequence

1. **Gather Foundation** (30 min)
   - Read architecture document—understand goal state
   - Read lifecycle document—understand the path
   - Identify stakeholders and their concerns

2. **Draft Scope and Objectives** (45 min)
   - Derive objectives from architecture
   - Define scope boundaries
   - Document constraints and assumptions

3. **Map Execution Approach** (30 min)
   - Summarize lifecycle for this program
   - Identify V&V touchpoints
   - Note where lifecycle phases map to activities

4. **Build Work Breakdown** (60 min)
   - Decompose into activities
   - Establish dependencies
   - Identify critical path
   - Create timeline visualization

5. **Assign Teams and Responsibilities** (45 min)
   - Identify teams/individuals
   - Build RACI matrix
   - Identify external dependencies

6. **Develop Timeline and Milestones** (45 min)
   - Define milestones with criteria
   - Estimate durations
   - Assess schedule confidence
   - Create visual timeline

7. **Estimate Resources** (45 min)
   - Personnel by role
   - Budget by category
   - Infrastructure needs
   - Confidence assessment

8. **Analyze Risks** (60 min)
   - Brainstorm risks specific to program
   - Assess probability and impact
   - Develop mitigations
   - Create contingency plans
   - Assign ownership

9. **Define Deliverables and Acceptance** (30 min)
   - List deliverables traced to objectives
   - Define acceptance criteria
   - Establish acceptance process

10. **Establish Operations** (30 min)
    - Define governance structure
    - Set reporting cadence
    - Identify metrics
    - Document change management

11. **Write Executive Summary** (30 min)
    - Synthesize key points for stakeholders
    - Review for non-technical accessibility
    - Include honest confidence assessment

12. **Quality Review** (45 min)
    - Check traceability chains
    - Verify all sections complete
    - Review for realism
    - Test against quality criteria

### Quality Checkpoints

- **After step 3:** Do objectives clearly trace to architecture?
- **After step 5:** Can you trace the critical path?
- **After step 6:** Is every activity owned?
- **After step 8:** Are risks specific and actionable?
- **After step 11:** Would a funder understand and trust this plan?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Disconnected from Architecture** | Objectives seem arbitrary | Create explicit trace table; delete objectives that don't trace |
| **Lifecycle Duplication** | Plan copies lifecycle content | Reference lifecycle document; only add program-specific details |
| **Optimistic Scheduling** | All estimates aggressive | Add basis for estimates; include confidence levels; add contingency |
| **Generic Risks** | "Schedule may slip" | Identify specific program risks; conduct pre-mortem exercise |
| **Diffuse Accountability** | "The team" owns activities | Assign single owner to each activity; complete RACI |
| **Technical Executive Summary** | Stakeholders can't understand | Rewrite for non-technical audience; lead with value |
| **Unmeasurable Milestones** | "Phase 1 complete" | Add specific, verifiable criteria for each milestone |
| **Missing Contingency** | Plan assumes everything works | Add time/budget contingency; create contingency plans for high risks |
| **Stale Risk Register** | Boilerplate risks | Conduct program-specific risk workshop; update throughout execution |
| **Governance Overhead** | Weekly exec meetings for 2-year program | Match governance intensity to plan level and program phase |

## Best Practices

1. **Write Executive Summary Last** - Only after you understand everything can you summarize effectively
2. **Trace Everything** - Architecture → objectives → activities → deliverables should be traceable
3. **Be Honest About Confidence** - Stakeholders trust honest uncertainty more than false certainty
4. **Make Risks Specific** - Generic risks signal lack of thought; specific risks enable action
5. **Single Owner Per Activity** - Shared ownership is no ownership
6. **Verifiable Milestones** - If you can't tell whether a milestone is achieved, it's not a milestone
7. **Right-Size Governance** - Match reporting and oversight to program scale and risk
8. **Update Living Documents** - Plans should evolve; establish update cadence
9. **Respect Stakeholder Time** - Executive summary should fit on one page
10. **Connect to Lifecycle Gates** - Program milestones should align with lifecycle V&V gates

## Validation vs. Verification

**Verification** (deterministic, against spec-for-program-plan):
- Are all required sections present?
- Are architecture_ref and lifecycle_ref specified?
- Are there at least 3 objectives, 3 milestones, 5 risks?
- Is plan_level specified as strategic or tactical?

**Validation** (qualitative, against this guidance):
- Does the plan inspire stakeholder confidence?
- Are objectives traceable to architecture?
- Is the schedule realistic with honest confidence assessment?
- Are risks specific and well-mitigated?
- Is accountability clear throughout?
- Could this plan be executed effectively?

This guidance document supports **validation** - assessing fitness-for-purpose.

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

- **Stakeholder Confidence:** Written for program plan authors with clear value proposition
- **Traceability:** References spec-for-program-plan and builds on architecture/lifecycle guidance
- **Realism:** Acknowledges differences between strategic and tactical plans
- **Risk Awareness:** Common issues section addresses what typically goes wrong
- **Accountability Clarity:** Clear guidance ownership at section level
- **Operational Readiness:** Workflow guidance enables immediate application

## Document Metadata

| Property | Value |
|----------|-------|
| Specification | [[spec-for-program-plan]] |
| Guidance Version | 1.0.0 |
| Specification Version | 1.0.0 |
| Prerequisites | [[guidance-for-architecture]], [[guidance-for-lifecycle]] |
| Target Users | Program managers, engineers creating execution plans |

---

**Note:** This guidance is coupled with [[spec-for-program-plan]] via a coupling edge. Together with architecture and lifecycle guidance, it supports the complete architecture → lifecycle → program plan progression for delivering assured capability.
