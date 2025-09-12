from langchain_huggingface import HuggingFaceEmbeddings
from .config import EMBEDDING

def get_embeddings(model_name=EMBEDDING):
    return HuggingFaceEmbeddings(model_name=model_name)
