# PASS 3 — European AI Report Improvement

## Context

You are continuing the improvement of a research report on "The State of Artificial Intelligence in Europe: A 2026 Report". This is **PASS 3** of a 4-pass improvement plan. Each pass is fully self-contained — you have no context from previous passes. You must read everything provided below and produce a complete, self-contained revised document.

## Files to Read

1. **Current document:** `/mnt/DATA/trabajo_hermes/EUROPEAN_AI/european_ai_report_2026_pass2.md` (the version from Pass 2)
2. **Improvement plan:** `/mnt/DATA/trabajo_hermes/EUROPEAN_AI/improvement_plan.md` (contains the full 4-pass plan with all task details)
3. **Quality assessment:** `/mnt/DATA/trabajo_hermes/EUROPEAN_AI/quality_assessment_report.md` (the assessment that identified issues and improvement recommendations)

## What This Pass Must Do

Read the improvement plan, find the section for **Pass 3**, and execute ALL tasks listed there.

### PASS 3 OBJECTIVES

#### 3.1 Generate Charts

Use Python/matplotlib to generate the following 4 charts. Save each as a PNG file in `/mnt/DATA/trabajo_hermes/EUROPEAN_AI/charts/`:

**Chart 1: AI Investment Comparison by Region (2025)**
- Type: Vertical bar chart
- Data: US private AI investment (~$70B), European private AI investment (~€11B ≈ $12B), China AI investment (~$15B estimate)
- Style: Colorblind-safe palette (viridis or plasma), ascending order, complete axis labels with units
- Title: "Private AI Investment by Region, 2025 (USD billions)"
- Source line below chart with tier labels
- Filename: `chart01_ai_investment_comparison.png`

**Chart 2: European AI Market Growth Projection**
- Type: Line chart
- Data: 2025 ($86.24B), 2026, 2027, 2028, 2029, 2030, 2031, 2032 ($548.03B) at 30.2% CAGR
- Style: Clean line chart, data labels on key points
- Title: "European AI Market Size Projection, 2025-2032"
- Source line below chart
- Filename: `chart02_market_growth.png`

**Chart 3: European AI Investment by Country (2025)**
- Type: Horizontal bar chart
- Data: UK, France, Germany, Sweden, Netherlands (ranked by investment volume)
- Style: Colorblind-safe palette, ascending order
- Title: "European AI VC Investment by Country, 2025"
- Source line below chart
- Filename: `chart03_investment_by_country.png`

**Chart 4: Source Quality Distribution (Donut Chart)**
- Type: Donut chart (max 6 segments)
- Data: Use the corrected tier distribution from Pass 1/Pass 2: T1 (3.3%), T2 (20.0%), T3 (43.3%), T4 (36.7%), T5 (0%), T6 (0%)
- Style: Minimal, colorblind-safe
- Title: "Source Tier Distribution in Report"
- Filename: `chart04_source_distribution.png`

#### 3.2 Integrate Charts into Report

For each chart:
1. Insert the chart image inline at the location indicated below
2. Add a caption: "Figure N: [Descriptive title]. Source: [Source, Year] [Tier]. Notes: [if needed]."
3. Add 2-3 sentences of explanatory text referencing the chart and explaining what it means
4. Place charts near their relevant analysis section

**Chart placement (adapted to current document structure):**
- Chart 1 → Insert in Section 2.1 (Market Size and Growth Trajectory), after the paragraph comparing US vs European investment (after the paragraph citing McKinsey's 45-70% gap finding)
- Chart 2 → Insert in Section 2.1 (Market Size and Growth Trajectory), after the CAGR paragraph (after the MarketsandMarkets projection paragraph)
- Chart 3 → Insert in Section 2.3 (Geographic Distribution), after the paragraph about geographic concentration
- Chart 4 → Insert in Section 1 (Methodology), after the paragraph describing the analytical approach

#### 3.3 Update Source References

For each chart, update the source line to include the correct tier label. If a chart uses data from a source not already in the bibliography, add it to the Sources section.

## Rules

1. **Read the full current document** before making any changes.
2. **Preserve all content from the current document** that you did not explicitly change. The output must be a complete, self-contained document.
3. **Do not invent sources, titles, URLs, or data points.** If you cannot find a source, mark the claim as [UNVERIFIED].
4. **Write in long-form prose** for analytical sections. Use bullets only for comparison tables, prioritized lists, and methodology steps.
5. **Paragraphs must be substantive** — minimum 4-6 sentences each. Maximum 12-15 sentences.
6. **Maintain the existing structure** (headings, sections) but convert content within sections as instructed.
7. **Do not undo changes from previous passes** unless explicitly instructed.
8. **Charts must be publication-quality:** Use matplotlib with clean styling, colorblind-safe palettes (viridis, plasma, Set2), proper axis labels, and source attribution. No cluttered grids or default matplotlib aesthetics.

## Output

Save the complete revised document to: `/mnt/DATA/trabajo_hermes/EUROPEAN_AI/european_ai_report_2026_pass3.md`

At the end of the document, append a note:
*This is Pass 3 of the improvement plan. Pass 3 focused on: (1) generating 4 publication-quality charts using matplotlib, (2) integrating charts into the report with captions and explanatory text, (3) updating source references for chart data.*
