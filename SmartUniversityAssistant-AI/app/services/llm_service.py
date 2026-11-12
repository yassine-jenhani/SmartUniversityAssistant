from ollama import Client
from app.core.config import MODEL_NAME, OLLAMA_BASE_URL

client = Client(host=OLLAMA_BASE_URL)


def generate_response(messages: list) -> str:

    response = client.chat(
        model=MODEL_NAME,
        messages=messages
    )

    return response.message.content