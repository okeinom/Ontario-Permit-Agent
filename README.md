# 🏗️ Ontario Permit Agent

## Overview

Ontario Permit Agent is a **local-first, agentic RAG system** that answers Ontario building permit and code questions using official PDF documents.

Unlike a basic chatbot, this system:

* Retrieves grounded information from documents
* Uses tools (calculation, classification, checklist)
* Dynamically decides which tools to run per question

---

## Features

* 📄 PDF ingestion and semantic search
* 🧠 Local LLM via Ollama (no paid API required)
* 🔍 Context-aware answers with citations
* 🛠️ Tool-based architecture:

  * Structure classification
  * Area calculation
  * Checklist generation
* 🤖 Lightweight agent planner (dynamic tool selection)

---

## Tech Stack

* Python
* ChromaDB
* SentenceTransformers
* Ollama
* Streamlit
* PyPDF

---

## Architecture

```text
User Question
      ↓
Agent Planner (LLM)
      ↓
Tool Selection
      ↓
Tools:
 - search_building_docs (RAG)
 - classify_structure
 - calculate_area
 - generate_checklist
      ↓
Context + Tool Outputs
      ↓
Local LLM (Ollama)
      ↓
Final Answer + Citations
```

---

## Project Structure

```text
ontario-permit-agent/
│
├── app.py                # Streamlit UI
├── agent.py              # Agent orchestrator
├── llm.py                # LLM interaction (Ollama)
├── ingest.py             # PDF ingestion
├── config.py             # Configuration
│
├── tools/
│   ├── rag_tool.py
│   ├── calculator_tool.py
│   ├── classifier_tool.py
│   └── checklist_tool.py
│
├── data/pdfs/            # Add PDFs here (gitignored)
├── chroma_db/            # Vector DB (gitignored)
└── README.md
```

---

## Setup

### 1. Clone

```bash
git clone https://github.com/okeinom/Ontario-Permit-Agent
cd Ontario-Permit-Agent
```

### 2. Virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Run a local model:

```bash
ollama run phi3
```

This exposes a local API:

```text
http://localhost:11434
```

---

## Add Documents

Place PDFs in:

```text
data/pdfs/
```

---

## Ingest Documents

```bash
python ingest.py
```

---

## Run App

```bash
streamlit run app.py
```

---

## Example Questions

* Do I need a permit for a 10x16 shed?
* What is the maximum height for a shed?
* What are the rules for accessory structures?

---

## How It Works

```text
PDF → chunks → embeddings → ChromaDB
         ↓
User question → embedding search
         ↓
Relevant document context
         ↓
Agent decides tools
         ↓
Tools run (optional)
         ↓
LLM generates grounded answer
```
---

## Roadmap

* Add evaluation layer (accuracy + hallucination scoring)
* Improve planner reliability
* Add more domain-specific tools
* Optional: integrate LangChain or LlamaIndex

---

## License

MIT
