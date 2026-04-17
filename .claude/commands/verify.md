# Verify Command

Before claiming any task is complete, run through this protocol. No exceptions.

## The Iron Law (from obra/superpowers)
**NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE.**

Saying "should work" or "I think it's fixed" = not done.

## Verification Gate

For every completion claim, answer:
1. What specific command PROVES this works?
2. Run it now — read the FULL output
3. Does the output confirm the claim? (Check exit codes, not just last line)
4. Only then say it's done

## Red Flags — Stop and Re-verify
- Using words like "should", "probably", "seems to", "I believe"
- Relying on a run from earlier in the session
- Checking only part of the output
- Trusting agent reports without running independently

## For This Project Specifically
Before saying "report sent":
- [ ] PDF file actually exists on disk (check file size > 0)
- [ ] No Python errors in stdout
- [ ] Telegram API confirmed delivery (no exception thrown)

Before saying "analysis complete":
- [ ] JSON parsed without error
- [ ] All required fields present (issues, executive_summary, etc.)
- [ ] Issue count > 0 if messages were found

## When 3+ Fixes Fail
Stop patching symptoms. The architecture has a problem. Redesign the component, don't add another workaround.
