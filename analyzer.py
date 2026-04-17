import os
import json

from anthropic import Anthropic

client = Anthropic()

SYSTEM_PROMPT = """You are a senior UX researcher. Analyze user feedback from a Telegram channel and produce a structured usability research report.

Focus on:
- Identifying recurring problems and pain points
- Grouping similar issues by theme
- Counting frequency of each issue cluster
- Mapping issues to UX principles (Nielsen's 10 Heuristics, Fitts' Law, Hick's Law, Jakob's Law, Miller's Law, Gestalt Principles)
- Proposing specific, actionable improvements

Be objective and data-driven. Prioritize by frequency and severity."""


def _build_content(data: dict) -> list:
    texts = data["texts"]
    images = data["images"]

    messages_block = "\n".join(
        f"[{m['date'][:10]}] {m['text']}" for m in texts
    )

    content = [
        {
            "type": "text",
            "text": f"""Analyze these {len(texts)} user messages and {len(images)} screenshots from the past 24 hours.

MESSAGES:
{messages_block}

Return ONLY valid JSON with this exact structure:
{{
  "total_messages": {len(texts)},
  "total_images": {len(images)},
  "executive_summary": "2-3 sentence overview of main themes",
  "issues": [
    {{
      "title": "Short issue title",
      "frequency": N,
      "severity": "critical|high|medium|low",
      "description": "What users are experiencing",
      "quotes": ["exact quote 1", "exact quote 2"],
      "ux_principle": "UX law or heuristic name",
      "ux_explanation": "Why this principle applies here",
      "recommendation": "Specific actionable improvement"
    }}
  ],
  "quick_wins": ["fix 1", "fix 2", "fix 3"],
  "positive_feedback": "Any positive mentions or what users like",
  "screenshots_insights": "Insights from screenshots, or empty string if none"
}}

Sort issues by frequency descending.""",
        }
    ]

    for img in images:
        content.append(
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": img["media_type"],
                    "data": img["data"],
                },
            }
        )

    if images:
        content.append(
            {
                "type": "text",
                "text": f"The {len(images)} screenshots above are from users. Analyze visible UI issues and include insights in 'screenshots_insights'.",
            }
        )

    return content


def analyze_feedback(data: dict) -> dict:
    if not data["texts"] and not data["images"]:
        return {"error": "No messages found in the last 24 hours"}

    content = _build_content(data)

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": content}],
    )

    raw = response.content[0].text
    start = raw.find("{")
    end = raw.rfind("}") + 1
    return json.loads(raw[start:end])
