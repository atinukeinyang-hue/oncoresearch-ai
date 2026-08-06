from tools.pubmed_tool import search_pubmed
from tools.excel_exporter import export_to_excel
from tools.report_exporter import export_pubmed_report


def research(query):
    """
    Search PubMed, analyse papers with Claude,
    export the results to Excel and Word,
    then display the results in the terminal.
    """

    print(f"\nResearch Topic: {query}")

    papers = search_pubmed(query)

    if not papers:
        print("\nNo papers were found.")
        return

    # Export results to Excel
    export_to_excel(papers)

    # Export results to Word
    report_path = export_pubmed_report(query, papers)

    print(f"\nWord report saved as: {report_path}")

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

        print("CLAUDE ANALYSIS")

        summary = paper.get("summary", {})

        if isinstance(summary, dict):

            print(f"Study Design: {summary.get('study_design', 'Not specified')}")
            print()

            print(f"Key Findings: {summary.get('key_findings', 'Not specified')}")
            print()

            print(
                f"Clinical Significance: "
                f"{summary.get('clinical_significance', 'Not specified')}"
            )
            print()

            print(f"Limitations: {summary.get('limitations', 'Not specified')}")
            print()

            keywords = summary.get("keywords", [])

            if isinstance(keywords, list):
                keywords = ", ".join(keywords)

            print(f"Keywords: {keywords}")

        else:
            print(summary)

        print()
        print("=" * 80)
        print()