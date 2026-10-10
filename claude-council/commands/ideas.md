---
description: Generate zero-startup-cost AI business ideas a college student can run (3 scouts in parallel, then a picker)
argument-hint: [optional: your major, skills, interests, hours/week, city]
---

Generate business ideas for me with the idea scouts.

<profile>
$ARGUMENTS
</profile>

If the profile above is empty, do not stop: tell the scouts "No profile given; assume a typical US undergraduate with a laptop, free AI tools and about 10 hours a week."

Follow these steps exactly:

**Step 1 — Scouts, in parallel.** In a SINGLE message, make three Agent tool calls at once so they run in parallel:
- `subagent_type: "idea-campus-scout"`
- `subagent_type: "idea-skills-scout"`
- `subagent_type: "idea-trend-scout"`

Give each one ONLY the profile text above, verbatim, with the instruction "Find business ideas for this student:". Do not add your own ideas, framing, or opinions, and never include another scout's output. Run them in the foreground and wait for all three to finish.

**Step 2 — Picker.** Once all three have returned, make one Agent tool call with `subagent_type: "idea-picker"`. Pass it the profile plus the FULL, unedited outputs of all three scouts, each clearly labeled (`## Campus Scout`, `## Skills Scout`, `## Trend Scout`). Do not summarize or trim them.

**Step 3 — Report.** Show me all four outputs in full, unedited, under these headings in this order:

## 🏫 Campus Scout
## 🛠️ Skills Scout
## 📈 Trend Scout
## 🏆 Picker

Do not add your own commentary before or after. The Picker's output ends with `/council` lines I can run to stress-test the top ideas.
