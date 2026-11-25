import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv(
    "OLLAMA_MODEL",
    "smartuni-assistant"
)

EMBEDDING_MODEL = os.getenv("OLLAMA_EMBEDDING_MODEL", "bge-m3")

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)