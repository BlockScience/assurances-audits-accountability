# Repository Cleanup Plan

**Date**: 2025-12-28
**Purpose**: Organize repository for use as both template and learning resource

---

## Repository Purpose

This repository serves two primary functions:

1. **Template Repository** - Starter kit for creating new knowledge complexes
2. **Learning Resource** - Educational journey for understanding knowledge complex concepts

---

## Current State Analysis

### Assets Inventory

**Core Simplicial Complex** (132 documents):
- `00_vertices/` - Vertex documents (specs, guidances, docs, personas, purposes, protocols, system_prompts)
- `01_edges/` - Edge documents (verifications, validations, couplings, dependencies, inherits)
- `02_faces/` - Face documents (assurance triangles)

**Chart Collections**:
- `charts/test-tetrahedron/` - Minimal test chart with deliberate hole
- `charts/boundary-complex/` - Foundational chart (specs + guidances)
- `charts/boundary-kernel/` - Foundational core chart
- `charts/chart-types-audit/` - Doc-kit registry chart

**Infrastructure**:
- `scripts/` - Python verification, generation, and analysis tools
- `tests/` - 10 test suites with 76+ tests (100% coverage)
- `templates/` - Document templates for all element types

**Documentation** (scattered):
- `docs/` - Test coverage reports, template generation docs, learning path
- `documentation/` - Chart concepts, validation accountability
- `workshop/` - Development artifacts (56MB, mostly snapshots and logs)

**Use Case Examples**:
- RACI coordination (organization/staff/team/role chart-type) - Deferred
- Assurance audit trail (chart-types-audit with complete audit)
- Learning syllabi (student/skill/learning-module with syllabus chart-type) - In Progress

### Problems Identified

1. **Workshop Bloat**: `workshop/` is 56MB, contains development artifacts no longer needed
2. **Documentation Duplication**: Both `docs/` and `documentation/` exist
3. **Missing Use Case Clarity**: RACI example exists but needs better organization
4. **Incomplete Assurance Example**: Assurance audit use case needs updating for compatibility
5. **No Learning Path Structure**: Educational assets exist but aren't organized as journey
6. **Mixed Concerns**: Development docs mixed with user-facing docs

---

## Cleanup Strategy

### Phase 1: Remove Workshop Directory

**Action**: Delete `workshop/` entirely (56MB weight reduction)

**Rationale**:
- Development snapshots no longer needed (snapshot-20251227)
- Input docs and logs are ephemeral development artifacts
- Development plan captured in committed docs
- Core concepts now stable and documented

**Files to Preserve** (move to appropriate locations):
- `workshop/assurance-inheritance-analysis.md` → Consider if still relevant
- `workshop/development-plan.md` → Archive or extract key learnings

**Command**:
```bash
# Archive if needed
tar -czf workshop-archive-20251228.tar.gz workshop/
# Then remove
rm -rf workshop/
```

### Phase 2: Consolidate Documentation

**Action**: Merge `documentation/` into `docs/` with clear structure

**New Structure**:
```
docs/
├── README.md                           # Documentation index
├── learning/                           # Educational materials
│   ├── README.md                       # Learning path overview
│   ├── 00-getting-started.md           # Repository overview
│   ├── 01-core-concepts.md             # Simplicial complexes, types
│   ├── 02-verification.md              # Verification, validation, assurance
│   ├── 03-templates.md                 # Template system
│   ├── 04-chart-basics.md              # Charts and visualization
│   └── 05-use-cases.md                 # RACI and assurance examples
├── concepts/                           # Reference documentation
│   ├── charts-vs-documents.md          # Chart theory
│   ├── validation-accountability.md    # Validation governance
│   └── template-generation.md          # Template system design
├── development/                        # Developer documentation
│   ├── test-coverage.md                # Test suite documentation
│   ├── template-generation-design.md   # Template generation internals
│   └── scripts-reference.md            # Script usage guide
└── use-cases/                          # Example implementations
    ├── raci-coordination/              # RACI chart-type example
    │   ├── README.md
    │   ├── chart.md
    │   └── analysis.md
    └── assurance-audit/                # Assurance audit example
        ├── README.md
        ├── boundary-complex-audit.md
        └── audit-trail.md
```

**Moves**:
- `documentation/charts-vs-chart-documents.md` → `docs/concepts/`
- `documentation/validation-accountability.md` → `docs/concepts/`
- Current `docs/LEARNING-PATH.md` → `docs/learning/README.md` (expand)
- Test coverage docs stay in `docs/development/`
- Template docs consolidate to `docs/development/template-generation-design.md`

### Phase 3: Organize Use Case Examples

#### RACI Coordination Chart-Type

**Current State**: Elements exist but scattered

**Action**: Create `docs/use-cases/raci-coordination/`

**Contents**:
- `README.md` - Overview of RACI chart-type and coordination structs
- `chart.md` - Chart document showing org structure (copied from charts/)
- `analysis.md` - Analysis of actor/property pattern, inheritance (staff→actor, team→actor, role→property)
- `elements.md` - List of vertices, edges, faces in this example

**Chart Location**: Keep actual chart in `charts/raci-coordination/` (rename from current location if needed)

#### Assurance Audit Use Case

**Current State**: Boundary-complex assurance audit exists but may need updates

**Action**: Create `docs/use-cases/assurance-audit/`

**Contents**:
- `README.md` - Overview of assurance audit workflow
- `audit-trail.md` - Complete audit trail for a document (spec-for-spec or guidance-for-guidance)
- `triangle-pattern.md` - Explanation of verification→validation→assurance triangle
- `tooling.md` - How to use audit tools

**Decision Needed**: Should we rebuild assurance audit example for compatibility?

**Recommendation**: Yes, rebuild with current tools to ensure:
- Compatible with updated verification/validation/assurance templates
- Uses current accountability patterns
- Demonstrates full audit trail clearly

### Phase 4: Create Learning Path Structure

**Action**: Transform `docs/LEARNING-PATH.md` into structured journey

**docs/learning/README.md** - Journey overview with progression

**00-getting-started.md**:
- What is a knowledge complex?
- Repository structure overview
- Quick start: verify existing elements
- Run test suite

**01-core-concepts.md**:
- Simplicial complexes (vertices, edges, faces)
- Type system (spec, guidance, doc)
- IDs and naming conventions
- Frontmatter structure

**02-verification.md**:
- Template-based verification
- Verification edges (tool checks spec compliance)
- Validation edges (human reviews guidance compliance)
- Assurance faces (complete audit triangle)
- Accountability patterns

**03-templates.md**:
- Template system architecture
- Generating templates from specs
- Template freshness checking
- Creating new document types

**04-chart-basics.md**:
- What are charts?
- Chart structure and frontmatter
- Creating a chart
- Verifying chart topology
- Visualizing charts

**05-use-cases.md**:
- RACI coordination chart-type walkthrough
- Assurance audit trail walkthrough
- Creating your own chart-type
- Extending the system

**Each file should have**:
- Prerequisites (what to read first)
- Learning objectives
- Concepts explained
- Hands-on exercises
- Next steps

### Phase 5: Chart Organization

**Current Charts**:
- `test-tetrahedron/` - Keep (regression test baseline)
- `boundary-complex/` - Keep (foundational example)
- `boundary-kernel/` - Keep (minimal kernel example)
- `chart-types-audit/` - Keep (doc-kit registry)

**New Charts to Add** (if RACI example organized):
- `raci-coordination/` - RACI org structure example

**Chart README Updates**:
- Update `charts/README.md` to reference learning path
- Add "Example Charts for Learning" section
- Link to use case documentation

### Phase 6: Template Organization

**Current State**: Templates well-organized

**Improvements**:
- Add `templates/README.md` explaining template system
- Add "Extending Templates" guide
- Link to template generation docs

### Phase 7: Scripts and Tests Organization

**Current State**: Good organization, comprehensive testing

**Improvements**:
- Add `scripts/README.md` with script reference
- Group scripts by category (verification, generation, analysis, visualization)
- Add usage examples for each script
- Link to learning path sections

**No Changes Needed**:
- Test suite structure is excellent
- Test coverage documentation is comprehensive

---

## Implementation Order

### Stage 1: Safe Deletions
1. ✅ Archive and remove `workshop/` directory
2. ✅ Remove any `.DS_Store` files
3. ✅ Remove `__pycache__` directories (add to .gitignore)

### Stage 2: Documentation Consolidation
4. ✅ Create `docs/` subdirectories (learning, concepts, development, use-cases)
5. ✅ Move and rename documentation files
6. ✅ Create `docs/README.md` as documentation index
7. ✅ Update cross-references

### Stage 3: Use Case Organization
8. ✅ Create RACI use case documentation
9. ✅ Rebuild assurance audit use case (if needed)
10. ✅ Create use case READMEs

### Stage 4: Learning Path Creation
11. ✅ Transform learning path into structured journey
12. ✅ Create individual learning modules
13. ✅ Add exercises and examples
14. ✅ Add progression path

### Stage 5: Supporting Documentation
15. ✅ Create `charts/README.md` updates
16. ✅ Create `templates/README.md`
17. ✅ Create `scripts/README.md`
18. ✅ Update top-level README.md

---

## Success Criteria

### Repository is Template-Ready
- [ ] Clear structure for starting new knowledge complex
- [ ] Templates easily discoverable and documented
- [ ] Scripts documented with usage examples
- [ ] Example charts demonstrate patterns

### Repository is Learning Resource
- [ ] Clear learning progression (beginner → advanced)
- [ ] Each concept explained with examples
- [ ] Hands-on exercises at each stage
- [ ] Use cases demonstrate real-world application

### Repository is Maintainable
- [ ] No development artifacts (workshop removed)
- [ ] Documentation in one clear location (docs/)
- [ ] Logical organization by concern
- [ ] Cross-references working
- [ ] README files guide navigation

### Repository is Lightweight
- [ ] Removed ~56MB of workshop artifacts
- [ ] No duplicate documentation
- [ ] Only essential files remain
- [ ] Clean git history (workshop in archive if needed)

---

## Files to Review with User

**Before Deleting**:
- `workshop/assurance-inheritance-analysis.md` - Extract key insights?
- `workshop/development-plan.md` - Archive historical context?

**Assurance Audit Decision**:
- Should we rebuild assurance audit use case from scratch for compatibility?
- OR update existing boundary-complex assurance audit?
- RECOMMENDED: Rebuild with clear step-by-step documentation

**RACI Example**:
- Where are the RACI chart files currently?
- Do we have org/staff/team/role vertices and edges?
- Should we create a dedicated `charts/raci-coordination/` chart?

---

## Future Enhancements (Not in Current Cleanup)

### Learning Modules for Framework Development

Create learning modules that teach users how to extend the framework itself:

1. **Creating New Specs and Guidance**
   - Learning module on spec creation process
   - Learning module on guidance creation process
   - Exercises: Create a new vertex type with spec + guidance
   - Integration with template generation system

2. **Creating New Templates**
   - Learning module on template structure
   - Learning module on edge templates (relationships, no specs)
   - Learning module on face templates (triangles, no specs)
   - Exercises: Create templates for new types

3. **Extending Chart Types**
   - Learning module on chart specs and guidance
   - Learning module on chart-specific constraints
   - Exercises: Create a new chart type for a domain

**Rationale**: This would enable users to not just use the framework, but extend it for their own domains. Teaching how to create specs/guidance documents demonstrates the self-referential nature of the system.

**Status**: Planned for future phase after initial cleanup complete

---

## Post-Cleanup Tasks

1. **Update Top-Level README.md**:
   - Link to learning path
   - Link to use cases
   - Clarify template vs learning purposes

2. **Verify All Links**:
   - Run link checker on all markdown files
   - Fix any broken references
   - Update relative paths

3. **Test Suite Verification**:
   - Run full test suite after cleanup
   - Verify all scripts still work
   - Update any hardcoded paths

4. **Git Commit Strategy**:
   - Commit deletions separately
   - Commit moves separately
   - Commit new content separately
   - Clear commit messages for archaeology

---

## Questions for User

1. **Workshop Archive**: Do you want `workshop/` archived before deletion, or just delete?

2. **Assurance Audit**: Should we rebuild the assurance audit use case from scratch to ensure compatibility and clarity?

3. **RACI Location**: Where are the current RACI coordination elements? Should we create a dedicated chart?

4. **Learning Path Depth**: How detailed should the learning modules be? (Quick start vs comprehensive tutorial)

5. **Chart Cleanup**: Are there any other charts in development that should be removed or completed?

---

**Next Step**: User approval and answers to questions, then proceed with Stage 1 (safe deletions).
