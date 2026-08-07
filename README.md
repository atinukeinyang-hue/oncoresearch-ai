# 🩺 OncoResearch AI

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-Sonnet-D97706?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20DB-16A34A?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Evidence%20Grounded-DC2626?style=for-the-badge)
![PubMed](https://img.shields.io/badge/PubMed-NCBI-2563EB?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-059669?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-v1.0.1-7C3AED?style=for-the-badge)

> 🚧 **Project Status:** Active Development (Version 1.0.1)
>
> This project is actively maintained, with additional AI capabilities planned for future releases.

## *An Evidence-Based AI Research Assistant for Radiotherapy and Medical Physics*

**OncoResearch AI** is an AI-powered **Retrieval-Augmented Generation (RAG)** research assistant designed to help clinicians, medical physicists, researchers, and students explore scientific literature more efficiently.

The application searches **PubMed**, builds a local semantic knowledge base using **ChromaDB**, retrieves relevant research papers, generates evidence-grounded answers using **Claude Sonnet**, compares research topics, and exports professionally formatted research reports.

> **Important:** OncoResearch AI is a research and educational software project. It is not clinically validated and is not intended for patient-specific clinical decision-making.

---

## ⚡ Quick Start

Clone the repository:

```bash
git clone https://github.com/atinukeinyang-hue/oncoresearch-ai.git
cd oncoresearch-ai
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Create your local environment file.

**Windows PowerShell:**

```powershell
Copy-Item .env.example .env
```

**macOS/Linux:**

```bash
cp .env.example .env
```

Open `.env` and add your Anthropic API key:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

> Never commit your real `.env` file or API key to GitHub.

Before using the **RAG Research Assistant**, build the local knowledge base:

```bash
python rag/build_vector_db.py
```

Launch OncoResearch AI:

```bash
python app.py
```

---

## 📚 Table of Contents

- [Why OncoResearch AI?](#why-oncoresearch-ai)
- [Project Highlights](#-project-highlights)
- [Application Preview](#-application-preview)
- [System Architecture](#️-system-architecture)
- [Installation](#️-installation)
- [Usage Guide](#️-usage-guide)
- [Project Structure](#-project-structure)
- [Technologies Used](#️-technologies-used)
- [Key Skills Demonstrated](#-key-skills-demonstrated)
- [Research and Education Applications](#-research-and-education-applications)
- [Roadmap](#️-roadmap)
- [Acknowledgements](#-acknowledgements)
- [About the Author](#-about-the-author)
- [License](#-license)

---

## Why OncoResearch AI?

Medical literature is expanding rapidly, making it increasingly difficult for clinicians, medical physicists, researchers, and students to stay current with relevant scientific evidence.

OncoResearch AI was developed to streamline evidence-based literature exploration by combining live PubMed retrieval, AI-assisted analysis, Retrieval-Augmented Generation (RAG), semantic retrieval using ChromaDB, and automated report generation within a single research workflow.

The project demonstrates how modern AI engineering techniques can support scientific research while reducing repetitive work involved in identifying, analyzing, comparing, and summarizing biomedical publications.

---

## 🚀 Project Highlights

- 🔍 **Live PubMed research search**
- 🤖 **AI-powered paper analysis with Claude Sonnet**
- ⚖️ **Research-topic comparison**
- 🧠 **Retrieval-Augmented Generation (RAG)**
- 📚 **ChromaDB semantic retrieval**
- 📑 **Evidence-grounded AI responses**
- 📄 **Professional Microsoft Word report generation**
- 📊 **Microsoft Excel research export**
- 🖥️ **Interactive menu-driven application**
- 🧩 **Modular Python architecture**

---

## 📸 Application Preview

### Main Menu

![OncoResearch AI Main Menu](docs/screenshots/menu.png)

---

### Retrieval-Augmented Generation (RAG)

![OncoResearch AI RAG Answer](docs/screenshots/rag_answer.png)

---

### AI Paper Comparison

![OncoResearch AI Paper Comparison](docs/screenshots/paper_comparison.png)

---

### Professional Word Report

![OncoResearch AI Word Report](docs/screenshots/word_report.png)

---

## 🏗️ System Architecture

The diagram below illustrates the high-level architecture of **OncoResearch AI** and how the major components work together to support evidence-based research workflows.

<p align="center">
  <img src="docs/architecture.png" alt="OncoResearch AI System Architecture">
</p>

---

## ⚙️ Installation

### Requirements

- Python 3.11 recommended
- Git
- Internet access for PubMed and external API requests
- Anthropic API key for Claude-powered features

### Clone the repository

```bash
git clone https://github.com/atinukeinyang-hue/oncoresearch-ai.git
```

Navigate into the project:

```bash
cd oncoresearch-ai
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### Configure the environment file

Create your local `.env` file from the provided `.env.example` template.

**Windows PowerShell:**

```powershell
Copy-Item .env.example .env
```

**macOS/Linux:**

```bash
cp .env.example .env
```

Open `.env` and add your Anthropic API key:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

> Keep your real `.env` file private. It is excluded from Git tracking and should never be committed.

### Initialize the RAG knowledge base

Before using the **RAG Research Assistant**, run:

```bash
python rag/build_vector_db.py
```

Enter a PubMed research topic when prompted.

The builder retrieves PubMed literature and creates or loads the local ChromaDB collection:

```text
pubmed_papers
```

The persistent database is stored locally in:

```text
vector_db/
```

### Launch the application

```bash
python app.py
```

---

## ▶️ Usage Guide

After installation, launch the application:

```bash
python app.py
```

The Version 1.0 application menu provides four options:

```text
=======================================================
RADIOTHERAPY RESEARCH ASSISTANT v1.0
=======================================================

1. Search and analyse PubMed papers
2. Compare two research topics
3. Ask the RAG Research Assistant
4. Exit

=======================================================
```

### 1. Search and Analyse PubMed Papers

Choose:

```text
1
```

Enter a PubMed research topic.

Example:

```text
HDR brachytherapy cervical cancer
```

The workflow retrieves relevant PubMed literature, performs AI-assisted analysis, and generates structured research outputs.

### 2. Compare Two Research Topics

Choose:

```text
2
```

Enter two research topics when prompted.

The comparison workflow retrieves relevant literature and produces an AI-assisted comparison of the available research evidence.

### 3. Ask the RAG Research Assistant

Before using this feature, initialize the local knowledge base:

```bash
python rag/build_vector_db.py
```

Then launch:

```bash
python app.py
```

Choose:

```text
3
```

Enter a research question.

Example:

```text
What are recent advances in HDR brachytherapy for cervical cancer?
```

The application searches the local ChromaDB knowledge base, retrieves relevant papers, and provides those papers as context to Claude for an evidence-grounded response.

If the RAG knowledge base has not been initialized, the application provides setup guidance instead of terminating during startup.

### 4. Exit

Choose:

```text
4
```

to close the application.

### Professional Research Outputs

OncoResearch AI supports:

- Microsoft Word research reports (`.docx`)
- Microsoft Excel research exports (`.xlsx`)
- Structured command-line output

---

## 📁 Project Structure

```text
oncoresearch-ai/
│
├── agents/                       # Research and comparison agents
├── docs/                         # Documentation, architecture, screenshots
├── outputs/                      # Generated research outputs
├── rag/                          # Retrieval-Augmented Generation pipeline
├── tools/                        # PubMed, Claude, and export utilities
│
├── .env.example                  # Environment variable template
├── .gitignore                    # Git ignore rules
├── LICENSE                       # MIT License
├── README.md                     # Project documentation
├── app.py                        # Main application entry point
├── requirements.txt              # Python dependencies
└── sample_research_results.xlsx  # Example research export
```

### Local Runtime Files

The following are created locally when the project is configured or used and are **not part of the distributed source repository**:

```text
.env
vector_db/
research_results.xlsx
```

- `.env` stores the user's private Anthropic API key.
- `vector_db/` stores the persistent local ChromaDB knowledge base.
- `research_results.xlsx` is a generated research-output file.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| --- | --- |
| **Python 3.11** | Core application development |
| **NCBI PubMed API** | Biomedical literature retrieval |
| **Anthropic Claude Sonnet** | AI-assisted scientific analysis and RAG generation |
| **ChromaDB** | Persistent local vector storage and semantic retrieval |
| **Retrieval-Augmented Generation (RAG)** | Evidence-grounded research question answering |
| **Requests** | HTTP and API communication |
| **XML / ElementTree** | Processing structured PubMed responses |
| **OpenPyXL** | Microsoft Excel export |
| **python-docx** | Microsoft Word report generation |
| **Git** | Version control |
| **GitHub** | Open-source repository and release management |
| **VS Code** | Development environment |

---

## 🧠 Key Skills Demonstrated

- Python application development
- Modular software architecture
- REST API integration
- Biomedical literature retrieval
- XML and structured-data processing
- Environment-variable management
- External LLM API integration
- Prompt engineering
- Retrieval-Augmented Generation (RAG)
- Vector databases
- Semantic retrieval
- Exception handling
- Dependency management
- Reproducible Python environments
- Microsoft Word automation
- Microsoft Excel automation
- Git version control
- GitHub repository management
- Technical documentation
- Clean-environment testing and debugging

---

## 🔬 Research and Education Applications

- Evidence-based literature review
- Radiotherapy research
- Medical physics research and education
- Clinical guideline literature exploration
- Research paper comparison
- AI-assisted research report generation
- Scientific knowledge retrieval

> **Note:** OncoResearch AI is a research and educational tool. It is not clinically validated and is not intended for patient-specific clinical decision-making.

---

## 🗺️ Roadmap

### ✅ Version 1.0 — Core Feature Release

Version 1.0 introduced:

- Live PubMed integration
- AI-powered paper analysis
- Research-topic comparison
- Retrieval-Augmented Generation (RAG)
- ChromaDB semantic retrieval
- Evidence-grounded AI responses
- Professional Microsoft Word report generation
- Microsoft Excel export
- Interactive command-line application
- Project documentation

### 🛠️ Version 1.0.1 — Maintenance and Reproducibility Update

Version 1.0.1 improves the reliability and reproducibility of the Version 1.0 release through:

- Corrected dependency declarations
- Removal of unused LangChain and LangGraph dependencies
- Improved handling of an uninitialized RAG knowledge base
- Delayed Claude API initialization until Claude-powered functionality is used
- Improved environment configuration handling
- Clean-environment dependency verification
- Fresh-clone application testing
- Improved README and setup documentation
- Generated-output Git cleanup

### 🚀 Planned for Version 2.0

Potential future development includes:

- PDF research-paper ingestion
- Multi-LLM support
- Clinical-guideline research assistant
- Citation-management features
- Web-based interface
- User authentication
- Research-history storage
- API layer
- Docker containerization
- Cloud deployment

Future capabilities will be added incrementally and documented when implemented.

---

## 🙏 Acknowledgements

This project makes use of open-source libraries and external services including:

- NCBI PubMed
- Anthropic Claude API
- ChromaDB
- OpenPyXL
- python-docx
- Python Requests

---

## 👩🏽‍💻 About the Author

Developed by **Atinuke Inyang**.

Medical Physicist exploring AI engineering for radiotherapy, medical physics research, medical AI, and evidence-based research automation.

This project forms part of a broader portfolio focused on combining medical physics domain knowledge with Python, APIs, Retrieval-Augmented Generation (RAG), vector databases, and modern AI-assisted research workflows.

- GitHub: [atinukeinyang-hue](https://github.com/atinukeinyang-hue)
- LinkedIn: [Atinuke Inyang](https://www.linkedin.com/in/atinukeinyang/)

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software in accordance with the terms of the MIT License.

See the [LICENSE](LICENSE) file for details.

---

⭐ **If you find OncoResearch AI useful or interesting, consider starring the repository.**