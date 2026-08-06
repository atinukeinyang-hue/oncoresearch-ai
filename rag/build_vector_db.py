import chromadb

from tools.pubmed_tool import search_pubmed

# ==========================================
# Create (or load) the vector database
# ==========================================

client = chromadb.PersistentClient(path="vector_db")

collection = client.get_or_create_collection(
    name="pubmed_papers"
)

print("\n===================================")
print("PubMed Vector Database Builder")
print("===================================\n")

topic = input("Enter a research topic: ")

papers = search_pubmed(topic, use_claude=False)

print(f"\nRetrieved {len(papers)} papers.\n")

for index, paper in enumerate(papers):

    document_id = f"paper_{index + 1}"

    collection.add(
        ids=[document_id],

        documents=[
            paper["abstract"]
        ],

        metadatas=[
            {
                "title": paper["title"],
                "authors": paper["authors"],
                "journal": paper["journal"],
                "year": paper["year"]
            }
        ]
    )

    print(f"Stored: {paper['title']}")

print("\n===================================")
print("Vector database successfully built!")
print(f"Papers stored: {len(papers)}")
print("===================================")