from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from .config import DATA_FILE

def load_and_split_documents(chunk_size=1000, chunk_overlap=4):
    loader = TextLoader(str(DATA_FILE))
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = splitter.split_documents(documents)
    return docs
