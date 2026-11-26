from sqlalchemy.orm import Session

import logging

logger = logging.getLogger(__name__)

from app.retrieval.semantic_search import search_similar_chunks
from app.services.llm_service import (
    generate_answer,
    rewrite_question
)


MIN_SIMILARITY = 0.55


def answer_question(
    db: Session,
    question: str,
    top_k: int = 3,
    conversation_history: list[dict] | None = None
) -> dict:

    if not question or not question.strip():
        raise ValueError("Question cannot be empty")

    # 1. Rewrite the question using conversation history
    search_question = rewrite_question(
        question=question,
        conversation_history=conversation_history or []
    )

    logger.info("RAG search question: %s", search_question)

    # 2. Retrieve relevant chunks using the contextualized question
    retrieved_chunks = search_similar_chunks(
        db=db,
        query=search_question,
        top_k=top_k,
        min_similarity=MIN_SIMILARITY
    )

    # 3. Handle questions with no relevant information
    if not retrieved_chunks:
        return {
            "question": question,
            "answer": (
                "I couldn't find sufficient relevant information "
                "to answer your question in the available university documents."
            ),
            "sources": []
        }

    # 4. Build context for the LLM
    context_parts = []

    for index, chunk in enumerate(retrieved_chunks, start=1):

        context_parts.append(
            f"""
SOURCE {index}
Document: {chunk['document_name']}
Page: {chunk['page_number']}
Content:
{chunk['content']}
"""
        )

    context = "\n\n".join(context_parts)

    # 5. Generate the answer
    answer = generate_answer(
        question=search_question,
        original_question=question,
        context=context
    )

    # 6. Build unique source citations
    sources = []
    seen_sources = set()

    for chunk in retrieved_chunks:

        source_key = (
            chunk["document_name"],
            chunk["page_number"]
        )

        if source_key not in seen_sources:

            seen_sources.add(source_key)

            sources.append({
                "document_name": chunk["document_name"],
                "page_number": chunk["page_number"],
                "similarity": chunk["similarity"]
            })

    # 7. Return final RAG response
    return {
        "question": question,
        "answer": answer,
        "sources": sources
    }
