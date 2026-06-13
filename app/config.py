import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
USE_FAISS = os.getenv("USE_FAISS", "false").lower() == "true"
