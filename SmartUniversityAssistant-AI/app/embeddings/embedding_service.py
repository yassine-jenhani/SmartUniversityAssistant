from ollama import Client

from app.core.config import (
    OLLAMA_BASE_URL,
    EMBEDDING_MODEL
)

client = Client(host=OLLAMA_BASE_URL)


def generate_embedding(text: str) -> list[float]:
    """
    Generate an embedding for one text.
    """

    if not text or not text.strip():
        raise ValueError("Cannot generate an embedding for empty text")

    response = client.embed(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response.embeddings[0]


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for multiple text chunks.
    """

    if not texts:
        return []

    if any(not text.strip() for text in texts):
        raise ValueError("Input contains an empty text")

    response = client.embed(
        model=EMBEDDING_MODEL,
        input=texts
    )

    return response.embeddings
