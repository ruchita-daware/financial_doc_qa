# 📊 Financial Document Q&A Assistant

A Streamlit-based application that allows users to **upload financial PDFs**, extract text, build embeddings with FAISS, and ask **natural language questions**.  
Answers are generated using **Ollama (local LLM)** grounded in document context.

---

## 🚀 Features
- Upload **PDF financial reports**
- Extract text & preview
- Build **semantic embeddings** using FAISS + Sentence Transformers
- Ask **natural questions** (Revenue, Assets, Liabilities, etc.)
- Get answers from **Ollama models (Llama 3.2, etc.)**
- Clean Streamlit UI

---

## 🖥️ System Requirements
- **windows 10 ++, Windows 11 (64-bit)**
- **Python 3.9+**
- **Ollama for Windows** (installed & a model pulled, e.g., `llama3.2`)
- Disk space: ~8GB free (Ollama models are large)

---

## 📦 Installation

### 1. Clone the Repository
```powershell
git clone https://github.com/<ruchita-daware>financial-doc-qa.git
cd financial-doc-qa# financial_doc_qa
