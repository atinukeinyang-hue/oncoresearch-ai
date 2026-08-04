import chromadb

# ==========================================
# Connect to the vector database
# ==========================================

client = chromadb.PersistentClient(path="vector_db")

collection = client.get_collection(
    name="pubmed_papers"
)


def retrieve_papers(question, n_results=3):

    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )

    documents = results["documents"][0]
    metadata = results["metadatas"][0]

    papers = []

    for i in range(len(documents)):

        papers.append(
            {
                "title": metadata[i]["title"],
                "authors": metadata[i]["authors"],
                "journal": metadata[i]["journal"],
                "year": metadata[i]["year"],
                "abstract": documents[i]
            }
        )

    return papers


if __name__ == "__main__":

    print("\n===================================")
    print("Semantic Paper Search")
    print("===================================\n")

    question = input("Ask a research question: ")

    papers = retrieve_papers(question)

    print("\n===================================")
    print("Top Matching Papers")
    print("===================================\n")

    for i, paper in enumerate(papers, start=1):

        print(f"Paper {i}\n")

        print(f"Title   : {paper['title']}")
        print(f"Authors : {paper['authors']}")
        print(f"Journal : {paper['journal']}")
        print(f"Year    : {paper['year']}")

        print("\nAbstract\n")
        print(paper["abstract"])

        print("\n-----------------------------------------\n")