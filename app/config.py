import os
from dotenv import load_dotenv


# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()


# ==========================================================
# Groq Configuration
# ==========================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-120b"
)


# ==========================================================
# Embedding Configuration
# ==========================================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# ==========================================================
# Vector Database Configuration
# ==========================================================

USE_FAISS = os.getenv(
    "USE_FAISS",
    "false"
).lower() == "true"
