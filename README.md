# 🏗️ Ontario Permit Agent (Phase 1)

## Overview

Ontario Permit Agent is a **local-first Retrieval-Augmented Generation (RAG) application** that answers questions about Ontario building permits and codes using official PDF documents.

This project is designed as the foundation for an **agentic AI system**, where future phases will introduce tool usage, planning, and evaluation layers.

---

## Features (Phase 1)

* 📄 Upload and process PDF documents (Ontario Building Code, permits, etc.)
* 🔍 Semantic search using embeddings
* 🧠 Local LLM (via Ollama) for answer generation
* 📚 Source-aware answers with document citations (page numbers)
* 💻 Fully local — no paid API required

---

## Tech Stack

* Python
* ChromaDB
* SentenceTransformers
* Ollama
* Streamlit
* PyPDF

---

## Project Structure

```
ontario-permit-agent/
│
├── app.py                # Streamlit UI
├── ingest.py             # PDF ingestion and embedding
├── config.py             # Config values
│
├── tools/
│   └── rag_tool.py       # Document retrieval (RAG tool)
│
├── data/
│   └── pdfs/             # Add your PDFs here (ignored in git)
│
├── chroma_db/            # Vector database (ignored in git)
├── .env
└── README.md
```

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd ontario-permit-agent
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

*or manually:*

```bash
pip install streamlit chromadb sentence-transformers pypdf requests python-dotenv
```

---

## Install Ollama

Download and install Ollama, then run a model:

```bash
ollama run phi3
```

This starts a local API at:

```
http://localhost:11434
```

---

## Add Documents

Place your PDF files in:

```
data/pdfs/
```

Example:

* Ontario Building Code (Part 9)
* Local permit guidelines

---

## Ingest Documents

Run:

```bash
python ingest.py
```

This will:

* Extract text from PDFs
* Chunk the content
* Generate embeddings
* Store everything in ChromaDB

---

## Run the App

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## Example Questions

* Do I need a permit for a 10x16 shed?
* What are the rules for accessory structures?
* What is the maximum building height?
* What inspections are required?

---

## How It Works

```
User Question
      ↓
Embedding Search (ChromaDB)
      ↓
Relevant Document Chunks
      ↓
Prompt + Context
      ↓
Local LLM (Ollama)
      ↓
Answer with Citations
```

---

## Important Notes

* This is a **local-first system** — no external APIs required
* Answers are limited to provided documents (RAG)
* Not legal advice — informational use only

---

## Roadmap

### Phase 2

* Add tools (area calculator, checklist generator)

### Phase 3

* Convert to agent (tool selection + planning)

### Phase 4

* Add evaluation layer (accuracy, hallucination scoring)

---

## Portfolio Statement

> Built a local-first RAG system that answers Ontario building permit questions using ChromaDB, Hugging Face embeddings, and a locally hosted LLM via Ollama, with source-aware responses and no paid API dependency.

---

## License

MIT
