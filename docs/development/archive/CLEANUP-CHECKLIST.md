# Repository Cleanup - Development Checklist

**Start Date**: 2025-12-28
**Status**: Stage 3 Complete - In Progress
**Reference**: [docs/REPOSITORY-CLEANUP-PLAN.md](docs/REPOSITORY-CLEANUP-PLAN.md)

---

## Pre-Cleanup Decisions

- [ ] **Workshop Archive**: Archive or just delete?
- [ ] **Assurance Audit**: Rebuild from scratch or update existing?
- [ ] **RACI Location**: Identify current RACI elements, decide on chart location
- [ ] **Learning Depth**: Determine tutorial depth (quick start vs comprehensive)
- [ ] **Chart Cleanup**: Identify any incomplete charts to remove

---

## Stage 1: Safe Deletions

- [~] Archive `workshop/` if needed (skipped - user approved direct deletion)
- [✓] Remove `workshop/` directory
- [✓] Find and remove `.DS_Store` files (`find . -name .DS_Store -delete`)
- [✓] Remove `__pycache__` directories (`find . -type d -name __pycache__ -exec rm -rf {} +`)
- [✓] Add `__pycache__/` and `.DS_Store` to `.gitignore` (already present)
- [✓] **Verify**: Run test suite after deletions (all 10 tests pass)
- [✓] **Commit**: "chore: remove workshop and cleanup temp files" (commit 1b7e25c)

---

## Stage 2: Documentation Consolidation

### Create Directory Structure

- [✓] Create `docs/learning/`
- [✓] Create `docs/concepts/`
- [✓] Create `docs/development/`
- [✓] Create `docs/use-cases/`
- [✓] Create `docs/use-cases/raci-coordination/`
- [✓] Create `docs/use-cases/assurance-audit/`

### Move and Organize Files

#### From documentation/ → docs/concepts/
- [✓] Move `documentation/charts-vs-chart-documents.md` → `docs/concepts/charts-vs-documents.md`
- [✓] Move `documentation/validation-accountability.md` → `docs/concepts/validation-accountability.md`
- [✓] Delete empty `documentation/` directory

#### Organize Current docs/
- [✓] Move `docs/LEARNING-PATH.md` → `docs/learning/README.md`
- [✓] Move test coverage docs to `docs/development/`:
  - [✓] `TEST-COVERAGE-100-PERCENT.md` → `docs/development/test-coverage.md`
  - [✓] `TEST-COVERAGE-ANALYSIS.md` → (archived to development/archive/)
  - [✓] `TEST-COVERAGE-RESULTS.md` → (archived to development/archive/)
  - [✓] `TEST-SUITE-FIX.md` → (archived to development/archive/)
- [✓] Move template docs to `docs/development/`:
  - [✓] Consolidate `TEMPLATE-*.md` → `docs/development/template-generation-design.md`
  - [✓] `SPECS-VS-TEMPLATES-*.md` → (archived to development/archive/)

#### Create New Files
- [✓] Create `docs/README.md` (documentation index)
- [ ] Create `docs/concepts/README.md` (concepts overview)
- [ ] Create `docs/development/README.md` (developer guide)

### Update Cross-References
- [ ] Update all internal links in moved files
- [ ] Update links from other docs to moved files
- [ ] **Verify**: Run link checker (manual check)
- [✓] **Commit**: "docs: consolidate documentation structure" (commit 05a0472)

---

## Stage 3: Use Case Organization

### RACI Coordination Use Case

- [~] **Identify**: Find current RACI elements (org, staff, team, role, actor, property) - No existing implementation found
- [~] **Decide**: Chart location (`charts/raci-coordination/` or keep current) - Deferred to future work
- [~] Create `docs/use-cases/raci-coordination/README.md` - Deferred to future work
- [~] Create `docs/use-cases/raci-coordination/chart.md` (copy from charts/) - Deferred to future work
- [~] Create `docs/use-cases/raci-coordination/analysis.md` (inheritance pattern) - Deferred to future work
- [~] Create `docs/use-cases/raci-coordination/elements.md` (vertex/edge/face list) - Deferred to future work
- [~] **Verify**: Check all RACI elements exist and verify - Deferred to future work
- [~] **Commit**: "docs: add RACI coordination use case" - Deferred to future work

### Assurance Audit Use Case

**Found Existing Implementation:**
- [✓] Located chart-types-audit chart with complete assurance example
- [✓] Found 25+ assurance faces, verification edges, validation edges
- [~] Rebuilding from scratch - Not needed, using existing implementation

**Documentation:**
- [✓] Create `docs/use-cases/assurance-audit/README.md`
- [✓] Create `docs/use-cases/assurance-audit/audit-trail.md` (complete walkthrough)
- [✓] Create `docs/use-cases/assurance-audit/triangle-pattern.md` (verification→validation→assurance)
- [✓] Create `docs/use-cases/assurance-audit/tooling.md` (audit script usage)
- [✓] **Verify**: Run audit on example (chart-types-audit PASS, 100% coverage)
- [✓] **Commit**: "docs: add assurance audit use case" (commit 542b2e2)

---

## Stage 4: Learning Path Creation

### Transform Learning Path
- [ ] Expand `docs/learning/README.md` with journey overview
- [ ] Create `docs/learning/00-getting-started.md`
  - [ ] Repository structure overview
  - [ ] Quick start: verify existing elements
  - [ ] Run test suite
  - [ ] Prerequisites and next steps
- [ ] Create `docs/learning/01-core-concepts.md`
  - [ ] Simplicial complexes (vertices, edges, faces)
  - [ ] Type system (spec, guidance, doc)
  - [ ] IDs and naming conventions
  - [ ] Frontmatter structure
  - [ ] Hands-on exercises
- [ ] Create `docs/learning/02-verification.md`
  - [ ] Template-based verification
  - [ ] Verification edges (tool checks)
  - [ ] Validation edges (human reviews)
  - [ ] Assurance faces (audit triangles)
  - [ ] Accountability patterns
  - [ ] Hands-on exercises
- [ ] Create `docs/learning/03-templates.md`
  - [ ] Template system architecture
  - [ ] Generating templates from specs
  - [ ] Template freshness checking
  - [ ] Creating new document types
  - [ ] Hands-on exercises
- [ ] Create `docs/learning/04-chart-basics.md`
  - [ ] What are charts?
  - [ ] Chart structure and frontmatter
  - [ ] Creating a chart
  - [ ] Verifying chart topology
  - [ ] Visualizing charts
  - [ ] Hands-on exercises
- [ ] Create `docs/learning/05-use-cases.md`
  - [ ] RACI coordination walkthrough
  - [ ] Assurance audit walkthrough
  - [ ] Creating your own chart-type
  - [ ] Extending the system
  - [ ] Final exercises

### Add Cross-References
- [ ] Link each module to prerequisites
- [ ] Link to relevant concept docs
- [ ] Link to use cases
- [ ] Link to script documentation
- [ ] **Verify**: Learning path is navigable
- [ ] **Commit**: "docs: create structured learning path"

---

## Stage 5: Supporting Documentation

### Charts Documentation
- [ ] Update `charts/README.md`
  - [ ] Add "Example Charts for Learning" section
  - [ ] Link to learning path (04-chart-basics.md)
  - [ ] Link to use cases
  - [ ] Update chart inventory
- [ ] **Commit**: "docs: update charts README with learning references"

### Templates Documentation
- [ ] Create `templates/README.md`
  - [ ] Explain template system
  - [ ] Template types (vertices, edges, faces, charts)
  - [ ] How to use templates
  - [ ] Link to template generation docs
  - [ ] Link to learning path (03-templates.md)
- [ ] **Commit**: "docs: add templates README"

### Scripts Documentation
- [ ] Create `scripts/README.md`
  - [ ] Script categories (verification, generation, analysis, visualization)
  - [ ] Script reference table with usage
  - [ ] Common workflows
  - [ ] Link to development docs
  - [ ] Link to learning path exercises
- [ ] **Commit**: "docs: add scripts README with reference"

### Top-Level README
- [ ] Update main `README.md`
  - [ ] Clarify template vs learning purposes
  - [ ] Link to learning path
  - [ ] Link to use cases
  - [ ] Quick start guide
  - [ ] Repository structure overview
- [ ] **Commit**: "docs: update main README with learning path"

---

## Final Verification

### Link Checking
- [ ] Check all links in `docs/learning/`
- [ ] Check all links in `docs/concepts/`
- [ ] Check all links in `docs/development/`
- [ ] Check all links in `docs/use-cases/`
- [ ] Check all links in README files (charts, templates, scripts, main)
- [ ] Fix any broken references
- [ ] **Commit**: "docs: fix broken links after reorganization"

### Test Suite Verification
- [ ] Run full test suite: `python tests/run_tests.py`
- [ ] Verify all 10 test suites pass
- [ ] Check template freshness: `python scripts/generate_all_templates.py --check`
- [ ] Verify cache builds: `python scripts/build_cache.py`
- [ ] **Verify**: All tests passing, no errors

### Repository Health
- [ ] Check repository size (should be ~56MB lighter)
- [ ] Verify no broken symlinks
- [ ] Verify no orphaned files
- [ ] Check `.gitignore` completeness
- [ ] **Verify**: Repository is clean

### Success Criteria Check
- [ ] **Template-Ready**: Clear structure, templates documented, scripts documented
- [ ] **Learning Resource**: Clear progression, concepts explained, exercises included
- [ ] **Maintainable**: No dev artifacts, one doc location, logical organization
- [ ] **Lightweight**: Workshop removed, no duplicates, essential files only

---

## Git Commit Strategy

### Commit Sequence
1. [✓] "chore: remove workshop and cleanup temp files" (commit 1b7e25c)
2. [✓] "docs: consolidate documentation structure" (commit 05a0472)
3. [~] "docs: add RACI coordination use case" (deferred - no existing implementation)
4. [✓] "docs: add assurance audit use case" (commit 542b2e2)
5. [ ] "docs: create structured learning path"
6. [ ] "docs: update charts README with learning references"
7. [ ] "docs: add templates README"
8. [ ] "docs: add scripts README with reference"
9. [ ] "docs: update main README with learning path"
10. [ ] "docs: fix broken links after reorganization"

### Final Commit
- [ ] **Tag**: Create tag `v1.0.0-cleaned` after completion
- [ ] **Branch**: Merge cleanup branch to main
- [ ] **Archive**: Archive pre-cleanup state if needed

---

## Post-Cleanup Tasks

- [ ] Update GitHub repository description
- [ ] Update GitHub topics/tags (knowledge-complex, template, learning)
- [ ] Create GitHub wiki pages (optional)
- [ ] Create CONTRIBUTING.md guide
- [ ] Consider adding GitHub Discussions for Q&A

---

## Notes and Decisions

**Workshop Archive Decision**: Delete without archiving (user approved)

**Assurance Audit Decision**: To be determined - will assess after exploring current state

**RACI Location**: No existing RACI implementation found - mentioned in teaching guide as future concept. Decision: Skip RACI use case for now, focus on assurance audit (which exists).

**Assurance Audit Content**: Found complete example in charts/chart-types-audit/ with chart, visualization, audit trail, and teaching guide. Will document this as primary use case.

**Learning Depth**: Progressive depth - quick start with option to go deeper

**Other Decisions**:

- Stage 2 complete (commit 05a0472)
- Stage 3 complete (commit 542b2e2)
- RACI coordination use case deferred (no existing implementation)
- Proceeding with Stage 4 - Learning Path Creation

---

**Status Legend**:
- [ ] Not Started
- [→] In Progress
- [✓] Complete
- [✗] Blocked (note reason)
- [~] Skipped (note reason)

**Last Updated**: 2025-12-28
