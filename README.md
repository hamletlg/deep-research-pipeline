# Deep Research Report Pipeline — Automation Kit

This folder contains the complete automation kit for producing deep research reports
on any topic using Hermes Agent. It was derived from the actual workflow used to
produce *"The State of Artificial Intelligence in Europe: A 2026 Report"*.

## Directory Structure

```
deep-research-pipeline/
├── README.md                          ← You are here
├── docs/                              ← Analysis & blueprints
│   ├── workflow_analysis.md           ← Pipeline reconstruction
│   └── automation_blueprint.md        ← Templates & orchestrator
├── templates/                         ← Reusable prompt templates (topic-agnostic)
│   ├── reusable_pass_prompt_template.md
│   ├── prompt_to_produce_pass_prompt_from_template.txt
│   └── prompt_files/                  ← Parameterized stage prompts
│       ├── initial.md                 ← Stage 1: Initial research
│       ├── assessment.md              ← Stage 2: Quality assessment
│       ├── cleanup.md                 ← Stage 7: Cleanup
│       └── meta_prompt.txt            ← Meta-prompt generator
├── scripts/                           ← Python scripts
│   ├── orchestrator.py                ← Full pipeline orchestrator
│   ├── generate_charts.py             ← Chart generation (matplotlib)
│   └── integrate_charts.py            ← Chart insertion into document
├── config/                            ← Pipeline configuration
│   └── cron_job_config.yaml           ← Cron job definitions for chaining
├── references/                      ← Reference materials (skill copies, source docs)
│   └── deep-research-framework/     ← Copy of the deep-research-framework skill
│       └── SKILL.md                 ← The methodology that drives this pipeline
└── case-studies/                    ← Example case studies
    └── european-ai-2026/              ← The Europe report (example)
        ├── artifacts/                 ← Report versions, charts, exports
        ├── analysis/                  ← Quality assessment, improvement plan
        ├── prompts/                   ← Original prompts used
        └── pass-prompts/              ← Generated pass prompts
```

## The Foundation: Deep-Research-Framework Skill

The entire pipeline is built on the `deep-research-framework` skill (a copy of which is
available in `references/deep-research-framework/SKILL.md`). This skill defines the 10-component
quality methodology that drives every stage of the pipeline — from the initial research persona
and PICO framing, through the source quality hierarchy, to the quality assessment criteria
used in Stage 2.

The skill is kept as a reference copy in this folder so the pipeline is fully self-contained:
you can reproduce the workflow on any machine without depending on the installed skill set.

## Quick Start

```bash
# Run the full pipeline for a new topic
python3 scripts/orchestrator.py \
  --topic "Your Research Topic" \
  --output-dir /path/to/output \
  --passes 4

# Dry run to see what would happen
python3 scripts/orchestrator.py \
  --topic "Your Research Topic" \
  --output-dir /path/to/output \
  --dry-run
```

The pipeline consists of **9 sessions across 7 logical stages**:

```
Session 1:  Initial Research → report.md
Session 2:  Quality Assessment → assessment.md + improvement_plan.md
Session 3A: Pass 1 Meta-Prompt → pass_1_prompt.md
Session 3B: Pass 1 Execute → pass1 report
Session 4A: Pass 2 Meta-Prompt → pass_2_prompt.md
Session 4B: Pass 2 Execute → pass2 report
Session 5A: Pass 3 Meta-Prompt → pass_3_prompt.md
Session 5B: Pass 3 Execute → pass3 report + charts
Session 6A: Pass 4 Meta-Prompt → pass_4_prompt.md
Session 6B: Pass 4 Execute → final report
Session 7:  Cleanup → clean report + exports
```

### The Key Innovation: Two-Level Automation

For each improvement pass, there are **two separate Hermes sessions**:

1. **Meta-Prompt Generation** — Reads the reusable template + improvement plan,
   extracts tasks for the specified pass number, and generates a complete pass prompt.
   This is the `prompt_to_produce_pass_prompt_from_template.txt` command.

2. **Pass Execution** — Reads the generated prompt + current document, executes
   the tasks, and produces the revised document.

This means **no pre-written prompt files are needed**. The improvement plan is the
single source of truth. If you update the plan, all pass prompts regenerate automatically.

## How to Use

### Option A: Python Orchestrator (Recommended)

```bash
python3 scripts/orchestrator.py \
  --topic "Your Research Topic" \
  --output-dir /path/to/output \
  --template-path templates/reusable_pass_prompt_template.md \
  --meta-prompt-path templates/prompt_to_produce_pass_prompt_from_template.txt \
  --passes 4
```

### Option B: Cron Job Chaining

1. Import the cron job definitions from `config/cron_job_config.yaml`
2. Replace `{TOPIC}`, `{OUTPUT_DIR}`, `{TEMPLATE_PATH}`, and `{PLAN_PATH}` with actual values
3. Run the jobs in sequence using `context_from` to chain them

### Option C: Manual Execution

1. Run Session 1 with `templates/prompt_files/initial.md`
2. Run Session 2 with `templates/prompt_files/assessment.md`
3. For each pass N (1-4):
   a. Run the meta-prompt with `templates/prompt_to_produce_pass_prompt_from_template.txt`
   b. Run the pass with the generated `pass_{n}_prompt.md`
4. Run Session 7 with `templates/prompt_files/cleanup.md`

## Customization

To customize for different topics:

1. **Replace the topic** — Change `{TOPIC}` in the prompt files
2. **Adjust research parameters** — Modify depth, source mix, time period, etc.
3. **Customize chart generation** — Edit `scripts/generate_charts.py` for topic-specific charts
4. **Adjust cleanup rules** — Modify `templates/prompt_files/cleanup.md` for topic-specific cleanup
5. **Add/remove passes** — Change `--passes` in the orchestrator or adjust the cron config

## Files You'll Need to Create for Each New Topic

| File | How to Create |
|------|---------------|
| `{TOPIC}.md` | Run Session 1 (initial research) |
| `assessment.md` | Run Session 2 (quality assessment) |
| `improvement_plan.md` | Generated by Session 2 |
| `pass_{n}_prompt.md` | Generated by meta-prompt for each pass N |
| `pass_{n}_report.md` | Generated by pass execution for each pass N |
| `report_clean.md` | Generated by Session 7 (cleanup) |

## Key Design Decisions

1. **Fresh sessions per pass** — Each session is completely isolated. No cross-session
   memory dependency. This respects the 181K context limit.

2. **Two-level automation** — Pass prompts are generated at runtime from the template
   and improvement plan. No pre-written prompts needed.

3. **Sequential execution** — Passes run in order because each pass builds on the
   previous one.

4. **Improvement plan is the single source of truth** — If you update the plan, all
   pass prompts regenerate automatically.

## Lessons Learned

1. The two-level automation is the key insight — separating prompt generation from
   prompt execution means no pre-written prompts are needed.

2. The meta-prompt is the most reusable artifact — `prompt_to_produce_pass_prompt_from_template.txt`
   is a generic, parameterized command that works for any pass number.

3. The 4-pass strategy works — Separating concerns (methodology → prose → visualization → QA)
   produced a significantly better result than trying to fix everything at once.

4. Self-contained prompts are essential — Every pass execution session successfully
   read all three input files and produced the correct output.

5. Quality assessment is the bottleneck — Stage 2 produced the improvement plan that
   guided all subsequent work. A poor assessment would have led to poor improvements.

6. Chart integration is mechanical — The `integrate_charts.py` script proved that chart
   insertion is a deterministic operation that can be automated.

7. Cleanup is topic-specific — The diagnosis of what to remove from the final report
   depends on the internal artifacts generated, which vary by topic and research depth.

## File Flow Diagram

```
topic + parameters
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 1: INITIAL RESEARCH                                  │
│  hermes-cli run --prompt-file templates/prompt_files/initial.md       │
│  Output: report_<topic>.md                                  │
└─────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 2: QUALITY ASSESSMENT                                │
│  hermes-cli run --prompt-file templates/prompt_files/assessment.md    │
│  Output: assessment.md + improvement_plan.md                │
└─────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 3-6: IMPROVEMENT PASSES (x4)                         │
│  For each pass N:                                           │
│    hermes-cli run --prompt-file templates/prompt_to_produce_pass...   │
│    hermes-cli run --prompt-file pass_{n}_prompt.md          │
│  Output: report_<topic>_pass{1-4}.md                        │
│         charts/ (if applicable)                             │
└─────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 7: CLEANUP                                           │
│  hermes-cli run --prompt-file templates/prompt_files/cleanup.md       │
│  Output: report_<topic>_clean.md                            │
│         report_<topic>.docx                                 │
│         report_<topic>.pdf                                  │
└─────────────────────────────────────────────────────────────┘
```

## License

This automation kit is derived from the actual workflow used to produce the
*"State of AI in Europe"* report. It is provided as-is for reuse and customization.
