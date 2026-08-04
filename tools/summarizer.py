"""
Summarizer module.

This module prepares the research paper information
and optionally sends it to Claude for analysis.
"""

from tools.claude_client import summarize_with_claude


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