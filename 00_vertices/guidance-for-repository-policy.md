---
type: vertex/guidance
extends: doc
id: v:guidance:repository-policy
name: Guidance for Repository Policy Documents
description: Quality criteria and best practices for creating effective repository policy documents that govern contribution patterns and collaboration
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2026-01-02T12:00:00Z
modified: 2026-01-02T12:00:00Z
dependencies: []
criteria:
  - clarity
  - completeness
  - enforceability
  - inclusivity
  - maintainability
rubric: validation-assessment
---

# Guidance for Repository Policy Documents

**This guidance defines quality criteria and best practices for creating effective repository policy documents that govern contribution patterns, collaboration rules, and operational standards.**

## Purpose

While [spec-for-repository-policy](spec-for-repository-policy.md) defines what structural elements must be present, this guidance helps authors assess **how well** a repository policy serves its purpose. Great repository policies are clear, enforceable, inclusive, and appropriate to the repository's context (open source, internal, documentation, code, research, or operations).

## Document Overview

### What This Guidance Covers

This guidance supports authors creating repository policy documents by providing:
- Quality assessment criteria for effective policies
- Best practices for writing clear, enforceable rules
- Context-specific advice for different repository types
- Common pitfalls and their solutions
- Section-by-section authoring guidance
- Workflow recommendations for policy development

### Best Use Cases

Use this guidance when:
- Creating a new repository policy from scratch
- Reviewing an existing policy for quality and completeness
- Adapting a policy template to your specific context
- Onboarding contributors to understand policy expectations
- Evaluating whether a policy effectively governs the repository
- Harmonizing policies across multiple repositories

## Quality Criteria

### 1. Clarity

**Definition:** Policy language is unambiguous and actionable; contributors know exactly what is expected.

**Excellent:**
- Rules use precise, actionable language (MUST, SHOULD, MAY)
- No ambiguous terms without definitions
- Examples illustrate expected behavior
- Edge cases explicitly addressed
- Non-native speakers can understand requirements

**Good:**
- Generally clear with minor ambiguities
- Most common scenarios addressed
- Language mostly consistent

**Needs Improvement:**
- Vague requirements ("contributions should be reasonable")
- Undefined jargon or acronyms
- Contradictory statements
- Missing explanations for non-obvious rules

### 2. Completeness

**Definition:** Policy covers all necessary governance areas without significant gaps.

**Excellent:**
- All required sections present and substantive
- Recommended sections included where applicable
- No implicit assumptions - all rules stated explicitly
- Covers both happy path and exception handling
- Platform-specific details included when relevant

**Good:**
- Required sections present
- Major scenarios covered
- Minor gaps don't prevent contribution

**Needs Improvement:**
- Missing required sections
- Critical scenarios unaddressed (e.g., what happens on conflict?)
- Implicit rules that contributors must guess
- Platform behavior assumed but not documented

### 3. Enforceability

**Definition:** Rules can be consistently applied and verified; policies don't rely on judgment calls for basic compliance.

**Excellent:**
- Rules are objectively checkable where possible
- CI/CD can enforce technical rules automatically
- Human review criteria are specific and consistent
- Consequences of violations clearly stated
- Escalation paths defined

**Good:**
- Most rules are checkable
- Some automation in place
- Review criteria generally clear

**Needs Improvement:**
- Rules depend on subjective interpretation
- No enforcement mechanism for stated rules
- Inconsistent application likely
- No consequences or accountability

### 4. Inclusivity

**Definition:** Policy welcomes diverse contributors and doesn't create unnecessary barriers.

**Excellent:**
- Clear path for new contributors to get started
- Multiple contribution types recognized (code, docs, issues, reviews)
- No gatekeeping beyond necessary quality requirements
- Accommodates different skill levels
- Time zone and language considerations addressed

**Good:**
- Basic path for new contributors
- Primary contribution types covered
- Reasonable requirements

**Needs Improvement:**
- High barrier to entry with no justification
- Only values code contributions
- Insider knowledge required
- Exclusive or unwelcoming tone

### 5. Maintainability

**Definition:** Policy can evolve with the project without requiring complete rewrites.

**Excellent:**
- Versioned with clear changelog
- Modular sections allow independent updates
- Amendment process defined
- Periodic review schedule stated
- Historical context preserved

**Good:**
- Version tracked
- Structure allows some flexibility
- Can be updated incrementally

**Needs Improvement:**
- No version tracking
- Monolithic policy hard to update
- Changes require full rewrite
- No review process

## Section-by-Section Guidance

### Purpose Statement

**Purpose:** Establish why this repository exists and why the policy matters.

**Tips:**
- Lead with the repository's value proposition
- Explain who benefits from this repository
- Connect policy to project success
- Keep to 2-4 sentences

**Anti-patterns:**
- Legalistic opening that intimidates contributors
- Vague mission statements with no specifics
- Assuming reader knows the project

### Repository Identity

**Purpose:** Define scope, ownership, and relationships.

**Tips:**
- Be specific about what's in scope and out of scope
- Name roles, not just individuals (roles survive personnel changes)
- Link to related repositories when part of a system
- State the stability expectations (experimental vs production)

**Anti-patterns:**
- "This repo contains stuff for the project"
- Naming individuals without roles
- Undefined relationship to other repos

### Policy Dependencies (upstream_policies / downstream_policies)

**Purpose:** Declare explicit policy alignment relationships with other repositories.

**Tips:**
- `upstream_policies`: List policies this policy must align with - constraints flow downstream
- `downstream_policies`: List policies that depend on this one - changes here may break them
- Use policy identifiers (e.g., `v:repository-policy:parent-repo`) for internal policies
- For external policies, use clear references (URLs or document names)
- Even if no dependencies exist, institutional repos should declare empty arrays `[]` to show explicit consideration
- Review upstream policies before making breaking changes to your own
- Notify downstream consumers when making changes that may affect them

**Anti-patterns:**
- Omitting fields for institutional repos (REQUIRED, even if empty)
- Listing repositories instead of their policies
- One-way declaration (if A lists B as downstream, B should list A as upstream)
- Forgetting to update when relationships change

**Symmetry Principle:**
When policy A declares policy B as `downstream`, policy B should declare policy A as `upstream`. This symmetry enables:
- Bidirectional impact analysis
- Change notification in both directions
- Audit trail of intentional alignment

### Contribution Rules

**Purpose:** Define the core governance - who can contribute what, and how.

**Tips:**
- Start with "Who Can Contribute" - open with welcome, then any restrictions
- List all recognized contribution types explicitly
- Be prescriptive about submission process (branch naming, commit format)
- Specify review requirements clearly (number, who, criteria)

**Anti-patterns:**
- Assuming everyone knows "the normal PR process"
- Inconsistent rules for different contribution types
- Review requirements that create bottlenecks
- Missing guidance on draft/WIP contributions

**Context-Specific Advice:**

| Repository Type | Contribution Guidance                                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Open Source     | Emphasize CLA/DCO (see [[#Open Source Repositories]]), first-timer friendliness, clear license                         |
| Internal        | Focus on team boundaries, access controls, compliance                                                                  |
| Private         | Minimal process; owner discretion; document when transitioning to collaborative                                        |
| Hybrid          | Separate rules for core team vs external contributors; clear escalation paths                                          |
| Institutional   | Identify clear upstream dependencies and downstream intended uses, and align polices where possible                    |
| Educational     | Expert review for accuracy; edition-based acceptance; errata process for corrections                                   |
| Documentation   | Emphasize this framework; support non-coders                                                                           |
| Research        | Balance reproducibility with iteration speed                                                                           |
| Operations      | Emphasize change control, rollback procedures                                                                          |

### Quality Standards (Recommended)

**Purpose:** Define what "good enough" means for contributions.

**Tips:**
- Start with the most important standards (the ones that cause rejections)
- Link to external style guides rather than duplicating them
- Specify minimum test coverage if applicable
- Address security requirements explicitly

**Anti-patterns:**
- "Code must be high quality" without specifics
- Standards that can't be checked automatically
- Missing security considerations

### Governance (Recommended)

**Purpose:** Define decision-making and conflict resolution.

**Tips:**
- Choose a simple decision model and state it explicitly
- Define escalation paths before you need them
- Assign clear responsibilities to roles
- Address what happens when maintainers disagree

**Anti-patterns:**
- Undefined decision authority ("we'll figure it out")
- No escalation path
- All power to one person with no backup

### Lifecycle (Recommended)

**Purpose:** Define how the repository evolves over time.

**Tips:**
- Choose a branching strategy and commit to it
- Define versioning scheme if releasing artifacts
- State deprecation policy for breaking changes
- Include archival criteria for transparency

**Anti-patterns:**
- Multiple conflicting branching strategies
- No versioning for releasable artifacts
- Surprise deprecations

### Communication (Recommended)

**Purpose:** Define how contributors interact and stay informed.

**Tips:**
- List all official communication channels
- Set realistic response expectations
- Define how major changes are announced
- Consider asynchronous and global contributors

**Anti-patterns:**
- Assuming everyone is on Slack
- Unrealistic response time expectations
- Major changes announced only in meetings

### Implementation (Recommended)

**Purpose:** Bridge the gap from policy definition (why, what, how) to physical enforcement (where). Document platform-specific mechanisms that realize the policy.

**Tips:**

- Structure around four key areas: Access Control, Branch Protection, Automation, Compliance Tooling
- Trace each implementation detail to the policy rule it enforces
- Be specific about platform features (GitHub Actions, GitLab CI, branch protection rules)
- Include actual configuration values, not just descriptions
- Reference external configuration files where appropriate (`.github/CODEOWNERS`, `branch-protection.json`)
- Use tables for role/permission mappings - they're easier to audit

**Anti-patterns:**

- Describing policy rules again instead of implementation mechanisms
- Vague implementation ("we use CI") without specific workflows or checks
- Platform-agnostic language in implementation section (that belongs in policy rules)
- Implementation details that don't trace to any policy rule
- Outdated implementation that doesn't match actual platform configuration

**Access Control Guidance:**

| Access Model             | When to Use                                    | Platform Examples                  |
|--------------------------|------------------------------------------------|------------------------------------|
| RBAC (Role-Based)        | Clear role hierarchy, team-based permissions   | GitHub Teams, GitLab Groups        |
| ABAC (Attribute-Based)   | Complex permission logic, conditional access   | Custom middleware, policy engines  |
| ACL (Access Control List)| Simple, per-resource permissions               | Repository collaborators           |

**Branch Protection Guidance:**

| Policy Rule                 | Implementation Mechanism                         |
|-----------------------------|--------------------------------------------------|
| "Requires review"           | `required_approvals: N`                          |
| "Maintainer approval for X" | CODEOWNERS file + `require_code_owners: true`    |
| "All checks must pass"      | `require_status_checks: [check-names]`           |
| "Signed commits required"   | `require_signed_commits: true`                   |
| "No force push"             | `allow_force_push: false`                        |

**Automation Guidance:**

| Enforcement Type       | Implementation Approach                        |
|------------------------|------------------------------------------------|
| Style enforcement      | Linter in CI (eslint, ruff, markdownlint)      |
| Test requirements      | Test suite in required status check            |
| Commit message format  | Commit-lint or custom validation               |
| Security scanning      | Dependabot, CodeQL, secret scanning            |
| Documentation checks   | Doc linters, link checkers                     |

**Context-Specific Implementation:**

| Repository Type | Implementation Priorities                                              |
|-----------------|------------------------------------------------------------------------|
| Open Source     | CLA bot, first-timer detection, community metrics                      |
| Internal        | SSO integration, team sync, compliance logging                         |
| Institutional   | Audit logging, signed commits, retention policies, evidence collection |
| Educational     | Edition tagging, errata tracking, citation validation                  |

## Workflow Guidance

### Recommended Authoring Sequence

1. **Understand Context** (30 min)
   - What type of repository is this?
   - Who are the contributors?
   - What problems has the lack of policy caused?

2. **Draft Purpose and Identity** (15 min)
   - Why does this repository exist?
   - Who owns it?

3. **Define Contribution Rules** (45-60 min)
   - Who contributes?
   - How do they contribute?
   - What's the review process?

4. **Add Recommended Sections** (30-45 min)
   - Quality standards
   - Governance
   - Lifecycle
   - Communication

5. **Document Implementation** (30-45 min)
   - Map policy rules to platform enforcement mechanisms
   - Configure access control (roles, teams, permissions)
   - Define branch protection rules
   - Set up automation (CI/CD, bots, webhooks)
   - Enable compliance tooling (signing, scanning, logging)

6. **Review for Quality Criteria** (30 min)
   - Check against all 5 criteria
   - Get feedback from diverse contributors

7. **Test with New Contributor** (variable)
   - Have someone unfamiliar follow the policy
   - Note where they get stuck

### Quality Checkpoints

- **After step 2:** Can a stranger understand what this repo is for?
- **After step 3:** Could a new contributor make their first PR using only this document?
- **After step 4:** Are there any "what if" scenarios without answers?
- **After step 5:** Does every policy rule have a corresponding enforcement mechanism?
- **After step 6:** Would you feel confident pointing to this in a disagreement?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Too Long** | Policy is overwhelming and nobody reads it | Split into summary + detailed sections; lead with essentials |
| **Too Short** | Policy leaves too much undefined | Add recommended sections; address common questions explicitly |
| **Wrong Audience** | Written for experts, confuses newcomers | Add "Getting Started" section; define terms |
| **Outdated** | Policy doesn't match actual practice | Regular reviews; version tracking; amendment process |
| **Copied Template** | Generic policy doesn't fit context | Customize every section; remove irrelevant parts |
| **No Enforcement** | Rules exist but aren't applied | Add automation; define review checklists; state consequences |
| **Exclusive Tone** | Discourages contribution | Use welcoming language; recognize all contribution types |
| **Platform Lock-in** | Policy only works on GitHub | Abstract platform concepts; add platform-specific appendix |

## Best Practices

1. **Lead with Welcome** - Start with what contributors CAN do, not restrictions
2. **Be Specific** - "Submit a PR" is vague; "Create a branch named `fix/issue-123`" is actionable
3. **Automate Where Possible** - Use CI to enforce style, tests, commit format
4. **Version Your Policy** - Track changes so contributors know what's current
5. **Review Regularly** - Set a calendar reminder for quarterly policy review
6. **Test with Newcomers** - Have someone new try to contribute using only the docs
7. **Recognize All Contributions** - Docs, issues, reviews are contributions too
8. **Define Escalation** - Know how to resolve conflicts before they happen
9. **Keep It Current** - Outdated policy is worse than no policy
10. **Link Don't Duplicate** - Reference external style guides; keep policy focused on governance

## Validation vs. Verification

**Verification** (deterministic):
- Does the document have required frontmatter fields?
- Are required sections present?
- Do enum fields have valid values?
- Does type match `vertex/repository-policy`?

**Validation** (qualitative):
- Is the policy clear and unambiguous?
- Does it effectively govern the repository?
- Is it appropriate for the repository type?
- Does it follow best practices?

This guidance document supports **validation** - assessing fitness-for-purpose.

## Repository Type Selection

Choosing the correct `repository_type` is fundamental to writing an appropriate policy. Each type implies different governance priorities, accountability structures, and contribution patterns.

### Open Source

**Description:** Publicly accessible repositories where contributions are welcomed from the broader community. Governance emphasizes transparency, community building, and lowering barriers to participation while maintaining quality.

**When to use:**
- Project is publicly available and accepts external contributions
- Goal is community growth and broad adoption
- Transparency in decision-making is a core value
- License permits redistribution and modification

**When NOT to use:**
- Repository contains proprietary or confidential information
- Contributions are restricted to a defined group
- External visibility would create security or competitive risks
- Compliance requirements prohibit public disclosure

### Internal

**Description:** Repositories accessible only within an organization, governed by internal standards and team agreements. Focus is on productivity, consistency across teams, and alignment with organizational practices.

**When to use:**
- Repository serves internal teams only
- Content is proprietary but has no external accountability requirements
- Governance follows organizational hierarchy
- Access is managed through corporate identity systems

**When NOT to use:**
- External parties need access (use `hybrid` or `institutional`)
- Regulatory bodies may audit the repository (use `institutional`)
- Goal is community contribution (use `open-source`)
- Repository is personal/experimental with no team governance (use `private`)

### Private

**Description:** Restricted-access repositories with minimal formal governance, typically for personal projects, experiments, or early-stage work. Governance is lightweight or informal.

**When to use:**
- Personal projects or experiments
- Early-stage work before formal governance is needed
- Scratch space or proof-of-concept repositories
- Single-owner repositories with no collaboration expectations

**When NOT to use:**
- Multiple contributors need coordination (use `internal` or `open-source`)
- Work product may face external scrutiny (use `institutional`)
- Repository will eventually need formal governance (start with appropriate type)
- Content has compliance or regulatory implications (use `institutional`)

### Hybrid

**Description:** Repositories that combine characteristics of multiple types - typically a core team with internal governance plus external contributors or consumers. Common for open-core models or consortium projects.

**When to use:**
- Open source project with commercial backing and internal roadmap
- Consortium or multi-organization collaboration
- Public documentation for internal tooling
- Community contributions welcomed but core decisions are internal

**When NOT to use:**
- Clear single governance model applies (use that specific type)
- Hybrid complexity isn't justified by actual usage patterns
- External accountability requirements exist (use `institutional`)
- Trying to avoid choosing - hybrid should be intentional, not a default

### Institutional

**Description:** Repositories where documents must satisfy external accountability requirements - regulatory bodies, auditors, standards organizations, or public oversight. Like `internal` in access control, but with traceability, auditability, and accountability requirements that satisfy external scrutiny.

**When to use:**
- Regulated industry (healthcare, finance, aerospace, energy)
- Public sector or government repositories
- Professional engineering or other licensed professions
- Any context requiring proof of compliance to external parties
- Upstream/downstream dependencies with other institutional repositories
- Work products that may be legally discoverable

**When NOT to use:**
- No external accountability requirements exist (use `internal`)
- Overhead of audit trails isn't justified by actual requirements
- Repository is experimental or not yet subject to compliance (use `private` or `internal`)
- Public community contribution is the goal (use `open-source`, possibly with institutional fork)

### Educational

**Description:** Repositories containing expert-curated didactic content designed to teach - comparable to textbooks or knowledge bases. A small group of authoritative maintainers produces content for broad consumption. Governance emphasizes academic rigor, citation standards, pedagogical structure, and deliberate edition-based evolution rather than continuous delivery.

**When to use:**
- Content is designed to teach, not just document
- Small expert maintainer group with pedagogical authority
- Broad consumption expected (students, self-learners, reference users)
- Academic norms apply: citation, accuracy, structured progression
- Knowledge complexes, textbooks, curricula, learning resources
- Edition-like lifecycle with deliberate major revisions

**When NOT to use:**
- Content documents a system rather than teaches concepts (use `documentation`)
- Active research with evolving conclusions (use `research`)
- Community-driven content curation (use `open-source`)
- Regulatory accountability required (use `institutional`, possibly with educational content)
- Content is operational procedures, not learning material (use `internal` or `operations`)

---

## Context-Specific Considerations

### Open Source Repositories

- **License clarity is critical** - State license prominently, explain contribution licensing
- **CLA/DCO decision** - Choose one, explain it, make signing easy
  - **CLA (Contributor License Agreement):** A legal agreement where contributors grant specific rights to the project, often including copyright assignment or broad licensing rights. Common in corporate-backed projects.
  - **DCO (Developer Certificate of Origin):** A lightweight attestation (via `Signed-off-by` line) that contributors have the right to submit the code under the project's license. Simpler than CLA, common in Linux kernel and many open source projects.
- **First-timer friendliness** - Tag good first issues, provide mentorship path
- **Community standards** - Link to CODE_OF_CONDUCT if separate

### Internal/Corporate Repositories

- **Access control** - Define who can access, contribute, approve
- **Compliance requirements** - Security reviews, legal approval for certain changes
- **Integration with internal tools** - How does this fit your CI/CD, issue tracking?
- **Team boundaries** - Who owns what parts?

### Documentation Repositories

- **Writing standards** - Style guide, terminology, formatting
- **Review criteria** - Accuracy, clarity, completeness
- **Update triggers** - What events require doc updates?
- **Translation considerations** - If applicable

### Research Repositories

- **Reproducibility** - Environment specs, data access, random seeds
- **Citation requirements** - How to cite, DOI if applicable
- **Collaboration models** - How experiments are shared
- **Publication coordination** - What can be shared when?

### Institutional Repositories

- **Traceability requirements** - Every change must be attributable; commit signing may be required
- **Audit trail preservation** - History must be immutable; force-push restrictions essential
- **External accountability** - Document who can be called to testify or explain decisions
- **Upstream/downstream alignment** - Identify dependencies on other institutional repos and align policies
- **Retention policies** - How long must records be kept? What triggers archival vs deletion?
- **Access logging** - Who accessed what and when may need to be recorded
- **Change control rigor** - Reviews may require specific roles or qualifications
- **Evidence of compliance** - How do you prove the policy was followed?

### Educational Repositories

- **Pedagogical authority** - Define who has authority to approve content (subject matter experts, curriculum designers)
- **Citation standards** - Require proper attribution; define citation format for the domain
- **Accuracy requirements** - Establish review process for factual correctness; define correction procedures
- **Versioning as editions** - Major revisions are deliberate events; communicate edition changes clearly to users
- **Structural progression** - Content should follow logical learning paths; prerequisites should be explicit
- **Errata process** - How are errors reported, tracked, and corrected between editions?
- **Accessibility** - Content should be accessible to target learners; consider reading level, prerequisites, formats
- **Feedback channels** - How do learners report confusion or suggest improvements? (distinct from contribution)

---

**Note:** This guidance is coupled with spec-for-repository-policy via a coupling edge. Together they enable both verification (structural compliance) and validation (quality assessment) of repository policy documents.
