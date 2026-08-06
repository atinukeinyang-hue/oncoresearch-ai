from datetime import datetime
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt


def configure_document(document):
    """
    Apply document-wide formatting.
    """

    section = document.sections[0]

    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.9)
    section.right_margin = Inches(0.9)

    normal_style = document.styles["Normal"]
    normal_style.font.name = "Arial"
    normal_style.font.size = Pt(11)

    heading_one = document.styles["Heading 1"]
    heading_one.font.name = "Arial"
    heading_one.font.size = Pt(16)
    heading_one.font.bold = True

    heading_two = document.styles["Heading 2"]
    heading_two.font.name = "Arial"
    heading_two.font.size = Pt(13)
    heading_two.font.bold = True


def add_cover_page(document, query):
    """
    Add a professional cover page.
    """

    title = document.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    title_run = title.add_run(
        "Radiotherapy Research Assistant"
    )
    title_run.bold = True
    title_run.font.size = Pt(24)

    subtitle = document.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

    subtitle_run = subtitle.add_run(
        "PubMed Research Report"
    )
    subtitle_run.italic = True
    subtitle_run.font.size = Pt(16)

    document.add_paragraph()

    topic_heading = document.add_paragraph()
    topic_heading.alignment = WD_ALIGN_PARAGRAPH.CENTER

    topic_heading_run = topic_heading.add_run(
        "Research Topic"
    )
    topic_heading_run.bold = True
    topic_heading_run.font.size = Pt(13)

    topic = document.add_paragraph()
    topic.alignment = WD_ALIGN_PARAGRAPH.CENTER

    topic_run = topic.add_run(query)
    topic_run.font.size = Pt(12)

    document.add_paragraph()

    generated = document.add_paragraph()
    generated.alignment = WD_ALIGN_PARAGRAPH.CENTER

    generated_run = generated.add_run(
        "Generated: "
        f"{datetime.now().strftime('%d %B %Y, %I:%M %p')}"
    )
    generated_run.font.size = Pt(10)

    version = document.add_paragraph()
    version.alignment = WD_ALIGN_PARAGRAPH.CENTER

    version_run = version.add_run(
        "Application Version: 1.0"
    )
    version_run.font.size = Pt(10)

    document.add_page_break()


def add_label_value(document, label, value):
    """
    Add a bold label followed by its value.
    """

    paragraph = document.add_paragraph()

    label_run = paragraph.add_run(f"{label}: ")
    label_run.bold = True
    label_run.font.size = Pt(11)

    value_run = paragraph.add_run(str(value))
    value_run.font.size = Pt(11)

    paragraph.paragraph_format.space_after = Pt(6)


def add_summary_section(document, summary):
    """
    Add Claude's structured analysis for one paper.
    """

    document.add_heading("Claude Analysis", level=2)

    if not isinstance(summary, dict):
        document.add_paragraph(
            "Structured AI analysis was not available."
        )
        return

    add_label_value(
        document,
        "Study Design",
        summary.get("study_design", "Not specified")
    )

    add_label_value(
        document,
        "Key Findings",
        summary.get("key_findings", "Not specified")
    )

    add_label_value(
        document,
        "Clinical Significance",
        summary.get(
            "clinical_significance",
            "Not specified"
        )
    )

    add_label_value(
        document,
        "Limitations",
        summary.get("limitations", "Not specified")
    )

    keywords = summary.get("keywords", [])

    if isinstance(keywords, list):
        keywords = ", ".join(str(item) for item in keywords)

    add_label_value(
        document,
        "Keywords",
        keywords or "Not specified"
    )


def add_paper(document, paper, index):
    """
    Add one PubMed paper and its Claude analysis.
    """

    document.add_heading(
        f"Paper {index}",
        level=1
    )

    add_label_value(
        document,
        "Title",
        paper.get("title", "Unknown")
    )

    add_label_value(
        document,
        "Authors",
        paper.get("authors", "Unknown")
    )

    add_label_value(
        document,
        "Journal",
        paper.get("journal", "Unknown")
    )

    add_label_value(
        document,
        "Year",
        paper.get("year", "Unknown")
    )

    document.add_heading("Abstract", level=2)

    abstract = paper.get(
        "abstract",
        "No abstract available."
    )

    abstract_paragraph = document.add_paragraph(
        str(abstract)
    )
    abstract_paragraph.paragraph_format.space_after = Pt(8)
    abstract_paragraph.paragraph_format.line_spacing = 1.15

    add_summary_section(
        document,
        paper.get("summary", {})
    )

    document.add_paragraph()
    document.add_paragraph("-" * 70)
    document.add_paragraph()


def add_footer(document):
    """
    Add a footer to every section.
    """

    for section in document.sections:
        footer = section.footer

        paragraph = footer.paragraphs[0]
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        run = paragraph.add_run(
            "Generated by Radiotherapy Research Assistant v1.0"
        )
        run.font.size = Pt(9)


def export_pubmed_report(query, papers):
    """
    Export PubMed search results and Claude analyses
    to a professionally formatted Word document.
    """

    output_folder = Path("outputs")
    output_folder.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    filename = (
        output_folder
        / f"pubmed_report_{timestamp}.docx"
    )

    document = Document()

    configure_document(document)
    add_cover_page(document, query)

    for index, paper in enumerate(papers, start=1):
        add_paper(
            document=document,
            paper=paper,
            index=index
        )

    add_footer(document)

    document.save(filename)

    return str(filename)