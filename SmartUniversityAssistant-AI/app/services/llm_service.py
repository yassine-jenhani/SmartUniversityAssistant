from ollama import Client

from app.core.config import OLLAMA_BASE_URL, OLLAMA_MODEL

client = Client(host=OLLAMA_BASE_URL)


def generate_answer(
    question: str,
    context: str
) -> str:

    system_prompt = """
    You are SmartUniversity, an academic AI assistant.

    Your responsibilities:
    - Answer students clearly and pedagogically.
    - Use the provided context as your primary source.
    - Do not invent facts or information.
    - If the context does not contain the answer,
      explicitly say that you cannot find sufficient
      information in the available documents.
    - Answer in the same language as the student's question.
    """

    user_prompt = f"""
    CONTEXT:
    {context}

    STUDENT QUESTION:
    {question}

    Provide a clear answer based on the context.
    """

    response = client.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.message.content