"""
Summarizer module.

This module prepares the research paper information
and sends it to Claude for analysis.
"""

from tools.claude_client import summarize_with_claude


def summarize_paper(title, abstract, journal, year):
    """
    Send the paper title, journal, year, and abstract
    to Claude for structured summarization.
    """

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