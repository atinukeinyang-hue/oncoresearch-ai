"""
Summarizer module.

This module prepares the research paper information
and optionally sends it to Claude for analysis.
"""

from tools.claude_client import (
    summarize_with_claude,
    synthesize_papers_with_claude,
)


def summarize_paper(title, abstract, journal, year, use_claude=True):
    """
    Send the paper to Claude if requested.

    Otherwise return a placeholder.
    """

    if not use_claude:
        return "Summary skipped for RAG indexing."

    paper = f"""
Title:
{title}

Journal:
{journal}

Year:
{year}

Abstract:
{abstract}
"""

    return summarize_with_claude(paper)

def synthesize_papers(query, papers, use_claude=True):
    """
    Create a concise synthesis across the retrieved papers.
    """

    if not use_claude:
        return {
            "overview": "Synthesis was not requested.",
            "evidence_patterns": [],
            "clinical_relevance": "",
            "evidence_limitations": "",
            "conclusion": "",
        }

    return synthesize_papers_with_claude(query, papers)