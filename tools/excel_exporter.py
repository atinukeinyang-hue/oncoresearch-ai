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

        summary = paper.get("summary", {})

        # If summary is not a dictionary, convert it to an empty one
        if not isinstance(summary, dict):
            summary = {}

        sheet.append([
            paper.get("title", ""),
            paper.get("authors", ""),
            paper.get("journal", ""),
            paper.get("year", ""),
            summary.get("study_design", ""),
            summary.get("key_findings", ""),
            summary.get("clinical_significance", ""),
            summary.get("limitations", ""),
            ", ".join(summary.get("keywords", []))
        ])

    workbook.save(filename)

    print(f"\nExcel file saved as '{filename}'")