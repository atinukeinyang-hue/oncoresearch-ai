from tools.pubmed_tool import search_pubmed
from tools.excel_exporter import export_to_excel


def research(query):
    print(f"\nResearch Topic: {query}")

    papers = search_pubmed(query)

    # Export results to Excel
    export_to_excel(papers)

    print("\nResults:\n")

    for paper in papers:

        print("=" * 80)

        print("TITLE")
        print(paper["title"])
        print()

        print("AUTHORS")
        print(paper["authors"])
        print()

        print("JOURNAL")
        print(paper["journal"])
        print()

        print("YEAR")
        print(paper["year"])
        print()

        print("CLAUDE ANALYSIS")
        print(paper["summary"])
        print()

        print("=" * 80)
        print()