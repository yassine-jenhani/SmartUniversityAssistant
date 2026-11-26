from sqlalchemy.orm import Session
from sqlalchemy import select

from app.vectorstore.models import DocumentChunk
from app.embeddings.embedding_service import generate_embedding


def search_similar_chunks(
    db: Session,
    query: str,
    top_k: int = 5
) -> list[dict]:

    if not query or not query.strip():
        raise ValueError("Search query cannot be empty")

    if top_k <= 0:
        raise ValueError("top_k must be positive")

    # 1. Convert the student's question into an embedding
    query_embedding = generate_embedding(query)

    # 2. Calculate cosine distance and retrieve the closest chunks
    distance = DocumentChunk.embedding.cosine_distance(query_embedding)

    statement = (
        select(
            DocumentChunk,
            distance.label("distance")
        )
        .order_by(distance)
        .limit(top_k)
    )

    results = db.execute(statement).all()

    # 3. Format the retrieved results
    retrieved_chunks = []

    for chunk, distance_value in results:
        retrieved_chunks.append({
            "chunk_id": chunk.id,
            "document_id": chunk.document_id,
            "page_number": chunk.page_number,
            "chunk_index": chunk.chunk_index,
            "content": chunk.content,
            "similarity": round(1 - distance_value, 4)
        })

    return retrieved_chunks