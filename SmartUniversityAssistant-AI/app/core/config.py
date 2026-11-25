import os
from pathlib import Path
from dotenv import load_dotenv

# Project root: C:\SmartUniversityAssistant
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Load .env from the main project folder
ENV_FILE = PROJECT_ROOT / ".env"
load_dotenv(ENV_FILE)

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "smartuni-assistant")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
EMBEDDING_MODEL = os.getenv("OLLAMA_EMBEDDING_MODEL", "bge-m3")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(f"DATABASE_URL is missing from {ENV_FILE}")