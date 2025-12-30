#!/usr/bin/env python3
"""
Figure 3: Boundary Complex Structure - Iterative refinement

Shows the 5-vertex self-referential foundation with root anchor.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, RegularPolygon, Polygon
from matplotlib.lines import Line2D
from pathlib import Path

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica'],
    'font.size': 10,
    'figure.dpi': 150,
    'savefig.dpi': 300,
})

COLORS = {
    'spec': '#27AE60',
    'guidance': '#E67E22',
    'root': '#F1C40F',
    'verification': '#27AE60',
    'validation': '#E74C3C',
    'coupling': '#8E44AD',
    'boundary': '#95A5A6',
    'face_standard': '#E8F8F5',
    'face_boundary': '#EBF5FB',
    'text': '#2C3E50',
}


def generate_figure3_v1(output_path: Path):
    """
    Version 1: 2D layout with root at center

    Layout (diamond/bowtie shape):
              [SS]          [SG]
                 \    R    /
                  \   |   /
                   \  |  /
                    [GS]----[GG]

    Actually let's try a cleaner layout:

           [SS] ---------- [SG]
             \      |      /
              \     |     /
               \   [R]   /
                \   |   /
                 \  |  /
           [GS] ---------- [GG]
    """
    fig, ax = plt.subplots(figsize=(8, 7))

    # Positions - square with root at center
    positions = {
        'ss': (0.25, 0.75),    # Top left (Spec-for-Spec)
        'sg': (0.75, 0.75),    # Top right (Spec-for-Guidance)
        'gs': (0.25, 0.25),    # Bottom left (Guidance-for-Spec)
        'gg': (0.75, 0.25),    # Bottom right (Guidance-for-Guidance)
        'root': (0.5, 0.5),    # Center
    }

    labels = {
        'ss': 'SS',
        'sg': 'SG',
        'gs': 'GS',
        'gg': 'GG',
        'root': 'ROOT',
    }

    full_labels = {
        'ss': 'spec-for-spec',
        'sg': 'spec-for-guidance',
        'gs': 'guidance-for-spec',
        'gg': 'guidance-for-guidance',
    }

    # Draw faces first (background)
    # Boundary face b2:spec-spec (root-GS-SS) - left triangle
    b2_ss_verts = [positions['root'], positions['gs'], positions['ss']]
    b2_ss = Polygon(b2_ss_verts, facecolor=COLORS['face_boundary'],
                    edgecolor='none', alpha=0.5, zorder=1)
    ax.add_patch(b2_ss)

    # Boundary face b2:guidance-guidance (root-SG-GG) - right triangle
    b2_gg_verts = [positions['root'], positions['sg'], positions['gg']]
    b2_gg = Polygon(b2_gg_verts, facecolor=COLORS['face_boundary'],
                    edgecolor='none', alpha=0.5, zorder=1)
    ax.add_patch(b2_gg)

    # Standard face f:assurance:spec-guidance (SG-SS-GS) - top-left triangle
    f_sg_verts = [positions['sg'], positions['ss'], positions['gs']]
    f_sg = Polygon(f_sg_verts, facecolor=COLORS['face_standard'],
                   edgecolor='none', alpha=0.4, zorder=1)
    ax.add_patch(f_sg)

    # Standard face f:assurance:guidance-spec (GS-SG-GG) - bottom-right triangle
    f_gs_verts = [positions['gs'], positions['sg'], positions['gg']]
    f_gs = Polygon(f_gs_verts, facecolor=COLORS['face_standard'],
                   edgecolor='none', alpha=0.4, zorder=1)
    ax.add_patch(f_gs)

    # Helper functions
    def draw_arrow(start, end, color, style='-', width=2):
        x1, y1 = positions[start]
        x2, y2 = positions[end]
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='-|>', color=color,
                                  linewidth=width, linestyle=style,
                                  shrinkA=18, shrinkB=18))

    def draw_line(start, end, color, style='-', width=2):
        x1, y1 = positions[start]
        x2, y2 = positions[end]
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=width,
                linestyle=style, zorder=2)

    # Coupling edges (purple - undirected)
    draw_line('ss', 'gs', COLORS['coupling'], '-', 2.5)
    draw_line('sg', 'gg', COLORS['coupling'], '-', 2.5)
    draw_line('sg', 'gs', COLORS['coupling'], '-', 2.5)

    # Verification edges (green - directed)
    draw_arrow('sg', 'ss', COLORS['verification'], '-', 2)
    draw_arrow('gs', 'sg', COLORS['verification'], '-', 2)
    draw_arrow('gg', 'sg', COLORS['verification'], '-', 2)

    # Validation edges (red - directed, dashed)
    draw_arrow('ss', 'gs', COLORS['validation'], '--', 2)
    draw_arrow('sg', 'gs', COLORS['validation'], '--', 2)
    draw_arrow('gs', 'gg', COLORS['validation'], '--', 2)

    # Boundary edges to root (gray - dotted)
    draw_arrow('ss', 'root', COLORS['boundary'], ':', 1.8)
    draw_arrow('gg', 'root', COLORS['boundary'], ':', 1.8)
    draw_line('root', 'gs', COLORS['boundary'], ':', 1.8)
    draw_line('root', 'sg', COLORS['boundary'], ':', 1.8)

    # Draw vertices
    vertex_size = 0.055

    # Spec vertices (green squares)
    for v in ['ss', 'sg']:
        x, y = positions[v]
        rect = FancyBboxPatch((x - vertex_size/2, y - vertex_size/2),
                               vertex_size, vertex_size,
                               boxstyle="round,pad=0.005,rounding_size=0.005",
                               facecolor=COLORS['spec'], edgecolor='white',
                               linewidth=2.5, zorder=10)
        ax.add_patch(rect)
        ax.text(x, y, labels[v], ha='center', va='center',
                fontsize=12, fontweight='bold', color='white', zorder=11)

    # Guidance vertices (orange rounded)
    for v in ['gs', 'gg']:
        x, y = positions[v]
        rect = FancyBboxPatch((x - vertex_size/2, y - vertex_size/2),
                               vertex_size, vertex_size,
                               boxstyle="round,pad=0.005,rounding_size=0.02",
                               facecolor=COLORS['guidance'], edgecolor='white',
                               linewidth=2.5, zorder=10)
        ax.add_patch(rect)
        ax.text(x, y, labels[v], ha='center', va='center',
                fontsize=12, fontweight='bold', color='white', zorder=11)

    # Root (gold hexagon at center)
    root_x, root_y = positions['root']
    star = RegularPolygon((root_x, root_y), numVertices=6, radius=0.05,
                          facecolor=COLORS['root'], edgecolor='#B7950B',
                          linewidth=2.5, zorder=10)
    ax.add_patch(star)
    ax.text(root_x, root_y, 'R', ha='center', va='center',
            fontsize=14, fontweight='bold', color='#7D6608', zorder=11)

    # Full labels outside vertices (positioned to avoid legend)
    ax.text(positions['ss'][0] + 0.12, positions['ss'][1] + 0.06, full_labels['ss'],
            ha='left', va='bottom', fontsize=9, color='#555', fontstyle='italic')
    ax.text(positions['sg'][0], positions['sg'][1] + 0.08, full_labels['sg'],
            ha='center', va='bottom', fontsize=9, color='#555', fontstyle='italic')
    ax.text(positions['gs'][0], positions['gs'][1] - 0.08, full_labels['gs'],
            ha='center', va='top', fontsize=9, color='#555', fontstyle='italic')
    ax.text(positions['gg'][0], positions['gg'][1] - 0.08, full_labels['gg'],
            ha='center', va='top', fontsize=9, color='#555', fontstyle='italic')

    # Face labels
    ax.text(0.33, 0.52, 'b2', fontsize=11, fontweight='bold', color='#3498DB',
            ha='center', va='center')
    ax.text(0.67, 0.52, 'b2', fontsize=11, fontweight='bold', color='#3498DB',
            ha='center', va='center')
    ax.text(0.42, 0.62, 'f', fontsize=11, fontweight='bold', color='#27AE60',
            ha='center', va='center')
    ax.text(0.58, 0.38, 'f', fontsize=11, fontweight='bold', color='#27AE60',
            ha='center', va='center')

    # Legend
    legend_elements = [
        Line2D([0], [0], color=COLORS['verification'], linewidth=2.5, marker='>',
               markersize=7, label='Verification'),
        Line2D([0], [0], color=COLORS['validation'], linewidth=2.5, linestyle='--',
               marker='>', markersize=7, label='Validation'),
        Line2D([0], [0], color=COLORS['coupling'], linewidth=2.5,
               label='Coupling'),
        Line2D([0], [0], color=COLORS['boundary'], linewidth=2, linestyle=':',
               label='Boundary'),
        mpatches.Patch(facecolor=COLORS['face_boundary'], alpha=0.5,
                       edgecolor='#3498DB', label='b2: Boundary face'),
        mpatches.Patch(facecolor=COLORS['face_standard'], alpha=0.4,
                       edgecolor='#27AE60', label='f: Standard face'),
    ]
    leg = ax.legend(handles=legend_elements, loc='upper left',
                    bbox_to_anchor=(0.02, 0.98), framealpha=0.95,
                    fontsize=9, frameon=True, fancybox=True)
    leg.get_frame().set_edgecolor('#CCCCCC')

    # Statistics
    stats_text = "V = 5   E = 12   F = 4\nEuler char. = -3"
    ax.text(0.98, 0.02, stats_text, transform=ax.transAxes, fontsize=9,
            ha='right', va='bottom', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.95,
                      edgecolor='#CCCCCC'))

    # Title
    ax.set_title('Boundary Complex Structure', fontsize=15, fontweight='bold',
                 pad=12, color=COLORS['text'])

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {output_path}")


if __name__ == '__main__':
    output_dir = Path('figures')
    output_dir.mkdir(exist_ok=True)
    generate_figure3_v1(output_dir / 'figure3-v1.png')
