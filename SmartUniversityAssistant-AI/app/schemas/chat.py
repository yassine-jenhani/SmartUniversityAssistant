
from pydantic import BaseModel, Field
from typing import Optional


class ChatRequest(BaseModel):
    conversation_id: Optional[str] = None

    message: str = Field(
        min_length=1,
        max_length=4000
    )


class SourceCitation(BaseModel):
    document_name: str
    page_number: Optional[int] = None
    similarity: float


class ChatResponse(BaseModel):
    conversation_id: str
    response: str
    sources: list[SourceCitation] = Field(default_factory=list)
