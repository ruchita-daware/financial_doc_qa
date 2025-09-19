import streamlit as st
import requests
import fitz  # PyMuPDF
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

st.set_page_config(page_title="Financial Doc Q&A", layout="wide")
st.title("📊 FinDocs AI: Financial Document Q&A with Streamlit + Ollama")

# -------------------------
# PDF Parser
# -------------------------
def parse_pdf_file(uploaded_file):
    text = ""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text("text")
    return text

# -------------------------
# File Upload
# -------------------------
uploaded_file = st.file_uploader("Upload a financial PDF", type=["pdf"])

if uploaded_file is not None:
    pdf_text = parse_pdf_file(uploaded_file)
    st.subheader("Extracted text (first 1000 characters)")
    st.text_area("Text", pdf_text[:1000], height=200)

    # -------------------------
    # Build Embeddings
    # -------------------------
    st.info("Building embeddings, please wait...")
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(pdf_text)

    embeddings = OllamaEmbeddings(model="llama3.2")
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

    # Save vectorstore for Q&A
    st.session_state['vectorstore'] = vectorstore
    st.success("✅ Embeddings created successfully! You can now ask questions.")

# -------------------------
# Q&A Section
# -------------------------
st.markdown("---")
st.subheader("Ask a question (LLM-powered Q&A)")

question = st.text_input("Type your question (e.g. What is the revenue in 2023?)")

if st.button("Get Answer") and question:
    vs = st.session_state.get('vectorstore')

    if vs:
        # 1. Retrieve relevant chunks
        results = vs.similarity_search(question, k=5)
        context_texts = [doc.page_content for doc in results]
        context = "\n".join(context_texts)

        # 2. Build prompt for Ollama
        prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer using only the context."

        # 3. Call Ollama API
        try:
            r = requests.post("http://localhost:11434/api/generate", json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            }, timeout=120)

            if r.status_code == 200:
                data = r.json()
                answer = data.get("response") or data.get("text")
                st.success(answer)
            else:
                st.error(f"Ollama error: {r.text}")
        except Exception as e:
            st.error(f"Could not reach Ollama: {e}")
    else:
        st.warning("⚠ No embeddings built yet. Please upload a PDF first.")
