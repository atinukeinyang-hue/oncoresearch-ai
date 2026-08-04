from datetime import datetime
from pathlib import Path

from docx import Document
from docx.shared import Pt


def export_rag_report(question, answer, papers):
    """
    Export the RAG research answer and references to a Word document.
    """

    output_folder = Path("outputs")
    output_folder.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = output_folder / f"research_report_{timestamp}.docx"

    document = Document()

    title = document.add_heading(
        "Radiotherapy Research Assistant",
        level=0
    )
    title.alignment = 1

    document.add_paragraph(
        f"Generated: {datetime.now().strftime('%d %B %Y, %I:%M %p')}"
    )

    document.add_heading("Research Question", level=1)
    document.add_paragraph(question)

    document.add_heading("AI Research Summary", level=1)

    for paragraph_text in answer.split("\n"):
        paragraph_text = paragraph_text.strip()

        if paragraph_text:
            paragraph = document.add_paragraph(paragraph_text)

            for run in paragraph.runs:
                run.font.size = Pt(11)

    document.add_heading("References", level=1)

    for index, paper in enumerate(papers, start=1):
        reference = (
            f"[{index}] {paper['title']}\n"
            f"{paper['authors']}\n"
            f"{paper['journal']} ({paper['year']})"
        )

        document.add_paragraph(reference)

    document.save(filename)

    return str(filename)