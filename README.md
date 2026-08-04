## 🚀 Sprint 5 – AI Paper Comparison Engine

### Features Implemented

✅ Compare two PubMed research papers using AI

The comparison includes:

- Study Design
- Key Differences
- Key Similarities
- Clinical Significance
- Strengths
- Limitations
- Overall Conclusion

### Technologies Used

- Python
- Anthropic Claude API
- PubMed API
- JSON Processing

### Status

✅ Completed

*Screenshot coming in the next update.*


## Sprint 6 – Retrieval-Augmented Generation (RAG)

### ✅ Local Vector Database

- Integrated ChromaDB as the local vector database.
- Built a persistent knowledge base from PubMed research papers.
- Stored paper abstracts together with metadata including title, authors, journal, and publication year.

### ✅ Semantic Retrieval

- Implemented semantic similarity search using ChromaDB.
- Users can ask research questions in natural language.
- The system retrieves the most relevant papers from the local knowledge base instead of querying PubMed every time.

### ✅ Retrieval-Augmented Generation (RAG)

- Built a complete Retrieval-Augmented Generation pipeline.
- Integrated ChromaDB for local semantic search.
- Retrieves the most relevant PubMed papers.
- Uses Claude Sonnet to generate evidence-based research summaries from retrieved literature.
- Produces structured clinical insights instead of returning raw abstracts.

### ✅ Evidence Grounding

- Displays the retrieved research papers used to generate each AI answer.
- Lists supporting references including title, authors, journal, and publication year.
- Improves transparency and trustworthiness of generated research summaries.

## Sprint 7 – Professional Report Export

### ✅ Microsoft Word Report Generation

- Automatically exports every AI-generated research answer to a professionally formatted Microsoft Word document.
- Reports include:
  - Research Question
  - AI Research Summary
  - References
  - Generation Date
- Saves reports into an `outputs/` folder with unique timestamps.