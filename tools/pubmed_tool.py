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

    # Step 3: Fetch article details
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

    papers = []

    for article in root.findall(".//PubmedArticle"):

        title = article.findtext(".//ArticleTitle")

        if title is None:
            title = "No title available"

        author_list = article.findall(".//Author")

        authors = []

        for author in author_list:

            lastname = author.findtext("LastName")
            initials = author.findtext("Initials")

            if lastname and initials:
                authors.append(f"{lastname} {initials}")

        if authors:
            authors = ", ".join(authors)
        else:
            authors = "Unknown"

        year = article.findtext(".//PubDate/Year")

        if year is None:
            year = "Unknown"

        papers.append(
            {
                "title": title,
                "authors": authors,
                "year": year
            }
        )

    return papers


def search_pubmed_dummy(query):
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