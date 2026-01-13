---
type: vertex/guidance
extends: doc
id: v:guidance:system_prompt
name: Guidance for System Prompt Documents
description: Quality criteria and best practices for creating excellent system prompt documents that integrate Persona, Purpose, and Protocol using the PPP framework
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-27T22:00:00Z
modified: 2025-12-27T22:00:00Z
dependencies:
  - v:guidance:persona
  - v:guidance:purpose
  - v:guidance:protocol
---

# Guidance for System Prompt Documents

**This guidance defines quality criteria and best practices for creating excellent system prompt documents.**

## Purpose

While [[spec-for-system-prompt]] defines what structural elements must be present, this guidance helps authors assess **how well** a system prompt integrates its three components. Great system prompts have individually excellent components that also work together seamlessly. **CRITICAL: Design in order - Purpose → Persona → Protocol.**

## Document Overview

### What This Guidance Covers

This guidance supports authors creating complete AI model system prompts using the PPP (Persona-Purpose-Protocol) framework.

### Best Use Cases

Use this guidance when creating integrated system prompts where Persona, Purpose, and Protocol must work together coherently.

## Quality Criteria

### 1. Component Verification

**Excellent:** All three sections (Persona, Purpose, Protocol) verify individually against their specs
**Good:** Most sections verify
**Needs Improvement:** Components fail individual verification

### 2. Persona-Purpose Alignment

**Excellent:** Persona expertise specifically enables Purpose objectives
**Good:** General alignment between expertise and objectives
**Needs Improvement:** Persona expertise doesn't support Purpose

### 3. Purpose-Protocol Alignment

**Excellent:** Protocol workflow systematically achieves Purpose deliverables
**Good:** Protocol generally achieves Purpose
**Needs Improvement:** Protocol doesn't accomplish Purpose objectives

### 4. Persona-Protocol Consistency

**Excellent:** Protocol reflects Persona's approach and methodology
**Good:** Some reflection of Persona in Protocol
**Needs Improvement:** Protocol contradicts Persona approach

### 5. Tone Consistency

**Excellent:** Tone from Persona is maintained throughout Purpose and Protocol
**Good:** Mostly consistent tone
**Needs Improvement:** Tone varies or contradicts across components

### 6. No Contradictions

**Excellent:** Persona boundaries align with Purpose constraints; no conflicts anywhere
**Good:** Few minor contradictions
**Needs Improvement:** Major contradictions between components

### 7. Integration Validation

**Excellent:** Explicit validation section confirms component alignment and checks for contradictions
**Good:** Some integration checking present
**Needs Improvement:** No integration validation

### 8. Obsidian Compatibility

**Excellent:** Links dependencies to [[spec-for-persona]], [[spec-for-purpose]], [[spec-for-protocol]]
**Good:** Basic linking present
**Needs Improvement:** Missing dependency links

## Workflow Guidance

### Design Sequence (CRITICAL)

1. **Design Purpose FIRST** (40 min)
   - Purpose is the anchor
   - Define problem, objectives, deliverables, constraints, success
   - Verify against [[spec-for-purpose]]

2. **Design Persona to Match** (30 min)
   - What expertise is needed for this Purpose?
   - Define role, expertise, approach, tone, boundaries
   - Verify against [[spec-for-persona]]

3. **Design Protocol to Deliver** (60 min)
   - How to achieve Purpose through Persona?
   - Define workflow, phases, collaboration, quality, principles
   - Verify against [[spec-for-protocol]]

4. **Validate Integration** (20 min)
   - Check all components verify individually
   - Verify Persona enables Purpose
   - Verify Protocol achieves Purpose
   - Check for contradictions
   - Ensure tone consistency

### Total Estimated Time: 2.5 hours

## Integration Validation Checklist

**Component Alignment:**
- ✅ Persona expertise enables Purpose objectives
- ✅ Persona role matches Purpose domain
- ✅ Protocol workflow achieves Purpose deliverables
- ✅ Persona approach reflected in Protocol phases

**Consistency Checks:**
- ✅ Tone consistent across all components
- ✅ No contradictions between components
- ✅ Boundaries in Persona align with constraints in Purpose
- ✅ All three components verify individually

**Coherence Tests:**
- ✅ 30-second test: Can user quickly understand who, why, how?
- ✅ Consistency test: Are there contradictions?
- ✅ Practicality test: Is this executable?
- ✅ Value test: Does this solve real problem?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Components Designed in Isolation | No integration | Design Purpose first, then Persona to match, then Protocol to deliver |
| Misaligned Expertise | Persona doesn't enable Purpose | Ensure Persona expertise specifically supports Purpose objectives |
| Protocol Doesn't Achieve Purpose | Workflow doesn't deliver | Map Protocol phases to Purpose objectives explicitly |
| Contradictions | Boundaries vs constraints conflict | Check alignment: Persona boundaries should match Purpose constraints |
| Inconsistent Tone | Tone varies across components | Verify tone in Persona maintained in Purpose and Protocol |
| Failed Individual Verification | Component doesn't meet spec | Each section MUST verify against its spec before integration |

## Best Practices

1. **ALWAYS design in order:** Purpose → Persona → Protocol
2. **Verify each component individually** against its spec
3. **Check integration:** Do components align and support each other?
4. **Test coherence:** 30-second test, consistency test, practicality test
5. **Ensure tone consistency** across all components
6. **Look for contradictions** between components
7. **Make each component excellent** individually AND integrated
8. **Purpose drives everything** - Persona and Protocol serve Purpose

---

**Note:** System prompts demonstrate the compositional document pattern where subsections must conform to other specifications. This is analogous to typing fields with schemas (like context in JSON-LD).
