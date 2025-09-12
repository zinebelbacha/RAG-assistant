from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from .config import PINECONE_API_KEY
from .embeddings import get_embeddings
from .data_loader import load_and_split_documents
from .config import INDEX_NAME

INDEX_NAME = "rag-app"

def init_vectorstore():
    pc = Pinecone(api_key=PINECONE_API_KEY)

    if INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=INDEX_NAME,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        print(f"Index '{INDEX_NAME}' created.")
    else:
        print(f"Index '{INDEX_NAME}' already exists.")

    index = pc.Index(INDEX_NAME)
    docs = load_and_split_documents()
    embeddings = get_embeddings()

    vectorstore = PineconeVectorStore.from_documents(
        documents=docs,
        embedding=embeddings,
        index_name=INDEX_NAME
    )
    return vectorstore
