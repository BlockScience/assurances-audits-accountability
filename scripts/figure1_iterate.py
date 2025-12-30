#!/usr/bin/env python3
"""
Figure 1: Assurance Triangle - Iterative refinement
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.lines import Line2D
from pathlib import Path

# Publication quality settings
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica'],
    'font.size': 11,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

COLORS = {
    'spec': '#27AE60',       # Green
    'guidance': '#E67E22',   # Orange
    'doc': '#3498DB',        # Blue
    'verification': '#27AE60',
    'validation': '#E74C3C', # Red (more distinct from orange)
    'coupling': '#8E44AD',   # Purple
    'face': '#ECF0F1',       # Light gray
    'text': '#2C3E50',
}


def generate_figure1_v2(output_path: Path):
    """
    Version 2: Flatter view, more spread out, cleaner labels
    """
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # More spread out triangle, flatter in z
    # Think of it as laying mostly flat with slight tilt for depth
    positions = {
        'doc': np.array([0, 1.5, 0.3]),        # Top center, slightly raised
        'guidance': np.array([1.3, -0.7, 0]),  # Bottom right
        'spec': np.array([-1.3, -0.7, 0]),     # Bottom left
    }

    # Draw face first (background)
    verts = [positions['doc'], positions['spec'], positions['guidance']]
    triangle = Poly3DCollection([verts], alpha=0.3, facecolor=COLORS['face'],
                                 edgecolor='#BDC3C7', linewidth=1)
    ax.add_collection3d(triangle)

    # Draw edges with clear separation
    # Verification: Doc → Spec (green solid)
    ax.plot([positions['doc'][0], positions['spec'][0]],
            [positions['doc'][1], positions['spec'][1]],
            [positions['doc'][2], positions['spec'][2]],
            color=COLORS['verification'], linewidth=3, linestyle='-', zorder=5)

    # Validation: Doc → Guidance (red dashed)
    ax.plot([positions['doc'][0], positions['guidance'][0]],
            [positions['doc'][1], positions['guidance'][1]],
            [positions['doc'][2], positions['guidance'][2]],
            color=COLORS['validation'], linewidth=3, linestyle='--', zorder=5)

    # Coupling: Spec ↔ Guidance (purple solid)
    ax.plot([positions['spec'][0], positions['guidance'][0]],
            [positions['spec'][1], positions['guidance'][1]],
            [positions['spec'][2], positions['guidance'][2]],
            color=COLORS['coupling'], linewidth=3, linestyle='-', zorder=5)

    # Draw vertices as scatter points (cleaner than spheres)
    ax.scatter(*positions['doc'], s=800, c=COLORS['doc'], marker='o',
               edgecolors='white', linewidths=2, zorder=10, label='Document')
    ax.scatter(*positions['spec'], s=600, c=COLORS['spec'], marker='s',
               edgecolors='white', linewidths=2, zorder=10, label='Specification')
    ax.scatter(*positions['guidance'], s=600, c=COLORS['guidance'], marker='o',
               edgecolors='white', linewidths=2, zorder=10, label='Guidance')

    # Labels - positioned clearly away from vertices
    ax.text(positions['doc'][0], positions['doc'][1] + 0.4, positions['doc'][2] + 0.15,
            'Document', fontsize=13, fontweight='bold', ha='center', va='bottom',
            color=COLORS['text'])
    ax.text(positions['spec'][0] - 0.3, positions['spec'][1] - 0.3, positions['spec'][2],
            'Specification', fontsize=12, fontweight='bold', ha='center', va='top',
            color=COLORS['text'])
    ax.text(positions['guidance'][0] + 0.3, positions['guidance'][1] - 0.3, positions['guidance'][2],
            'Guidance', fontsize=12, fontweight='bold', ha='center', va='top',
            color=COLORS['text'])

    # Edge labels - positioned at midpoints, offset to avoid overlap
    mid_ver = (positions['doc'] + positions['spec']) / 2
    ax.text(mid_ver[0] - 0.5, mid_ver[1] + 0.1, mid_ver[2] + 0.2,
            'Verification', fontsize=10, ha='center', color=COLORS['verification'],
            fontweight='bold')

    mid_val = (positions['doc'] + positions['guidance']) / 2
    ax.text(mid_val[0] + 0.5, mid_val[1] + 0.1, mid_val[2] + 0.2,
            'Validation', fontsize=10, ha='center', color=COLORS['validation'],
            fontweight='bold')

    mid_coup = (positions['spec'] + positions['guidance']) / 2
    ax.text(mid_coup[0], mid_coup[1] - 0.5, mid_coup[2],
            'Coupling', fontsize=10, ha='center', color=COLORS['coupling'],
            fontweight='bold')

    # Axis settings
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 2.5)
    ax.set_zlim(-0.5, 1)

    # View from above-front (bird's eye with slight tilt)
    ax.view_init(elev=35, azim=-60)

    ax.set_axis_off()

    # Legend
    legend_elements = [
        Line2D([0], [0], color=COLORS['verification'], linewidth=3, label='Verification (structural)'),
        Line2D([0], [0], color=COLORS['validation'], linewidth=3, linestyle='--', label='Validation (qualitative)'),
        Line2D([0], [0], color=COLORS['coupling'], linewidth=3, label='Coupling (type coherence)'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', framealpha=0.95,
              fontsize=10, frameon=True)

    plt.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {output_path}")
    return output_path


def generate_figure1_v3(output_path: Path):
    """
    Version 3: More symmetric, better label placement, title added
    Try nearly top-down view to show triangle clearly
    """
    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Equilateral-ish triangle when viewed from above
    # Arranged so it looks symmetric from chosen angle
    h = 1.5  # height from center to top vertex
    w = 1.3  # half-width at base
    positions = {
        'doc': np.array([0, h, 0.4]),          # Top, raised
        'spec': np.array([-w, -0.6, 0]),       # Bottom left
        'guidance': np.array([w, -0.6, 0]),    # Bottom right
    }

    # Draw face first (background)
    verts = [positions['doc'], positions['spec'], positions['guidance']]
    triangle = Poly3DCollection([verts], alpha=0.25, facecolor='#D5DBDB',
                                 edgecolor='#AAB7B8', linewidth=1.5)
    ax.add_collection3d(triangle)

    # Draw edges
    # Verification: Doc → Spec (green solid)
    ax.plot([positions['doc'][0], positions['spec'][0]],
            [positions['doc'][1], positions['spec'][1]],
            [positions['doc'][2], positions['spec'][2]],
            color=COLORS['verification'], linewidth=3.5, linestyle='-', zorder=5)

    # Validation: Doc → Guidance (red dashed)
    ax.plot([positions['doc'][0], positions['guidance'][0]],
            [positions['doc'][1], positions['guidance'][1]],
            [positions['doc'][2], positions['guidance'][2]],
            color=COLORS['validation'], linewidth=3.5, linestyle='--', zorder=5)

    # Coupling: Spec ↔ Guidance (purple solid)
    ax.plot([positions['spec'][0], positions['guidance'][0]],
            [positions['spec'][1], positions['guidance'][1]],
            [positions['spec'][2], positions['guidance'][2]],
            color=COLORS['coupling'], linewidth=3.5, linestyle='-', zorder=5)

    # Draw vertices
    ax.scatter(*positions['doc'], s=900, c=COLORS['doc'], marker='o',
               edgecolors='white', linewidths=2.5, zorder=10)
    ax.scatter(*positions['spec'], s=700, c=COLORS['spec'], marker='s',
               edgecolors='white', linewidths=2, zorder=10)
    ax.scatter(*positions['guidance'], s=700, c=COLORS['guidance'], marker='o',
               edgecolors='white', linewidths=2, zorder=10)

    # Labels - clear positioning
    ax.text(positions['doc'][0], positions['doc'][1] + 0.35, positions['doc'][2] + 0.1,
            'Document', fontsize=14, fontweight='bold', ha='center', va='bottom',
            color=COLORS['text'])
    ax.text(positions['spec'][0], positions['spec'][1] - 0.45, positions['spec'][2],
            'Spec', fontsize=13, fontweight='bold', ha='center', va='top',
            color=COLORS['text'])
    ax.text(positions['guidance'][0], positions['guidance'][1] - 0.45, positions['guidance'][2],
            'Guidance', fontsize=13, fontweight='bold', ha='center', va='top',
            color=COLORS['text'])

    # Edge labels with explanations
    mid_ver = (positions['doc'] + positions['spec']) / 2
    ax.text(mid_ver[0] - 0.6, mid_ver[1], mid_ver[2] + 0.25,
            'Verification', fontsize=11, ha='center', color=COLORS['verification'],
            fontweight='bold', fontstyle='italic')

    mid_val = (positions['doc'] + positions['guidance']) / 2
    ax.text(mid_val[0] + 0.6, mid_val[1], mid_val[2] + 0.25,
            'Validation', fontsize=11, ha='center', color=COLORS['validation'],
            fontweight='bold', fontstyle='italic')

    mid_coup = (positions['spec'] + positions['guidance']) / 2
    ax.text(mid_coup[0], mid_coup[1] - 0.45, mid_coup[2] - 0.1,
            'Coupling', fontsize=11, ha='center', color=COLORS['coupling'],
            fontweight='bold', fontstyle='italic')

    # Axis settings - tighter
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-1.8, 2.5)
    ax.set_zlim(-0.3, 1.0)

    # Near top-down but with enough tilt to see depth
    ax.view_init(elev=50, azim=-90)

    ax.set_axis_off()

    # Legend - positioned in corner
    legend_elements = [
        Line2D([0], [0], color=COLORS['verification'], linewidth=3,
               label='Verification (structural compliance)'),
        Line2D([0], [0], color=COLORS['validation'], linewidth=3, linestyle='--',
               label='Validation (qualitative assessment)'),
        Line2D([0], [0], color=COLORS['coupling'], linewidth=3,
               label='Coupling (type coherence)'),
    ]
    leg = ax.legend(handles=legend_elements, loc='upper right', framealpha=0.95,
                    fontsize=9, frameon=True, fancybox=True)
    leg.get_frame().set_edgecolor('#CCCCCC')

    # Title
    ax.set_title('The Assurance Triangle', fontsize=16, fontweight='bold',
                 pad=15, color=COLORS['text'])

    plt.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white',
                edgecolor='none')
    plt.close()
    print(f"Saved: {output_path}")
    return output_path


def generate_figure1_v4(output_path: Path):
    """
    Version 4: Final polish - symmetric triangle, arrows, better layout
    """
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Truly equilateral triangle positions (calculated for symmetry at chosen view)
    # Using 60 degree angles
    positions = {
        'doc': np.array([0, 1.4, 0.35]),          # Top apex
        'spec': np.array([-1.2, -0.7, 0]),        # Bottom left
        'guidance': np.array([1.2, -0.7, 0]),     # Bottom right
    }

    # Draw face first (background)
    verts = [positions['doc'], positions['spec'], positions['guidance']]
    triangle = Poly3DCollection([verts], alpha=0.2, facecolor='#E8E8E8',
                                 edgecolor='none')
    ax.add_collection3d(triangle)

    # Draw edges with arrows using quiver for direction
    def draw_arrow_edge(start, end, color, linestyle='-', with_arrow=True):
        # Draw the line
        ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]],
                color=color, linewidth=3, linestyle=linestyle, zorder=5)
        # Add arrowhead near the end
        if with_arrow:
            direction = end - start
            direction = direction / np.linalg.norm(direction)
            arrow_start = end - direction * 0.35
            ax.quiver(arrow_start[0], arrow_start[1], arrow_start[2],
                      direction[0]*0.25, direction[1]*0.25, direction[2]*0.25,
                      color=color, arrow_length_ratio=0.6, linewidth=2.5)

    # Verification: Doc → Spec (green solid with arrow)
    draw_arrow_edge(positions['doc'], positions['spec'], COLORS['verification'], '-', True)

    # Validation: Doc → Guidance (red dashed with arrow)
    draw_arrow_edge(positions['doc'], positions['guidance'], COLORS['validation'], '--', True)

    # Coupling: Spec ↔ Guidance (purple solid, NO arrow - bidirectional)
    draw_arrow_edge(positions['spec'], positions['guidance'], COLORS['coupling'], '-', False)

    # Draw vertices
    ax.scatter(*positions['doc'], s=1000, c=COLORS['doc'], marker='o',
               edgecolors='white', linewidths=2.5, zorder=10)
    ax.scatter(*positions['spec'], s=750, c=COLORS['spec'], marker='s',
               edgecolors='white', linewidths=2, zorder=10)
    ax.scatter(*positions['guidance'], s=750, c=COLORS['guidance'], marker='o',
               edgecolors='white', linewidths=2, zorder=10)

    # Labels - clear positioning outside the triangle
    ax.text(positions['doc'][0], positions['doc'][1] + 0.3, positions['doc'][2] + 0.1,
            'Document', fontsize=14, fontweight='bold', ha='center', va='bottom',
            color=COLORS['text'])
    ax.text(positions['spec'][0] - 0.15, positions['spec'][1] - 0.4, positions['spec'][2],
            'Spec', fontsize=13, fontweight='bold', ha='center', va='top',
            color=COLORS['text'])
    ax.text(positions['guidance'][0] + 0.15, positions['guidance'][1] - 0.4, positions['guidance'][2],
            'Guidance', fontsize=13, fontweight='bold', ha='center', va='top',
            color=COLORS['text'])

    # Edge labels - outside the triangle edges
    ax.text(-0.95, 0.5, 0.25,
            'Verification', fontsize=10, ha='center', color=COLORS['verification'],
            fontweight='bold', fontstyle='italic')

    ax.text(0.95, 0.5, 0.25,
            'Validation', fontsize=10, ha='center', color=COLORS['validation'],
            fontweight='bold', fontstyle='italic')

    ax.text(0, -1.15, 0,
            'Coupling', fontsize=10, ha='center', color=COLORS['coupling'],
            fontweight='bold', fontstyle='italic')

    # Axis settings - tight around content
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.6, 2.0)
    ax.set_zlim(-0.2, 0.8)

    # Top-down with slight forward tilt
    ax.view_init(elev=55, azim=-90)

    ax.set_axis_off()

    # Legend at bottom
    legend_elements = [
        Line2D([0], [0], color=COLORS['verification'], linewidth=3, marker='>',
               markersize=8, label='Verification (structural)'),
        Line2D([0], [0], color=COLORS['validation'], linewidth=3, linestyle='--',
               marker='>', markersize=8, label='Validation (qualitative)'),
        Line2D([0], [0], color=COLORS['coupling'], linewidth=3,
               label='Coupling (type coherence)'),
    ]
    leg = ax.legend(handles=legend_elements, loc='lower center',
                    bbox_to_anchor=(0.5, -0.02), ncol=1,
                    framealpha=0.95, fontsize=9, frameon=True, fancybox=True)
    leg.get_frame().set_edgecolor('#CCCCCC')

    # Title
    ax.set_title('The Assurance Triangle', fontsize=15, fontweight='bold',
                 pad=5, color=COLORS['text'])

    plt.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white',
                edgecolor='none')
    plt.close()
    print(f"Saved: {output_path}")
    return output_path


if __name__ == '__main__':
    output_dir = Path('figures')
    output_dir.mkdir(exist_ok=True)
    generate_figure1_v4(output_dir / 'figure1-v4.png')
