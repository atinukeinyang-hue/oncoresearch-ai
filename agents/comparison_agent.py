from tools.pubmed_tool import search_pubmed
from tools.comparison_client import compare_with_claude


def compare_papers(query1, query2):
    """
    Search PubMed for two research topics and compare the first paper
    returned from each search using Claude.
    """

    print("\nSearching for Paper Set 1...\n")
    papers1 = search_pubmed(query1)

    print("\nSearching for Paper Set 2...\n")
    papers2 = search_pubmed(query2)

    if len(papers1) == 0 or len(papers2) == 0:
        print("Not enough papers found for comparison.")
        return

    print("\nGenerating AI comparison...\n")

    comparison = compare_with_claude(
        papers1[0],
        papers2[0]
    )

    print("=" * 80)
    print("AI PAPER COMPARISON")
    print("=" * 80)
    print(comparison)
    print("=" * 80)

    return comparison