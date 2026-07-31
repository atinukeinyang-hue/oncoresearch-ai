import anthropic

# --------------------------------------------------
# TEMPORARY TEST
# Paste your NEW Anthropic API key below
# --------------------------------------------------

client = anthropic.Anthropic(
    api_key="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"
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