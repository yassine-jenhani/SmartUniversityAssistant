import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv(
    "OLLAMA_MODEL",
    "smartuni-assistant"
)

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)