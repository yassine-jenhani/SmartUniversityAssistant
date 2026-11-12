from pydantic import BaseModel, Field
from typing import Optional


class ChatRequest(BaseModel):
    conversation_id: Optional[str] = None

    message: str = Field(
        min_length=1,
        max_length=4000
    )


class ChatResponse(BaseModel):
    conversation_id: str
    response: str