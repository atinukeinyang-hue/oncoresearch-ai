from tools.pubmed_tool import search_pubmed


def research(query):
    print(f"\nResearch Topic: {query}")
    search_pubmed(query)