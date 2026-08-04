from rag.retrieve import retrieve_papers
from rag.rag_client import generate_rag_answer


print("\n========================================")
print(" Radiotherapy Research Assistant v1.0")
print(" Retrieval-Augmented Generation (RAG)")
print("========================================\n")

question = input("Ask a research question:\n\n> ")

print("\nSearching knowledge base...\n")

papers = retrieve_papers(question)

if not papers:
    print("No relevant papers were found.")
    raise SystemExit

print(f"Retrieved {len(papers)} relevant papers.\n")

print("Generating evidence-based answer...\n")

answer = generate_rag_answer(question, papers)

print("\n========================================")
print(" AI RESEARCH SUMMARY")
print("========================================\n")

print(answer)

print("\n========================================")
print(" REFERENCES")
print("========================================\n")

for i, paper in enumerate(papers, start=1):
    print(f"[{i}]")
    print(paper["title"])
    print(paper["authors"])
    print(f"{paper['journal']} ({paper['year']})")
    print()

print("========================================")
print(" End of Report")
print("========================================")