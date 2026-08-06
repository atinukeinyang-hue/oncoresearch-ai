from agents.research_agent import research
from agents.comparison_agent import compare_papers
from rag.retrieve import retrieve_papers
from rag.rag_client import generate_rag_answer
from rag.report_exporter import export_rag_report


def run_rag_assistant():
    question = input("\nAsk a research question:\n\n> ").strip()

    if not question:
        print("\nPlease enter a research question.")
        return

    print("\nSearching the knowledge base...\n")

    papers = retrieve_papers(question)

    if not papers:
        print("No relevant papers were found.")
        return

    print(f"Retrieved {len(papers)} relevant papers.")
    print("\nGenerating an evidence-based answer...\n")

    answer = generate_rag_answer(question, papers)

    print("\n" + "=" * 60)
    print("AI RESEARCH SUMMARY")
    print("=" * 60 + "\n")

    print(answer)

    print("\n" + "=" * 60)
    print("SUPPORTING REFERENCES")
    print("=" * 60 + "\n")

    for index, paper in enumerate(papers, start=1):
        print(f"[{index}]")
        print(paper["title"])
        print(paper["authors"])
        print(f"{paper['journal']} ({paper['year']})")
        print()

    report_path = export_rag_report(
        question=question,
        answer=answer,
        papers=papers
    )

    print(f"Word report saved as: {report_path}")


def show_menu():
    print("\n" + "=" * 55)
    print("RADIOTHERAPY RESEARCH ASSISTANT v1.0")
    print("=" * 55)
    print("1. Search and analyse PubMed papers")
    print("2. Compare two research topics")
    print("3. Ask the RAG Research Assistant")
    print("4. Exit")
    print("=" * 55)


def main():
    while True:
        show_menu()

        choice = input("\nChoose an option (1–4): ").strip()

        try:
            if choice == "1":
                query = input("\nEnter a PubMed research topic: ").strip()

                if query:
                    research(query)
                else:
                    print("\nPlease enter a research topic.")

            elif choice == "2":
                query1 = input(
                    "\nEnter the first research topic: "
                ).strip()

                query2 = input(
                    "Enter the second research topic: "
                ).strip()

                if query1 and query2:
                    compare_papers(query1, query2)
                else:
                    print("\nPlease enter both research topics.")

            elif choice == "3":
                run_rag_assistant()

            elif choice == "4":
                print("\nThank you for using the Research Assistant.")
                break

            else:
                print("\nInvalid option. Please choose 1, 2, 3, or 4.")

        except Exception as error:
            print(f"\nAn error occurred: {error}")

        if choice != "4":
            input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    main()