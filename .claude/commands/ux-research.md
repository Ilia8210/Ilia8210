# UX Research Command

When invoked, conduct rigorous mixed-methods UX research on the provided data or topic.

## Research Process

### Phase 1: Planning
- Define precise research questions (not vague goals)
- Identify user segments from the data
- Select appropriate methods (behavioral vs. attitudinal)
- Establish what "actionable insight" means for this specific product

### Phase 2: Analysis
- **Quantitative**: Count frequency of issue mentions, severity distribution, trend over time
- **Qualitative**: Extract verbatim quotes, identify emotional language, note workarounds users invented
- **Visual**: Analyze screenshots for cognitive load, visual hierarchy, affordance failures, consistency breaks

### Phase 3: Synthesis
Group findings by:
1. **User Goal Blocked** — can't complete core task
2. **Confusion** — wrong mental model, unclear affordances
3. **Friction** — extra steps, slow feedback, information overload
4. **Trust/Confidence** — users uncertain about state or outcome

### Phase 4: Recommendations
For every issue, apply the most relevant framework:

**Nielsen's 10 Heuristics:**
- Visibility of system status
- Match between system and real world
- User control and freedom
- Consistency and standards
- Error prevention
- Recognition over recall
- Flexibility and efficiency
- Aesthetic and minimalist design
- Help users recognize/recover from errors
- Help and documentation

**Laws of UX:**
- **Fitts' Law** — target size vs. distance for interactive elements
- **Hick's Law** — reduce choices to reduce decision time
- **Jakob's Law** — users expect your product to work like others they know
- **Miller's Law** — chunk information into ≤7 items
- **Gestalt Laws** — proximity, similarity, continuity, closure
- **Zeigarnik Effect** — incomplete tasks stay in memory (use for progress)
- **Peak-End Rule** — users judge experience by peak moment and ending

## Quality Gates (from VoltAgent UX Researcher standard)
- [ ] Sample size adequate for confidence
- [ ] Bias sources identified and minimized
- [ ] Insights are specific and actionable (not "improve UX")
- [ ] Data triangulated from ≥2 sources
- [ ] Findings validated against actual user behavior

## Output Format
1. Executive Summary (3 sentences max)
2. Issues ranked by: frequency × severity
3. Each issue: title, count, user quote, UX principle violated, specific fix
4. Quick Wins (implementable in <1 day)
5. Strategic Improvements (require design/dev sprint)
