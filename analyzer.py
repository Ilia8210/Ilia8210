import os
import json
import base64
from io import BytesIO

import google.generativeai as genai
from PIL import Image

SYSTEM_PROMPT = """You are a senior UX researcher. Analyze user feedback from a Telegram channel and produce a structured usability research report.

Focus on:
- Identifying recurring problems and pain points
- Grouping similar issues by theme
- Counting frequency of each issue cluster
- Mapping issues to UX principles (Nielsen's 10 Heuristics, Fitts' Law, Hick's Law, Jakob's Law, Miller's Law, Gestalt Principles)
- Proposing specific, actionable improvements

Be objective and data-driven. Prioritize by frequency and severity."""


def _build_parts(data: dict) -> list:
    texts = data["texts"]
    images = data["images"]

    messages_block = "\n".join(
        f"[{m['date'][:10]}] {m['text']}" for m in texts
    )

    prompt = f"""{SYSTEM_PROMPT}

Analyze these {len(texts)} user messages and {len(images)} screenshots from the past 24 hours.

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

Sort issues by frequency descending."""

    parts = [prompt]

    for img in images:
        raw = base64.b64decode(img["data"])
        parts.append(Image.open(BytesIO(raw)))

    if images:
        parts.append(f"The {len(images)} images above are screenshots from users. Analyze visible UI issues and include insights in 'screenshots_insights'.")

    return parts


def analyze_feedback(data: dict) -> dict:
    if not data["texts"] and not data["images"]:
        return {"error": "No messages found in the last 24 hours"}

    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")

    parts = _build_parts(data)
    response = model.generate_content(parts)

    raw = response.text
    start = raw.find("{")
    end = raw.rfind("}") + 1
    return json.loads(raw[start:end])
