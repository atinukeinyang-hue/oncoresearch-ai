def search_pubmed(query):
    """
    Simulates searching PubMed.
    """

    papers = [
        {
            "title": "AI Contouring for Prostate Radiotherapy",
            "authors": "Smith et al.",
            "year": 2024,
        },
        {
            "title": "Deep Learning in Cervical Brachytherapy",
            "authors": "Johnson et al.",
            "year": 2023,
        },
        {
            "title": "MRI-guided Adaptive Radiotherapy",
            "authors": "Williams et al.",
            "year": 2022,
        },
    ]

    print("\nPubMed Results")
    print("=" * 50)

    for paper in papers:
        print(f"Title: {paper['title']}")
        print(f"Authors: {paper['authors']}")
        print(f"Year: {paper['year']}")
        print("-" * 50)