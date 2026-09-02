import requests
import xml.etree.ElementTree as ET

from tools.summarizer import summarize_paper


def get_element_text(element):
    """
    Extract all text from an XML element, including nested formatting tags.
    """
    if element is None:
        return ""

    return " ".join(
        text.strip()
        for text in element.itertext()
        if text and text.strip()
    )


def search_pubmed(query, use_claude=True, max_results=10):
    """
    Search PubMed and return structured article records.
    """

    print(f"\nSearching PubMed for: {query}\n")

    search_url = (
        "https://eutils.ncbi.nlm.nih.gov/"
        "entrez/eutils/esearch.fcgi"
    )

    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results,
        "sort": "relevance",
    }

    try:
        response = requests.get(
            search_url,
            params=search_params,
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as error:
        print(f"PubMed search failed: {error}")
        return []
    except ValueError as error:
        print(f"PubMed returned invalid search data: {error}")
        return []

    pmids = data.get("esearchresult", {}).get("idlist", [])

    if not pmids:
        print("No PubMed records were found.")
        return []

    print(f"PMIDs retrieved: {pmids}")

    fetch_url = (
        "https://eutils.ncbi.nlm.nih.gov/"
        "entrez/eutils/efetch.fcgi"
    )

    fetch_params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
    }

    try:
        fetch_response = requests.get(
            fetch_url,
            params=fetch_params,
            timeout=60,
        )
        fetch_response.raise_for_status()
        root = ET.fromstring(fetch_response.content)
    except requests.RequestException as error:
        print(f"PubMed article download failed: {error}")
        return []
    except ET.ParseError as error:
        print(f"PubMed XML could not be read: {error}")
        return []

    papers = []

    for article in root.findall("./PubmedArticle"):

        # PMID and source URL
        pmid = article.findtext("./MedlineCitation/PMID") or ""
        pubmed_url = (
            f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            if pmid
            else ""
        )

        # Title
        title_element = article.find(
            "./MedlineCitation/Article/ArticleTitle"
        )
        title = get_element_text(title_element)

        if not title:
            title = "No title available"

        # Authors
        author_elements = article.findall(
            "./MedlineCitation/Article/AuthorList/Author"
        )

        authors = []

        for author in author_elements:
            collective_name = author.findtext("CollectiveName")

            if collective_name:
                authors.append(collective_name)
                continue

            lastname = author.findtext("LastName")
            initials = author.findtext("Initials")

            if lastname and initials:
                authors.append(f"{lastname} {initials}")
            elif lastname:
                authors.append(lastname)

        authors_text = ", ".join(authors) if authors else "Unknown"

        # Journal
        journal = article.findtext(
            "./MedlineCitation/Article/Journal/Title"
        )

        if not journal:
            journal = "Unknown"

        # Publication year
        year = article.findtext(
            "./MedlineCitation/Article/Journal/"
            "JournalIssue/PubDate/Year"
        )

        if not year:
            year = article.findtext(
                "./MedlineCitation/Article/ArticleDate/Year"
            )

        if not year:
            medline_date = article.findtext(
                "./MedlineCitation/Article/Journal/"
                "JournalIssue/PubDate/MedlineDate"
            )

            if medline_date:
                year = medline_date[:4]
            else:
                year = "Unknown"

        # Abstract
        abstract_elements = article.findall(
            "./MedlineCitation/Article/Abstract/AbstractText"
        )

        abstract_sections = []

        for abstract_element in abstract_elements:
            section_text = get_element_text(abstract_element)
            section_label = abstract_element.attrib.get("Label", "")

            if not section_text:
                continue

            if section_label:
                abstract_sections.append(
                    f"{section_label}: {section_text}"
                )
            else:
                abstract_sections.append(section_text)

        abstract = " ".join(abstract_sections)

        # DOI
        doi = ""

        for article_id in article.findall(
            "./PubmedData/ArticleIdList/ArticleId"
        ):
            if article_id.attrib.get("IdType") == "doi":
                doi = get_element_text(article_id)
                break

        # Avoid sending missing abstracts to the AI summarizer
        if abstract:
            summary = summarize_paper(
                title,
                abstract,
                journal,
                year,
                use_claude=use_claude,
            )

            verification_status = (
                "PubMed source retrieved — "
                "AI summary requires human verification"
            )
        else:
            abstract = "No abstract available in PubMed."

            summary = {
                "study_design": "Not determined",
                "key_findings": "Abstract unavailable",
                "clinical_significance": "Manual review required",
                "limitations": (
                    "The PubMed record does not contain an abstract."
                ),
                "keywords": [],
            }

            verification_status = (
                "Manual full-text or abstract check required"
            )

        papers.append({
            "pmid": pmid,
            "doi": doi,
            "pubmed_url": pubmed_url,
            "title": title,
            "authors": authors_text,
            "journal": journal,
            "year": year,
            "abstract": abstract,
            "summary": summary,
            "verification_status": verification_status,
        })

    print(f"\nSuccessfully processed {len(papers)} PubMed records.")

    return papers


def search_pubmed_dummy(query):
    """
    Return simulated records for offline testing.
    """

    title = f"Recent Advances in {query}"
    abstract = "This is a simulated abstract for testing purposes."

    papers = [
        {
            "pmid": "TEST001",
            "doi": "10.0000/example.001",
            "pubmed_url": "",
            "title": title,
            "authors": "Johnson A, Williams B",
            "journal": "Journal of Radiotherapy",
            "year": "2024",
            "abstract": abstract,
            "summary": summarize_paper(
                title,
                abstract,
                "Journal of Radiotherapy",
                "2024",
            ),
            "verification_status": "Simulated test record",
        }
    ]

    return papers


def test_requests():
    """
    Test access to the PubMed service.
    """

    response = requests.get(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi",
        timeout=30,
    )
    print(response.status_code)