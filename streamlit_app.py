import streamlit as st
import requests

st.title("RAG Document Chatbot")

api_key = st.text_input("Enter your Groq API Key", type="password")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file and api_key:
    if st.button("Process PDF"):
        with st.spinner("Processing..."):
            response = requests.post("http://localhost:8000/upload", files={"file": uploaded_file}, data={"api_key": api_key})
            if response.status_code == 200:
                st.success("PDF processed! You can now ask questions.")
            else:
                st.error("Something went wrong.")

st.divider()
question = st.text_input("Ask a question about your document")

if question and api_key:
    if st.button("Ask"):
        with st.spinner("Thinking..."):
            response = requests.post("http://localhost:8000/ask", data={"question": question, "api_key": api_key})
            if response.status_code == 200:
                st.write("### Answer")
                st.write(response.json()["answer"])
            else:
                st.error("Something went wrong.")