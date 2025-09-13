# INPT Virtual Guide: RAG Assistant

## Overview

The INPT Virtual Guide is a Retrieval-Augmented Generation (RAG) system designed to assist visitors to the [Institut National des Postes et Télécommunications (INPT)](https://inpt.ac.ma) website. Built using Python and LangChain, the assistant answers questions about INPT’s programs, admissions, campus life, and more by retrieving relevant information from a knowledge base and generating friendly, engaging responses.


## Project Structure

```

RAD-Assistant/
│
├─ data/
│   └─ inpt.txt           # INPT documents
├─ src/
│   ├─ __init__.py
│   ├─ llm_wrapper.py     # LLM setup
│   ├─ rag_chain.py       # Main RAG pipeline
│   ├─ vectorstore.py     # Vector store setup
│   ├─ embeddings.py      
│   ├─ data_loader.py     # Document loader
│   └─ config.py          # Config & environment variables
│
├─ app.py                 # FastAPI entrypoint
├─ main.py                # Optional CLI script
├─ requirements.txt       # Python dependencies
├─ Dockerfile             # Docker instructions
└─ .dockerignore          # Files to ignore in Docker
```

## Tech Stack

- **Programming Language**: Python 3.11
- **Frameworks and Libraries**:
  - `langchain`: For RAG pipeline and Pinecone integration
  - `pinecone`: Cloud-based vector store
  - `sentence-transformers`: For document embeddings
- **Vector Store**: Pinecone
- **LLM**: Gemini-1.5-flash
- **Embedding Model**: Sentence-BERT (all-MiniLM-L6-v2, 384 dimensions)


## Setup Instructions

### Prerequisites
- Python 3.11+ or higher
- Gemini API key or any equivalent model
- Pinecone account with API key ([sign up here](https://www.pinecone.io/))
- Git (optional, for version control)
- Docker (optional, recommended for deployment)

### Setup
1. **Clone the Repository** (if using Git):
   ```bash
   git clone https://github.com/zinebelbacha/RAG-Assistant.git
   cd RAG-Assistant
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the project root:
     ```
     PINECONE_API_KEY=your-pinecone-api-key
     GEMINI_API_KEY=your-gemini-api-key
     ```

5. **Run the FastAPI app locally:**
   ```
   uvicorn app:app --reload
   ```
   - Visit http://localhost:8000/docs
 to test /ask endpoint.

### Docker Setup
1. **Build the Docker image:**
   ```
   docker build -t ragassistant .

   ```

2. **Run the container with environment variables:**
   ```
   docker run -p 8000:8000 --env-file .env ragassistant
   ```

3. **Access your API: http://localhost:8000/docs**
