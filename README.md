# BFSI Call Center AI Assistant

## Project Overview

This project implements a lightweight, compliant AI assistant for handling Banking, Financial Services, and Insurance (BFSI) call center queries.

The system prioritizes curated dataset responses and uses retrieval for complex financial queries, ensuring compliance and safety.

---

## Architecture Flow

User Query  
↓  
Guardrails (Security & Compliance Check)  
↓  
Tier 1: Dataset Similarity Match (FAISS + Sentence Transformers)  
↓  
Tier 3: RAG Retrieval (if no strong dataset match)  
↓  
Final Response  

---

## Core Features

- 150+ Alpaca-formatted BFSI dataset
- Local embedding-based similarity search
- FAISS vector indexing
- Retrieval-Augmented Generation (RAG) layer
- Security guardrails (out-of-domain + sensitive data protection)
- Fully local execution

---

## How to Run

1. Create virtual environment:
python -m venv venv
venv\Scripts\activate.bat

2. Install dependencies:
pip install -r requirements.txt

3. Run assistant:
python app.py

---

## Compliance Features

- No guessing financial numbers
- No fake policy generation
- No exposure of sensitive personal data
- Strict domain filtering

---

## Tech Stack

- Python
- SentenceTransformers
- FAISS
- Torch
