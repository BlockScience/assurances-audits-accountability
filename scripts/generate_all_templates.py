#!/usr/bin/env python3
"""
Generate all templates from all specs.

This script auto-generates templates for all vertex types that have specs,
ensuring templates stay in sync with authoritative spec documents.

Usage:
    python scripts/generate_all_templates.py              # Generate all
    python scripts/generate_all_templates.py --type vertex # Generate vertices only
    python scripts/generate_all_templates.py --check       # Check if up-to-date
    python scripts/generate_all_templates.py --dry-run     # Show what would be generated
    python scripts/generate_all_templates.py --verbose     # Show generation details
"""

import sys
import argparse
from pathlib import Path
from typing import List, Dict, Tuple
import difflib

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))
from generate_template_from_spec import SpecParser, TemplateGenerator

# Map of spec files to their template output paths
SPEC_TO_TEMPLATE_MAP = {
    # Vertices (7 types)
    '00_vertices/spec-for-persona.md': 'templates/00_vertices/persona.md',
    '00_vertices/spec-for-purpose.md': 'templates/00_vertices/purpose.md',
    '00_vertices/spec-for-protocol.md': 'templates/00_vertices/protocol.md',
    '00_vertices/spec-for-spec.md': 'templates/00_vertices/spec.md',
    '00_vertices/spec-for-guidance.md': 'templates/00_vertices/guidance.md',
    '00_vertices/spec-for-system-prompt.md': 'templates/00_vertices/system_prompt.md',
    # Note: b0 doesn't have a spec (it's a boundary element)

    # Charts (2 types)
    '00_vertices/spec-for-charts.md': 'templates/charts/chart.md',
    '00_vertices/spec-for-assurance-audits.md': 'templates/charts/assurance_audit.md',
}

class BatchTemplateGenerator:
    """Generate multiple templates from specs."""

    def __init__(self, repo_root: Path, verbose: bool = False, dry_run: bool = False):
        self.repo_root = repo_root
        self.verbose = verbose
        self.dry_run = dry_run
        self.results: List[Dict] = []

    def log(self, message: str):
        """Log if verbose mode."""
        if self.verbose:
            print(f"  {message}")

    def generate_all(self, filter_type: str = None) -> bool:
        """
        Generate all templates from specs.

        Args:
            filter_type: Optional filter ('vertex', 'chart')

        Returns:
            True if all generations successful
        """
        success = True

        for spec_path, template_path in SPEC_TO_TEMPLATE_MAP.items():
            # Apply type filter if specified
            if filter_type:
                if filter_type == 'vertex' and not template_path.startswith('templates/00_vertices/'):
                    continue
                elif filter_type == 'chart' and not template_path.startswith('templates/charts/'):
                    continue

            result = self.generate_one(spec_path, template_path)
            self.results.append(result)

            if not result['success']:
                success = False

        return success

    def generate_one(self, spec_path: str, template_path: str) -> Dict:
        """Generate a single template from spec."""
        result = {
            'spec': spec_path,
            'template': template_path,
            'success': False,
            'message': '',
            'changed': False
        }

        spec_full = self.repo_root / spec_path
        template_full = self.repo_root / template_path

        # Check spec exists
        if not spec_full.exists():
            result['message'] = f"Spec not found: {spec_path}"
            print(f"✗ {spec_path} → {template_path}")
            print(f"  ERROR: {result['message']}")
            return result

        try:
            # Parse spec and generate template
            parser = SpecParser(spec_full)
            generator = TemplateGenerator(parser)
            new_content = generator.generate_template()

            # Check if template already exists
            if template_full.exists():
                old_content = template_full.read_text(encoding='utf-8')
                if old_content == new_content:
                    result['success'] = True
                    result['changed'] = False
                    result['message'] = "Up-to-date"
                    if self.verbose:
                        print(f"✓ {spec_path} → {template_path}")
                        self.log("Template already up-to-date")
                    else:
                        print(f"✓ {spec_path} → {template_path} (up-to-date)")
                    return result
                else:
                    result['changed'] = True
                    result['message'] = "Updated"
                    if self.dry_run:
                        print(f"⚠ {spec_path} → {template_path}")
                        self.log("Would update (dry-run)")
                        if self.verbose:
                            self.show_diff(old_content, new_content, template_path)
                    else:
                        # Create backup
                        backup_path = template_full.with_suffix('.md.backup')
                        backup_path.write_text(old_content, encoding='utf-8')

                        # Write new template
                        template_full.write_text(new_content, encoding='utf-8')
                        print(f"✓ {spec_path} → {template_path}")
                        self.log(f"Updated (backup: {backup_path.name})")
            else:
                # New template
                result['changed'] = True
                result['message'] = "Created"
                if self.dry_run:
                    print(f"⚠ {spec_path} → {template_path}")
                    self.log("Would create (dry-run)")
                else:
                    # Ensure directory exists
                    template_full.parent.mkdir(parents=True, exist_ok=True)
                    template_full.write_text(new_content, encoding='utf-8')
                    print(f"✓ {spec_path} → {template_path}")
                    self.log("Created new template")

            result['success'] = True

        except Exception as e:
            result['message'] = f"Error: {str(e)}"
            print(f"✗ {spec_path} → {template_path}")
            print(f"  ERROR: {result['message']}")
            if self.verbose:
                import traceback
                traceback.print_exc()

        return result

    def show_diff(self, old_content: str, new_content: str, template_path: str):
        """Show diff between old and new content."""
        old_lines = old_content.splitlines(keepends=True)
        new_lines = new_content.splitlines(keepends=True)

        diff = difflib.unified_diff(
            old_lines, new_lines,
            fromfile=f"{template_path} (current)",
            tofile=f"{template_path} (generated)",
            lineterm=''
        )

        print("\n  Diff:")
        for line in diff:
            print(f"    {line}")
        print()

    def check_freshness(self) -> bool:
        """
        Check if all templates are up-to-date with their specs.

        Returns:
            True if all templates are fresh, False otherwise
        """
        print("Checking template freshness...\n")

        all_fresh = True
        stale_templates = []

        for spec_path, template_path in SPEC_TO_TEMPLATE_MAP.items():
            spec_full = self.repo_root / spec_path
            template_full = self.repo_root / template_path

            if not spec_full.exists():
                print(f"✗ {spec_path} - Spec not found")
                all_fresh = False
                continue

            if not template_full.exists():
                print(f"✗ {template_path} - Template missing (should be generated from spec)")
                stale_templates.append(template_path)
                all_fresh = False
                continue

            try:
                # Generate what template should be
                parser = SpecParser(spec_full)
                generator = TemplateGenerator(parser)
                expected_content = generator.generate_template()

                # Compare with actual
                actual_content = template_full.read_text(encoding='utf-8')

                if actual_content == expected_content:
                    print(f"✓ {template_path} - Fresh")
                else:
                    print(f"✗ {template_path} - Stale (doesn't match spec)")
                    stale_templates.append(template_path)
                    all_fresh = False

            except Exception as e:
                print(f"✗ {template_path} - Error: {e}")
                all_fresh = False

        if not all_fresh:
            print(f"\n❌ {len(stale_templates)} template(s) are stale")
            print("\nRun: python scripts/generate_all_templates.py")
            return False
        else:
            print("\n✅ All templates are fresh")
            return True

    def print_summary(self):
        """Print summary of generation results."""
        if not self.results:
            return

        total = len(self.results)
        successful = sum(1 for r in self.results if r['success'])
        failed = total - successful
        changed = sum(1 for r in self.results if r['changed'])
        unchanged = successful - changed

        print(f"\n{'='*60}")
        print("Summary:")
        print(f"  Total:     {total}")
        print(f"  Success:   {successful}")
        print(f"  Failed:    {failed}")
        print(f"  Changed:   {changed}")
        print(f"  Unchanged: {unchanged}")

        if self.dry_run:
            print("\n(Dry-run mode: no files were modified)")

        print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate templates from spec documents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Generate all templates:
    python scripts/generate_all_templates.py

  Generate only vertex templates:
    python scripts/generate_all_templates.py --type vertex

  Check if templates are up-to-date:
    python scripts/generate_all_templates.py --check

  Dry-run (see what would change):
    python scripts/generate_all_templates.py --dry-run --verbose
"""
    )

    parser.add_argument(
        '--type',
        choices=['vertex', 'chart'],
        help='Only generate templates of specified type'
    )
    parser.add_argument(
        '--check',
        action='store_true',
        help='Check if templates are up-to-date (exit 1 if stale)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be generated without modifying files'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed output'
    )

    args = parser.parse_args()

    # Determine repo root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent

    generator = BatchTemplateGenerator(
        repo_root=repo_root,
        verbose=args.verbose,
        dry_run=args.dry_run
    )

    if args.check:
        # Check mode
        fresh = generator.check_freshness()
        sys.exit(0 if fresh else 1)
    else:
        # Generate mode
        print(f"Generating templates from specs...\n")
        if args.dry_run:
            print("(Dry-run mode: no files will be modified)\n")

        success = generator.generate_all(filter_type=args.type)
        generator.print_summary()

        sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
