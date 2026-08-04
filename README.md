# 🩺 OncoResearch AI

### *An Evidence-Based AI Research Assistant for Radiotherapy and Medical Physics*

OncoResearch AI is an AI-powered Retrieval-Augmented Generation (RAG) research assistant designed to help clinicians, medical physicists, researchers, and students rapidly explore the scientific literature.

The application searches PubMed, builds a local semantic knowledge base using ChromaDB, retrieves the most relevant research papers, generates evidence-based answers using Claude AI, compares scientific publications, and exports professionally formatted research reports.

---

## 🚀 Project Highlights

- 🔍 Live PubMed research search
- 🤖 AI-powered paper analysis with Claude Sonnet
- ⚖️ AI comparison of research papers
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 ChromaDB semantic vector database
- 📑 Evidence-grounded AI answers
- 📄 Professional Microsoft Word report generation
- 📊 Excel research report export
- 🖥️ Interactive menu-driven application

---

# 🏗 System Architecture

```text
                     User

                       │

                 app.py Menu

       ┌───────────────┼────────────────┐

       ▼               ▼                ▼

 PubMed Search   Paper Comparison   RAG Assistant

       │               │                │

       ▼               ▼                ▼

  PubMed API      Claude Sonnet     ChromaDB

                       │

                       ▼

        Evidence-Based Research Summary

                       │

             ┌─────────┴─────────┐

             ▼                   ▼

      Word Report          Excel Report
```

---

# 💻 Technology Stack

## Programming

- Python

## Artificial Intelligence

- Claude Sonnet API
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)

## Vector Database

- ChromaDB

## Data Sources

- PubMed API

## Data Processing

- XML Parsing
- JSON Processing

## Document Generation

- python-docx
- openpyxl

## Development

- Git
- GitHub
- VS Code

---

# ✨ Features

## 📖 Literature Search

Search PubMed directly from the application.

---

## 🧠 AI Paper Analysis

Claude AI automatically extracts:

- Study Design
- Key Findings
- Clinical Significance
- Limitations
- Keywords

---

## ⚖️ AI Paper Comparison

Compare two research topics and receive:

- Similarities
- Differences
- Strengths
- Weaknesses
- Clinical relevance
- Overall conclusion

---

## 📚 Retrieval-Augmented Generation (RAG)

Instead of answering from memory, the assistant:

1. Searches a local ChromaDB knowledge base.
2. Retrieves the most relevant papers.
3. Sends only those papers to Claude.
4. Generates an evidence-based research summary.

---

## 📄 Professional Report Generation

Automatically generates:

- Microsoft Word reports
- Excel reports

Including:

- Research Question
- AI Summary
- References
- Generation Date

---

# 📂 Project Structure

```text
OncoResearch-AI/

│

├── agents/

├── rag/

├── tools/

├── outputs/

│ ├── word_reports/

│ ├── excel_reports/

│

├── docs/

├── data/

├── app.py

└── README.md
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/OncoResearch-AI.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
ANTHROPIC_API_KEY=your_api_key_here
```

Run the application

```bash
python app.py
```

---

# 🖥 Application Menu

```
===========================================
OncoResearch AI
===========================================

1. Search and analyse PubMed papers

2. Compare two research topics

3. Ask the AI Research Assistant (RAG)

4. Exit
```

---

# 🧪 Skills Demonstrated

This project demonstrates practical experience with:

- REST API integration
- XML parsing
- JSON processing
- Prompt engineering
- Claude API integration
- Vector databases
- Semantic search
- Retrieval-Augmented Generation (RAG)
- AI workflow orchestration
- Microsoft Word automation
- Excel automation
- Git branching workflow
- Professional software architecture

---

# 🛣 Development Timeline

| Sprint | Feature |
|---------|---------|
| Sprint 1 | Project Foundation |
| Sprint 2 | PubMed Integration |
| Sprint 3 | Claude AI Analysis |
| Sprint 4 | Excel Export |
| Sprint 5 | AI Paper Comparison |
| Sprint 6 | ChromaDB + Complete RAG Pipeline |
| Sprint 7 | Professional Word Report Export |
| Sprint 8 | Interactive Application Menu |

---

# 🚀 Version Roadmap

## ✅ Version 1.0

- PubMed Integration
- Claude AI
- ChromaDB
- Semantic Search
- RAG
- Word Reports
- Excel Reports
- Interactive Menu

### Planned for Version 2.0

- PDF report export
- Conversation memory
- Medical imaging support
- Multi-agent research workflows
- Clinical guideline integration
- Web application interface

---

# 👩‍💻 Author

**Atinuke A. Inyang**

Medical Physicist • AI Engineer • Researcher

Building AI systems for radiotherapy, medical physics, and evidence-based clinical research.

---

# 📄 License

MIT License