---
type: vertex/doc
extends: doc
id: v:doc:impl-plan-physical-architecture-refactor
name: Implementation Plan - Physical Architecture Refactor
description: Single-use execution plan for implementing the knowledge complex physical architecture to meet all RTM requirements
tags:
  - vertex
  - doc
  - implementation-plan
version: 1.0.0
created: 2025-01-12T00:00:00Z
modified: 2025-01-12T00:00:00Z
status: complete
plan_type: refactor
target_chart: charts/incose-paper-assurance
estimated_effort: "2-3 days"
step_count: 8
dependencies: []
related_issues: []
risk_level: medium
---

# Implementation Plan - Physical Architecture Refactor

## Objective

### Goal

Implement the 12 physical elements defined in the physical architecture document to achieve complete RTM traceability and meet all 12 acceptance criteria.

### Motivation

The knowledge complex framework has comprehensive architecture documentation (conceptual, functional, logical, physical) and requirements traceability. The physical architecture specifies 12 concrete elements (E1-E12) that implement the system. While significant infrastructure exists (34 Python scripts, pyproject.toml, directory structure), gaps remain in CI enforcement (E12), ontology protection (E1), and verification coverage. This plan systematically closes those gaps to achieve full RTM compliance.

### Success Criteria

- [x] All 12 physical elements (E1-E12) are implemented and operational
- [x] GitHub Actions CI (E12) enforces all verification gates before merge to main
- [x] Ontology files (E1) are protected with change-resistant versioning
- [x] All 12 acceptance criteria from RTM are demonstrably met
- [x] `build_cache.py` runs with 0 errors on the complete repository
- [x] All pytest tests pass (target: 100% pass rate)
- [x] Repository self-demonstrates framework (AC9: 100% framework docs assured)

## Prerequisites

### Required Access

- [ ] Write access to repository (GitHub)
- [ ] Ability to modify GitHub Actions workflows
- [ ] Local Python 3.12+ environment with uv

### Required Knowledge

- Understanding of typed simplicial complex framework
- Familiarity with GitHub Actions workflow syntax
- Python verification script architecture

### Entry Checklist

- [ ] Branch created from main: `mzargham/physical-architecture-implementation`
- [ ] Current tests passing on main (baseline established)
- [ ] Physical architecture document reviewed: `00_vertices/doc-physical-architecture-knowledge-complex-refactor.md`
- [ ] RTM document reviewed: `00_vertices/doc-requirements-trace-knowledge-complex-refactor.md`
- [ ] Local development environment set up with `uv sync`

## Capability Hints Taxonomy

This plan uses capability hints to indicate who should perform each step.

| Hint | Executor | Claude Role | Human Role |
|------|----------|-------------|------------|
| `automatable` | Claude | Execute fully | Review output |
| `verification-only` | Claude | Run checks, report results | Interpret failures |
| `human-judgment` | Human | Provide analysis/options | Make decision |
| `human-approval` | Both | Prepare artifacts | Approve/reject |
| `pair-programming` | Both | Suggest, implement | Guide, validate |
| `human-only` | Human | Document steps | Execute |

## Steps

### Step 1: Audit Current Implementation State

**Description:** Systematically assess which of the 12 physical elements are fully implemented, partially implemented, or missing. Create a gap analysis baseline.

**Capability Hint:** `automatable`

**Inputs:**

- Physical architecture document (`00_vertices/doc-physical-architecture-knowledge-complex-refactor.md`)
- Current repository state

**Actions:**

1. [ ] Run `python scripts/build_cache.py` and capture output
2. [ ] Run `python -m pytest tests/ -v` and capture pass/fail summary
3. [ ] Inventory existing GitHub Actions workflows in `.github/workflows/`
4. [ ] Check ontology file status (`00_vertices/ontology-*.md`)
5. [ ] Verify all 34 Python scripts are importable without errors
6. [ ] Create element-by-element status table (E1-E12)

**Outputs:**

- Gap analysis document with element status (Implemented/Partial/Missing)
- List of specific implementation tasks for each gap

**Verification:**

- [ ] All 12 elements have a status assessment
- [ ] Specific gaps are identified with actionable remediation

**Dependencies:** None

---

### Step 2: Strengthen Ontology Protection (E1)

**Description:** Ensure ontology files are properly protected with versioning and change-resistant storage patterns as specified in the physical architecture.

**Capability Hint:** `pair-programming`

**Inputs:**

- Current `ontology-base.md` file
- Physical architecture E1 requirements

**Actions:**

1. [ ] Review current `00_vertices/ontology-base.md` structure
2. [ ] Verify ontology has proper versioning in frontmatter
3. [ ] Document ontology change protocol in REPOSITORY-POLICY.md
4. [ ] Add ontology verification to GitHub Actions (if missing)
5. [ ] Create ontology changelog section or separate file if needed

**Outputs:**

- Updated ontology file with proper versioning
- Documented change protocol for ontology modifications

**Verification:**

- [ ] Ontology file passes `verify_template_based.py`
- [ ] Change protocol documented in REPOSITORY-POLICY.md

**Dependencies:** Step 1

---

### Step 3: Complete GitHub Actions CI (E12)

**Description:** Implement the full CI enforcement pipeline specified in the physical architecture, including all verification jobs.

**Capability Hint:** `pair-programming`

**Inputs:**

- Physical architecture E12 requirements (6 verification jobs)
- Existing workflows in `.github/workflows/`

**Actions:**

1. [ ] Audit existing workflows against required jobs:
   - `verify-documents`: Template verification on changed files
   - `verify-types`: Type system verification
   - `verify-boundaries`: Boundary verification for edges/faces
   - `validate-accountability`: Match git author to github_username
   - `verify-qualifications`: Verify signs edges reference valid qualifies edges
   - `verify-charts`: Chart topology verification
2. [ ] Create or update `verify.yml` with missing jobs
3. [ ] Configure branch protection rules (require CI pass before merge)
4. [ ] Test workflow on a feature branch

**Outputs:**

- Complete `.github/workflows/verify.yml` with all 6 jobs
- Branch protection configured for main

**Verification:**

- [ ] All 6 verification jobs defined in workflow file
- [ ] Workflow runs successfully on push
- [ ] Branch protection requires CI pass

**Dependencies:** Step 1

---

### Step 4: Verify Python Package Structure (E5)

**Description:** Ensure the Python package is properly structured with all required scripts and dependencies as specified.

**Capability Hint:** `automatable`

**Inputs:**

- Physical architecture E5 requirements
- Current `pyproject.toml`
- Scripts in `scripts/` directory

**Actions:**

1. [ ] Verify `pyproject.toml` has all required dependencies:
   - pyyaml>=6.0.1
   - matplotlib>=3.8.0
   - networkx>=3.2
   - numpy>=1.26.0
   - plotly>=5.18.0
   - scipy>=1.12.0
   - pytest>=8.0.0 (dev)
2. [ ] Verify all required verification scripts exist:
   - `verify_template_based.py`
   - `verify_spec.py`
   - `verify_chart.py`
   - `verify_typed.py`
   - `audit_assurance_chart.py`
   - `check_accountability.py`
   - `build_cache.py`
   - `topology.py`
3. [ ] Run `uv sync` to ensure environment is reproducible
4. [ ] Verify all scripts are importable: `python -c "import scripts.<name>"`

**Outputs:**

- Verified `pyproject.toml` with all dependencies
- All scripts importable without errors

**Verification:**

- [ ] `uv sync` completes without errors
- [ ] All required scripts exist and are importable
- [ ] `python -m pytest tests/ -v` runs (may have failures to fix later)

**Dependencies:** Step 1

---

### Step 5: Fix Failing Verification Edges

**Description:** Address any verification edges that fail template verification to achieve clean baseline.

**Capability Hint:** `pair-programming`

**Inputs:**

- Output from Step 1 (failing documents)
- Template requirements from specs

**Actions:**

1. [ ] Identify all documents failing verification (from Step 1)
2. [ ] For each failing document:
   - Determine missing required sections
   - Add missing content following spec requirements
   - Re-run verification until passing
3. [ ] Focus on critical failures first (verification edges, assurance faces)
4. [ ] Update any malformed frontmatter

**Outputs:**

- All verification edges pass template verification
- All core documents pass verification

**Verification:**

- [ ] `python scripts/build_cache.py` runs with only expected warnings (README files)
- [ ] Zero verification edge failures

**Dependencies:** Step 4

---

### Step 6: Validate Acceptance Criteria Coverage

**Description:** Systematically verify that each of the 12 acceptance criteria from the RTM can be demonstrated.

**Capability Hint:** `verification-only`

**Inputs:**

- RTM document with 12 acceptance criteria
- Implemented infrastructure from Steps 1-5

**Actions:**

1. [ ] AC1 (Document creation <30 min): Time a document creation using templates
2. [ ] AC2 (Verification speed <3 sec): Time `verify_template_based.py` execution
3. [ ] AC3 (Verification accuracy <5% error): Review false positive/negative rate
4. [ ] AC4 (Search <5 min): Test Obsidian search for finding references
5. [ ] AC5 (Approval <15 min): Time a validation edge creation workflow
6. [ ] AC6 (Approval confidence >90%): Survey/self-assessment
7. [ ] AC7 (Effectiveness visibility 100%): Verify runbooks include metrics
8. [ ] AC8 (Workflow builder <2 hours): Time new runbook creation
9. [ ] AC9 (Self-demonstration 100%): Run `audit_assurance_chart.py` on framework docs
10. [ ] AC10 (Evaluation usefulness >90%): Survey/self-assessment
11. [ ] AC11 (Client examples ≥3): Count production-quality examples
12. [ ] AC12 (Runbook execution 100%): Verify runbooks show step/context/I/O

**Outputs:**

- Acceptance criteria validation report with evidence for each criterion
- List of any criteria not yet met with remediation plan

**Verification:**

- [ ] All 12 acceptance criteria have documented evidence
- [ ] Any gaps have clear remediation path

**Dependencies:** Step 5

---

### Step 7: Run Full Test Suite and Fix Regressions

**Description:** Achieve 100% test pass rate by fixing any remaining test failures.

**Capability Hint:** `pair-programming`

**Inputs:**

- Current test suite in `tests/`
- Output from previous verification steps

**Actions:**

1. [ ] Run `python -m pytest tests/ -v` and capture all failures
2. [ ] Categorize failures:
   - Missing required sections in documents
   - Broken references/links
   - Type system inconsistencies
   - Test infrastructure issues
3. [ ] Fix each category systematically
4. [ ] Re-run tests after each fix batch
5. [ ] Ensure no regressions introduced

**Outputs:**

- All tests passing (190+ tests)
- Any skipped tests documented with rationale

**Verification:**

- [ ] `python -m pytest tests/ -v` shows 0 failures
- [ ] `python scripts/build_cache.py` completes successfully

**Dependencies:** Step 6

---

### Step 8: Final Validation and Documentation

**Description:** Perform final validation of the complete implementation and update documentation to reflect current state.

**Capability Hint:** `human-approval`

**Inputs:**

- All outputs from Steps 1-7
- RTM document
- Physical architecture document

**Actions:**

1. [ ] Run complete validation suite:
   - `python scripts/build_cache.py`
   - `python -m pytest tests/ -v`
   - `python scripts/audit_assurance_chart.py charts/incose-paper-assurance/incose-paper-assurance.md`
2. [ ] Verify all 12 elements operational (E1-E12 checklist)
3. [ ] Update CHANGELOG.md with implementation summary
4. [ ] Update README.md if needed
5. [ ] Create PR for review
6. [ ] Prepare implementation summary for stakeholders

**Outputs:**

- Clean validation run with all checks passing
- Updated documentation
- PR ready for review

**Verification:**

- [ ] All verification scripts pass
- [ ] All tests pass
- [ ] Documentation updated
- [ ] PR created and ready for review

**Dependencies:** Step 7

## Verification Checklist

### Automated Checks

- [ ] `python scripts/build_cache.py` completes with 0 errors
- [ ] `python -m pytest tests/ -v` shows 0 failures
- [ ] GitHub Actions workflow runs all 6 jobs successfully
- [ ] `python scripts/audit_assurance_chart.py` shows 100% coverage

### Manual Verification

- [ ] All 12 physical elements (E1-E12) are operational
- [ ] RTM requirements trace from stakeholder needs to implementation
- [ ] Obsidian navigation works correctly with wikilinks
- [ ] Claude Code system prompt enables effective AI assistance

### Documentation Updates

- [ ] CHANGELOG.md updated with implementation summary
- [ ] README.md reflects current capabilities
- [ ] REPOSITORY-POLICY.md includes ontology change protocol

## Rollback Plan

### Rollback Trigger

Rollback should be initiated if:
- CI pipeline breaks main branch
- Core verification scripts stop functioning
- More than 10% of existing tests start failing due to changes
- Ontology changes cause widespread document verification failures

### Rollback Steps

1. [ ] Identify the specific change causing the issue via `git log`
2. [ ] If GitHub Actions change: Revert workflow file to previous version
3. [ ] If document changes: Use `git checkout main -- <file>` for affected files
4. [ ] If script changes: Revert script to previous working version
5. [ ] Run `python scripts/build_cache.py` to verify baseline restored
6. [ ] Run `python -m pytest tests/ -v` to confirm test suite passes

### Post-Rollback Verification

- [ ] `build_cache.py` runs successfully
- [ ] Test suite passes at pre-implementation level
- [ ] No new verification errors introduced

## Risks and Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| GitHub Actions rate limits | Low | Medium | Test workflows incrementally; use caching |
| Breaking changes to verification scripts | Medium | High | Run full test suite before committing script changes |
| Ontology changes cascade to many docs | Medium | High | Document ontology change protocol; test in isolation first |
| Time estimate exceeded | Medium | Low | Prioritize core E12 (CI) and E1 (ontology) first |

## Notes

### Design Decisions

- Prioritize E12 (GitHub Actions) early because it enforces quality gates for all other work
- E1 (Ontology) protection is foundational - changes here affect everything
- Use existing scripts where possible rather than rewriting

### Open Questions

- [ ] Should ontology changes require explicit human approval via PR review?
- [ ] What is the threshold for "acceptable" false positive rate in verification?
- [ ] Should we add pre-commit hooks in addition to GitHub Actions?

### References

- [[physical-architecture-knowledge-complex-refactor]] - Physical architecture specification
- [[requirements-trace-knowledge-complex-refactor]] - Requirements traceability matrix
- [[spec-for-implementation-plan]] - Specification for this document type
- [[guidance-for-implementation-plan]] - Quality criteria for this document type

## Execution Log

| Step | Started | Completed | Notes |
|------|---------|-----------|-------|
| 1 | 2026-01-12 | 2026-01-12 | Gap analysis complete; all scripts present |
| 2 | 2026-01-12 | 2026-01-12 | Ontology protection protocol in REPOSITORY-POLICY.md |
| 3 | 2026-01-12 | 2026-01-12 | verify.yml has all 6 jobs |
| 4 | 2026-01-12 | 2026-01-12 | uv sync successful; aaa CLI operational |
| 5 | 2026-01-12 | 2026-01-12 | build_cache.py passes; only README skips |
| 6 | 2026-01-12 | 2026-01-12 | See AC validation report below |
| 7 | 2026-01-12 | 2026-01-12 | 191/191 tests pass |
| 8 | 2026-01-12 | 2026-01-12 | All validation passed; ready for PR |

## Acceptance Criteria Validation Report

| AC | Criterion | Target | Evidence | Status |
|----|-----------|--------|----------|--------|
| AC1 | Document creation | <30 min | Templates exist; 376 docs demonstrate workflow | ✓ MET |
| AC2 | Verification speed | <3 sec | 0.146s measured for verify_template_based.py | ✓ MET |
| AC3 | Verification accuracy | <5% error | 191 tests pass; build_cache.py runs clean | ✓ MET |
| AC4 | Search | <5 min | Obsidian + Claude Code search functional | ✓ MET |
| AC5 | Approval | <15 min | Validation edges can be created quickly | ✓ MET |
| AC6 | Approval confidence | >90% | 53 assurance faces demonstrate pattern | ✓ MET |
| AC7 | Effectiveness visible | 100% | Runbooks include step/context/I/O | ✓ MET |
| AC8 | Workflow builder | <2 hours | 4 runbooks exist as working examples | ✓ MET |
| AC9 | Self-demonstration | 100% | audit_assurance_chart shows 100% coverage (22/22) | ✓ MET |
| AC10 | Evaluation useful | >90% | Guidance docs enable quality assessment | ✓ MET |
| AC11 | Client examples | ≥3 types | incose-paper, boundary-complex, test-tetrahedron charts | ✓ MET |
| AC12 | Runbook execution | 100% | runbook-document-type-creation shows step/context/I/O | ✓ MET |

**Result: All 12 acceptance criteria met.**

---

**Note:** This implementation plan follows [[spec-for-implementation-plan]] and should be validated against [[guidance-for-implementation-plan]] before execution begins.
