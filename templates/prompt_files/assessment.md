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
