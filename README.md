# INPT Virtual Guide: RAG Assistant

## Overview

The INPT Virtual Guide is a Retrieval-Augmented Generation (RAG) system designed to assist visitors to the [Institut National des Postes et Télécommunications (INPT)](https://inpt.ac.ma) website. Built using Python and LangChain, the assistant answers questions about INPT’s programs, admissions, campus life, and more by retrieving relevant information from a knowledge base and generating friendly, engaging responses.


## Tech Stack

- **Programming Language**: Python 3.11
- **Frameworks and Libraries**:
  - `langchain-pinecone`: For RAG pipeline and Pinecone integration
  - `pinecone`: Cloud-based vector store
  - `sentence-transformers`: For document embeddings (all-MiniLM-L6-v2)
- **Environment**: Jupyter Notebook
- **Vector Store**: Pinecone (serverless, AWS us-east-1)
- **LLM**: Gemini-1.5-flash
- **Embedding Model**: Sentence-BERT (all-MiniLM-L6-v2, 384 dimensions)


## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook (`pip install jupyter`)
- Gemini API key or any equivalent model
- Pinecone account with API key ([sign up here](https://www.pinecone.io/))
- Git (optional, for version control)

### Installation
1. **Clone the Repository** (if using Git):
   ```bash
   git clone https://github.com/zinebelbacha/RAG-Application.git
   cd RAG-application
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
   - Load the `.env` file in the notebook using `python-dotenv`.

5. **Prepare the Knowledge Base**:
   - The current knowledge base is in `Data/inpt.txt`, containing INPT details (e.g., programs, admissions, clubs).

### Running the Notebook
1. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```
   Open `inpt_rag_assistant.ipynb` in your browser.

2. **Execute Cells**:
   - Run cells sequentially
   - The final “‘Test the Assistant’” cell allows you to input queries (e.g., “What clubs are at INPT?”).
   - Ensure the Pinecone index (`rag-app`) is created with dimension 384 and cosine metric.

3. **Ask Questions**:
   - In the notebook’s interactive cell, input queries like:
     - “What fields of study are available at INPT?”
     - “How can I apply as an international student?”
     - “What’s campus life like at INPT?”

