from pathlib import Path

import anthropic
from dotenv import dotenv_values


# ==========================================
# Read the API key directly from .env
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"

config = dotenv_values(ENV_FILE)
api_key = config.get("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError(
        "ANTHROPIC_API_KEY was not found in the .env file. "
        "Check that .env is beside app.py and contains:\n"
        "ANTHROPIC_API_KEY=your_key_here"
    )


# ==========================================
# Create Claude client
# ==========================================

client = anthropic.Anthropic(
    api_key=api_key
)


def generate_rag_answer(question, retrieved_papers):

    context = ""

    for i, paper in enumerate(retrieved_papers, start=1):

        context += f"""
Paper {i}

Title:
{paper['title']}

Authors:
{paper['authors']}

Journal:
{paper['journal']}

Year:
{paper['year']}

Abstract:
{paper['abstract']}

----------------------------------------
"""

    prompt = f"""
You are an expert medical research assistant.

A user asked the following question:

{question}

Below are the most relevant research papers retrieved from a medical
knowledge base:

{context}

Using ONLY the evidence from these papers, provide:

1. A concise research summary.
2. Key findings as bullet points.
3. Clinical significance.
4. Limitations or uncertainty.
5. A concluding answer to the user's question.
6. A references section listing the retrieved papers.

Do not invent information.

If the retrieved evidence is insufficient, clearly state that.
"""

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1200,
        thinking={"type": "disabled"},
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = ""

    for block in response.content:
        if getattr(block, "type", "") == "text":
            answer += block.text

    return answer.strip()