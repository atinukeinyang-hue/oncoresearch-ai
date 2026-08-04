import requests
import xml.etree.ElementTree as ET

from tools.summarizer import summarize_paper


def search_pubmed(query, use_claude=True):
    print(f"\nSearching PubMed for: {query}\n")

    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 5
    }

    response = requests.get(search_url, params=search_params)
    data = response.json()

    pmids = data["esearchresult"]["idlist"]

    print(pmids)

    ids = ",".join(pmids)

    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    fetch_params = {
        "db": "pubmed",
        "id": ids,
        "retmode": "xml"
    }

    fetch_response = requests.get(fetch_url, params=fetch_params)

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

        journal = article.findtext(".//Journal/Title")

        if journal is None:
            journal = "Unknown"

        year = article.findtext(".//PubDate/Year")

        if year is None:
            year = "Unknown"

        abstract_parts = article.findall(".//Abstract/AbstractText")

        if abstract_parts:
            abstract = " ".join(
                part.text for part in abstract_parts if part.text
            )
        else:
            abstract = "No abstract available."

        summary = summarize_paper(
            title,
            abstract,
            journal,
            year,
            use_claude=use_claude
        )

        papers.append(
            {
                "title": title,
                "authors": authors,
                "journal": journal,
                "year": year,
                "abstract": abstract,
                "summary": summary
            }
        )

    return papers


def search_pubmed_dummy(query):
    print(f"\nSearching PubMed for: {query}\n")

    papers = [
        {
            "title": f"Recent Advances in {query}",
            "authors": "Johnson et al.",
            "journal": "Journal of Radiotherapy",
            "year": "2024",
            "abstract": "This is a simulated abstract.",
            "summary": summarize_paper(
                f"Recent Advances in {query}",
                "This is a simulated abstract.",
                "Journal of Radiotherapy",
                "2024"
            )
        },
        {
            "title": f"Artificial Intelligence for {query}",
            "authors": "Williams et al.",
            "journal": "Medical Physics",
            "year": "2023",
            "abstract": "This is another simulated abstract.",
            "summary": summarize_paper(
                f"Artificial Intelligence for {query}",
                "This is another simulated abstract.",
                "Medical Physics",
                "2023"
            )
        }
    ]

    return papers


def test_requests():
    response = requests.get("https://www.google.com")
    print(response.status_code)