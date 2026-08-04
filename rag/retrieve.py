import chromadb

# ==========================================
# Connect to the vector database
# ==========================================

client = chromadb.PersistentClient(path="vector_db")

collection = client.get_collection(
    name="pubmed_papers"
)

print("\n===================================")
print("Semantic Paper Search")
print("===================================\n")

question = input("Ask a research question: ")

results = collection.query(
    query_texts=[question],
    n_results=3
)

print("\n===================================")
print("Top Matching Papers")
print("===================================\n")

documents = results["documents"][0]
metadata = results["metadatas"][0]

for i in range(len(documents)):

    print(f"Paper {i+1}")

    print(f"Title   : {metadata[i]['title']}")
    print(f"Authors : {metadata[i]['authors']}")
    print(f"Journal : {metadata[i]['journal']}")
    print(f"Year    : {metadata[i]['year']}")

    print("\nAbstract\n")
    print(documents[i])

    print("\n-----------------------------------------\n")