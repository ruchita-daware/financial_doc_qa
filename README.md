# 🧠 FinDocs AI: Financial Document Q&A with Streamlit + Ollama

## Project Overview
This project allows you to run a **Large Language Model (LLM)** locally using **Ollama** to answer questions from financial PDF documents. 
All functionality is consolidated into a **single Python file (`app.py`)**, making it easy to set up and use.

## Features
- Upload financial PDFs and extract text.
- Split text into chunks and build embeddings using Ollama.
- Ask questions about the PDF content with LLM-powered answers.
- Everything runs in **one script** – no additional parser files needed.
- Streamlit-based user interface.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/<ruchita-daware>/<repo-name>.git
2. **Navigate to the project folder**:
cd <repo-name>

3.**Install required packages**:

pip install -r requirements.txt

4.**Ensure Ollama is installed and running locally at http://localhost:11434.**

**Usage**

Run the Streamlit app:

streamlit run app.py

-**Upload a financial PDF.**

-**Wait for embeddings to be created.**

-**Ask questions about the document in the input box.**

-**Get LLM-powered answers instantly.**
-**Example:**

-**Enter your question: What is the revenue in 2024?**

-**Response: The revenue in 2024 is $5.6 million according to the uploaded PDF document.**

