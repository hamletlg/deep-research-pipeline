# Cleanup: {TOPIC} Research Report

## Context
The final research report is at `{OUTPUT_DIR}/report_{TOPIC}_final.md`.
It contains internal research artifacts that must be removed for delivery.

## Task
1. Read the final report at `{OUTPUT_DIR}/report_{TOPIC}_final.md`
2. Identify all internal research artifacts that should not appear in a delivery-ready document
3. Remove the following categories of artifacts:
   - **Research Framework section** — Internal persona, PICO, scope boundaries
   - **Source tier distribution chart** — Internal methodology artifact
   - **Source corrections table** — Internal QA documentation
   - **Pass notes** — Version control metadata at end of document
   - **Section transition sentences** — Meta-navigation cues (rewrite as natural prose)
   - **Source tier markers inline** — All `[T#]` tags
   - **Evidence grading labels** — `(well-established)`, etc.
   - **Counterargument markers** — `*Counterargument:*` labels
   - **Source list tier annotations** — `[T#]` in bibliography
4. Rewrite transitions to be natural prose
5. Rewrite methodology section to remove internal jargon
6. Re-number sections after removing internal sections
7. Ensure professional policy-briefing tone throughout

## Output
Save the cleaned document to: `{OUTPUT_DIR}/report_{TOPIC}_clean.md`

Also save a diagnosis document at `{OUTPUT_DIR}/diagnosis_cleanup.md` describing:
- What artifacts were removed
- What transitions were rewritten
- What sections were renumbered
- Any other changes made
