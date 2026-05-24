# RAG Document Chatbot 🤖

An AI-powered chatbot that lets you upload any PDF and ask questions about it using Retrieval-Augmented Generation (RAG).

🔗 **Live Demo:** [https://rag-document-chatbot-34w9tqdapgsajwlajejxxm.streamlit.app](https://rag-document-chatbot-34w9tqdapgsajwlajejxxm.streamlit.app)

## Features
- Upload any PDF document
- Ask questions in natural language
- Get accurate answers based on document content
- Powered by Groq LLM (free & fast)

## Tech Stack
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Vector Store:** FAISS
- **LLM:** Groq (Llama 3.1)
- **Framework:** LangChain

## How to Run Locally

1. Clone the repo
2. Create a virtual environment and install dependencies:
```bash
pip install -r requirements.txt
```
3. Run FastAPI backend:
```bash
uvicorn app.main:app --reload
```
4. Run Streamlit frontend:
```bash
streamlit run streamlit_app.py
```
5. Open http://localhost:8501 and enter your Groq API key

## Demo
Upload any PDF → Ask questions → Get instant answers!
