from agents.comparison_agent import compare_papers

print("===================================")
print("Radiotherapy Research Assistant")
print("AI Paper Comparison")
print("===================================\n")

query1 = input("Enter first research topic: ")
query2 = input("Enter second research topic: ")

compare_papers(query1, query2)