---
description: Convene the business idea council (believer, skeptic, investor in parallel, then judge) on an idea
argument-hint: <describe your business idea>
---

Convene the business idea council on this idea:

<idea>
$ARGUMENTS
</idea>

If the idea above is empty, ask me to describe my idea and stop.

Follow these steps exactly:

**Step 1 — Advisors, in parallel.** In a SINGLE message, make three Agent tool calls at once so they run in parallel:
- `subagent_type: "believer"`
- `subagent_type: "skeptic"`
- `subagent_type: "investor"`

Give each one ONLY the idea text above, verbatim, with the instruction "Evaluate this business idea:". Do not add your own analysis, framing, or opinions, and never include any other advisor's output. Run them in the foreground and wait for all three to finish.

**Step 2 — Judge.** Once all three have returned, make one Agent tool call with `subagent_type: "judge"`. Pass it the original idea plus the FULL, unedited outputs of all three advisors, each clearly labeled (`## Believer`, `## Skeptic`, `## Investor`). Do not summarize or trim them.

**Step 3 — Report.** Show me all four outputs in full, unedited, under these headings in this order:

## 🟢 Believer
## 🔴 Skeptic
## 💰 Investor
## ⚖️ Judge

Do not add your own commentary, summary, or verdict before or after — the Judge's output is the conclusion.
