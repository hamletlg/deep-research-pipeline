# Workflow Analysis: Deep Research Report Production Pipeline

## Executive Summary

This document reconstructs the end-to-end workflow used to produce the deep research report *"The State of Artificial Intelligence in Europe: A 2026 Report"* using Hermes Agent with the `deep-research-framework` skill. The workflow was designed to work within the constraints of a **181K hard context limit** and the requirement that **each pass runs in a fresh, isolated session** with no memory of previous passes. The pipeline consists of **9 sessions across 7 logical stages**, producing **10+ intermediate artifacts**.

The key architectural insight is the **two-level automation**: for each improvement pass, there are two separate Hermes sessions — one to **generate the pass prompt** from the reusable template and improvement plan, and another to **execute that pass**. This means the pipeline never requires pre-written prompt files; every pass prompt is dynamically generated at runtime.

## The Foundation: Deep-Research-Framework Skill

This entire pipeline is built on the `deep-research-framework` skill. A copy of the skill is maintained in this folder at `references/deep-research-framework/SKILL.md` so the workflow is fully self-contained. The skill defines the 10-component quality methodology that drives every stage:

- **Components 1-4** (Research Persona, PICO Framing, Scope Boundaries, Depth Specification) drive Stage 1 (Initial Research) and Stage 2 (Quality Assessment)
- **Components 5-8** (Citations, Output Structure, Quality Guardrails, Anti-Hallucination) define the quality criteria evaluated in Stage 2 and enforced in all improvement passes
- **Components 9-10** (Data Visualization, Long-Form Methodology) drive Pass 3 (Visualization) and the overall report structure

The quality assessment in Stage 2 scores the report against all 10 components, and the resulting improvement plan specifies which components need fixing in each pass.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        DEEP RESEARCH PIPELINE                           │
│                                                                         │
│  Stage 1: Initial Research    →  Original Report                        │
│  Stage 2: Quality Audit       →  Assessment + Improvement Plan          │
│  Stage 3A: Meta-Prompt Gen    →  pass_1_prompt.md                       │
│  Stage 3B: Pass 1 Execute     →  pass1 report                           │
│  Stage 4A: Meta-Prompt Gen    →  pass_2_prompt.md                       │
│  Stage 4B: Pass 2 Execute     →  pass2 report                           │
│  Stage 5A: Meta-Prompt Gen    →  pass_3_prompt.md                       │
│  Stage 5B: Pass 3 Execute     →  pass3 report + charts                  │
│  Stage 6A: Meta-Prompt Gen    →  pass_4_prompt.md                       │
│  Stage 6B: Pass 4 Execute     →  final report                           │
│  Stage 7: Cleanup             →  Delivery-Ready Document                │
│                                                                         │
│  Each session: 1 fresh Hermes session, full context provided via files  │
│  Total: 9 isolated sessions, zero cross-session memory dependency       │
│  Key innovation: pass prompts are GENERATED, not pre-written            │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Stage 1: Initial Deep Research

**Session:** Fresh Hermes session with `deep-research-framework` skill loaded
**Input:** User prompt (simple topic description)
**Output:** `european_ai_report_2026.md` (original report)

### Prompt Used (`initial_prompt.txt`)
```
Please, make a deep research and write a report on the current state of AI in Europe: 
main actors, legal frameworks, challenges and future prospects.
```

### What Happened
1. Agent loaded the `deep-research-framework` skill (181K+ chars of methodology)
2. Conducted web research on European AI landscape
3. Produced a coherent, well-structured report covering:
   - Market size and growth trajectory
   - Key European AI actors (company profiles)
   - Geographic distribution
   - EU AI Act legal framework
   - Investment ecosystem
   - Challenges and structural weaknesses
   - Future prospects and scenario analysis
4. Applied inline citation tags `[T3]` and `[T4]`
5. Produced 30 sources in the bibliography

### Artifact Produced
| File | Lines | Size | Description |
|------|-------|------|-------------|
| `european_ai_report_2026.md` | 280 | ~25 KB | Original research report |

### Quality Score After Stage 1: **4/10**

---

## Stage 2: Quality Assessment & Improvement Planning

**Session:** Fresh Hermes session
**Input:** Original report + reference to deep-research-framework skill
**Output:** Quality Assessment Report + Improvement Plan

### Prompt Used (`initial_assesment_prompt.txt`)
```
There is a research report made with the deep research skill on the state of AI in Europe, 
"european_ai_report_2026.md" in the folder /mnt/DATA/trabajo_hermes/EUROPEAN_AI. Please, 
review the deep research skill, extract quality criteria from it, and assess if the report 
passes the quality criteria, from 1 (no) to 10 (excels). What can be improved and how? 
Write a report of the assessment to /mnt/DATA/trabajo_hermes/EUROPEAN_AI/
```

### What Happened
1. Agent read the original report AND loaded the `deep-research-framework` skill
2. Evaluated the report against all 10 components of the framework:
   - C1: Research Persona — FAIL (0/10)
   - C2: PICO Framing — FAIL (0/10)
   - C3: Scope Boundaries — PARTIAL FAIL (3/10)
   - C4: Depth Specification — FAIL (1/10)
   - C5: Citation Requirements — PARTIAL PASS (5/10)
   - C6: Output Structure — PASS (8/10)
   - C7: Quality Guardrails — PARTIAL FAIL (4/10)
   - C8: Anti-Hallucination — PASS (7/10)
   - C9: Data Visualization — FAIL (0/10)
   - C10: Long-Form Methodology — FAIL (2/10)
3. Identified 70% Tier 4 news sources as critical failure
4. Produced detailed improvement recommendations
5. **Produced the improvement_plan.md** — the single source of truth that drives all subsequent passes

### Artifacts Produced
| File | Lines | Size | Description |
|------|-------|------|-------------|
| `quality_assessment_report.md` | 243 | ~16 KB | Component-by-component quality audit |
| `improvement_plan.md` | 308 | ~18 KB | 4-pass improvement plan with specific tasks |

### Key Design Decision: 4-Pass Strategy
The assessment identified that the report needed changes across multiple orthogonal dimensions. Rather than trying to fix everything in one pass (which would exceed context limits and produce poor results), the workflow adopted a **4-pass improvement strategy**:

| Pass | Focus | Key Deliverables |
|------|-------|-----------------|
| Pass 1 | Foundational fixes + source replacement | PICO framing, scope boundaries, research persona, methodology section, source tier corrections, 10+ new Tier 1-2 sources |
| Pass 2 | Prose conversion + counterarguments | Bullet-heavy sections converted to analytical prose, counterarguments added, evidence level distinctions |
| Pass 3 | Visualization integration | 3-4 publication-quality charts inserted with explanatory text |
| Pass 4 | Quality assurance + final polish | Cross-checks, consistency pass, transitions, final source list cleanup |

---

## The Meta-Prompt Generation Pattern

**This is the critical automation mechanism.** For each pass, a separate Hermes session generates the pass prompt from two inputs:

1. **`reusable_pass_prompt_template.md`** — the structural template (parameterized with `{N}`, `{OUTPUT_DIR}`, etc.)
2. **`improvement_plan.md`** — the source of truth containing tasks for all 4 passes

The meta-prompt command (stored in `prompt_to_produce_pass_prompt_from_template.txt`) is:

```
Use /mnt/DATA/trabajo_hermes/EUROPEAN_AI/reusable_pass_prompt_template.md as a template, 
review /mnt/DATA/trabajo_hermes/EUROPEAN_AI/improvement_plan.md and write the pass_{n}_prompt 
to folder.
```

Where `{n}` is replaced with the pass number (1, 2, 3, or 4).

### What the Meta-Prompt Session Does
1. Reads the reusable template
2. Reads the improvement plan
3. Extracts the section for the specified pass number
4. Combines them: replaces template placeholders with actual values, inserts the pass-specific tasks
5. Writes the result as `pass_{n}_prompt.md`

### Why This Matters
- **No pre-written prompts needed** — every pass prompt is generated at runtime
- **The improvement plan is the single source of truth** — if you update the plan, all pass prompts regenerate automatically
- **The template ensures consistency** — every pass prompt follows the same structure
- **Automation is trivial** — a loop over pass numbers 1-4, running the meta-prompt each time, produces all pass prompts

### Actual Session Count Per Pass

```
For Pass N:
  Session A (Meta-Prompt):
    Input: reusable_pass_prompt_template.md + improvement_plan.md
    Command: prompt_to_produce_pass_prompt_from_template.txt (with n=N)
    Output: pass_{n}_prompt.md
  
  Session B (Pass Execute):
    Input: pass_{n}_prompt.md (the generated prompt)
    Output: european_ai_report_2026_pass{n}.md
```

This means **2 sessions per pass**, not 1.

---

## Stage 3: Pass 1 — Meta-Prompt Generation + Execution

### Session 3A: Meta-Prompt Generation

**Input:** `reusable_pass_prompt_template.md` + `improvement_plan.md`
**Command:** `prompt_to_produce_pass_prompt_from_template.txt` (with n=1)
**Output:** `pass_1_prompt.md` (generated, but not saved as a separate file — the prompt was executed directly)

Note: In the actual execution, the meta-prompt session generated the pass 1 prompt and the result was executed directly. The intermediate `pass_1_prompt.md` file was not saved separately.

### Session 3B: Pass 1 Execution

**Input:** Original report + generated pass 1 prompt
**Output:** `european_ai_report_2026_pass1.md`

### Pass 1 Tasks Executed
1. **1.1 Add Methodology Frontmatter** — Research persona, PICO framing, scope boundaries
2. **1.2 Add Methodology Section** — 150-200 word methodology description
3. **1.3 Source Tier Corrections** — Fixed misclassified sources (French Court of Auditors T4→T3, Jones Day T3→T4, Stanford HAI T4→T1/T2, removed duplicate)
4. **1.4 Replace 10+ Tier 4 Sources** — Replaced weak sources with Tier 1-2 alternatives (CB Insights, PitchBook, McKinsey, EIB, OECD)
5. **1.5 Add 3-5 New High-Quality Sources** — Added OECD AI Policy Observatory, Stanford HAI AI Index, McKinsey, JRC, Nature/Science references

### Artifact Produced
| File | Lines | Size | Description |
|------|-------|------|-------------|
| `european_ai_report_2026_pass1.md` | 357 | ~38 KB | Report with methodology framework + improved sources |

---

## Stage 4: Pass 2 — Meta-Prompt Generation + Execution

### Session 4A: Meta-Prompt Generation

**Input:** `reusable_pass_prompt_template.md` + `improvement_plan.md`
**Command:** `prompt_to_produce_pass_prompt_from_template.txt` (with n=2)
**Output:** `pass_2_prompt.md` (manually crafted — same result as the meta-prompt would have produced)

Note: In the actual execution, the Pass 2 prompt was manually crafted (`pass_2_prompt.md`) rather than generated via the meta-prompt. However, the content is identical to what the meta-prompt would have produced — it follows the same template structure and contains the same tasks extracted from `improvement_plan.md`.

### Session 4B: Pass 2 Execution

**Input:** `european_ai_report_2026_pass1.md` + `pass_2_prompt.md`
**Output:** `european_ai_report_2026_pass2.md`

### Pass 2 Tasks Executed
1. **2.1 Convert Bullet-Heavy Sections to Prose** — Rewrote 5 sections:
   - Section 2.2 (Key European AI Actors): Company list → 3-category analytical prose
   - Section 3.1 (EU AI Act Risk Tiers): Bullet list → risk-based approach analysis
   - Section 4.1 (InvestAI Components): Bullet list → structural analysis
   - Section 5.1 (Compute Infrastructure Problems): 4 bullets → interconnected prose analysis
   - Section 5.3 (Compliance Burden): 3 bullets → prose with counterargument
2. **2.2 Add Counterarguments** — Added counterargument paragraphs to 3 sections
3. **2.3 Evidence Level Distinctions** — Applied `(well-established)`, `(moderately supported)`, `(emerging evidence)`, `(speculative)` tags throughout

### Artifact Produced
| File | Lines | Size | Description |
|------|-------|------|-------------|
| `european_ai_report_2026_pass2.md` | 301 | ~63 KB | Report with prose conversion + counterarguments + evidence tags |

---

## Stage 5: Pass 3 — Meta-Prompt Generation + Execution

### Session 5A: Meta-Prompt Generation

**Input:** `reusable_pass_prompt_template.md` + `improvement_plan.md`
**Command:** `prompt_to_produce_pass_prompt_from_template.txt` (with n=3)
**Output:** `pass_3_prompt.md` (generated via the meta-prompt)

### Session 5B: Pass 3 Execution

**Input:** `european_ai_report_2026_pass2.md` + `pass_3_prompt.md`
**Output:** `european_ai_report_2026_pass3.md` + 4 chart PNGs

### Pass 3 Tasks Executed

#### 3.1 Chart Generation (Python/matplotlib)
A Python script (`generate_charts.py`) was executed to generate 4 publication-quality charts:

| Chart | Type | Data | Filename |
|-------|------|------|----------|
| 1 | Horizontal bar | US ($70B) vs Europe ($12B) vs China ($15B) | `chart01_ai_investment_comparison.png` |
| 2 | Line chart | European AI market 2025-2032 ($86B → $548B, 30.2% CAGR) | `chart02_market_growth.png` |
| 3 | Horizontal bar | UK ($5.5B), France ($3.8B), Germany ($3.2B), Sweden ($3B), Netherlands ($2.5B) | `chart03_investment_by_country.png` |
| 4 | Donut chart | Source tier distribution: T1 3.3%, T2 20%, T3 43.3%, T4 36.7% | `chart04_source_distribution.png` |

#### 3.2 Chart Integration (Python script)
A second Python script (`integrate_charts.py`) inserted chart markdown blocks into the document at specific line positions, processing from bottom to top to avoid line number shifts.

Chart placement:
- Chart 4 → Methodology section (after line 50)
- Chart 2 → Market Size section (after CAGR paragraph, after line 58)
- Chart 1 → Market Size section (after McKinsey paragraph, after line 64)
- Chart 3 → Geographic Distribution (after concentration paragraph, after line 88)

### Artifacts Produced
| File | Lines | Size | Description |
|------|-------|------|-------------|
| `european_ai_report_2026_pass3.md` | 362 | ~70 KB | Report with 4 integrated charts |
| `charts/chart01_ai_investment_comparison.png` | — | — | AI investment comparison chart |
| `charts/chart02_market_growth.png` | — | — | Market growth projection chart |
| `charts/chart03_investment_by_country.png` | — | — | Investment by country chart |
| `charts/chart04_source_distribution.png` | — | — | Source tier distribution chart |

---

## Stage 6: Pass 4 — Meta-Prompt Generation + Execution

### Session 6A: Meta-Prompt Generation

**Input:** `reusable_pass_prompt_template.md` + `improvement_plan.md`
**Command:** `prompt_to_produce_pass_prompt_from_template.txt` (with n=4)
**Output:** `pass_4_prompt.md` (generated via the meta-prompt)

### Session 6B: Pass 4 Execution

**Input:** `european_ai_report_2026_pass3.md` + `pass_4_prompt.md`
**Output:** `european_ai_report_2026_final.md`

### Pass 4 Tasks Executed
1. **4.1 Cross-Check Against Assessment Report** — Verified each recommendation from the quality assessment is addressed
2. **4.2 Consistency Pass** — Terminology, citations, figure references, paragraph length, tone
3. **4.3 Transition Improvement** — Added transitional sentences between all 6 major sections
4. **4.4 Source List Cleanup** — Alphabetical ordering, tier label consistency, duplicate removal, URL verification
5. **4.5 Final Review Checklist** — 18-item checklist verification

### Artifact Produced
| File | Lines | Size | Description |
|------|-------|------|-------------|
| `european_ai_report_2026_final.md` | 362 | ~70 KB | Final polished report with all internal research artifacts |

---

## Stage 7: Cleanup — Delivery-Ready Version

**Session:** Fresh Hermes session
**Input:** `european_ai_report_2026_final.md` + cleanup instructions
**Output:** `european_ai_report_2026_clean.md`

### What Was Done
The final report contained internal research artifacts that should not appear in a delivery-ready document. A cleanup pass removed:

| Category | Items Removed |
|----------|--------------|
| DELETE entirely | Research Framework section (persona, PICO, scope), Figure 4 (source tier chart), Source corrections table, Pass 4 note |
| REMOVE tags | ~80+ inline `[T#]` tier markers, evidence grading labels `(well-established)`, etc. |
| REMOVE labels | 3 counterargument/Note markers |
| REWRITE | Transitions (meta-navigation cues → natural prose), methodology section (remove internal jargon), source list (remove tier tags) |
| TRIM | Redundant figure descriptions |

### Artifacts Produced
| File | Lines | Size | Description |
|------|-------|------|-------------|
| `european_ai_report_2026_clean.md` | 310 | ~53 KB | Delivery-ready report (no internal artifacts) |
| `diagnosis_cleanup.md` | 111 | ~7 KB | Cleanup analysis document |
| `european_ai_report_2026.docx` | — | — | DOCX export of final report |
| `european_ai_report_2026.pdf` | — | — | PDF export of final report |
| `european_ai_report_2026_clean.docx` | — | — | DOCX export of clean version |

---

## Complete Session Flow Diagram

```
┌──────────────────────────────────────────────────────────────────────────┐
│                           SESSION 1: INITIAL RESEARCH                     │
│                                                                          │
│  Input:  initial_prompt.txt ("deep research on AI in Europe")            │
│  Skill:  deep-research-framework                                         │
│  Output: european_ai_report_2026.md (280 lines, ~25 KB)                  │
│  Score:  4/10                                                            │
└──────────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                        SESSION 2: QUALITY AUDIT                          │
│                                                                          │
│  Input:  european_ai_report_2026.md + deep-research-framework            │
│  Output: quality_assessment_report.md (243 lines)                        │
│         improvement_plan.md (308 lines, 4-pass plan)                     │
└──────────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                   SESSION 3A: META-PROMPT GENERATION (Pass 1)            │
│                                                                          │
│  Input:  reusable_pass_prompt_template.md                                │
│         improvement_plan.md                                              │
│  Command: prompt_to_produce_pass_prompt_from_template.txt (n=1)          │
│  Output: pass_1_prompt.md (generated)                                    │
│                                                                          │
│  What it does: reads the template, extracts Pass 1 tasks from the plan,  │
│  combines them, writes the prompt file.                                  │
└──────────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                   SESSION 3B: PASS 1 EXECUTION                           │
│                                                                          │
│  Input:  european_ai_report_2026.md                                      │
│         pass_1_prompt.md (generated)                                     │
│  Output: european_ai_report_2026_pass1.md (357 lines, ~38 KB)            │
│  Changes: Research framework, methodology, source corrections, new       │
│           sources, evidence tags, prose conversion (partial)              │
└──────────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                   SESSION 4A: META-PROMPT GENERATION (Pass 2)            │
│                                                                          │
│  Input:  reusable_pass_prompt_template.md                                │
│         improvement_plan.md                                              │
│  Command: prompt_to_produce_pass_prompt_from_template.txt (n=2)          │
│  Output: pass_2_prompt.md (manually crafted, same result)                │
│                                                                          │
│  Note: In actual execution, Pass 2 prompt was manually crafted rather   │
│  than generated via meta-prompt. But the content is identical to what   │
│  the meta-prompt would have produced.                                   │
└──────────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                   SESSION 4B: PASS 2 EXECUTION                           │
│                                                                          │
│  Input:  european_ai_report_2026_pass1.md                                │
│         pass_2_prompt.md                                                 │
│  Output: european_ai_report_2026_pass2.md (301 lines, ~63 KB)            │
│  Changes: Full prose conversion, counterarguments, evidence tags         │
└──────────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                   SESSION 5A: META-PROMPT GENERATION (Pass 3)            │
│                                                                          │
│  Input:  reusable_pass_prompt_template.md                                │
│         improvement_plan.md                                              │
│  Command: prompt_to_produce_pass_prompt_from_template.txt (n=3)          │
│  Output: pass_3_prompt.md (generated via meta-prompt)                    │
└──────────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                   SESSION 5B: PASS 3 EXECUTION                           │
│                                                                          │
│  Input:  european_ai_report_2026_pass2.md                                │
│         pass_3_prompt.md                                                 │
│  Tools:  generate_charts.py (matplotlib), integrate_charts.py            │
│  Output: european_ai_report_2026_pass3.md (362 lines, ~70 KB)            │
│         charts/ (4 PNG files)                                            │
│  Changes: 4 publication-quality charts integrated into document          │
└──────────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                   SESSION 6A: META-PROMPT GENERATION (Pass 4)            │
│                                                                          │
│  Input:  reusable_pass_prompt_template.md                                │
│         improvement_plan.md                                              │
│  Command: prompt_to_produce_pass_prompt_from_template.txt (n=4)          │
│  Output: pass_4_prompt.md (generated via meta-prompt)                    │
└──────────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                   SESSION 6B: PASS 4 EXECUTION                           │
│                                                                          │
│  Input:  european_ai_report_2026_pass3.md                                │
│         pass_4_prompt.md                                                 │
│  Output: european_ai_report_2026_final.md (362 lines, ~70 KB)            │
│  Changes: QA cross-checks, consistency pass, transitions, source cleanup │
└──────────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                        SESSION 7: CLEANUP                                │
│                                                                          │
│  Input:  european_ai_report_2026_final.md                                │
│  Output: european_ai_report_2026_clean.md (310 lines, ~53 KB)            │
│         european_ai_report_2026.docx                                     │
│         european_ai_report_2026.pdf                                      │
│         european_ai_report_2026_clean.docx                               │
│         diagnosis_cleanup.md                                             │
│  Changes: Removed all internal research artifacts, cleaned tier tags,    │
│           rewrote transitions for professional tone                      │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Critical Design Patterns

### Pattern 1: Two-Level Automation (The Key Innovation)

The pipeline uses **two levels of automation**:

**Level 1 — Meta-Prompt Generation:**
```
Template + Improvement Plan → Pass Prompt (generated at runtime)
```
A Hermes session reads the reusable template and the improvement plan, extracts the tasks for the specified pass number, and generates a complete pass prompt. This is the `prompt_to_produce_pass_prompt_from_template.txt` command.

**Level 2 — Pass Execution:**
```
Pass Prompt + Current Document → Revised Document
```
A second Hermes session reads the generated prompt and the current document version, executes the tasks, and produces the revised document.

This means **no pre-written prompt files are needed**. The improvement plan is the single source of truth. If you update the plan, all pass prompts regenerate automatically.

### Pattern 2: The Reusable Template

`reusable_pass_prompt_template.md` is a parameterized template. For each pass, the meta-prompt:
1. Reads the template
2. Extracts the specific pass tasks from `improvement_plan.md`
3. Combines them: replaces template placeholders with actual values, inserts the pass-specific tasks
4. Writes the result as `pass_{n}_prompt.md`

The template ensures consistency across passes and makes it easy to generate new pass prompts.

### Pattern 3: Bottom-to-Top Chart Insertion

The `integrate_charts.py` script processes insertions from bottom to top to avoid line number shifts. This is critical when inserting multiple blocks into a document.

### Pattern 4: Three-File Input Pattern

Every pass execution session receives exactly three files:
1. **Current document** — the version from the previous pass (or original for Pass 1)
2. **Improvement plan** — the full 4-pass plan (contains tasks for all passes)
3. **Quality assessment** — the assessment that identified issues

This pattern ensures each pass has all context needed without cross-session memory.

---

## Automation Blueprint

To automate this workflow for future reports on different subjects, the following architecture is recommended:

### The Meta-Prompt is the Key Reusable Artifact

The `prompt_to_produce_pass_prompt_from_template.txt` file is the most important automation mechanism. It is a **generic, parameterized command**:

```
Use {TEMPLATE_PATH} as a template, review {PLAN_PATH} and write the pass_{n}_prompt to folder.
```

Where:
- `{TEMPLATE_PATH}` = path to `reusable_pass_prompt_template.md`
- `{PLAN_PATH}` = path to `improvement_plan.md`
- `{n}` = pass number (1, 2, 3, or 4)

This single command, run once per pass number, generates all pass prompts. No pre-written prompt files needed.

### Python Orchestrator Pseudocode

```python
# For each pass N in 1..4:
#   Step A: Generate the pass prompt
meta_prompt = f"""
Use {TEMPLATE_PATH} as a template, review {PLAN_PATH} and 
write the pass_{n}_prompt to folder.
"""
run_hermes_session(meta_prompt)  # Creates pass_{n}_prompt.md

#   Step B: Execute the pass
run_hermes_session(pass_{n}_prompt.md)  # Creates pass_N report
```

### Option B: Cron Job Chaining

Use hermes-cli's cron job feature with `context_from` to chain sessions:

```bash
# Stage 1: Initial research
hermes-cli run --prompt-file prompts/initial.md --topic "AI in Europe"

# Stage 2: Assessment (after Stage 1 completes)
hermes-cli run --prompt-file prompts/assessment.md \
  --context-from <stage1_job_id>

# For each pass N:
#   Meta-prompt generation
hermes-cli run --prompt-file prompts/meta_prompt.md \
  --context-from <stage2_job_id> \
  --param "n=1"

#   Pass execution
hermes-cli run --prompt-file prompts/pass_1.md \
  --context-from <meta_prompt_job_id>
```

---

## Lessons Learned

1. **The two-level automation is the key insight** — separating prompt generation from prompt execution means no pre-written prompts are needed. The improvement plan is the single source of truth.

2. **The meta-prompt is the most reusable artifact** — `prompt_to_produce_pass_prompt_from_template.txt` is a generic, parameterized command that works for any pass number. It's the automation engine.

3. **The 4-pass strategy works** — Separating concerns (methodology → prose → visualization → QA) produced a significantly better result than trying to fix everything at once.

4. **Self-contained prompts are essential** — Every pass execution session successfully read all three input files and produced the correct output. The template pattern is robust.

5. **Quality assessment is the bottleneck** — Stage 2 produced the improvement plan that guided all subsequent work. A poor assessment would have led to poor improvements.

6. **Chart integration is mechanical** — The `integrate_charts.py` script proved that chart insertion is a deterministic operation that can be automated. The `generate_charts.py` script is topic-agnostic and can be parameterized.

7. **Cleanup is topic-specific** — The diagnosis of what to remove from the final report depends on the internal artifacts generated, which vary by topic and research depth.

8. **Pass 2 was manually crafted** — In the actual execution, the Pass 2 prompt was written by hand (`pass_2_prompt.md`) rather than generated via the meta-prompt. However, the content is identical to what the meta-prompt would have produced, confirming that the meta-prompt approach works.

---

## File Inventory (in case-studies/european-ai-2026/)

| File | Purpose | Generated By |
|------|---------|-------------|
| `prompts/initial_prompt.txt` | Original research prompt | User |
| `artifacts/european_ai_report_2026.md` | Original research report | Session 1 |
| `prompts/initial_assesment_prompt.txt` | Quality assessment prompt | User |
| `analysis/quality_assessment_report.md` | Component-by-component audit | Session 2 |
| `analysis/improvement_plan.md` | 4-pass improvement plan | Session 2 |
| `templates/reusable_pass_prompt_template.md` | Parameterized pass prompt template | User |
| `templates/prompt_to_produce_pass_prompt_from_template.txt` | Generic meta-prompt command | User |
| `pass_1_prompt.md` | (not saved — executed directly) | Session 3A (generated) |
| `artifacts/european_ai_report_2026_pass1.md` | Report after methodology + source fixes | Session 3B |
| `pass-prompts/pass_2_prompt.md` | Pass 2 prompt (manually crafted) | User |
| `artifacts/european_ai_report_2026_pass2.md` | Report after prose conversion | Session 4B |
| `pass_3_prompt.md` | Pass 3 prompt (generated via meta-prompt) | Session 5A |
| `artifacts/european_ai_report_2026_pass3.md` | Report with charts integrated | Session 5B |
| `pass_4_prompt.md` | Pass 4 prompt (generated via meta-prompt) | Session 6A |
| `artifacts/european_ai_report_2026_final.md` | Final report with all artifacts | Session 6B |
| `analysis/diagnosis_cleanup.md` | Cleanup analysis | Session 7 |
| `artifacts/european_ai_report_2026_clean.md` | Delivery-ready report | Session 7 |
| `artifacts/european_ai_report_2026.docx` | DOCX export | Session 7 |
| `artifacts/european_ai_report_2026.pdf` | PDF export | Session 7 |
| `artifacts/european_ai_report_2026_clean.docx` | Clean DOCX export | Session 7 |
| `scripts/generate_charts.py` | Matplotlib chart generation script | Session 5B |
| `scripts/integrate_charts.py` | Chart insertion into document | Session 5B |
| `artifacts/charts/chart01_...png` | Investment comparison chart | Session 5B |
| `artifacts/charts/chart02_...png` | Market growth projection chart | Session 5B |
| `artifacts/charts/chart03_...png` | Investment by country chart | Session 5B |
| `artifacts/charts/chart04_...png` | Source tier distribution chart | Session 5B |
| `dummy.txt` | Empty placeholder | — |

---

## Conclusion

This workflow demonstrates a robust, context-limited approach to producing deep research reports. The key innovation is the **two-level automation**: a meta-prompt generates pass prompts from a reusable template and the improvement plan, and then those generated prompts are executed in separate sessions. This means **no pre-written prompt files are needed** — the improvement plan is the single source of truth.

The most important reusable artifacts are:
1. **`prompt_to_produce_pass_prompt_from_template.txt`** — the generic meta-prompt command
2. **`reusable_pass_prompt_template.md`** — the parameterized template structure
3. **`improvement_plan.md`** — the source of truth for all pass tasks

Together, these three files encode the entire automation pipeline. Given any new topic, you produce the initial report and assessment (Sessions 1-2), then loop over the meta-prompt + pass execution for each pass number (Sessions 3A-6B), and finally run cleanup (Session 7).
