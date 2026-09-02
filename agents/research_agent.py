from tools.pubmed_tool import search_pubmed
from tools.excel_exporter import export_to_excel
from tools.report_exporter import (
    export_concise_summary,
    export_pubmed_report,
)


def research(query):
    """
    Search PubMed, analyse the retrieved papers,
    export the results to Excel and Word,
    and display the results in the terminal.
    """

    print(f"\nResearch Topic: {query}")

    papers = search_pubmed(query)

    if not papers:
        print("\nNo papers were found.")
        return None

    # Export the evidence table to Excel
    export_to_excel(papers)

    # Export the detailed Word report
    detailed_report_path = export_pubmed_report(
        query,
        papers,
    )

    # Export the concise client summary once
    concise_summary_path = export_concise_summary(
        query,
        papers,
    )

    print(
        f"\nDetailed Word report saved as: "
        f"{detailed_report_path}"
    )

    print(
        f"\nConcise client summary saved as: "
        f"{concise_summary_path}"
    )

    print("\nResults:\n")

    for paper in papers:
        print("=" * 80)

        print("TITLE")
        print(paper.get("title", "Unknown"))
        print()

        print("AUTHORS")
        print(paper.get("authors", "Unknown"))
        print()

        print("JOURNAL")
        print(paper.get("journal", "Unknown"))
        print()

        print("YEAR")
        print(paper.get("year", "Unknown"))
        print()

        print("PMID")
        print(paper.get("pmid", "Not available"))
        print()

        print("DOI")
        print(paper.get("doi", "Not available"))
        print()

        print("PUBMED SOURCE")
        print(paper.get("pubmed_url", "Not available"))
        print()

        print("VERIFICATION STATUS")
        print(
            paper.get(
                "verification_status",
                "Manual verification required",
            )
        )
        print()

        print("AI-ASSISTED ANALYSIS")

        summary = paper.get("summary", {})

        if isinstance(summary, dict):
            print(
                "Study Design: "
                f"{summary.get('study_design', 'Not specified')}"
            )
            print()

            print(
                "Key Findings: "
                f"{summary.get('key_findings', 'Not specified')}"
            )
            print()

            print(
                "Clinical Significance: "
                f"{summary.get('clinical_significance', 'Not specified')}"
            )
            print()

            print(
                "Limitations: "
                f"{summary.get('limitations', 'Not specified')}"
            )
            print()

            keywords = summary.get("keywords", [])

            if isinstance(keywords, list):
                keywords = ", ".join(
                    str(keyword)
                    for keyword in keywords
                )

            print(f"Keywords: {keywords or 'Not specified'}")

        else:
            print(summary)

        print()
        print("=" * 80)
        print()

    return {
        "papers": papers,
        "detailed_report": detailed_report_path,
        "concise_summary": concise_summary_path,
        "excel_file": "research_results.xlsx",
    }