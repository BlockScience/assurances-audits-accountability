# GitHub Actions Workflows

This directory contains GitHub Actions workflows for automated CI/CD checks.

## Workflows

### validate-accountability.yml

**Purpose:** Ensures validation edges are only committed by the accountable party.

**Triggers:**
- Pull requests to `main` or `dev` branches
- Pushes to `main` or `dev` branches

**What it checks:**
- Identifies validation edges (type: `edge/validation`) modified in commits
- Extracts the accountable party from frontmatter:
  - For `manual` validation: the `validator` field
  - For `llm-assisted` or `automated`: the `human_approver` field
- Compares against the Git committer and GitHub actor
- Fails if mismatch is detected

**Example failure:**

```
Accountability violation found in: 01_edges/validation-spec-spec.md
  Accountable party: mzargham
  Git committer: alice
  GitHub actor: alice
  Only the accountable party can commit this validation edge.
```

**How to fix:**
1. Have the accountable party commit the file, OR
2. Update the frontmatter to list the actual committer as accountable (and have them accept responsibility)

## Setup Instructions

### 1. Enable GitHub Actions

GitHub Actions should be enabled by default. Verify at:
`https://github.com/OWNER/REPO/settings/actions`

### 2. Set Up Branch Protection (Required)

To enforce accountability checks, make `validate-accountability` a required status check:

1. Go to: `https://github.com/OWNER/REPO/settings/branches`
2. Add a branch protection rule for `main`:
   - ☑ Require status checks to pass before merging
   - ☑ Require branches to be up to date before merging
   - Select: `check-accountability` (will appear after first run)
3. Repeat for `dev` branch if desired

This ensures PRs cannot be merged if accountability checks fail.

### 3. Grant Workflow Permissions (for PR comments)

If you want the workflow to comment on failed PRs:

1. Go to: `https://github.com/OWNER/REPO/settings/actions`
2. Under "Workflow permissions", select:
   - ☑ Read and write permissions
3. Click "Save"

### 4. Test the Workflow

Create a test PR that modifies a validation edge:

```bash
# On a new branch
git checkout -b test-accountability

# Modify a validation edge (change validator to someone else)
vim 01_edges/validation-spec-spec.md
# Change: validator: "mzargham"
# To: validator: "testuser"

git add 01_edges/validation-spec-spec.md
git commit -m "Test: accountability check (should fail)"
git push origin test-accountability

# Create PR and verify workflow fails with clear error message
```

Then revert and verify it passes:

```bash
# Fix the validator back
vim 01_edges/validation-spec-spec.md
# Change back to: validator: "mzargham"

git add 01_edges/validation-spec-spec.md
git commit -m "Fix: restore correct validator"
git push

# Verify workflow passes
```

## Workflow Behavior

### On Pull Requests

- ✓ **Pass:** Validation edges committed by accountable party
- ✗ **Fail:** Validation edges committed by someone else
- Posts comment on PR explaining the failure
- Blocks merge if configured as required status check

### On Direct Pushes

- Runs the check but cannot block the push (already committed)
- Useful for detecting issues on direct commits to protected branches

## Bypassing (Emergency Use Only)

Administrators can bypass branch protection rules, but this should only be used in emergencies. The accountability framework exists to maintain trust in the validation system.

If you need to commit a validation edge on behalf of someone:
1. Get explicit approval from the accountable party
2. Update the frontmatter to add both parties in a note
3. Document the exception in the commit message

## Local Testing

You can test accountability checks locally before pushing:

```bash
# Test on your current commit
python scripts/check_accountability.py

# Test on a specific commit
git checkout <commit-hash>
python scripts/check_accountability.py
```

## Troubleshooting

### "No validation edges modified in this commit"

This is normal - the check only runs when validation edges are actually modified. The workflow will pass with this message.

### Username matching issues

The script tries multiple matching strategies:
- Exact match: `mzargham` == `mzargham`
- Contains match: `mzargham` in `mzargham@users.noreply.github.com`
- Substring match: `alice` in `Alice Smith`

If matching fails incorrectly, check:
1. Git author name: `git config user.name`
2. GitHub username: Visible in `$GITHUB_ACTOR` in workflow logs
3. Frontmatter value: Must match one of the above

### Workflow doesn't appear in PR

- Check that the workflow file is on the base branch (usually `main` or `dev`)
- Workflow files must be merged to the base branch before they take effect on PRs
- Check Actions tab for error messages

## Security Considerations

**This is NOT cryptographically secure authentication.** It's an accountability framework based on:
- Social contract and professional trust
- Git commit attribution (can be spoofed with effort)
- GitHub actor identity (more reliable)
- Required status checks (enforceable via branch protection)

For highly sensitive validations, consider additional measures:
- GPG-signed commits
- Additional manual review gates
- Separate approval processes outside GitHub

The goal is to maintain clear accountability and prevent accidental misattribution, not to create a cryptographic proof system.
