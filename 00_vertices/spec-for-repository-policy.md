---
type: vertex/spec
extends: doc
id: v:spec:repository-policy
name: Specification for Repository Policy Documents
description: Defines structural requirements for repository policy documents that govern contribution patterns and collaboration rules for git repositories
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2026-01-02T12:00:00Z
modified: 2026-01-02T12:00:00Z
dependencies: []
---

# Specification for Repository Policy Documents

**This specification defines the structure and requirements for repository policy documents that govern contribution patterns, collaboration rules, and operational standards for git repositories.**

## Purpose

Repository policy documents define **governance rules and contribution patterns** for git-based collaborative environments. This spec establishes what fields and sections must be present in any valid repository-policy document, supporting open source projects, internal company repositories, institutional repositories with external accountability requirements, educational repositories with expert-curated didactic content, documentation-focused, code-focused, research, and operational process repositories.

## Required Frontmatter Fields

All repository-policy documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/repository-policy` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:repository-policy:<name>`) |
| `name` | string | REQUIRED | Human-readable policy name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, repository-policy]` in full inheritance chain |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Repository Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `repository_type` | enum | REQUIRED | One of: `open-source`, `internal`, `private`, `hybrid`, `institutional`, `educational` |
| `primary_content` | enum | REQUIRED | One of: `code`, `documentation`, `mixed`, `data`, `configuration` |
| `domain` | string | RECOMMENDED | Primary domain (e.g., `software`, `research`, `operations`, `education`) |

### Policy Dependencies

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `upstream_policies` | array[string] | REQUIRED if `institutional`, else OPTIONAL | Repository policies this policy must align with (parent policies) |
| `downstream_policies` | array[string] | REQUIRED if `institutional`, else OPTIONAL | Repository policies that depend on this policy (child policies) |

**Semantics:**
- `upstream_policies`: Policies that constrain this one. Changes to upstream policies may require updates here.
- `downstream_policies`: Policies that depend on this one. Changes here may require updates downstream.
- Values are policy identifiers (e.g., `v:repository-policy:parent-repo-name`) or references to external policy documents.
- For `institutional` repositories, these fields MUST be present (may be empty arrays if no dependencies exist).
- For other repository types, these fields are OPTIONAL but RECOMMENDED when dependencies exist.

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of what this repository contains |
| `license` | string | OPTIONAL | SPDX license identifier (e.g., `MIT`, `Apache-2.0`, `proprietary`) |
| `maintainers` | array[string] | OPTIONAL | List of maintainer identifiers or roles |
| `platform` | object | OPTIONAL | Platform-specific configuration (see Platform Configuration) |

### Platform Configuration (Optional)

When `platform` is present, it MAY contain:

```yaml
platform:
  type: github | gitlab | bitbucket | azure-devops | self-hosted
  settings:
    default_branch: <string>
    protected_branches: [<string>]
    required_reviews: <integer>
    ci_required: <boolean>
```

### Implementation Configuration (Optional)

The `implementation` field bridges policy definition to platform-specific enforcement mechanisms. When present, it documents how policy rules are physically enforced.

| Field            | Type   | Requirement | Description                                 |
|------------------|--------|-------------|---------------------------------------------|
| `implementation` | object | OPTIONAL    | Platform-specific enforcement configuration |

When `implementation` is present, it MAY contain:

```yaml
implementation:
  # Access Control
  access_control:
    model: rbac | abac | acl | custom
    roles:
      - name: <string>
        permissions: [read, write, admin, maintain, triage]
        scope: repository | organization | team
    teams:
      - name: <string>
        role: <role-name>

  # Branch Protection
  branch_protection:
    - branch: <pattern>
      rules:
        require_pull_request: <boolean>
        required_approvals: <integer>
        require_code_owners: <boolean>
        require_signed_commits: <boolean>
        require_linear_history: <boolean>
        require_status_checks: [<check-name>]
        restrict_pushes_to: [<role-or-team>]
        allow_force_push: <boolean>
        allow_deletions: <boolean>

  # Automation
  automation:
    ci_cd:
      platform: github-actions | gitlab-ci | jenkins | circleci | azure-pipelines
      required_workflows: [<workflow-name>]
      required_checks: [<check-name>]
    bots:
      - name: <string>
        purpose: <string>
        permissions: [<permission>]
    webhooks:
      - event: <event-type>
        target: <url-or-service>

  # Compliance Tooling
  compliance:
    signing:
      commits: required | recommended | none
      method: gpg | ssh | sigstore
    audit_logging:
      enabled: <boolean>
      retention_days: <integer>
    secret_scanning: <boolean>
    dependency_scanning: <boolean>
    code_scanning: <boolean>
```

**Semantics:**

- `access_control`: Documents role-based or attribute-based access control implementation
- `branch_protection`: Maps policy review requirements to platform branch protection rules
- `automation`: Documents CI/CD pipelines, bots, and webhooks that enforce policy
- `compliance`: Documents security and audit tooling that supports policy compliance

**Relationship to Policy:**

- Implementation details SHOULD directly trace to policy rules in Contribution Rules and Quality Standards
- Policy rules are platform-neutral (the "what"); implementation details are platform-specific (the "how")
- A policy MAY be valid without implementation details; implementation details document enforcement, not define policy

## Required Body Sections

The markdown body of a repository-policy document MUST contain:

### 1. Purpose Statement

A clear statement of what this repository is for and why this policy exists.

**Format:**
```markdown
## Purpose

[2-4 sentences explaining:
- What the repository contains
- Who it serves
- Why this policy exists]
```

### 2. Repository Identity

Core information about the repository and its ownership.

**Format:**
```markdown
## Repository Identity

### Scope

[What this repository contains and its boundaries]

### Ownership

[Who owns/maintains this repository - team, individual, organization]

### Related Repositories

[Optional: Links to related repositories if part of a larger system]
```

**Requirements:**
- MUST include Scope subsection
- MUST include Ownership subsection
- Related Repositories is OPTIONAL

### 3. Contribution Rules

The core governance section defining how contributions are made.

**Format:**
```markdown
## Contribution Rules

### Who Can Contribute

[Define contribution eligibility:
- Open to all / Team members only / Approved contributors
- Any role-based restrictions]

### Contribution Types

[Define what types of contributions are accepted:
- Code changes
- Documentation
- Bug reports / Issues
- Feature requests
- Reviews]

### Submission Process

[Define how contributions are submitted:
- Branch naming conventions
- Commit message format
- Pull/Merge request process
- Required information in submissions]

### Review Requirements

[Define review process:
- Number of approvals required
- Who can approve
- Review criteria]
```

**Requirements:**
- MUST include Who Can Contribute subsection
- MUST include Contribution Types subsection
- MUST include Submission Process subsection
- MUST include Review Requirements subsection

## Recommended Body Sections

The following sections are RECOMMENDED but not required:

### 4. Quality Standards

Standards that contributions must meet.

**Format:**
```markdown
## Quality Standards

### Code Standards

[If applicable: Style guides, linting rules, formatting requirements]

### Documentation Standards

[Documentation requirements for contributions]

### Testing Requirements

[Required tests, coverage thresholds, test types]

### Security Requirements

[Security considerations, vulnerability handling, secret management]
```

### 5. Governance

Decision-making and conflict resolution processes.

**Format:**
```markdown
## Governance

### Decision Making

[How decisions are made:
- Consensus / Maintainer authority / Voting
- Escalation paths]

### Roles and Responsibilities

[Define roles:
- Maintainer responsibilities
- Contributor expectations
- Reviewer duties]

### Conflict Resolution

[How disputes are handled]
```

### 6. Lifecycle

Repository and contribution lifecycle management.

**Format:**
```markdown
## Lifecycle

### Branching Strategy

[Branch naming, purpose of different branches, merge strategies]

### Release Process

[How releases are created, versioning scheme, changelog requirements]

### Deprecation Policy

[How features/APIs are deprecated, timeline expectations]

### Archival Criteria

[When and how repository may be archived]
```

### 7. Communication

Communication channels and expectations.

**Format:**
```markdown
## Communication

### Discussion Channels

[Where discussions happen: Issues, Discussions, Slack, etc.]

### Response Expectations

[Expected response times, SLAs if any]

### Announcements

[How major changes are communicated]
```

### 8. Implementation

Platform-specific enforcement mechanisms that realize the policy. This section bridges the conceptual policy to physical enforcement.

**Format:**
```markdown
## Implementation

### Access Control

[How roles and permissions are configured:
- Role definitions and permission mappings
- Team structure and membership
- Access model (RBAC, ABAC, ACL)]

### Branch Protection

[How branch protection rules enforce policy:
- Protected branches and their rules
- Required checks and approvals
- Push/merge restrictions]

### Automation

[CI/CD and tooling that enforces policy:
- Required workflows and checks
- Automated bots and their purposes
- Webhook integrations]

### Compliance Tooling

[Security and audit tooling:
- Commit signing requirements
- Audit logging configuration
- Security scanning (secrets, dependencies, code)]
```

**Requirements:**

- This section is RECOMMENDED, not required
- When present, subsections SHOULD trace to specific policy rules
- Platform-specific details belong here, not in policy rule definitions
- Implementation MAY reference external configuration files (e.g., `.github/CODEOWNERS`, `branch-protection.json`)

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/repository-policy`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:repository-policy:[kebab-case-name]`
4. **Tag Inheritance:** Tags MUST include full chain: `[vertex, doc, repository-policy]`

## Content Requirements

1. **Prescriptive Language:** Policy documents use clear, actionable language (MUST, SHALL, SHOULD, MAY)
2. **Completeness:** Required sections must fully address their topics
3. **Self-Contained:** All policy content should be in this document (not just references)
4. **Neutrality:** Rules should be platform-agnostic in description even if platform field specifies implementation

## Coupling Requirement

Every repository-policy spec SHOULD be paired with a corresponding guidance document via a `coupling` edge. The guidance defines how to evaluate quality and fitness-for-purpose for repository-policy documents.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that structural requirements are met
- **Validation** (against guidance-for-repository-policy): Qualitative assessment of policy clarity, completeness, and appropriateness

## Schema Summary

```yaml
# Required frontmatter
type: vertex/repository-policy
extends: doc
id: v:repository-policy:<name>
name: <string>
tags: [vertex, doc, repository-policy]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
repository_type: open-source | internal | private | hybrid | institutional | educational
primary_content: code | documentation | mixed | data | configuration

# Policy dependencies (REQUIRED if institutional, else OPTIONAL)
upstream_policies: [<policy-id>]
downstream_policies: [<policy-id>]

# Recommended frontmatter
domain: <string>
description: <string>

# Optional frontmatter
license: <SPDX-identifier>
maintainers: [<string>]
platform:
  type: github | gitlab | bitbucket | azure-devops | self-hosted
  settings: {...}

# Required body sections (markdown)
## Purpose
## Repository Identity
  ### Scope
  ### Ownership
  ### Related Repositories (optional)
## Contribution Rules
  ### Who Can Contribute
  ### Contribution Types
  ### Submission Process
  ### Review Requirements

# Recommended body sections
## Quality Standards
## Governance
## Lifecycle
## Communication
## Implementation
  ### Access Control
  ### Branch Protection
  ### Automation
  ### Compliance Tooling
```

## Example Instance

The following is a complete, valid repository-policy document for an institutional repository:

```yaml
---
type: vertex/repository-policy
extends: doc
id: v:repository-policy:assurances-audits-accountability
name: Repository Policy for Assurances, Audits, and Accountability
tags:
  - vertex
  - doc
  - repository-policy
version: 1.0.0
created: 2026-01-02T12:00:00Z
modified: 2026-01-02T12:00:00Z
repository_type: institutional
primary_content: documentation
domain: systems-engineering
description: Knowledge complex for assurance methodology research and practice
upstream_policies:
  - v:repository-policy:blockscience-engineering-standards
downstream_policies:
  - v:repository-policy:client-project-alpha
license: CC-BY-4.0
maintainers:
  - chief-engineer
  - technical-lead
---

# Repository Policy for Assurances, Audits, and Accountability

## Purpose

This repository contains the knowledge complex for assurance methodology,
including specifications, guidance documents, and verification tools. It
serves as both a research artifact and an operational resource for systems
engineering practice. This policy exists to ensure traceability, maintain
academic rigor, and satisfy external accountability requirements.

## Repository Identity

### Scope

This repository contains:
- Typed document specifications (specs and guidances)
- Verification and validation tooling
- Chart structures for assurance networks
- Supporting scripts and tests

Out of scope: Client-specific implementations, proprietary data.

### Ownership

Maintained by the Systems Engineering team at BlockScience.
Chief Engineer has final authority on architectural decisions.

### Related Repositories

- blockscience-engineering-standards (upstream)
- client-project-alpha (downstream consumer)

## Contribution Rules

### Who Can Contribute

- Core team members: Full contribution rights
- External collaborators: By invitation, subject to review

### Contribution Types

- Specification documents
- Guidance documents
- Verification scripts
- Documentation improvements
- Bug fixes

### Submission Process

1. Create branch from `main` with naming: `<type>/<description>`
2. Commits must be signed (required for institutional traceability)
3. Submit PR with description of changes and rationale
4. Reference related issues or upstream requirements

### Review Requirements

- Minimum 1 approval from maintainer
- All CI checks must pass
- Spec changes require Chief Engineer review

## Implementation

### Access Control

Role-based access control via GitHub Teams:

| Role | Team | Permissions |
|------|------|-------------|
| Chief Engineer | @blockscience/chief-engineers | Admin |
| Maintainer | @blockscience/aaa-maintainers | Maintain |
| Contributor | @blockscience/aaa-contributors | Write |
| Reader | Public | Read |

### Branch Protection

**`main` branch:**
- Require pull request before merging
- Required approvals: 1 (2 for spec changes)
- Require signed commits
- Require status checks: `verify-templates`, `run-tests`
- Restrict who can push: @blockscience/aaa-maintainers
- Do not allow force pushes
- Do not allow deletions

### Automation

**GitHub Actions Workflows:**
- `verify-templates.yml`: Runs on all PRs, verifies document structure
- `run-tests.yml`: Runs pytest suite on all PRs
- `build-cache.yml`: Rebuilds element cache on merge to main

**CODEOWNERS:**
- `00_vertices/spec-*.md` → @blockscience/chief-engineers
- `scripts/` → @blockscience/aaa-maintainers
- `*` → @blockscience/aaa-contributors

### Compliance Tooling

- **Commit signing:** Required (GPG or SSH)
- **Audit logging:** Enabled, 365-day retention
- **Secret scanning:** Enabled
- **Dependency scanning:** Enabled via Dependabot
```

## Compliance

A document claiming `type: vertex/repository-policy` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present with their required subsections
3. `repository_type` is one of the allowed enum values
4. `primary_content` is one of the allowed enum values
5. If `repository_type` is `institutional`, both `upstream_policies` and `downstream_policies` MUST be present
6. Type constraints are satisfied
7. Content uses prescriptive language appropriate for policy documents

---

**Note:** This specification extends [[spec-for-spec]] and supports governance of diverse repository types while remaining concise. The flexible structure (required core + recommended extensions) allows adaptation to open source, internal, institutional, educational, documentation, code, research, and operational contexts.
