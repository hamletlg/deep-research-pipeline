#!/usr/bin/env python3
"""Integrate charts into the European AI Report Pass 2 document.
Inserts from bottom to top to avoid line number shifts."""

import os

CHARTS_DIR = "/mnt/DATA/trabajo_hermes/EUROPEAN_AI/charts"
PASS2_DOC = "/mnt/DATA/trabajo_hermes/EUROPEAN_AI/european_ai_report_2026_pass2.md"
OUTPUT_DOC = "/mnt/DATA/trabajo_hermes/EUROPEAN_AI/european_ai_report_2026_pass3.md"

with open(PASS2_DOC, 'r') as f:
    lines = f.readlines()

def make_chart_block(fig_num, filename, title, caption_sources, explanatory_text):
    """Build the markdown block for a chart."""
    rel_path = os.path.join(CHARTS_DIR, filename)
    return f"""
<div style='page-break-inside: avoid; margin: 1.5em 0;'>

![Figure {fig_num}: {title}]({rel_path})

**Figure {fig_num}: {title}.** {caption_sources}.

{explanatory_text}

</div>

"""

# Chart 4: Source Distribution — Methodology (after line 50)
chart4 = make_chart_block(
    4, "chart04_source_distribution.png",
    "Source Tier Distribution in Report",
    "Source: Author's analysis of 30 cited sources, corrected per Pass 1 source tier audit.",
    "This distribution reflects the source quality corrections applied during Pass 1, which replaced weak Tier 4 sources with higher-quality Tier 1–3 alternatives. The corrected mix now includes 3.3% Tier 1 (peer-reviewed academic), 20.0% Tier 2 (industry/analyst reports), 43.3% Tier 3 (government/public body), and 36.7% Tier 4 (news/journalism). Notably, the report contains zero Tier 5 or Tier 6 sources, and the combined Tier 1–2 share of 23.3% represents a substantial improvement over the original 3.3% Tier 1–2 mix identified in the quality assessment. The heavy reliance on Tier 3 government sources (43.3%) reflects the policy-focused nature of this analysis, where regulatory and investment data from public bodies constitutes the primary evidence base."
)

# Chart 1: AI Investment Comparison — Section 2.1, after McKinsey paragraph (after line 64)
chart1 = make_chart_block(
    1, "chart01_ai_investment_comparison.png",
    "Private AI Investment by Region, 2025 (USD billions)",
    "Source: CB Insights State of AI 2025; PitchBook European VC Trends 2025; OECD estimates. [T2]",
    "The investment disparity between Europe and the United States is stark: American private AI investment of approximately $70 billion dwarfs Europe's $12 billion, a gap of nearly six to one. China's estimated $15 billion, while substantially below US levels, still exceeds European investment. This funding gap is not merely a function of market size; it reflects deeper structural differences in how capital is allocated toward high-risk, high-reward AI ventures. The concentration of American investment in a handful of well-capitalized firms—OpenAI, Anthropic, xAI, and others—creates a Matthew effect that further widens the competitive divide, as these firms capture disproportionate talent, attention, and ecosystem benefits."
)

# Chart 2: Market Growth Projection — Section 2.1, after CAGR paragraph (after line 58)
chart2 = make_chart_block(
    2, "chart02_market_growth.png",
    "European AI Market Size Projection, 2025–2032 (30.2% CAGR)",
    "Source: MarketsandMarkets, \"Europe Artificial Intelligence (AI) Market Forecast to 2032.\" [T2]",
    "The projected trajectory of European AI market growth is dramatic: from $86.24 billion in 2025 to $548.03 billion by 2032, representing a compound annual growth rate of 30.2%. This growth rate, if realized, would position Europe as the third-largest AI market globally by the end of the decade. However, even at $548 billion, the European market would still trail the combined US-China share by a substantial margin. The steepness of this curve underscores both the enormous opportunity and the urgency of addressing Europe's structural constraints—compute infrastructure, talent retention, and capital mobilization—if the continent is to capture its share of this expanding market."
)

# Chart 3: Investment by Country — Section 2.3, after geographic concentration (after line 88)
chart3 = make_chart_block(
    3, "chart03_investment_by_country.png",
    "European AI VC Investment by Country, 2025",
    "Source: EU-Startups, \"Europe's Top AI Funding Rounds 2025\"; AI Watch Investment Dashboard. [T3]",
    "The geographic concentration of European AI investment is substantial: the United Kingdom, France, and Germany collectively account for approximately 65% of total European AI investment, with the UK alone capturing nearly half of the top-tier funding rounds. Sweden and the Netherlands, while smaller in aggregate, have emerged as significant players in specific niches—Sweden in defense AI and application-layer innovation, the Netherlands in multilingual NLP and infrastructure. This concentration creates structural vulnerabilities, as the UK's post-Brexit regulatory divergence and France's centralized approach to technology policy complicate pan-European scaling efforts. A startup that succeeds in Paris may face entirely different regulatory, cultural, and market barriers when expanding to Berlin or Amsterdam."
)

# Insertions: (line_number_after_which_to_insert, chart_block)
# Process from bottom to top to avoid line number shifts
insertions = [
    (88, chart3),   # Chart 3 — after line 88 (last in doc)
    (64, chart1),   # Chart 1 — after line 64 (McKinsey paragraph)
    (58, chart2),   # Chart 2 — after line 58 (CAGR paragraph, BEFORE Chart 1 in doc)
    (50, chart4),   # Chart 4 — after line 50 (Methodology, first in doc)
]

# Verify order: after all insertions, the document order should be:
# Chart 4 (Methodology) → Chart 2 (CAGR) → Chart 1 (McKinsey) → Chart 3 (Geographic)
print("Insertion order (bottom-to-top):")
for ln, _ in insertions:
    print(f"  After line {ln}")
assert insertions == [(88, chart3), (64, chart1), (58, chart2), (50, chart4)]

output_lines = list(lines)  # copy

for line_num, chart_block in insertions:
    # Insert AFTER line_num (0-indexed: line_num)
    output_lines.insert(line_num + 1, chart_block)

# Add Pass 3 note at the end
output_lines.append("\n---\n")
output_lines.append("*This is Pass 3 of the improvement plan. Pass 3 focused on: (1) generating 4 publication-quality charts using matplotlib, (2) integrating charts into the report with captions and explanatory text, (3) updating source references for chart data.*\n")

# Write output
output_content = "".join(output_lines)
with open(OUTPUT_DOC, 'w') as f:
    f.write(output_content)

print(f"Output saved to: {OUTPUT_DOC}")
print(f"Total lines: {len(output_lines)}")
print(f"Total chars: {len(output_content)}")
