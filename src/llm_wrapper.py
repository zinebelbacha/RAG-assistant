from langchain_google_genai import ChatGoogleGenerativeAI
from .config import GOOGLE_API_KEY, LLM

def get_llm(model=LLM):
    return ChatGoogleGenerativeAI(model=model, api_key=GOOGLE_API_KEY)
