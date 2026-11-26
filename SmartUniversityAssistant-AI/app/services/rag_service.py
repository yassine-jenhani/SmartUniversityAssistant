from sqlalchemy.orm import Session

from app.retrieval.semantic_search import search_similar_chunks
from app.services.llm_service import generate_answer


def answer_question(
    db: Session,
    question: str,
    top_k: int = 3
) -> dict:

    if not question or not question.strip():
        raise ValueError("Question cannot be empty")

    # 1. Retrieve relevant document chunks
    retrieved_chunks = search_similar_chunks(
        db=db,
        query=question,
        top_k=top_k
    )

    if not retrieved_chunks:
        return {
            "question": question,
            "answer": "I couldn't find relevant information in the available documents.",
            "sources": []
        }

    # 2. Build context from retrieved chunks
    context_parts = []

    for index, chunk in enumerate(retrieved_chunks, start=1):
        context_parts.append(
            f"""
            SOURCE {index}
            Document ID: {chunk['document_id']}
            Page: {chunk['page_number']}
            Content:
            {chunk['content']}
            """
        )

    context = "\n\n".join(context_parts)

    # 3. Generate an answer using Qwen2.5
    answer = generate_answer(
        question=question,
        context=context
    )

    # 4. Return answer and sources
    sources = [
        {
            "document_id": chunk["document_id"],
            "page_number": chunk["page_number"],
            "chunk_id": chunk["chunk_id"],
            "similarity": chunk["similarity"]
        }
        for chunk in retrieved_chunks
    ]

    return {
        "question": question,
        "answer": answer,
        "sources": sources
    }