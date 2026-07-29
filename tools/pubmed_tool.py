import requests
import xml.etree.ElementTree as ET


def search_pubmed(query):
    print(f"\nSearching PubMed for: {query}\n")

    # Step 1: Search PubMed
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 5
    }

    response = requests.get(search_url, params=search_params)
    data = response.json()

    # Step 2: Extract PMIDs
    pmids = data["esearchresult"]["idlist"]

    print(pmids)

    # Step 3: Fetch paper details
    ids = ",".join(pmids)

    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    fetch_params = {
        "db": "pubmed",
        "id": ids,
        "retmode": "xml"
    }

    fetch_response = requests.get(fetch_url, params=fetch_params)

    # Step 4: Parse XML
    root = ET.fromstring(fetch_response.text)

    print(root.tag)

    # Step 5: Build a list of papers
    papers = []

    for article in root.findall(".//PubmedArticle"):

        title = article.findtext(".//ArticleTitle")

        if title is None:
            title = "No title available"

        papers.append(
            {
                "title": title,
                "authors": "Unknown",
                "year": "Unknown"
            }
        )

    return papers


def search_pubmed_dummy(query):
    """
    Backup copy of the simulated PubMed search.
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


def test_requests():
    response = requests.get("https://www.google.com")
    print(response.status_code)