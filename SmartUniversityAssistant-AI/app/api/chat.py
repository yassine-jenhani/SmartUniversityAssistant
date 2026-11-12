from fastapi import APIRouter, HTTPException
from uuid import uuid4

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.llm_service import generate_response

router = APIRouter()

# Temporary conversation storage
conversations = {}


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):

    conversation_id = (
        request.conversation_id or str(uuid4())
    )

    # Create a new conversation if necessary
    if conversation_id not in conversations:
        conversations[conversation_id] = []

    messages = conversations[conversation_id]

    # Add the student's message
    messages.append({
        "role": "user",
        "content": request.message
    })

    try:
        # Generate the answer using smartuni-assistant
        answer = generate_response(messages)

        # Save the AI response
        messages.append({
            "role": "assistant",
            "content": answer
        })

        # Keep only the latest 10 messages
        conversations[conversation_id] = messages[-10:]

        return ChatResponse(
            conversation_id=conversation_id,
            response=answer
        )

    except Exception as e:

        # Remove the failed user message
        messages.pop()

        print(f"Ollama error: {e}")

        raise HTTPException(
            status_code=503,
            detail="The AI service is currently unavailable."
        )