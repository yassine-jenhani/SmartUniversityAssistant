
from fastapi import APIRouter, HTTPException
from uuid import uuid4
import logging

from app.schemas.chat import ChatRequest, ChatResponse
from app.core.database import SessionLocal
from app.services.rag_service import answer_question

router = APIRouter()

logger = logging.getLogger(__name__)

# Temporary conversation storage
conversations = {}


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):

    conversation_id = (
        request.conversation_id or str(uuid4())
    )

    if not request.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty."
        )

    db = SessionLocal()

    try:
        # 1. Retrieve previous conversation history
        conversation_history = conversations.get(
            conversation_id,
            []
        )

        # 2. Generate answer using conversation-aware RAG
        result = answer_question(
            db=db,
            question=request.message,
            top_k=3,
            conversation_history=conversation_history
        )

        answer = result["answer"]
        sources = result["sources"]

        # 3. Save successful interaction
        messages = conversation_history.copy()

        messages.append({
            "role": "user",
            "content": request.message
        })

        messages.append({
            "role": "assistant",
            "content": answer
        })

        # 4. Keep only the latest 10 messages
        conversations[conversation_id] = messages[-10:]

        return ChatResponse(
            conversation_id=conversation_id,
            response=answer,
            sources=sources
        )

    except Exception as e:

        logger.exception("Error while processing chat request")

        raise HTTPException(
            status_code=503,
            detail="The AI service is currently unavailable."
        ) from e

    finally:
        db.close()
