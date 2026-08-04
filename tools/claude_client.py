import os
import json

import anthropic
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Create Anthropic client
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)


def summarize_with_claude(text):

    prompt = f"""
You are an expert medical research assistant.

You will receive a research paper containing:

- Title
- Journal
- Year
- Abstract

Extract the information below.

If information is missing, return "Not specified".

Return ONLY ONE valid JSON object.

Do NOT explain anything.

Do NOT use markdown.

Use exactly this format:

{{
  "title":"",
  "journal":"",
  "year":"",
  "study_design":"",
  "key_findings":"",
  "clinical_significance":"",
  "limitations":"",
  "keywords":[]
}}

{text}
"""

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=700,
        thinking={"type": "disabled"},
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = ""

    for block in response.content:
        if getattr(block, "type", "") == "text":
            result += block.text

    print("\n========== RAW CLAUDE RESPONSE ==========\n")
    print(result)
    print("\n=========================================\n")

    result = result.strip()
    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    start = result.find("{")
    end = result.rfind("}")

    if start == -1 or end == -1:
        print("\nNo JSON object was found in Claude's response.\n")
        raise ValueError("Claude did not return JSON.")

    json_text = result[start:end + 1]

    print("\n========== JSON EXTRACTED ==========\n")
    print(json_text)
    print("\n====================================\n")

    return json.loads(json_text)