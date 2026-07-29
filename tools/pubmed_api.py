import requests

url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

params = {
    "db": "pubmed",
    "term": "cervical cancer brachytherapy",
    "retmode": "json",
    "retmax": 5
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())