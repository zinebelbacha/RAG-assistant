from fastapi import FastAPI
from pydantic import BaseModel
from src.rag_chain import ask_question

app = FastAPI(title="RAG Assistant")

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):
    answer = ask_question(query.question)
    return {"answer": answer}
