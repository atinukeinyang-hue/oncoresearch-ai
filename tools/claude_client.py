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
You are extracting structured information from a PubMed record
for an oncology research evidence table.

Use ONLY the title, journal, year and abstract supplied below.
Do not use outside knowledge.
Do not invent, estimate or assume missing information.
Do not claim that you reviewed the full article.

Scientific accuracy rules:

- Preserve reported numerical results accurately.
- Distinguish reported results from author conclusions.
- Do not describe a study as randomized, prospective,
  retrospective or multicentre unless the supplied text supports it.
- Do not invent sample sizes, treatment details or outcomes.
- Do not invent study limitations.
- If limitations are not explicitly stated or directly evident from
  the supplied abstract, write:
  "Not reported in the supplied abstract."
- Clinical significance must be a cautious interpretation supported
  directly by the supplied abstract.
- Do not give treatment recommendations or patient-specific advice.
- Use "Not reported in the supplied abstract" whenever information
  cannot be determined reliably.

Output requirements:

- title: Copy the supplied title exactly.
- journal: Copy the supplied journal exactly.
- year: Copy the supplied year exactly.
- study_design: One concise sentence.
- key_findings: Maximum three concise sentences.
- clinical_significance: Maximum two cautious sentences.
- limitations: Maximum two concise sentences.
- keywords: Maximum five short keywords.

Return ONLY one valid JSON object.
Do not include introductory text, markdown, code fences or notes.

Use exactly these JSON keys:

{{
  "title": "",
  "journal": "",
  "year": "",
  "study_design": "",
  "key_findings": "",
  "clinical_significance": "",
  "limitations": "",
  "keywords": []
}}

SUPPLIED PUBMED RECORD:

{text}
"""

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=2000,
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


def synthesize_papers_with_claude(query, papers):
    """
    Create a cautious synthesis across multiple PubMed records.
    """

    paper_sections = []

    for index, paper in enumerate(papers, start=1):
        summary = paper.get("summary", {})

        if not isinstance(summary, dict):
            summary = {}

        paper_sections.append(
            f"""
RECORD {index}
PMID: {paper.get("pmid", "Not available")}
Title: {paper.get("title", "Unknown")}
Journal: {paper.get("journal", "Unknown")}
Year: {paper.get("year", "Unknown")}
Study design: {summary.get("study_design", "Not reported")}
Key findings: {summary.get("key_findings", "Not reported")}
Clinical significance: {
    summary.get("clinical_significance", "Not reported")
}
Limitations: {summary.get("limitations", "Not reported")}
"""
        )

    evidence_text = "\n".join(paper_sections)

    prompt = f"""
You are preparing a concise oncology literature synthesis from
structured PubMed evidence records.

Research question:
{query}

Use ONLY the supplied records below.
Do not use outside knowledge.
Do not invent results, comparisons, statistics or conclusions.
Do not give patient-specific treatment recommendations.
Do not describe this search as a systematic review.
Do not state that full-text articles were reviewed.
Clearly acknowledge heterogeneity and evidence limitations.
If the records do not support a conclusion, state that clearly.

Prepare a cautious synthesis suitable for a short client report.

Return ONLY one valid JSON object using exactly these keys:

{{
  "overview": "",
  "evidence_patterns": [],
  "clinical_relevance": "",
  "evidence_limitations": "",
  "conclusion": ""
}}

Requirements:

- overview: Maximum 120 words describing the evidence retrieved.
- evidence_patterns: Three to five concise evidence patterns.
- clinical_relevance: Maximum 120 cautious words.
- evidence_limitations: Maximum 120 words.
- conclusion: Maximum 100 words.
- Do not include markdown or code fences.
- Do not include text outside the JSON object.

SUPPLIED RECORDS:

{evidence_text}
"""

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1800,
        thinking={"type": "disabled"},
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    result = ""

    for block in response.content:
        if getattr(block, "type", "") == "text":
            result += block.text

    result = result.strip()
    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    start = result.find("{")
    end = result.rfind("}")

    if start == -1 or end == -1:
        raise ValueError(
            "Claude did not return a JSON synthesis."
        )

    synthesis = json.loads(result[start:end + 1])

    required_fields = [
        "overview",
        "evidence_patterns",
        "clinical_relevance",
        "evidence_limitations",
        "conclusion",
    ]

    for field in required_fields:
        if field not in synthesis:
            synthesis[field] = [] if field == "evidence_patterns" else ""

    if not isinstance(synthesis["evidence_patterns"], list):
        synthesis["evidence_patterns"] = [
            str(synthesis["evidence_patterns"])
        ]

    return synthesis