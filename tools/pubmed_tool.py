def search_pubmed(query):
    """
    Simulates searching PubMed.
    """

    print(f"\nSearching PubMed for: {query}\n")

    papers = [
        {
            "title": f"Recent Advances in {query}",
            "authors": "Johnson et al.",
            "year": 2024
        },
        {
            "title": f"Artificial Intelligence for {query}",
            "authors": "Williams et al.",
            "year": 2023
        }
    ]

    return papers