from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

BASE_DIR = Path(__file__).resolve().parent.parent # project root

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
DATA_FILE = BASE_DIR / "data" / "inpt.txt"

LLM = "gemini-1.5-flash"
EMBEDDING= "sentence-transformers/all-MiniLM-L6-v2"
INDEX_NAME = "rag-app"