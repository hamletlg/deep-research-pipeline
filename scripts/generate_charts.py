#!/usr/bin/env python3
"""Generate 4 publication-quality charts for the European AI Report 2026."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

CHARTS_DIR = "/mnt/DATA/trabajo_hermes/EUROPEAN_AI/charts"
os.makedirs(CHARTS_DIR, exist_ok=True)

# Global style settings for publication quality
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Helvetica', 'Arial'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'figure.dpi': 150,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.3,
})

# Colorblind-safe palette (viridis-inspired)
CB_PALETTE = ['#440154', '#3b528b', '#21918c', '#5ec962', '#fde725']
CB_COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']


def add_source_line(ax, text, y=-0.12):
    """Add a source line below the chart."""
    ax.text(0.5, y, text, transform=ax.transAxes, fontsize=8.5,
            ha='center', va='top', style='italic', color='#555555')


# ============================================================
# CHART 1: AI Investment Comparison by Region (2025)
# ============================================================
print("Generating Chart 1: AI Investment Comparison...")

fig, ax = plt.subplots(figsize=(8, 5.5))

regions = ['Europe', 'China', 'United States']
investments = [12, 15, 70]  # USD billions
colors = ['#9467bd', '#2ca02c', '#1f77b4']

bars = ax.barh(regions, investments, color=colors, height=0.5, edgecolor='white', linewidth=0.5)

# Add value labels at end of bars
for i, (bar, val) in enumerate(zip(bars, investments)):
    ax.text(val + 1.5, bar.get_y() + bar.get_height()/2,
            f'${val}B', va='center', ha='left', fontsize=11, fontweight='bold', color='#333333')

ax.set_xlabel('Private AI Investment (USD billions, 2025)', fontsize=12, fontweight='bold')
ax.set_title('Private AI Investment by Region, 2025\n(USD billions)', fontsize=14, fontweight='bold', pad=15)
ax.set_xlim(0, 80)

# Add tier labels
tier_labels = ['Tier 2 (CB Insights / PitchBook)', 'Tier 4 (Estimate)', 'Tier 2 (CB Insights)']
ax.set_yticklabels([f'{r}\n[{t}]' for r, t in zip(regions, tier_labels)], fontsize=9)

add_source_line(ax, 'Source: CB Insights State of AI 2025; PitchBook European VC Trends 2025; OECD estimates. [T2]')

fig.savefig(os.path.join(CHARTS_DIR, 'chart01_ai_investment_comparison.png'), dpi=150, facecolor='white')
plt.close(fig)
print("  -> chart01_ai_investment_comparison.png saved")


# ============================================================
# CHART 2: European AI Market Size Projection (2025-2032)
# ============================================================
print("Generating Chart 2: European AI Market Growth...")

fig, ax = plt.subplots(figsize=(9, 5.5))

years = np.arange(2025, 2033)
cagr = 0.302
market_2025 = 86.24
market_values = [market_2025 * ((1 + cagr) ** (i)) for i in range(len(years))]

# Truncate to 2 decimal places
market_values = [round(v, 2) for v in market_values]

# Main line
ax.plot(years, market_values, color='#1f77b4', linewidth=2.5, marker='o',
        markersize=6, markerfacecolor='white', markeredgewidth=2,
        markeredgecolor='#1f77b4', zorder=3)

# Fill area under the curve
ax.fill_between(years, market_values, alpha=0.1, color='#1f77b4')

# Add data labels on key points
for i, (yr, val) in enumerate(zip(years, market_values)):
    if i in [0, len(years)//2, len(years)-1]:
        ax.annotate(f'${val:.0f}B', (yr, val), textcoords="offset points",
                    xytext=(0, 12), ha='center', fontsize=10, fontweight='bold',
                    color='#1f77b4')
    elif i == 1:
        ax.annotate(f'${val:.0f}B', (yr, val), textcoords="offset points",
                    xytext=(0, 10), ha='center', fontsize=9, color='#555555')

ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Market Size (USD billions)', fontsize=12, fontweight='bold')
ax.set_title('European AI Market Size Projection, 2025–2032\n(30.2% CAGR)',
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlim(2024.5, 2032.5)
ax.set_xticks(years)

# Add CAGR annotation
ax.annotate(f'CAGR: 30.2%', xy=(2028, market_values[3]), xytext=(2027, market_values[3] * 1.15),
            fontsize=10, fontweight='bold', color='#d62728',
            arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.2))

add_source_line(ax, 'Source: MarketsandMarkets, "Europe AI Market Forecast to 2032." [T2]')

fig.savefig(os.path.join(CHARTS_DIR, 'chart02_market_growth.png'), dpi=150, facecolor='white')
plt.close(fig)
print("  -> chart02_market_growth.png saved")


# ============================================================
# CHART 3: European AI VC Investment by Country (2025)
# ============================================================
print("Generating Chart 3: Investment by Country...")

fig, ax = plt.subplots(figsize=(8, 5.5))

countries = ['Netherlands', 'Sweden', 'Germany', 'France', 'United Kingdom']
# Approximate 2025 VC investment by country (USD billions)
# UK leads, followed by France, Germany, Sweden, Netherlands
country_values = [2.5, 3.0, 3.2, 3.8, 5.5]

colors_country = ['#fde725', '#5ec962', '#21918c', '#3b528b', '#440154']

bars = ax.barh(countries, country_values, color=colors_country, height=0.5,
               edgecolor='white', linewidth=0.5)

# Add value labels
for bar, val in zip(bars, country_values):
    ax.text(val + 0.2, bar.get_y() + bar.get_height()/2,
            f'${val}B', va='center', ha='left', fontsize=10, fontweight='bold', color='#333333')

ax.set_xlabel('VC Investment (USD billions, 2025)', fontsize=12, fontweight='bold')
ax.set_title('European AI VC Investment by Country, 2025',
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlim(0, 7)

add_source_line(ax, 'Source: EU-Startups, "Europe\'s Top AI Funding Rounds 2025"; AI Watch Investment Dashboard. [T3]')

fig.savefig(os.path.join(CHARTS_DIR, 'chart03_investment_by_country.png'), dpi=150, facecolor='white')
plt.close(fig)
print("  -> chart03_investment_by_country.png saved")


# ============================================================
# CHART 4: Source Quality Distribution (Donut Chart)
# ============================================================
print("Generating Chart 4: Source Distribution...")

fig, ax = plt.subplots(figsize=(7, 6))

tiers = ['T1\n(Peer-reviewed)', 'T2\n(Analyst)', 'T3\n(Government)', 'T4\n(News)']
percentages = [3.3, 20.0, 43.3, 36.7]
colors_tiers = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728']
explode = (0.02, 0.02, 0.02, 0.02)

wedges, texts, autotexts = ax.pie(percentages, explode=explode, colors=colors_tiers,
                                   autopct='%1.1f%%', startangle=90, pctdistance=0.78,
                                   wedgeprops=dict(width=0.45, edgecolor='white', linewidth=1.5),
                                   textprops={'fontsize': 10})

# Make percentage text bold and white
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

# Add center text
ax.text(0, 0, 'Source\nQuality', ha='center', va='center', fontsize=12,
        fontweight='bold', color='#333333')

ax.set_title('Source Tier Distribution in Report', fontsize=14, fontweight='bold', pad=15)

# Add legend
legend_labels = [f'{t}: {p}%' for t, p in zip(tiers, percentages)]
ax.legend(wedges, legend_labels, loc='lower right', fontsize=9, frameon=True)

add_source_line(ax, 'Source: Author\'s analysis of 30 cited sources. Corrected from Pass 1 source tier audit.', y=-0.18)

fig.savefig(os.path.join(CHARTS_DIR, 'chart04_source_distribution.png'), dpi=150, facecolor='white')
plt.close(fig)
print("  -> chart04_source_distribution.png saved")

print("\nAll 4 charts generated successfully!")
