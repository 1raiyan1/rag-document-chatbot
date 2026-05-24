from fastapi import FastAPI, UploadFile, File, Form
from app.rag import process_pdf, ask_question
import shutil
import os

app = FastAPI()
vectorstore = None

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...), api_key: str = Form(...)):
    global vectorstore
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    vectorstore = process_pdf(temp_path, api_key)
    os.remove(temp_path)
    return {"message": "PDF processed successfully!"}

@app.post("/ask")
async def ask(question: str = Form(...), api_key: str = Form(...)):
    global vectorstore
    if vectorstore is None:
        return {"error": "Please upload a PDF first!"}
    answer = ask_question(vectorstore, question, api_key)
    return {"answer": answer}