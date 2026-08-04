import os

import anthropic
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Create Anthropic client
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)


def compare_with_claude(paper1, paper2):

    prompt = f"""
You are an expert medical research assistant.

Compare these two research papers.

Paper 1

Title:
{paper1['title']}

Abstract:
{paper1['abstract']}


Paper 2

Title:
{paper2['title']}

Abstract:
{paper2['abstract']}


Write your comparison using exactly these headings.

Study Design

Key Differences

Key Similarities

Clinical Significance

Strengths

Limitations

Overall Conclusion
"""

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1800,
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

    return result.strip()