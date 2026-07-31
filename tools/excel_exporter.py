from openpyxl import Workbook


def export_to_excel(papers, filename="research_results.xlsx"):
    """
    Export research papers to an Excel spreadsheet.
    """

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Research Papers"

    # Header row
    sheet.append([
        "Title",
        "Authors",
        "Journal",
        "Year",
        "Study Design",
        "Key Findings",
        "Clinical Significance",
        "Limitations",
        "Keywords"
    ])

    # Data rows
    for paper in papers:

        summary = paper["summary"]

        sheet.append([
            paper["title"],
            paper["authors"],
            paper["journal"],
            paper["year"],
            summary,
            "",   # Key Findings (later)
            "",   # Clinical Significance (later)
            "",   # Limitations (later)
            ""    # Keywords (later)
        ])

    workbook.save(filename)

    print(f"\nExcel file saved as '{filename}'")