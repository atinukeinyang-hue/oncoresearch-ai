from tools.pubmed_tool import search_pubmed

def research(query):
    print(f"\nResearch Topic: {query}")

    papers = search_pubmed(query)

    print("\nResults:\n")

    for paper in papers:
        print(f"Title: {paper['title']}")
        print(f"Authors: {paper['authors']}")
        print(f"Year: {paper['year']}")
        print("-" * 40)