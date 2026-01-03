# Personalization Guide

This guide walks you through creating your own AI assistant configuration using this repository as a template. By the end, you'll have a custom system prompt deployed to `.claude/CLAUDE.md` that defines how Claude assists you in your specific workspace.

---

## Overview

This repository is designed to be used as a **template**. You create a new repository from it, then follow a structured workflow to build a custom AI assistant configuration using the **PPP (Persona-Purpose-Protocol) framework**.

The process:

1. Create a new repository from this template
2. Narrate your workspace intent
3. Create a Purpose document (with full verification & validation)
4. Create a Persona document (with full verification & validation)
5. Create a Protocol document (with full verification & validation)
6. Assemble into a System Prompt document (with full verification & validation)
7. Deploy to `.claude/CLAUDE.md`
8. Clean up template artifacts
9. Start working (or create custom document types)

---

## Step 1: Create a New Repository from Template

### On GitHub

1. Navigate to this repository
2. Click **"Use this template"** → **"Create a new repository"**
3. Name your repository (e.g., `my-project-assistant`, `research-workspace`)
4. Choose visibility (public/private)
5. Click **"Create repository"**
6. Clone your new repository locally

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### Verify Setup

Ensure the verification tools work:

```bash
python scripts/verify_template_based.py 00_vertices/spec-for-spec.md --templates templates
```

Expected output: `Result: ✓ PASS`

---

## Step 2: Narrate Your Workspace Intent

Before writing any documents, take time to articulate what you're building and why. This narrative becomes the foundation for your Purpose document.

### Questions to Answer

Write down answers to these questions (in a scratchpad, notes file, or conversation with Claude):

**What is this workspace for?**

- What kind of work will happen here?
- What artifacts will be created?
- Is this code, documentation, research, or something else?

**What help do you need?**

- What tasks do you want assistance with?
- What expertise should the assistant have?
- What decisions should the assistant make vs. defer to you?

**What does success look like?**

- How will you know the assistant is helping effectively?
- What quality standards matter to you?
- What would failure look like?

**What are the boundaries?**

- What should the assistant never do?
- What requires your explicit approval?
- What authority levels are appropriate?

**What tools are available?**

- What scripts, CLI tools, or commands exist in your workspace?
- What build, test, or deployment tools do you use?
- What automation should the assistant be able to run?

### Example Narrative

> "This workspace is for developing a web application. I need help with code reviews, writing tests, and maintaining documentation. The assistant should understand React and Node.js, follow our coding standards, and always run tests before claiming work is complete. It should never deploy to production without my approval, and should ask clarifying questions rather than assume requirements.
>
> Tools available: `npm test`, `npm run lint`, `npm run build`, and custom scripts in `scripts/` for database migrations and API testing."

Keep this narrative handy - you'll reference it throughout the process.

---

## Step 3: Create Your Purpose Document

**Purpose is designed FIRST.** It establishes what value the assistant delivers before defining personality or workflow.

### Create the Document

Create `00_vertices/purpose-<your-name>.md`:

```yaml
---
type: vertex/purpose
extends: doc
id: v:purpose:<your-name>
name: Purpose - <Your Assistant Name>
description: Defines what value this assistant delivers and how success is measured
tags:
  - vertex
  - doc
  - purpose
version: 1.0.0
created: <ISO-8601-timestamp>
modified: <ISO-8601-timestamp>
dependencies: []
---

# Purpose - <Your Assistant Name>

## Purpose

This purpose document defines [brief statement of what this assistant does].

## Problem Statement

[What problem does this assistant solve? What need does it address?
Reference your workspace narrative.]

## Core Objectives

You accomplish this by:

- [Objective 1]: [Description]
- [Objective 2]: [Description]
- [Objective 3]: [Description]

## Specific Deliverables

- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]

## Constraints and Boundaries

- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

## Success Criteria

Your work is successful when:

- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

---

**Note:** This purpose is the anchor of the PPP design - designed FIRST to establish what value is delivered.
```

### Verify Your Purpose (Structure)

```bash
python scripts/verify_template_based.py 00_vertices/purpose-<your-name>.md --templates templates
```

Fix any structural issues until verification passes.

### Validate Your Purpose (Quality)

Review against [guidance-for-purpose](00_vertices/guidance-for-purpose.md):

- [ ] Problem statement is clear and specific
- [ ] Objectives are actionable (not vague aspirations)
- [ ] Deliverables are concrete and measurable
- [ ] Constraints define real boundaries
- [ ] Success criteria are objectively assessable

### Create Verification & Validation Edges

Create verification edge `01_edges/verification-<your-name>-purpose:spec.md` and validation edge `01_edges/validation-<your-name>-purpose:guidance.md` following the patterns in existing edges.

### Create Assurance Face

Create `02_faces/assurance-<your-name>-purpose.md` attesting that your purpose document satisfies both verification (structure) and validation (quality).

---

## Step 4: Create Your Persona Document

**Persona is designed SECOND.** It matches expertise and identity to the purpose's objectives.

### Create the Document

Create `00_vertices/persona-<your-name>.md`:

```yaml
---
type: vertex/persona
extends: doc
id: v:persona:<your-name>
name: Persona - <Your Assistant Name>
description: Defines the identity and expertise of this assistant
tags:
  - vertex
  - doc
  - persona
version: 1.0.0
created: <ISO-8601-timestamp>
modified: <ISO-8601-timestamp>
dependencies: []
---

# Persona - <Your Assistant Name>

## Purpose

This persona defines the identity of [brief description].

## Role and Identity

[Who is this assistant? What role do they play? How do they relate to you?
This should support the Purpose objectives.]

## Domain Expertise

- **[Expertise Area 1]**: [Description]
- **[Expertise Area 2]**: [Description]
- **[Expertise Area 3]**: [Description]

## Approach and Methodology

[How does this assistant work? What principles guide their approach?
This should enable achieving the Purpose deliverables.]

## Communication Tone

[How does this assistant communicate? Formal? Casual? Technical?
This should be appropriate for the Purpose context.]

## Boundaries and Limitations

- [Boundary 1]
- [Boundary 2]
- [Boundary 3]

---

**Note:** This persona is designed to work within the PPP framework, supporting [purpose reference].
```

### Verify, Validate, and Assure

1. **Verify** against spec-for-persona
2. **Validate** against guidance-for-persona
3. Create verification edge, validation edge, and assurance face

Check alignment with Purpose:

- [ ] Expertise enables the core objectives
- [ ] Boundaries align with constraints
- [ ] Tone fits the work context

---

## Step 5: Create Your Protocol Document

**Protocol is designed LAST.** It integrates persona's expertise with purpose's objectives into an operational workflow. **This is where you provision your assistant's tool capabilities.**

### Understanding Tool Provisioning

In Claude Code, your assistant can execute local scripts, CLI tools, and commands. The Protocol's **Tools and Scripts** section is where you tell the assistant:

- **What** tools exist (name, path, command)
- **When** to use them (which phase, what triggers)
- **How** to use them (syntax, parameters, examples)
- **What success/failure looks like** (expected output, error patterns)

Without explicit tool documentation, the assistant cannot use your tools effectively.

### Create the Document

Create `00_vertices/protocol-<your-name>.md`:

```yaml
---
type: vertex/protocol
extends: doc
id: v:protocol:<your-name>
name: Protocol - <Your Assistant Name>
description: Defines the operational workflow and tool usage for this assistant
tags:
  - vertex
  - doc
  - protocol
version: 1.0.0
created: <ISO-8601-timestamp>
modified: <ISO-8601-timestamp>
dependencies: []
---

# Protocol - <Your Assistant Name>

## Purpose

This protocol defines the workflow for [achieving purpose objectives] through [persona's approach].

## Workflow Overview

[High-level description of how work flows through phases or steps.]

## Phase Definitions

### Phase 1: [Phase Name]

**When:** [Trigger condition]

**Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Outputs:** [What this phase produces]

**Next:** [What phase follows]

[Repeat for each phase...]

## User Collaboration Points

### Validation Points

- [When to confirm understanding]

### Input Gathering

- [When to ask questions]

### Approval Steps

- [What requires user approval]

## Quality Assurance

### Input Validation

- [How to validate inputs]

### Process Verification

- [How to verify work in progress]

### Output Quality Checks

- [How to check deliverables]

## Tools and Scripts

This section provisions the assistant's operational capabilities. List all tools the assistant is authorized to use.

### [Category] Tools

- **[Tool name]** (`command/path/syntax`)
  - **When:** [Which phase(s), what trigger or condition]
  - **What:** [Purpose and expected output]
  - **Success:** [What successful output looks like]
  - **Failure:** [What failure looks like, how to handle]
  - **Example:** `full command with parameters`

### Build Tools

- **npm test** (`npm test`)
  - **When:** Phase 3, after making code changes
  - **What:** Runs the test suite
  - **Success:** "All tests passed" with exit code 0
  - **Failure:** Test failures listed; fix before proceeding
  - **Example:** `npm test -- --coverage`

### Verification Tools

- **lint** (`npm run lint`)
  - **When:** Phase 3, before committing
  - **What:** Checks code style compliance
  - **Success:** No output, exit code 0
  - **Failure:** Style violations listed with file:line
  - **Example:** `npm run lint -- --fix`

[Add all tools relevant to your workspace...]

## Consistent Principles

Throughout all phases:

- **[Principle 1]**: [Description]
- **[Principle 2]**: [Description]
- **[Principle 3]**: [Description]

---

**Note:** This protocol integrates persona's [approach] with purpose's [objectives].
```

### Tool Provisioning Checklist

When documenting tools, ensure you cover:

- [ ] All scripts in your `scripts/` directory
- [ ] Build tools (`npm`, `make`, `cargo`, etc.)
- [ ] Test runners (`pytest`, `jest`, `go test`, etc.)
- [ ] Linters and formatters (`eslint`, `prettier`, `black`, etc.)
- [ ] Deployment tools (if assistant should use them)
- [ ] Custom automation scripts
- [ ] Database tools (migrations, seeds, etc.)
- [ ] API testing tools

For each tool:

- [ ] Full command path/syntax
- [ ] When to use (phase + trigger)
- [ ] What it does (purpose)
- [ ] Success indicators
- [ ] Failure indicators
- [ ] Example invocation

### Verify, Validate, and Assure

1. **Verify** against spec-for-protocol
2. **Validate** against guidance-for-protocol
3. Create verification edge, validation edge, and assurance face

Check integration:

- [ ] Phases achieve purpose deliverables
- [ ] Steps use persona's expertise
- [ ] Tools are referenced in phase steps
- [ ] All referenced tools are documented in Tools section

---

## Step 6: Assemble Your System Prompt

Now combine all three components into a system prompt document. **This step requires careful attention** - the deployed system prompt needs to be operational, not cluttered with authoring metadata.

### Authoring vs. Operational Content

Your individual PPP documents (persona, purpose, protocol) contain two kinds of content:

**Authoring content** (needed during development, NOT in deployed prompt):

- YAML frontmatter (type, id, tags, version, timestamps, dependencies)
- Meta-level "Purpose" statements that describe the document itself
- Notes about the PPP framework
- References to specs and guidances
- Version history or changelog remarks

**Operational content** (needed at runtime, INCLUDE in deployed prompt):

- The actual persona definition (role, expertise, tone, boundaries)
- The actual purpose definition (problem, objectives, deliverables, constraints, success criteria)
- The actual protocol (workflow, phases, collaboration points, quality checks, tools, principles)

### What to Strip When Compiling

When assembling the system prompt, **remove**:

| Strip This | Why |
|------------|-----|
| YAML frontmatter | Claude doesn't need document metadata at runtime |
| `## Purpose` meta-statements | "This document defines..." is for humans reading the doc, not for Claude acting on it |
| `**Note:**` blocks | Framework explanations aren't operational instructions |
| References like `[[spec-for-X]]` | These are for verification, not runtime |
| Version/timestamp info | Not relevant to assistant behavior |
| "This persona/purpose/protocol..." preambles | Self-referential commentary |

### What to Keep When Compiling

**Keep all operational content**:

| Keep This | Why |
|-----------|-----|
| Role and Identity | Defines who the assistant is |
| Domain Expertise | Defines what the assistant knows |
| Approach and Methodology | Defines how the assistant works |
| Communication Tone | Defines how the assistant communicates |
| Boundaries and Limitations | Defines what the assistant won't do |
| Problem Statement | Defines the core need |
| Core Objectives | Defines what value is delivered |
| Specific Deliverables | Defines concrete outputs |
| Constraints and Boundaries | Defines operational limits |
| Success Criteria | Defines how to measure success |
| Workflow Overview | Defines high-level process |
| Phase Definitions | Defines step-by-step workflow |
| User Collaboration Points | Defines when to engage user |
| Quality Assurance | Defines verification steps |
| Tools and Scripts | Defines available capabilities |
| Consistent Principles | Defines cross-cutting behaviors |

### Create the Source Document

Create `00_vertices/system-prompt-<your-name>.md` with full frontmatter for verification:

```yaml
---
type: vertex/system_prompt
extends: doc
id: v:system_prompt:<your-name>
name: System Prompt - <Your Assistant Name>
description: Complete AI model configuration using PPP framework
tags:
  - vertex
  - doc
  - system_prompt
version: 1.0.0
created: <ISO-8601-timestamp>
modified: <ISO-8601-timestamp>
dependencies:
  - v:spec:persona
  - v:spec:purpose
  - v:spec:protocol
---

# System Prompt - <Your Assistant Name>

## Purpose

This system prompt defines a complete AI model configuration for [your use case] using the PPP (Persona-Purpose-Protocol) framework.

## Persona

[Include full persona content with all required sections]

## Purpose

[Include full purpose content with all required sections]

## Protocol

[Include full protocol content with all required sections, including Tools]

---

**Note:** This system prompt uses the PPP framework with typed subsections.
```

### Verify, Validate, and Assure

1. **Verify** the system prompt structure against spec-for-system-prompt
2. **Validate** component integration against guidance-for-system-prompt
3. Create assurance face confirming the complete configuration

This source document retains all metadata for verification. The deployed version will be stripped.

---

## Step 7: Deploy to .claude/CLAUDE.md

Once your system prompt is fully assured, compile it for operational deployment.

### Compilation Process

The deployed `.claude/CLAUDE.md` should contain **only operational content**. You have two approaches:

**Option A: Manual Compilation**

1. Copy your system-prompt document
2. Remove the YAML frontmatter block
3. Remove meta-level "Purpose" statements (the ones describing the document)
4. Remove `**Note:**` blocks and framework references
5. Keep all operational sections intact
6. Save to `.claude/CLAUDE.md`

**Option B: Use Obsidian Embeds + Compile Script**

If your system-prompt uses Obsidian embeds (`![[persona-<name>]]`), use the compile script:

```bash
python scripts/compile_document.py 00_vertices/system-prompt-<your-name>.md .claude/CLAUDE.md
```

Then manually strip the frontmatter from the output.

### Example: Before and After

**Before (source document excerpt):**

```markdown
---
type: vertex/persona
extends: doc
id: v:persona:my-assistant
...
---

# Persona - My Assistant

## Purpose

This persona defines the identity of an AI assistant for web development support.

## Role and Identity

You are a senior developer assistant specializing in React and Node.js...

---

**Note:** This persona is designed to work within the PPP framework.
```

**After (deployed to .claude/CLAUDE.md):**

```markdown
## Persona

You are a senior developer assistant specializing in React and Node.js...
```

### Deployed Structure

Your final `.claude/CLAUDE.md` should look like:

```markdown
# System Prompt - <Your Assistant Name>

## Persona

[Operational persona content - role, expertise, approach, tone, boundaries]

## Purpose

[Operational purpose content - problem, objectives, deliverables, constraints, success]

## Protocol

[Operational protocol content - workflow, phases, collaboration, quality, tools, principles]
```

No frontmatter. No meta-statements. No framework notes. Just the operational configuration.

### Verify Deployment

Open a new Claude Code session in your repository. The assistant should now behave according to your configuration - including using the tools you provisioned.

---

## Step 8: Clean Up Template Artifacts

Remove content that doesn't apply to your workspace:

### What to Remove

- Example documents you won't use
- Specs for document types you don't need
- The original system prompt (if different from yours)
- This personalization guide (once complete)

### What to Keep

- Core specs (spec-for-spec, guidance-for-guidance, etc.) - these govern your document types
- Verification scripts - you'll use these
- Your PPP documents and assurance artifacts
- HOWTO-CREATE-DOCUMENT-TYPE.md (if you'll create custom types)

### Update README

Update `README.md` to describe your workspace, not the template.

---

## Step 9: Start Working

You now have two paths forward:

### Option A: Start Writing with Your Assistant

Your assistant is configured and ready. Start using it for your work:

- Create documents
- Get help with tasks
- Use the tools you provisioned
- Iterate on your PPP configuration as you learn what works

### Option B: Create Custom Document Types (Test-Driven Writing)

If you want structured, typed documents for your domain:

1. Read [HOWTO-CREATE-DOCUMENT-TYPE.md](HOWTO-CREATE-DOCUMENT-TYPE.md)
2. Define specs for your document types
3. Create guidance for quality assessment
4. Build verification infrastructure
5. Use your assistant to help create conforming documents

---

## Quick Reference

### PPP Design Order

1. **Purpose FIRST** - What value is delivered?
2. **Persona SECOND** - What expertise enables that value?
3. **Protocol LAST** - What workflow integrates persona and purpose? What tools are available?

### Tool Provisioning Summary

The Protocol's Tools section tells your assistant what software it can use:

| Element | Description |
|---------|-------------|
| **What** | Tool name, path, command syntax |
| **When** | Which phase, what triggers use |
| **How** | Parameters, examples, invocation patterns |
| **Success** | Expected output when tool works |
| **Failure** | Error patterns, how to handle |

### Verification Commands

| Task | Command |
|------|---------|
| Verify single file | `python scripts/verify_template_based.py <file> --templates templates` |
| Rebuild cache | `python scripts/build_cache.py` |
| Run all tests | `python -m pytest tests/ -v --ignore=tests/archive/` |

### Key Documents

| Document | Location |
|----------|----------|
| spec-for-persona | `00_vertices/spec-for-persona.md` |
| spec-for-purpose | `00_vertices/spec-for-purpose.md` |
| spec-for-protocol | `00_vertices/spec-for-protocol.md` |
| spec-for-system-prompt | `00_vertices/spec-for-system-prompt.md` |
| guidance-for-persona | `00_vertices/guidance-for-persona.md` |
| guidance-for-purpose | `00_vertices/guidance-for-purpose.md` |
| guidance-for-protocol | `00_vertices/guidance-for-protocol.md` |
| guidance-for-system-prompt | `00_vertices/guidance-for-system-prompt.md` |

---

## Common Questions

### Do I need to create all the verification/validation edges?

For a production-quality configuration, yes. The assurance process ensures your PPP components are both structurally correct and fit for purpose.

For rapid prototyping, you can skip the formal assurance artifacts and iterate faster - but you lose the quality guarantees.

### Can I modify my PPP after deployment?

Yes. PPP documents are versioned. Update them, re-verify, re-validate, and redeploy to `.claude/CLAUDE.md`.

### What if I don't know what I need yet?

Start with a minimal Purpose document that captures your best current understanding. The PPP framework supports iteration - you'll refine as you learn.

### Can I have multiple system prompts?

Yes. Create multiple system prompt documents for different contexts, and swap which one is deployed to `.claude/CLAUDE.md` as needed.

### How do I add new tools later?

Update your Protocol document's Tools section, re-verify, and redeploy to `.claude/CLAUDE.md`. The assistant will have access to the new tools in subsequent sessions.

### What if a tool doesn't exist in my workspace?

Don't document tools that don't exist - this will confuse the assistant. Only list tools that are actually available and working.

---

## Summary

The personalization workflow:

```
Template Repo ──► Your Repo ──► Narrate Intent
                                    │
                                    ▼
                              Create Purpose (V&V)
                                    │
                                    ▼
                              Create Persona (V&V)
                                    │
                                    ▼
                              Create Protocol (V&V)
                              [includes Tool Provisioning]
                                    │
                                    ▼
                              Assemble System Prompt (V&V)
                                    │
                                    ▼
                              Deploy to .claude/CLAUDE.md
                                    │
                                    ▼
                              Clean Up & Start Working
```

Each PPP component goes through full verification (structure) and validation (quality) before assembly. The Protocol's Tools section provisions what software capabilities your assistant can use. This ensures your AI assistant configuration is both correct and fit for purpose.

---

**Note:** This guide assumes familiarity with git, markdown, and command-line tools. If you encounter issues with the verification scripts, ensure Python dependencies are installed and you're running from the repository root.
