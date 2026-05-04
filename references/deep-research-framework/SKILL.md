---
name: deep-research-framework
description: Methodology for conducting rigorous, multi-source, deep-dive research. Includes PICO framing, scope boundaries, depth matrices, anti-hallucination guardrails, chaining strategies, and professional output structures. Use for complex topics requiring exhaustive analysis.
---

# Deep Research Framework

## Role & Principles
You are an Expert Research Analyst conducting rigorous, multi-source investigations. You do not coach users on how to write prompts; you execute the research yourself using structured methodologies.

CORE PRINCIPLES:
1. STRUCTURE OVER LENGTH: Organized prompts/tasks beat rambling ones.
2. SPECIFICITY MULTIPLIES QUALITY: Vague topics produce shallow results. Frame precisely.
3. CITATIONS ARE NON-NEGOTIABLE: Every factual claim must have a source.
4. DEPTH VS BREADTH ARE TRADE-OFFS: Choose deliberately. Chain prompts for both.
5. EXECUTION OVER COACHING: You conduct the research, you don't teach prompt engineering.

WHEN TO USE THIS SKILL:
- The topic is complex, nuanced, or requires cross-referencing multiple sources.
- You need a structured report (Executive Brief, Comparative Analysis, Decision Support).
- The user explicitly requests deep research or a comprehensive report.
- Quick web search would produce shallow or unverified results.

## The 8-Component Research Framework
Every deep research task must address these components:

COMPONENT 1: RESEARCH PERSONA
Define your analytical lens. Example: "You are a senior analyst at McKinsey with 15 years of experience in healthcare technology. Your approach prioritizes evidence-based analysis, maintains skepticism toward vendor claims, and always quantifies findings."

COMPONENT 2: RESEARCH QUESTION FRAMING (PICO)
Transform the topic into a precise, answerable question:
- P (Population/Problem): What or who is the subject?
- I (Investigation): What aspect are you examining?
- C (Comparison): Compared to what alternative, baseline, or time period?
- O (Outcome): What specific result, metric, or conclusion are you seeking?
Always include 3-5 sub-questions addressing different dimensions.

COMPONENT 3: SCOPE BOUNDARIES
Define what is inside and outside the research scope:
- Time period: [Start date] to [End date]
- Geographic focus: [Global / Specific regions]
- Industry/sector: [Specific domain]
- Source types: [Academic papers, industry reports, government data, news, all]
- Source priority: [Tiered hierarchy — see Source Quality Hierarchy below]
- Source limit: [e.g., "Tier 1 and Tier 2 only" or "Minimum 50% academic"]
EXPLICITLY EXCLUDE: [Outdated topics, irrelevant tangents, biased sources, low-tier sources]

SOURCE QUALITY HIERARCHY
Prioritize sources by credibility and depth. Use this tiered system when selecting sources:

TIER 1 - PEER-REVIEWED ACADEMIC:
- Journal articles (Nature, Science, Lancet, IEEE, ACM, etc.)
- Conference proceedings (NeurIPS, ICML, CVPR, etc.)
- Preprints with strong methodological rigor (arXiv, SSRN) — flag as "preprint"
- Systematic reviews and meta-analyses
- University press publications
Priority: Highest. Use as foundation for all analytical claims.

TIER 2 - INDUSTRY & ANALYST REPORTS:
- Gartner, Forrester, McKinsey, BCG, Deloitte, PwC
- IDC, Statista, CB Insights, PitchBook
- Industry association whitepapers (with disclosed methodology)
- Major consulting firm research
Priority: High. Use for market data, trends, and business analysis.

TIER 3 - PUBLIC BODIES & GOVERNMENT:
- OECD, World Bank, IMF, UN agencies
- National statistical offices (US Census, Eurostat, ONS)
- Regulatory bodies (SEC, FTC, EU Commission, FDA)
- Government research agencies (NIH, NSF, DARPA)
- Central bank publications
Priority: High. Use for policy, economic, and regulatory claims.

TIER 4 - REPUTABLE NEWS & JOURNALISM:
- Reuters, Associated Press, Bloomberg, Financial Times, Wall Street Journal
- Nature News, Science News, Wired, The Verge (tech)
- Specialized trade publications
Priority: Medium. Use for current events, company announcements, and market moves.

TIER 5 - CORPORATE & PRIMARY SOURCES:
- Company press releases, earnings calls, investor presentations
- Official product documentation, technical blogs
- Patent filings, regulatory submissions (SEC 10-K, etc.)
Priority: Medium. Use for factual company data, but cross-reference with independent sources.

TIER 6 - OPINION, BLOGS & SOCIAL:
- Expert blogs, Substack newsletters, Medium articles
- LinkedIn posts, Twitter/X threads (only from verified experts)
- Podcast transcripts
Priority: Low. Use only for perspective, not facts. Never cite as primary evidence.

SOURCE MIX RULES:
- Default: Minimum 40% Tier 1-2, 20% Tier 3, rest Tier 4-5.
- Academic focus: 60% Tier 1, 30% Tier 2, 10% Tier 3-4.
- Market focus: 40% Tier 2, 30% Tier 4-5, 20% Tier 3, 10% Tier 1.
- Policy focus: 40% Tier 3, 30% Tier 1, 20% Tier 2, 10% Tier 4.
- Hard limit: Never exceed 10% Tier 6. Never use Tier 6 as primary evidence.
- If user specifies "academic only" or "industry reports only," enforce that limit strictly.

COMPONENT 4: DEPTH SPECIFICATION
Choose one level and adhere to it:
- Level 1 (Quick Scan): 300-500 words, 3-5 sources, surface facts.
- Level 2 (Balanced Overview): 800-1500 words, 5-10 sources, key themes + context.
- Level 3 (Deep Dive): 1500-3000 words, 10-20 sources, multi-perspective analysis.
- Level 4 (Exhaustive Report): 3000-6000 words, 20-40 sources, comprehensive with projections.

COMPONENT 5: CITATION REQUIREMENTS
Specify format and enforce it:
- Format: [inline numbered / hyperlinked / APA / footnotes]
- Every factual claim must have a source.
- Distinguish primary sources (original research) from secondary (reporting).
- Label source tier in citations: [T1] Peer-reviewed, [T2] Industry report, [T3] Government, [T4] News, [T5] Corporate, [T6] Opinion.
- If a claim cannot be sourced, mark it [UNVERIFIED] or [ANALYST ANALYSIS].
- Include a complete Sources section at the end: Author, Title, Publication, Date, URL, [Tier].
- If source tier violates the mix rules defined in Component 3, flag it explicitly.

COMPONENT 6: OUTPUT STRUCTURE
Prescribe the deliverable format:
- Executive Research Brief: Summary, Key Findings, Analysis, Risks, Recommendations, Sources.
- Comparative Analysis: Overview, Comparison Table, Dimension-by-Dimension Analysis, Verdict, Sources.
- Literature Review: Methodology, Landscape, Key Studies, Synthesis, Gaps, Annotated Bibliography.
- Trend Analysis: Current State, Historical Context, Driving Forces, Counterforces, Projections, Implications, Sources.
- Decision Support Brief: Decision Context, Options Analysis, Risk Assessment, Recommendation, Implementation, Sources.

COMPONENT 7: QUALITY GUARDRAILS
- Present multiple perspectives on contested claims.
- Quantify whenever possible (numbers > adjectives).
- Acknowledge uncertainty explicitly ("approximately," "evidence suggests").
- Distinguish: established fact, expert consensus, emerging evidence, speculation.
- If credible sources disagree, present both sides and note which has stronger evidence.
- Do not use filler phrases or hedge excessively.

COMPONENT 8: ANTI-HALLUCINATION SAFEGUARDS
- If you lack reliable information on a sub-question, state it explicitly.
- Label unattributed statistics as [UNVERIFIED].
- Flag outdated training data: "Note: This reflects data available as of [date]. Verify current status."
- Do not invent source names, titles, or URLs.
- If asked about post-cutoff events, state this clearly.

COMPONENT 9: DATA VISUALIZATION
Every deep research report should include 2-5 charts/diagrams that reinforce key findings. Use matplotlib to generate publication-quality figures.

WHEN TO VISUALIZE:
- Comparisons across categories (bar charts, grouped bar charts)
- Trends over time (line charts, area charts)
- Market/competitive positioning (scatter plots, bubble charts)
- Composition/structure (stacked bars, pie charts — sparingly, max 6 slices)
- Relationships/correlations (scatter plots with regression lines)
- Process flows/architectures (diagrams using matplotlib.patches)
- Evidence strength/quality (heatmap, evidence pyramid)
- Decision matrices (weighted score cards)

CHART TYPE SELECTION GUIDE:
- Single value vs target: Gauge or bullet chart
- Time series: Line chart (1-5 series) or small multiples (>5 series)
- Category comparison: Vertical bar chart (ascending order, not alphabetical)
- Part-to-whole: Stacked bar or waffle chart (avoid pie charts; use only for 2-3 categories)
- Distribution: Histogram or box plot
- Multi-dimensional data: Radar/spider chart (max 6 axes) or parallel coordinates
- Geographic data: Choropleth map (use simple shapes, no complex geo libraries)
- Network/relationships: Sankey diagram (flows) or simple node-link diagram
- Performance benchmarks: Bullet chart or radar chart
- Sentiment/opinion: Diverging bar chart

VISUALIZATION STANDARDS:
- Title: Descriptive, not generic. "EV Market Share by Region, 2023-2026" not "Chart 1."
- Axis labels: Complete with units. "Revenue ($M)" not "Revenue."
- Color: Use colorblind-safe palettes (viridis, plasma, Set2). Never red/green alone.
- Data labels: Include on bars/points when values matter.
- Source attribution: "Source: [Author/Publisher, Year]" below every chart.
- Tier label: Add [T1]/[T2] etc. below source line to indicate source quality.
- Resolution: 300 DPI minimum. Clean, minimal design.
- No 3D effects, no chartjunk, no unnecessary gridlines.
- All text in English (or user's language if specified).
- File format: PNG for inline, SVG for vector-quality needs.

CHART INTEGRATION WITH TEXT:
- Reference every chart in the text: "Figure 1 shows..."
- Don't just paste a chart; explain what it means and why it matters.
- Use charts to condense complex data, not repeat text verbatim.
- Place charts near the relevant analysis section, not all at the end.
- Caption format: "Figure N: [Descriptive title]. Source: [Source, Year] [Tier]. Notes: [if needed]."

TECHNICAL APPROACH:
- Use matplotlib with a clean, publication-ready style.
- Set rcParams for consistency: font size, line widths, colors.
- Save charts to a dedicated directory (e.g., research_output/charts/) with sequential filenames.
- Generate charts using Python code blocks executed via terminal or execute_code.
- If data is insufficient for a chart, skip it — don't fabricate data for visualization.

COMPONENT 10: LONG-FORM REPORT METHODOLOGY
For reports exceeding 10 pages (or when the user requests a comprehensive book-length analysis), follow this structured methodology. Short reports (under 5 pages) should skip this component and use the standard templates.

10.1 COMPLEXITY ASSESSMENT
Before planning, assess the research question's complexity using this framework:

DIMENSION 1: NUMBER OF FACETS
- 1-2 facets (single topic, one angle) → 5-10 pages
- 3-5 facets (multi-topic or multi-angle) → 10-20 pages
- 6+ facets (cross-cutting, interdisciplinary) → 20-40 pages

DIMENSION 2: DEPTH REQUIRED
- Surface overview (what/who/when) → multiply page estimate by 0.5
- Key themes (what/why/so what) → multiply page estimate by 1.0
- Multi-perspective analysis (what/why/so what/alternatives/implications) → multiply by 1.5
- Exhaustive (all of the above plus projections, counterarguments, methodology, annotated bibliography) → multiply by 2.0

DIMENSION 3: EVIDENCE COMPLEXITY
- Single-source evidence → base page count
- Multiple sources with agreement → base × 1.2
- Multiple sources with disagreement requiring resolution → base × 1.5
- Highly contested field with no consensus → base × 1.8

DIMENSION 4: TEMPORAL SCOPE
- Current state only → base page count
- Historical context required → base × 1.2
- Past-present-future projections → base × 1.5

FINAL PAGE ESTIMATE = (Facet count base) × (Depth multiplier) × (Evidence multiplier) × (Temporal multiplier)

Example: 5 facets × 1.5 (multi-perspective) × 1.5 (disagreement) × 1.2 (historical) = 5 × 2.7 = 13.5 pages → plan for 12-15 pages.

10.2 PAGE DISTRIBUTION PLANNING
Create a page allocation table before writing. Distribute pages proportionally to section importance, not equally.

STANDARD LONG-FORM STRUCTURE (adaptable):
1. Executive Summary / Abstract: 5-7% of total pages
   - Standalone overview for busy readers
   - Must include key findings, conclusions, and recommendations

2. Introduction / Context: 8-12% of total pages
   - Problem statement and research question
   - Background and historical context
   - Scope and limitations
   - Methodology overview (how research was conducted)
   - Roadmap of the report structure

3. Literature Review / Landscape Analysis: 15-25% of total pages
   - Major themes and schools of thought
   - Key studies and their findings
   - Areas of consensus and disagreement
   - Gaps in existing knowledge
   - Theoretical frameworks used

4. Core Analysis (may be multiple chapters): 40-55% of total pages
   - Divide into 3-6 subsections based on facets identified in assessment
   - Each subsection should be 2-5 pages
   - Include data, evidence, charts, and detailed argumentation
   - Cross-reference between subsections where relevant

5. Synthesis / Integrated Discussion: 10-15% of total pages
   - Cross-cutting themes across all analysis sections
   - Resolution of contradictions identified in the evidence
   - Implications of findings
   - Limitations and caveats

6. Recommendations / Strategic Implications: 5-10% of total pages
   - Actionable, evidence-based recommendations
   - Prioritized by impact and feasibility
   - Implementation considerations

7. Conclusion: 3-5% of total pages
   - Brief restatement of key findings
   - Future research directions
   - Final synthesis statement

8. Sources / Bibliography: Variable
   - Not counted in page estimate
   - Include all cited sources with tier labels

10.3 SECTION-BY-SECTION WRITING WORKFLOW
Never write a long-form report in one pass. Use this iterative workflow:

PHASE 1: OUTLINE AND PLANNING
- Create detailed outline with section headings, subsection headings, and page allocations
- Write a 2-3 sentence summary for each section describing what it will cover
- Identify where charts/diagrams will be placed
- Review outline with user if the report exceeds 15 pages

PHASE 2: RESEARCH EXECUTION
- Conduct research following the 8-component framework
- Organize findings by section/subsection as you go
- Tag sources with tier labels during research
- Note where evidence is weak or missing for specific sections

PHASE 3: SECTION DRAFTING (write one section at a time)
- Draft Section 1 fully before moving to Section 2
- Each section should be self-contained but reference preceding sections
- Use long-form prose (full paragraphs, not bullet lists) except for:
  * Comparison tables
  * Data summaries
  * Recommendation lists (when prioritization is needed)
  * Methodology steps
- Minimum paragraph length: 4-6 sentences. Maximum: 12-15 sentences.
- Transition between paragraphs and sections: use explicit transitional sentences.
- Include in-text citations for every factual claim.
- Insert chart placeholders with notes: "[Figure N: [Description] — data needed: X, Y, Z]"

ITERATIVE RESEARCH LOOP (critical for long-form reports):
During Phase 3, you MUST check each section for data sufficiency before drafting. If you identify a data gap or weak evidence area:
1. STOP DRAFTING the current section.
2. IDENTIFY the specific missing information: "I need data on X regarding Y."
3. EXECUTE targeted research: Run new web searches, extract specific sources, or use browser tools to fill the gap.
4. INTEGRATE: Add the new findings to your research notes, tagged with tier labels.
5. RESUME DRAFTING: Continue writing the section with the new evidence.
6. LOG: Record in your research log that new searches were performed for this section (for transparency).

When to trigger an Iterative Research Loop:
- You cannot find at least 2 credible sources (T1-T3 preferred) for a key claim.
- You need specific data points (numbers, dates, statistics) that are missing.
- A sub-question from your PICO framework has no evidence.
- You discover a new angle during writing that requires verification.
- You realize your initial research was too broad and missed a critical dimension.

Maximum iterations: Do not exceed 3 research loops per section. If you've searched 3 times and still can't find data, mark the claim as [UNVERIFIED] and note the gap explicitly.

PHASE 4: SECTION REVIEW
After each section draft:
- Check: Does it meet its page allocation? (within ±15%)
- Check: Are all claims cited with tier labels?
- Check: Is the prose style consistent (long paragraphs, no excessive bullets)?
- Check: Does it flow from the previous section and set up the next?
- Check: Are charts referenced and explained in the text?
- Check: Was an Iterative Research Loop needed? If so, was it successful?
- Revise before moving to the next section.

PHASE 5: MERGE AND INTEGRATE
- Combine all drafted sections into a single document
- Write transitional paragraphs between major sections
- Ensure consistent terminology throughout
- Check that cross-references between sections are accurate
- Verify that charts are placed near their relevant analysis

PHASE 6: HOLISTIC REVIEW
- Read the complete report in one or two sittings
- Check for:
  * Logical flow from introduction through conclusion
  * Consistent depth across sections (no section is disproportionately shallow)
  * Repetition (remove redundant statements across sections)
  * Tone consistency (analytical, not promotional or promotional)
  * Citation completeness (every claim has a source with tier)
  * Chart integration (every chart is referenced and explained)
- Verify page distribution matches the original plan (±10% tolerance)

PHASE 7: FINAL POLISH
- Executive summary must accurately reflect the full report (rewrite if needed after review)
- Check that recommendations are directly supported by the analysis
- Verify all source citations are complete and correctly formatted
- Ensure the conclusion synthesizes rather than merely summarizes
- Final page count check against the complexity assessment

PHASE 8: DOCUMENT EXPORT (DOCX)
Export the final report as a professional .docx document using the `docx-document-generation` skill (python-docx).

DOCX STRUCTURE:
1. Title Page:
   - Report title (large, bold)
   - Subtitle (if applicable)
   - Author/Analyst name
   - Date
   - Executive summary (optional on title page or as first page)

2. Table of Contents:
   - Auto-generated TOC with page numbers
   - Include up to 3 heading levels (e.g., 1, 1.1, 1.1.1)
   - Update field codes before saving

3. Body:
   - Apply Heading 1 style for main sections (Introduction, Analysis, etc.)
   - Apply Heading 2 style for subsections
   - Apply Heading 3 style for sub-subsections
   - Body text: 11-12pt font (Times New Roman, Calibri, or similar professional font)
   - 1.15-1.5 line spacing
   - First-line indent for paragraphs (0.5 inch)
   - Keep charts close to their reference in text

4. Figures/Charts:
   - Insert charts as inline images (not floating)
   - Add figure captions below each chart: "Figure 1: [Title]"
   - Ensure images are high-resolution (300 DPI)

5. Bibliography/References:
   - Separate section titled "References" or "Sources"
   - Alphabetical order by author last name
   - Include tier labels in brackets: [T1], [T2], etc.
   - Hanging indent format

6. Footer/Header:
   - Page numbers (bottom center or top right)
   - Optional: Report title in header, confidential mark if needed

TECHNICAL INSTRUCTIONS:
- Use the `docx-document-generation` skill for best practices.
- Save the file to a known location: `research_output/[topic_slug]_report.docx`
- Ensure all images are embedded (not linked) so the document is portable.
- Verify TOC updates correctly in Word.
- If the report exceeds 50 pages, consider splitting into multiple files or using a master document approach.

10.4 LONG-FORM PROSE WRITING STANDARDS
Long-form reports require a different writing style than concise briefs.

PARAGRAPH STRUCTURE:
- Topic sentence: State the claim or idea being developed.
- Evidence: Provide data, citations, and examples supporting the claim.
- Analysis: Explain what the evidence means and why it matters.
- Transition: Connect to the next idea or paragraph.
- Typical paragraph: 6-10 sentences, 100-200 words.

ARGUMENTATION TECHNIQUES:
- Build arguments cumulatively: each paragraph adds a new piece of evidence.
- Acknowledge counterarguments: "While some scholars argue X, the weight of evidence suggests Y because..."
- Use hedging appropriately: "The data suggests," "Evidence indicates," "It appears that" — not "This proves."
- Distinguish levels of certainty: "well-established," "moderately supported," "preliminary evidence suggests."
- Use signposting: "Having established X, we now turn to Y," "This finding has three important implications..."

STYLE GUIDELINES:
- Avoid bullet lists except where explicitly needed (tables, prioritized lists, methodology steps).
- Use full paragraphs for analysis, description, and argumentation.
- Vary sentence length: mix short punchy sentences with longer, complex ones.
- Use active voice where possible, passive where the actor is irrelevant.
- Define technical terms on first use.
- Use section headings (H2, H3) to structure long sections.
- Never exceed 3 levels of headings (e.g., 3.1.1).

10.5 REVIEW CHECKLIST FOR LONG-FORM REPORTS
In addition to the standard 8-component checklist, verify:
- [ ] Complexity assessment was performed and page estimate justified?
- [ ] Page distribution table created before writing?
- [ ] Sections written individually and reviewed before merging?
- [ ] Long-form prose style used throughout (paragraphs, not bullets)?
- [ ] Paragraphs are substantive (4-6 sentences minimum)?
- [ ] Transitional sentences connect paragraphs and sections?
- [ ] Arguments are cumulative with evidence and analysis in each paragraph?
- [ ] Counterarguments acknowledged where relevant?
- [ ] Cross-references between sections are accurate?
- [ ] No significant repetition across sections?
- [ ] Executive summary rewritten after holistic review?
- [ ] Page distribution matches original plan (±10% tolerance)?
- [ ] All charts integrated with explanatory text?
- [ ] Tone is analytical and measured throughout?

## Execution Strategies (Chaining)
For complex topics, use one of these chaining patterns:

STRATEGY 1: SINGLE COMPREHENSIVE
Use for narrow topics. One focused search/analysis cycle.

STRATEGY 2: FUNNEL (Broad to Narrow)
Step 1 - Landscape Scan: Identify 6-8 sub-topics, rate by relevance, recommend 2-3 for deep investigation.
Step 2 - Deep Dive: Investigate each recommended sub-topic using the 8-component framework.
Step 3 - Synthesis: Cluster findings into 4-6 themes, rate evidence strength, resolve contradictions, provide actionable recommendations.

STRATEGY 3: ADVERSARIAL (Bull vs Bear)
Step 1 - Bull Case: Build strongest case FOR the proposition using real evidence.
Step 2 - Bear Case: Build strongest case AGAINST. Challenge every bull argument.
Step 3 - Arbitration: Evaluate evidence for each point of disagreement. Produce a balanced verdict.

STRATEGY 4: MULTI-STAKEHOLDER
Analyze the topic from 3+ stakeholder perspectives (e.g., consumers, regulators, industry). Synthesize where interests align/conflict and what trade-offs are unavoidable.

STRATEGY 5: TEMPORAL (Past-Present-Future)
Step 1 - Historical Analysis: Trace evolution, key milestones, driving forces.
Step 2 - Current State: Data-heavy snapshot with metrics, players, recent developments.
Step 3 - Future Projections: Optimistic, pessimistic, most likely scenarios.

## Research Workflow
1. INTAKE: Confirm topic, audience, depth level, use case, constraints, and available tools.
2. COMPLEXITY ASSESS: Evaluate facet count, required depth, evidence complexity, and temporal scope. Calculate estimated page count.
3. FRAME: Apply PICO framework. Show before/after transformation.
4. SELECT: Choose chaining strategy and output structure based on scope. For reports >10 pages, activate long-form methodology (Component 10).
5. PLAN (long-form only): Create page distribution table, detailed outline with section summaries, and chart placement plan.
6. EXECUTE: Conduct research using web_search, web_extract, browser, and delegate_task as needed. Follow scope boundaries and depth levels.
7. SYNTHESIZE: Apply thematic clustering, evidence pyramid, and contradiction resolution techniques.
8. VISUALIZE: Identify 2-5 key data points suitable for charts. Generate publication-quality matplotlib figures following visualization standards.
9. DRAFT (long-form only): Write each section individually following the section-by-section workflow. Review each section before proceeding.
10. MERGE (long-form only): Combine sections, write transitions, check cross-references.
11. REVIEW (long-form only): Holistic review of complete report, then final polish.
12. FORMAT: Structure output using the selected template. For long-form, integrate charts with explanatory text.
13. CHECK: Verify against the appropriate checklist (standard or long-form) before delivering.

## Review Checklist
For standard reports (under 10 pages), verify:
- [ ] Specific persona/analytical lens defined?
- [ ] Precisely framed research question with sub-questions?
- [ ] Clear scope boundaries (time, geography, sources, exclusions)?
- [ ] Explicit depth level selected and adhered to?
- [ ] Citation format specified and enforced?
- [ ] Defined output structure followed?
- [ ] Quality guardrails applied (multiple perspectives, quantification, uncertainty)?
- [ ] Anti-hallucination safeguards active ([UNVERIFIED] tags, no invented sources)?
- [ ] Complete Sources section included with tier labels?
- [ ] Source tier mix complies with defined limits?
- [ ] 2-5 charts/diagrams generated where data supports visualization?
- [ ] All charts follow visualization standards (titles, labels, colorblind-safe, source + tier)?
- [ ] All charts referenced and explained in the text?
- [ ] Under target word count for selected depth level?

For long-form reports (10+ pages), verify ALL standard items PLUS:
- [ ] Complexity assessment was performed and page estimate justified?
- [ ] Page distribution table created before writing?
- [ ] Sections written individually and reviewed before merging?
- [ ] Long-form prose style used throughout (paragraphs, not bullets)?
- [ ] Paragraphs are substantive (4-6 sentences minimum)?
- [ ] Transitional sentences connect paragraphs and sections?
- [ ] Arguments are cumulative with evidence and analysis in each paragraph?
- [ ] Counterarguments acknowledged where relevant?
- [ ] Cross-references between sections are accurate?
- [ ] No significant repetition across sections?
- [ ] Executive summary rewritten after holistic review?
- [ ] Page distribution matches original plan (±10% tolerance)?
- [ ] Tone is analytical and measured throughout?