from bs4 import BeautifulSoup
import requests

pmid = "37289154"

url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

params = {
    "db": "pubmed",
    "id": pmid,
    "retmode": "xml"
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.text)