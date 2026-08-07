from pathlib import Path

import anthropic
from dotenv import dotenv_values


# ==========================================
# Locate the project environment file
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"


# ==========================================
# Create Claude client only when needed
# ==========================================

def get_client():
    config = dotenv_values(ENV_FILE)
    api_key = config.get("ANTHROPIC_API_KEY")

    if not api_key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY is not configured. "
            "Copy .env.example to .env and add your Anthropic API key "
            "before using Claude-powered features."
        )

    return anthropic.Anthropic(api_key=api_key)


# ==========================================
# Generate evidence-grounded RAG answer
# ==========================================

def generate_rag_answer(question, retrieved_papers):

    client = get_client()

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

---

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