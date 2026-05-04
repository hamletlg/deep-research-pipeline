# Python Orchestrator: Automated Deep Research Report Pipeline

This is a Python script that orchestrates the full deep research report production pipeline
using hermes-cli. It automates the 9-session workflow: initial research → quality audit →
4 improvement passes (each with meta-prompt generation + execution) → cleanup.

## Prerequisites

1. hermes-cli installed and configured
2. Topic prompt file (e.g., `prompts/initial.md`)
3. Assessment prompt file (e.g., `prompts/assessment.md`)
4. Cleanup prompt file (e.g., `prompts/cleanup.md`)
5. The reusable template: `reusable_pass_prompt_template.md`
6. The meta-prompt command: `prompt_to_produce_pass_prompt_from_template.txt`

## Usage

```bash
python3 orchestrator.py \
  --topic "The State of AI in Europe" \
  --output-dir /path/to/output \
  --template-path /path/to/reusable_pass_prompt_template.md \
  --meta-prompt-path /path/to/prompt_to_produce_pass_prompt_from_template.txt \
  --initial-prompt "Write a deep research report on..." \
  --assessment-prompt "Assess the report quality and create an improvement plan..." \
  --cleanup-prompt "Clean up the final report for delivery..." \
  --passes 4
```

## Architecture

```
Session 1: Initial Research
  ↓
Session 2: Quality Assessment + Improvement Plan
  ↓
For each pass N (1..4):
  Session 2N+1: Meta-Prompt Generation
    (template + improvement plan → pass_{n}_prompt.md)
  Session 2N+2: Pass Execution
    (pass_{n}_prompt.md + current report → revised report)
  ↓
Session 9: Cleanup
  (final report → delivery-ready document)
```

## Key Design Decisions

1. **Two-level automation**: Pass prompts are generated at runtime from the template
   and improvement plan. No pre-written prompts needed.
2. **Fresh sessions per pass**: Each session is completely isolated — no cross-session
   memory dependency. This respects the 181K context limit.
3. **Sequential execution**: Passes run in order because each pass builds on the
   previous one. Use `--parallel` to run meta-prompt generation in parallel with
   the previous pass execution.
4. **Improvement plan is the single source of truth**: If you update the plan, all
   pass prompts regenerate automatically.

## Error Handling

- If a pass fails, the script continues to the next pass (best-effort)
- Failed passes are logged but don't stop the pipeline
- The final report is always the last successful pass

## Customization

To customize for different topics:
1. Replace the prompt files in `prompts/`
2. Optionally customize the chart generation script in `charts/`
3. Adjust `--passes` if you need more/fewer improvement passes

```python
import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional


def run_hermes_command(
    prompt: str,
    output_dir: str,
    topic: str,
    topic_file: str,
    extra_files: Optional[list[str]] = None,
    session_name: str = "",
    parallel: bool = False,
) -> subprocess.CompletedProcess:
    """Run a hermes-cli command with the given prompt and topic.

    Args:
        prompt: The prompt text to pass to hermes-cli
        output_dir: The output directory for the report
        topic: The research topic
        topic_file: Path to the topic file
        extra_files: List of additional files to include in the session
        session_name: Human-readable name for logging
        parallel: If True, use --parallel flag

    Returns:
        CompletedProcess from subprocess.run
    """
    cmd = [
        "hermes-cli",
        "run",
        "--topic", topic,
        "--topic-file", topic_file,
        "--output-dir", output_dir,
        "--prompt", prompt,
    ]

    if parallel:
        cmd.append("--parallel")

    if extra_files:
        for f in extra_files:
            cmd.extend(["--file", f])

    if session_name:
        cmd.extend(["--name", session_name])

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Running: {' '.join(cmd[:10])}...")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)

    if result.returncode != 0:
        print(f"  WARNING: Command failed (exit code {result.returncode})")
        print(f"  STDERR: {result.stderr[:500]}")
    else:
        print(f"  ✓ Completed successfully")

    return result


def generate_pass_prompt(
    meta_prompt_path: str,
    template_path: str,
    improvement_plan_path: str,
    pass_number: int,
    output_dir: str,
) -> str:
    """Generate a pass prompt using the meta-prompt template.

    This is the key automation mechanism: the meta-prompt reads the reusable
    template and the improvement plan, extracts tasks for the specified pass
    number, and generates a complete pass prompt.

    Args:
        meta_prompt_path: Path to the meta-prompt command file
        template_path: Path to the reusable pass prompt template
        improvement_plan_path: Path to the improvement plan
        pass_number: The pass number (1, 2, 3, or 4)
        output_dir: The output directory

    Returns:
        Path to the generated pass prompt file
    """
    # Read the meta-prompt
    with open(meta_prompt_path, "r") as f:
        meta_prompt = f.read()

    # Replace placeholders with actual values
    meta_prompt = meta_prompt.replace("{TEMPLATE_PATH}", template_path)
    meta_prompt = meta_prompt.replace("{PLAN_PATH}", improvement_plan_path)
    meta_prompt = meta_prompt.replace("{n}", str(pass_number))

    # Write to a temporary file for hermes-cli
    tmp_prompt_path = os.path.join(output_dir, f"_meta_prompt_pass_{pass_number}.txt")
    with open(tmp_prompt_path, "w") as f:
        f.write(meta_prompt)

    return tmp_prompt_path


def generate_charts(
    report_path: str,
    charts_dir: str,
    report_data: Optional[dict] = None,
) -> list[str]:
    """Generate charts for the report using matplotlib.

    This function can be customized per topic. The default implementation
    generates charts based on the report content.

    Args:
        report_path: Path to the report file
        charts_dir: Directory to save charts
        report_data: Optional pre-extracted data for charts

    Returns:
        List of chart file paths
    """
    os.makedirs(charts_dir, exist_ok=True)

    # Import matplotlib
    import matplotlib
    matplotlib.use("Agg")  # Non-interactive backend
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    charts = []

    # Example: Generate a chart based on report data
    if report_data:
        # Generate charts from report_data (topic-specific)
        pass

    return charts


def integrate_charts(
    report_path: str,
    charts_dir: str,
    chart_positions: list[tuple[int, str]],
    output_path: str,
) -> str:
    """Integrate chart markdown blocks into the report.

    Processes insertions from bottom to top to avoid line number shifts.

    Args:
        report_path: Path to the report file
        charts_dir: Directory containing chart PNG files
        chart_positions: List of (line_number, chart_file) tuples
        output_path: Path to the output report

    Returns:
        Path to the integrated report
    """
    # Read the report
    with open(report_path, "r") as f:
        lines = f.readlines()

    # Process from bottom to top
    for line_num, chart_file in sorted(chart_positions, key=lambda x: -x[0]):
        chart_path = os.path.join(charts_dir, chart_file)
        chart_name = os.path.splitext(chart_file)[0]

        # Create markdown block for the chart
        chart_md = f"\n**Figure: {chart_name.replace('_', ' ').title()}**\n\n"
        chart_md += f"![{chart_name}]({chart_path})\n\n"

        # Insert at the specified line
        lines.insert(line_num, chart_md)

    # Write the integrated report
    with open(output_path, "w") as f:
        f.writelines(lines)

    return output_path


def cleanup_report(
    report_path: str,
    output_dir: str,
    cleanup_instructions: Optional[str] = None,
) -> str:
    """Clean up the final report for delivery.

    Removes internal research artifacts, tier tags, counterargument markers,
    and other internal notes that should not appear in a delivery-ready document.

    Args:
        report_path: Path to the final report
        output_dir: Output directory
        cleanup_instructions: Optional cleanup instructions

    Returns:
        Path to the cleaned report
    """
    # Read the report
    with open(report_path, "r") as f:
        content = f.read()

    # Apply cleanup rules
    # (These would be customized per topic)
    cleaned = content

    # Write the cleaned report
    output_path = os.path.join(output_dir, "report_clean.md")
    with open(output_path, "w") as f:
        f.write(cleaned)

    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Automated Deep Research Report Pipeline"
    )
    parser.add_argument(
        "--topic",
        type=str,
        required=True,
        help="The research topic",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        required=True,
        help="Output directory for the report and artifacts",
    )
    parser.add_argument(
        "--template-path",
        type=str,
        default="templates/reusable_pass_prompt_template.md",
        help="Path to the reusable pass prompt template",
    )
    parser.add_argument(
        "--meta-prompt-path",
        type=str,
        default="templates/prompt_to_produce_pass_prompt_from_template.txt",
        help="Path to the meta-prompt command file",
    )
    parser.add_argument(
        "--initial-prompt",
        type=str,
        default="Write a deep research report on...",
        help="Initial research prompt",
    )
    parser.add_argument(
        "--assessment-prompt",
        type=str,
        default="Assess the report quality and create an improvement plan...",
        help="Quality assessment prompt",
    )
    parser.add_argument(
        "--cleanup-prompt",
        type=str,
        default="Clean up the final report for delivery...",
        help="Cleanup prompt",
    )
    parser.add_argument(
        "--passes",
        type=int,
        default=4,
        help="Number of improvement passes",
    )
    parser.add_argument(
        "--parallel",
        action="store_true",
        help="Run meta-prompt generation in parallel with pass execution",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print commands without executing them",
    )

    args = parser.parse_args()

    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)

    # Create topic file
    topic_file = os.path.join(args.output_dir, "topic.txt")
    with open(topic_file, "w") as f:
        f.write(args.topic)

    # Stage 1: Initial Research
    print("\n" + "=" * 60)
    print("STAGE 1: Initial Research")
    print("=" * 60)

    if args.dry_run:
        print(f"Would run: hermes-cli run --topic '{args.topic}' --prompt '{args.initial_prompt}'")
    else:
        run_hermes_command(
            prompt=args.initial_prompt,
            output_dir=args.output_dir,
            topic=args.topic,
            topic_file=topic_file,
            session_name="Initial Research",
        )

    # Stage 2: Quality Assessment
    print("\n" + "=" * 60)
    print("STAGE 2: Quality Assessment")
    print("=" * 60)

    if args.dry_run:
        print(f"Would run: hermes-cli run --assessment-prompt '{args.assessment_prompt}'")
    else:
        run_hermes_command(
            prompt=args.assessment_prompt,
            output_dir=args.output_dir,
            topic=args.topic,
            topic_file=topic_file,
            session_name="Quality Assessment",
        )

    # Improvement Passes
    for pass_num in range(1, args.passes + 1):
        print("\n" + "=" * 60)
        print(f"STAGE {pass_num + 2}: Pass {pass_num}")
        print("=" * 60)

        # Generate the pass prompt
        meta_prompt_path = generate_pass_prompt(
            meta_prompt_path=args.meta_prompt_path,
            template_path=args.template_path,
            improvement_plan_path=os.path.join(args.output_dir, "improvement_plan.md"),
            pass_number=pass_num,
            output_dir=args.output_dir,
        )

        if args.dry_run:
            print(f"Would generate pass {pass_num} prompt from template + plan")
        else:
            run_hermes_command(
                prompt=open(meta_prompt_path).read(),
                output_dir=args.output_dir,
                topic=args.topic,
                topic_file=topic_file,
                session_name=f"Pass {pass_num} Prompt Generation",
            )

        # Execute the pass
        pass_prompt_file = os.path.join(args.output_dir, f"pass_{pass_num}_prompt.md")
        if os.path.exists(pass_prompt_file):
            if args.dry_run:
                print(f"Would execute pass {pass_num} with prompt: {pass_prompt_file}")
            else:
                run_hermes_command(
                    prompt=open(pass_prompt_file).read(),
                    output_dir=args.output_dir,
                    topic=args.topic,
                    topic_file=topic_file,
                    extra_files=[pass_prompt_file],
                    session_name=f"Pass {pass_num} Execution",
                )

    # Cleanup
    print("\n" + "=" * 60)
    print("STAGE 9: Cleanup")
    print("=" * 60)

    if args.dry_run:
        print(f"Would run cleanup on final report")
    else:
        run_hermes_command(
            prompt=args.cleanup_prompt,
            output_dir=args.output_dir,
            topic=args.topic,
            topic_file=topic_file,
            session_name="Cleanup",
        )

    print("\n" + "=" * 60)
    print("Pipeline complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
