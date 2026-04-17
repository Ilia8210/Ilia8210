# Claude Behavior Rules

### 1. Plan Mode Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately — don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

### 3. Self-Improvement Loop
- After ANY correction from the user: update `tasks/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes — don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests — then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

## Task Management

1. **Plan First**: Write plan to `tasks/todo.md` with checkable items
2. **Verify Plan**: Check in before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add review section to `tasks/todo.md`
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections

## Core Principles

- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.

## UX Research Standards (from /ux-research skill)

When analyzing user feedback, always:
- Triangulate: behavioral data + attitudinal data + visual (screenshots)
- Map every issue to a UX law (Fitts', Hick's, Jakob's, Miller's, Nielsen's heuristics)
- Rank by frequency × severity, not by recency
- Recommendations must be specific enough to implement without follow-up questions
- A finding from 1 source = hypothesis. From 3 sources = finding.

## Design & Report Standards (from /design-report skill)

When generating PDFs or visual output:
- Choose a bold aesthetic direction and commit — no safe middle ground
- Visual hierarchy must guide the eye: Title → Section → Stat → Detail
- Severity must be scannable without reading — use color + size contrast
- White space is not waste — it creates focus
- Never generic: no Inter font + purple gradient + card grid defaults

## Research Methodology (from /deep-research skill)

- Decompose before researching — break into 3–5 sub-questions first
- Parallel evidence gathering across independent sources
- Synthesis ≠ summary: identify patterns, quantify, flag conflicts
- Lead with the most important finding, not the most recent

## Available Commands

- `/ux-research` — Full UX research methodology with quality gates
- `/design-report` — Design principles for PDF/visual output
- `/deep-research` — Multi-source research protocol
- `/verify` — Verification gate before claiming completion
