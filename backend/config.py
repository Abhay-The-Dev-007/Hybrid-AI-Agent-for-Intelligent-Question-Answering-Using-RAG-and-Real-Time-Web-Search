import os
from dotenv import load_dotenv

load_dotenv()

# vector database
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT=os.getenv("PINECONE_ENVIRONMENT","us-east-1")
PINECONE_INDEX_NAME=os.getenv("PINECPNE_INDEX_NAME","rag-index")

# Groq
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

# tavily
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

EMBED_MODEL = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

#paths (adjust as needed)
DOC_SOURCE_DIR = os.getenv("DOC_SOURCE_DIR", "data")
