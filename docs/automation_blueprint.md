# Automation Blueprint: Deep Research Report Pipeline

## Overview

This document provides a complete automation blueprint for producing deep research reports on any topic using the Hermes Agent. It encodes the 7-stage pipeline, the reusable prompt templates, and the Python orchestration scripts needed to run the entire workflow as an automated pipeline.

## Architecture

```
topic + parameters
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 1: INITIAL RESEARCH                                  │
│  hermes-cli run --prompt-file stage1_prompt.md              │
│  Output: report_<topic>.md                                  │
└─────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 2: QUALITY ASSESSMENT                                │
│  hermes-cli run --prompt-file stage2_prompt.md              │
│  Output: assessment.md + improvement_plan.md                │
└─────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 3-6: IMPROVEMENT PASSES (x4)                         │
│  hermes-cli run --prompt-file stage3_prompt.md              │
│  hermes-cli run --prompt-file stage4_prompt.md              │
│  hermes-cli run --prompt-file stage5_prompt.md              │
│  hermes-cli run --prompt-file stage6_prompt.md              │
│  Output: report_<topic>_pass{1-4}.md                        │
│         charts/ (if applicable)                             │
└─────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 7: CLEANUP                                           │
│  hermes-cli run --prompt-file stage7_prompt.md              │
│  Output: report_<topic>_clean.md                            │
│         report_<topic>.docx                                 │
│         report_<topic>.pdf                                  │
└─────────────────────────────────────────────────────────────┘
```

## File Structure

```
deep-research-pipeline/
├── config/
│   └── cron_job_config.yaml       # Cron job definitions
├── docs/
│   ├── automation_blueprint.md    ← You are here
│   └── workflow_analysis.md       ← Pipeline reconstruction
├── scripts/
│   ├── generate_charts.py         # Chart generation (parameterized)
│   ├── integrate_charts.py        # Chart insertion (parameterized)
│   └── orchestrator.py            # Main pipeline orchestrator
├── templates/
│   ├── prompt_files/              # Parameterized stage prompts
│   │   ├── assessment.md          # Stage 2: Quality assessment
│   │   ├── cleanup.md             # Stage 7: Cleanup
│   │   ├── initial.md             # Stage 1: Initial research
│   │   └── meta_prompt.txt        # Meta-prompt generator
│   ├── prompt_to_produce_pass_prompt_from_template.txt  # Meta-prompt command
│   └── reusable_pass_prompt_template.md  # Pass prompt template
├── case-studies/                  # Example case studies
│   └── european-ai-2026/
│       ├── analysis/              # Quality assessment, improvement plan
│       ├── artifacts/             # Report versions, charts, exports
│       ├── pass-prompts/          # Generated pass prompts
│       └── prompts/               # Original prompts used
└── README.md
```

## Pipeline Configuration (config/cron_job_config.yaml)

```yaml
pipeline:
  # Topic and scope
  topic: "European AI Landscape 2026"
  output_dir: "/path/to/output/<topic>"
  
  # Research parameters
  research:
    depth: "Level 4"           # Level 1-4 (see deep-research-framework)
    source_mix: "policy"       # "default", "academic", "market", "policy"
    time_period: "2024-2026"
    geographic_focus: "EU-27 + UK, Switzerland, Norway, Iceland"
    exclusions: "Non-AI digital regulation, consumer AI, military AI"
  
  # Improvement plan
  improvement:
    passes: 4
    target_score: 8            # Target quality score out of 10
    
    # Pass 1: Foundational fixes
    pass1:
      add_methodology: true
      add_pico: true
      add_scope_boundaries: true
      add_research_persona: true
      replace_weak_sources: true
      min_tier1_2_percentage: 40
      
    # Pass 2: Prose conversion
    pass2:
      convert_bullets_to_prose: true
      add_counterarguments: true
      add_evidence_tags: true
      
    # Pass 3: Visualization
    pass3:
      generate_charts: true
      min_charts: 3
      max_charts: 5
      
    # Pass 4: QA
    pass4:
      cross_check: true
      consistency_pass: true
      transition_improvement: true
      source_cleanup: true
  
  # Cleanup
  cleanup:
    remove_internal_artifacts: true
    remove_tier_tags: true
    remove_evidence_tags: true
    remove_counterargument_labels: true
    remove_methodology_section: true
    remove_source_corrections_table: true
    remove_pass_notes: true
    rewrite_transitions: true
    professional_tone: true
  
  # Export
  export:
    formats: ["md", "docx", "pdf"]
    docx_font: "Calibri"
    docx_size: "11pt"
```

## Stage 1: Initial Research Prompt Template

```markdown
# Deep Research Report: {TOPIC}

## Context
You are conducting a deep research investigation on "{TOPIC}".
You have access to the `deep-research-framework` skill which defines the methodology.

## Research Parameters
- **Depth:** {DEPTH}
- **Source Mix:** {SOURCE_MIX}
- **Time Period:** {TIME_PERIOD}
- **Geographic Focus:** {GEOGRAPHIC_FOCUS}
- **Exclusions:** {EXCLUSIONS}

## Task
Conduct a comprehensive deep research report on the topic above. Follow the deep research framework methodology:

1. Define a research persona appropriate to the topic
2. Frame the research question using PICO methodology
3. Define explicit scope boundaries
4. Conduct multi-source research using web_search and web_extract
5. Apply the Source Quality Hierarchy (Tier 1-6)
6. Write in long-form prose (paragraphs, not bullets)
7. Include inline citation tags [T#] for every factual claim
8. Generate 2-5 publication-quality charts using matplotlib
9. Include a complete Sources section with tier labels

## Output
Save the complete report to: `{OUTPUT_DIR}/report_{TOPIC}.md`

The report should follow a Trend Analysis structure:
- Executive Summary
- Current State / Landscape
- Historical Context / Background
- Driving Forces
- Counterforces / Challenges
- Projections / Future Outlook
- Strategic Implications
- Conclusion
- Sources (with tier labels)
```

## Stage 2: Quality Assessment Prompt Template

```markdown
# Quality Assessment: {TOPIC} Research Report

## Context
A research report on "{TOPIC}" has been produced at `{OUTPUT_DIR}/report_{TOPIC}.md`.
You have access to the `deep-research-framework` skill which defines the quality criteria.

## Task
1. Read the report at `{OUTPUT_DIR}/report_{TOPIC}.md`
2. Load the `deep-research-framework` skill to understand quality criteria
3. Evaluate the report against ALL 10 components:
   - C1: Research Persona
   - C2: PICO Framing
   - C3: Scope Boundaries
   - C4: Depth Specification
   - C5: Citation Requirements
   - C6: Output Structure
   - C7: Quality Guardrails
   - C8: Anti-Hallucination
   - C9: Data Visualization
   - C10: Long-Form Methodology

4. For each component, provide:
   - Score (0-10)
   - Finding (what was found)
   - Impact (why it matters)
   - Status (PASS/FAIL/PARTIAL FAIL/PARTIAL PASS)

5. Identify strengths and weaknesses
6. Produce prioritized improvement recommendations (Critical/Important/Nice-to-Have)

## Output
Write TWO files:

1. `{OUTPUT_DIR}/assessment.md` — The component-by-component quality assessment
2. `{OUTPUT_DIR}/improvement_plan.md` — A multi-pass improvement plan with:
   - Target score (e.g., 8/10)
   - Pass structure table
   - Detailed tasks for each pass
   - File flow diagram
   - Execution notes for each pass agent
```

## Reusable Pass Prompt Template

This is the most important reusable artifact. It encodes the self-contained prompt pattern.

```markdown
# PASS {N} — {TOPIC} Report Improvement

## Context

You are continuing the improvement of a research report on "{TOPIC}". 
This is **PASS {N}** of a {TOTAL_PASSES}-pass improvement plan. 
Each pass is fully self-contained — you have no context from previous passes. 
You must read everything provided below and produce a complete, self-contained revised document.

## Files to Read

1. **Current document:** `{OUTPUT_DIR}/report_{TOPIC}_pass{N-1}.md` 
   (or `{OUTPUT_DIR}/report_{TOPIC}.md` if this is Pass 1)
2. **Improvement plan:** `{OUTPUT_DIR}/improvement_plan.md`
3. **Quality assessment:** `{OUTPUT_DIR}/assessment.md`

## What This Pass Must Do

Read the improvement plan, find the section for **PASS {N}**, and execute ALL tasks listed there.

### PASS {N} OBJECTIVES

{PASTE_SPECIFIC_TASKS_FROM_IMPROVEMENT_PLAN}

## Rules

1. **Read the full current document** before making any changes.
2. **Preserve all content** that you did not explicitly change. Output must be complete.
3. **Do not invent sources, titles, URLs, or data points.** Use [UNVERIFIED] for unsourced claims.
4. **Write in long-form prose** for analytical sections. Bullets only for tables, prioritized lists, methodology.
5. **Paragraphs must be substantive** — minimum 4-6 sentences each. Maximum 12-15 sentences.
6. **Maintain the existing structure** but convert content within sections as instructed.
7. **Do not undo changes from previous passes** unless explicitly instructed.

## Output

Save the complete revised document to: `{OUTPUT_DIR}/report_{TOPIC}_pass{N}.md`

At the end of the document, append a note:
*This is Pass {N} of the improvement plan. Pass {N} focused on: [SUMMARIZE KEY CHANGES].*
```

## Stage 3-6: Pass Generation

Each pass prompt is generated by the meta-prompt command:
1. Reading `templates/reusable_pass_prompt_template.md`
2. Reading the `improvement_plan.md` from the case study's analysis/ folder
3. Extracting the tasks for the specified pass number
4. Writing the result as `pass_{n}_prompt.md`

The meta-prompt command is: `templates/prompt_to_produce_pass_prompt_from_template.txt`

## Stage 7: Cleanup Prompt Template

```markdown
# Cleanup: {TOPIC} Research Report

## Context
The final research report is at `{OUTPUT_DIR}/report_{TOPIC}_final.md`.
It contains internal research artifacts that must be removed for delivery.

## Issues to Address

### CRITICAL — Remove Entirely
1. **Research Framework section** — Internal persona, PICO, scope boundaries
2. **Source tier distribution chart** — Internal methodology artifact
3. **Source corrections table** — Internal QA documentation
4. **Pass notes** — Version control metadata at end of document
5. **Section transition sentences** — Meta-navigation cues (rewrite as natural prose)

### HIGH — Remove/Clean
6. **Source tier markers inline** — All `[T#]` tags
7. **Evidence grading labels** — `(well-established)`, etc.
8. **Counterargument markers** — `*Counterargument:*` labels
9. **Source list tier annotations** — `[T#]` in bibliography
10. **Source tier summary table** — Delete

### MEDIUM — Refine
11. **Figure descriptions** — Trim redundant text
12. **Methodology section** — Remove internal jargon
13. **Section numbering** — Renumber after removing internal sections
14. **Tone** — Professional policy-briefing style

## Output
Save the cleaned document to: `{OUTPUT_DIR}/report_{TOPIC}_clean.md`
```

## Python Orchestrator (scripts/orchestrator.py)

```python
#!/usr/bin/env python3
"""
Deep Research Report Pipeline Orchestrator

Runs the 7-stage pipeline for producing deep research reports
on any topic using Hermes Agent.

Usage:
    python orchestrator.py --topic "Topic Name" --output-dir /path/to/output
"""

import yaml
import subprocess
import os
import sys
import shutil
from pathlib import Path
from datetime import datetime


def load_config(config_path: str) -> dict:
    with open(config_path) as f:
        return yaml.safe_load(f)


def create_output_dir(output_dir: str, topic: str) -> Path:
    topic_dir = Path(output_dir) / topic
    topic_dir.mkdir(parents=True, exist_ok=True)
    (topic_dir / "charts").mkdir(exist_ok=True)
    return topic_dir


def generate_initial_prompt(config: dict, topic_dir: Path) -> Path:
    """Generate Stage 1 prompt for initial research."""
    prompt = f"""# Deep Research Report: {config['pipeline']['topic']}

## Context
You are conducting a deep research investigation on "{config['pipeline']['topic']}".
You have access to the `deep-research-framework` skill.

## Research Parameters
- **Depth:** {config['research']['depth']}
- **Source Mix:** {config['research']['source_mix']}
- **Time Period:** {config['research']['time_period']}
- **Geographic Focus:** {config['research']['geographic_focus']}
- **Exclusions:** {config['research']['exclusions']}

## Task
Conduct a comprehensive deep research report on the topic above. Follow the 
deep research framework methodology. Include:
1. Research persona
2. PICO framing
3. Scope boundaries
4. Long-form prose analysis with inline citation tags [T#]
5. 2-5 publication-quality charts using matplotlib (save to {topic_dir}/charts/)
6. Complete Sources section with tier labels

## Output
Save the report to: {topic_dir}/report_{config['pipeline']['topic']}.md
"""
    prompt_file = topic_dir / "stage1_prompt.md"
    prompt_file.write_text(prompt)
    return prompt_file


def generate_assessment_prompt(config: dict, topic_dir: Path) -> Path:
    """Generate Stage 2 prompt for quality assessment."""
    report_file = topic_dir / f"report_{config['pipeline']['topic']}.md"
    prompt = f"""# Quality Assessment: {config['pipeline']['topic']}

## Context
A research report on "{config['pipeline']['topic']}" has been produced at 
{report_file}. You have access to the `deep-research-framework` skill.

## Task
1. Read the report at {report_file}
2. Load the `deep-research-framework` skill
3. Evaluate against ALL 10 components (C1-C10)
4. Score each component (0-10)
5. Identify strengths and weaknesses
6. Produce prioritized improvement recommendations

## Output
Write TWO files:
1. {topic_dir}/assessment.md — Component-by-component assessment
2. {topic_dir}/improvement_plan.md — Multi-pass improvement plan with:
   - Target score
   - Pass structure table
   - Detailed tasks for each pass
   - File flow diagram
   - Execution notes
"""
    prompt_file = topic_dir / "stage2_prompt.md"
    prompt_file.write_text(prompt)
    return prompt_file


def generate_pass_prompt(config: dict, topic_dir: Path, pass_number: int) -> Path:
    """Generate a pass prompt from the reusable template."""
    template_file = Path(__file__).parent / "templates" / "pass_prompt_template.md"
    
    # Read the improvement plan to extract tasks for this pass
    plan_file = topic_dir / "improvement_plan.md"
    plan_content = plan_file.read_text()
    
    # Extract tasks for this pass (find the section for PASS N)
    import re
    pass_pattern = rf'## Pass {pass_number}:.*?(?=\n## Pass {pass_number + 1}:|\n## |\Z)'
    match = re.search(pass_pattern, plan_content, re.DOTALL)
    
    if match:
        tasks = match.group()
        # Clean up the header
        tasks = '\n'.join('\n'.join(tasks.split('\n')[1:]))
    else:
        tasks = "Execute all tasks listed in the improvement plan for Pass N."
    
    template = template_file.read_text()
    template = template.replace('{N}', str(pass_number))
    template = template.replace('{TOPIC}', config['pipeline']['topic'])
    template = template.replace('{TOTAL_PASSES}', str(config['improvement']['passes']))
    template = template.replace('{OUTPUT_DIR}', str(topic_dir))
    template = template.replace('{PASTE_SPECIFIC_TASKS_FROM_IMPROVEMENT_PLAN}', tasks)
    
    prompt_file = topic_dir / f"stage{pass_number + 2}_prompt.md"
    prompt_file.write_text(template)
    return prompt_file


def run_hermes_session(prompt_file: Path, topic_dir: Path) -> bool:
    """Run a single Hermes session with the given prompt."""
    try:
        result = subprocess.run(
            ['hermes-cli', 'run', '--prompt-file', str(prompt_file)],
            cwd=str(topic_dir),
            capture_output=True,
            text=True,
            timeout=3600  # 1 hour timeout per session
        )
        if result.returncode == 0:
            print(f"  ✓ Session completed: {prompt_file.name}")
            return True
        else:
            print(f"  ✗ Session failed: {prompt_file.name}")
            print(f"    stderr: {result.stderr[:500]}")
            return False
    except subprocess.TimeoutExpired:
        print(f"  ✗ Session timed out: {prompt_file.name}")
        return False
    except FileNotFoundError:
        print(f"  ✗ hermes-cli not found. Install it first.")
        return False


def generate_charts(config: dict, topic_dir: Path) -> bool:
    """Generate charts for the report."""
    chart_script = Path(__file__).parent / "scripts" / "generate_charts.py"
    try:
        result = subprocess.run(
            ['python3', str(chart_script)],
            cwd=str(topic_dir),
            capture_output=True,
            text=True,
            timeout=300
        )
        if result.returncode == 0:
            print(f"  ✓ Charts generated")
            return True
        else:
            print(f"  ✗ Chart generation failed: {result.stderr[:500]}")
            return False
    except Exception as e:
        print(f"  ✗ Chart generation error: {e}")
        return False


def cleanup_report(config: dict, topic_dir: Path) -> bool:
    """Run cleanup stage."""
    prompt_file = topic_dir / "stage7_prompt.md"
    if not prompt_file.exists():
        # Generate cleanup prompt
        final_file = topic_dir / "report_final.md"
        prompt = f"""# Cleanup: {config['pipeline']['topic']}

## Context
The final research report is at {final_file}.
It contains internal research artifacts that must be removed for delivery.

## Task
Remove all internal research artifacts:
1. Research Framework section (persona, PICO, scope)
2. Source tier distribution chart
3. Source corrections table
4. Pass notes at end of document
5. All [T#] tier markers
6. All evidence grading labels
7. Counterargument markers
8. Section transition meta-sentences
9. Rewrite methodology section in plain language
10. Renumber sections

Save the cleaned document to: {topic_dir}/report_{config['pipeline']['topic']}_clean.md
"""
        prompt_file.write_text(prompt)
    
    return run_hermes_session(prompt_file, topic_dir)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Deep Research Report Pipeline')
    parser.add_argument('--topic', required=True, help='Topic name')
    parser.add_argument('--config', default='config.yaml', help='Config file path')
    parser.add_argument('--output-dir', default='/tmp/research_output', help='Output directory')
    parser.add_argument('--stage', type=int, default=0, help='Run from specific stage (0=all)')
    parser.add_argument('--skip', nargs='+', type=int, default=[], help='Skip specific stages')
    args = parser.parse_args()
    
    config = load_config(args.config)
    topic_dir = create_output_dir(args.output_dir, args.topic)
    
    print(f"\n{'='*60}")
    print(f"  Deep Research Pipeline: {args.topic}")
    print(f"  Output: {topic_dir}")
    print(f"{'='*60}\n")
    
    stages = [
        (1, "Initial Research", lambda: generate_initial_prompt(config, topic_dir) and run_hermes_session(
            topic_dir / "stage1_prompt.md", topic_dir)),
        (2, "Quality Assessment", lambda: generate_assessment_prompt(config, topic_dir) and run_hermes_session(
            topic_dir / "stage2_prompt.md", topic_dir)),
        (3, "Pass 1 — Foundational Fixes", lambda: run_hermes_session(
            generate_pass_prompt(config, topic_dir, 1), topic_dir)),
        (4, "Pass 2 — Prose Conversion", lambda: run_hermes_session(
            generate_pass_prompt(config, topic_dir, 2), topic_dir)),
        (5, "Pass 3 — Visualization", lambda: (
            generate_charts(config, topic_dir) and
            run_hermes_session(generate_pass_prompt(config, topic_dir, 3), topic_dir)
        )),
        (6, "Pass 4 — QA + Polish", lambda: run_hermes_session(
            generate_pass_prompt(config, topic_dir, 4), topic_dir)),
        (7, "Cleanup", lambda: cleanup_report(config, topic_dir)),
    ]
    
    results = {}
    for stage_num, stage_name, stage_func in stages:
        if args.stage > 0 and stage_num < args.stage:
            print(f"  ⊘ Skipping stage {stage_num}: {stage_name}")
            results[stage_num] = True
            continue
        if stage_num in args.skip:
            print(f"  ⊘ Skipping stage {stage_num}: {stage_name}")
            results[stage_num] = True
            continue
        
        print(f"\n  Stage {stage_num}: {stage_name}...")
        results[stage_num] = stage_func()
    
    # Summary
    print(f"\n{'='*60}")
    print(f"  Pipeline Results:")
    for stage_num, success in results.items():
        status = "✓" if success else "✗"
        print(f"    {status} Stage {stage_num}")
    print(f"{'='*60}\n")
    
    if all(results.values()):
        print("All stages completed successfully!")
        print(f"Output files in: {topic_dir}")
    else:
        failed = [s for s, ok in results.items() if not ok]
        print(f"Failed stages: {failed}")
        sys.exit(1)


if __name__ == '__main__':
    main()
```

## Usage

### Running the Full Pipeline

```bash
# Run the full pipeline for a new topic
python3 scripts/orchestrator.py \
  --topic "My Research Topic" \
  --output-dir /path/to/output \
  --passes 4

# Dry run to see what would happen
python3 scripts/orchestrator.py \
  --topic "My Research Topic" \
  --output-dir /path/to/output \
  --dry-run
```

### Manual Execution (Per-Session)

For maximum control, run each stage manually:

```bash
# Stage 1
hermes-cli run --prompt-file templates/prompt_files/initial.md

# Stage 2
hermes-cli run --prompt-file templates/prompt_files/assessment.md

# For each pass N (1-4):
#   Meta-prompt generation
hermes-cli run --prompt-file templates/prompt_to_produce_pass_prompt_from_template.txt

#   Pass execution
hermes-cli run --prompt-file pass_{n}_prompt.md

# Stage 7: Cleanup
hermes-cli run --prompt-file templates/prompt_files/cleanup.md
```

### Cron Job Chaining

Import the cron job definitions from `config/cron_job_config.yaml` and chain them
using `context_from` to pass output between jobs.

## Key Design Principles

1. **Each stage is independent** — No stage depends on another's context. All context is provided via files.
2. **The improvement plan drives everything** — Stage 2 produces the plan that guides Stages 3-6.
3. **The reusable template is the key** — `templates/reusable_pass_prompt_template.md` encodes the self-contained pattern.
4. **Charts are parameterized** — `scripts/generate_charts.py` and `scripts/integrate_charts.py` take topic-specific data.
5. **Cleanup is configurable** — Different topics may need different cleanup rules.
6. **Error handling is explicit** — The orchestrator reports which stages succeeded/failed.
