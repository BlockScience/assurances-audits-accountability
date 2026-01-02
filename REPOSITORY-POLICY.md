---
type: vertex/repository-policy
extends: doc
id: v:repository-policy:assurances-audits-accountability
name: Repository Policy for Assurances, Audits, and Accountability
description: Governance policy for the knowledge complex repository containing typed document specifications, verification tooling, and assurance methodology
tags:
  - vertex
  - doc
  - repository-policy
version: 1.0.0
created: 2026-01-02T19:00:00Z
modified: 2026-01-02T19:00:00Z
repository_type: hybrid
primary_content: documentation
domain: systems-engineering
upstream_policies: []
downstream_policies: []
maintainers:
  - mzargham
  - davidfsol5
  - danlessa
---

# Repository Policy for Assurances, Audits, and Accountability

## Purpose

This repository contains the knowledge complex for assurance methodology research and practice, including typed document specifications, guidance documents, verification tooling, and chart structures. It serves as both a research artifact for systems engineering methodology and a practical resource for implementing assurance processes.

This policy exists to govern contribution patterns as the repository evolves from internal development toward a package-manager-like consumption model where users can extend document types through inheritance or compose compound types with typed sections.

**License Status:** All rights reserved. Appropriate licensing is under research and will be determined in a future policy revision.

## Repository Identity

### Scope

This repository contains:

- **Typed Document Specifications** (`00_vertices/spec-*.md`): Structural requirements for document types
- **Guidance Documents** (`00_vertices/guidance-*.md`): Quality criteria and best practices
- **Edge Documents** (`01_edges/`): Relationships between vertices (coupling, verification, validation, dependency)
- **Face Documents** (`02_faces/`): Assurance attestations bounding edge triangles
- **Chart Documents** (`charts/`): Simplicial complex structures organizing vertices, edges, and faces
- **Verification Scripts** (`scripts/`): Tooling for template-based verification and validation
- **Test Suite** (`tests/`): Automated tests for verification infrastructure

**Out of Scope:**

- Client-specific implementations
- Proprietary data or configurations
- Production deployment artifacts

### Ownership

This repository is maintained by BlockScience. The maintainer team has authority over architectural decisions, merge approvals, and policy evolution.

**Maintainers:**

- mzargham
- davidfsol5
- danlessa

### Related Repositories

None currently. Future upstream and downstream policy relationships will be documented as they are established.

## Contribution Rules

### Who Can Contribute

| Role             | Members                        | Access Level                                       |
| ---------------- | ------------------------------ | -------------------------------------------------- |
| Maintainers      | mzargham, davidfsol5, danlessa | Admin: merge to main, approve PRs, manage settings |
| Core Team        | BlockScience team members      | Write: create branches, push commits, open PRs     |
| Trusted External | ipatka (by invitation)         | Write: same as core team, granted individually     |
| Public           | Everyone else                  | Read: view repository, clone, fork                 |

**Adding Trusted External Contributors:**

External contributors may be added to the whitelist by maintainer consensus. This is reserved for a small group of trusted collaborators.

### Contribution Types

The following contribution types are accepted:

- Specification documents (`spec-*.md`)
- Guidance documents (`guidance-*.md`)
- Edge documents (coupling, verification, validation, dependency)
- Face documents (assurance attestations)
- Chart documents and structures
- Verification and validation scripts
- Test cases and test infrastructure
- Documentation improvements
- Bug fixes and corrections

### Submission Process

1. **Create a developer branch** from `main`:
   - Format: `<developer-name>/<work-description>`
   - Example: `mzargham/add-repository-policy-type`
   - Each developer works on a small set of closely related documents (ideally a single document)

2. **Commit requirements:**
   - All commits MUST be signed (GPG or SSH)
   - Commit messages should be clear and descriptive
   - Reference related issues when applicable

3. **Open a Pull Request:**
   - Provide a clear description of changes
   - Explain rationale for non-obvious decisions
   - Ensure all CI checks pass before requesting review

4. **File naming conventions:**
   - Use lowercase letters, numbers, and hyphens only
   - No spaces or special characters (OS-compatible)
   - Vertices: `<type>-for-<name>.md` or `<type>-<name>.md`
   - Edges: `<edge-type>-<name>.md` or `<edge-type>-<source>:<target>.md`
   - Faces: `<face-type>-<name>.md`

### Review Requirements

- **Approval:** 1 maintainer approval required for all changes
- **CI Checks:** All automated checks MUST pass
- **Merge Authority:** Only maintainers can merge pull requests to `main`

## Quality Standards

### Document Standards

All typed documents MUST:

- Pass template-based verification (`python scripts/verify_template_based.py <file> --templates templates`)
- Include valid YAML frontmatter with all required fields for the document type
- Follow the structural requirements defined in the applicable specification

### Verification Requirements

Before merging:

- Run `python scripts/build_cache.py` to validate all documents
- Run `python -m pytest tests/ --ignore=tests/archive` to execute the test suite
- Ensure no regressions in existing verification checks

### File Naming Requirements

All files MUST use names compatible with all major operating systems:

- Lowercase letters (`a-z`)
- Numbers (`0-9`)
- Hyphens (`-`) as word separators
- Colons (`:`) only for edge source:target notation
- No spaces, underscores in new files, or special characters
- Maximum path length: 260 characters (Windows compatibility)

## Governance

### Decision Making

- **Routine changes:** Any maintainer can approve and merge
- **Specification changes:** Maintainer approval required; significant changes should be discussed before implementation
- **Policy changes:** Maintainer consensus required
- **Architectural decisions:** Chief Engineer (mzargham) has final authority

### Roles and Responsibilities

**Maintainers:**

- Review and merge pull requests
- Maintain verification infrastructure
- Evolve specifications and guidance documents
- Manage contributor access
- Resolve conflicts and make judgment calls

**Contributors (Core Team and Trusted External):**

- Submit well-formed pull requests
- Respond to review feedback
- Ensure contributions pass verification
- Follow file naming and commit signing requirements

### Conflict Resolution

1. Discuss in PR comments or GitHub Issues
2. If unresolved, escalate to maintainer group
3. Chief Engineer makes final decision if maintainers cannot reach consensus

## Lifecycle

### Branching Strategy

**Trunk-based development with developer branches:**

- `main` is the trunk; always in a deployable state
- Developer branches: `<developer-name>/<work-description>`
- Branches should be short-lived (merge or close within reasonable time)
- No long-lived feature branches

### Versioning

- Document versions use semantic versioning (`major.minor.patch`)
- Document versions must be reflected in the YAML frontmatter
- Repository releases (when applicable) will use git tags
- Breaking changes to specifications require major version increment

### Deprecation Policy

- Deprecated document types will be marked in frontmatter (`status: deprecated`)
- Deprecation notices will include migration guidance
- Deprecated types will be supported for at least one major version cycle

### Archival Criteria

This repository will be archived if:

- Research objectives are completed and no ongoing maintenance is needed
- A successor repository supersedes this one
- Maintainer team is no longer able to support it

## Communication

### Discussion Channels

- **GitHub Issues:** Bug reports, feature requests, questions
- **Pull Request Comments:** Code review discussion
- **GitHub Discussions:** (if enabled) Broader design conversations

### Response Expectations

- PR reviews: Best effort within 1 week
- Issue triage: Best effort within 2 weeks
- No SLA guarantees; this is a research repository

### Announcements

Major changes (breaking spec changes, policy updates) will be communicated via:

- Commit messages and PR descriptions
- README updates when applicable
- Direct notification to active contributors for significant changes

## Implementation

### Access Control

Role-based access control via GitHub:

| Role | GitHub Permission | Capabilities |
|------|-------------------|--------------|
| Maintainer | Admin | Full repository access, manage settings, merge PRs |
| Core Team | Write | Push to branches, open PRs, cannot merge to main |
| Trusted External | Write | Same as Core Team, added individually |
| Public | Read | Clone, fork, view |

### Branch Protection

**`main` branch protection rules:**

- Require pull request before merging
- Required approvals: 1
- Require signed commits
- Require status checks to pass:
  - `verify-templates` (when implemented)
  - `run-tests` (when implemented)
- Restrict who can push: Maintainers only
- Do not allow force pushes
- Do not allow deletions

### Automation

**Current CI/CD:**

- Template verification via `verify_template_based.py`
- Test suite via `pytest`
- Cache building via `build_cache.py`

**Planned automation:**

- GitHub Actions workflows for PR verification
- Automated cache rebuild on merge to main

### Compliance Tooling

- **Commit signing:** Required (GPG or SSH)
- **Secret scanning:** Enabled (GitHub default)
- **Dependency scanning:** Via Dependabot (when applicable)

---

**Note:** This policy governs the assurances-audits-accountability repository. It will evolve as the repository matures toward a package-manager-like consumption model for typed document specifications.
