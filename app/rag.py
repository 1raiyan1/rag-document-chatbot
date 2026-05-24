from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings
from groq import Groq
import os

def process_pdf(pdf_path, groq_api_key):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    docs = [Document(page_content=c) for c in chunks]
    
    embeddings = FakeEmbeddings(size=384)
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

def ask_question(vectorstore, question, groq_api_key):
    client = Groq(api_key=groq_api_key)
    
    docs = vectorstore.similarity_search(question, k=4)
    context = "\n".join([d.page_content for d in docs])
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Answer questions based on the provided context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
        ]
    )
    return response.choices[0].message.content