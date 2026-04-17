# Design Report Command

When generating PDF reports or any visual output, apply these design principles.

## Philosophy (from Anthropic canvas-design + frontend-design skills)
- 90% visual design, 10% text — information lives in layout, not paragraphs
- Choose ONE bold aesthetic direction and commit fully — no safe middle ground
- Every element must be intentional: spacing, color, type, weight
- Ask: "Would a senior designer approve this?"

## Typography Rules
- Avoid generic defaults — use weight contrast (Bold 700 for hierarchy, Regular 400 for body)
- Type as visual accent, not explanatory blocks
- Hierarchy: Title → Section → Body → Caption — never skip levels
- Line height: 1.4–1.6 for body, 1.1–1.2 for headings

## Color System
- 1 dominant color (structure/backgrounds)
- 1 accent color (CTAs, severity indicators, key numbers)
- Neutrals for body text (never pure black — use #1a1a1a or #2d2d2d)
- Severity palette: critical → red, high → orange, medium → amber, low → blue

## Layout Principles (Gestalt)
- **Proximity**: group related items, add space between unrelated ones
- **Contrast**: size/weight difference must be obvious, not subtle
- **Alignment**: strict grid — nothing floats arbitrarily
- **White space is not wasted space** — it creates focus

## PDF Report Specific Rules
- Cover: title + date + 3 key stats in large numerals
- Dividers between sections — not just line breaks
- Issue cards: title → severity badge → frequency count → quote (indented) → recommendation (green)
- Quick wins section: visually distinct from deep issues
- Never use emoji in PDF — use typographic symbols instead (→, •, —)

## Quality Check Before Output
- [ ] Does the visual hierarchy guide the eye naturally?
- [ ] Can someone understand the severity without reading every word?
- [ ] Are recommendations visually distinct from problems?
- [ ] Is there enough white space to avoid cognitive overload?
