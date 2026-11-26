
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.vectorstore.models import Document, DocumentChunk
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

    query_embedding = generate_embedding(query)

    distance = DocumentChunk.embedding.cosine_distance(query_embedding)

    statement = (
        select(DocumentChunk, Document, distance.label("distance"))
        .join(
            Document,
            DocumentChunk.document_id == Document.id
        )
        .order_by(distance)
        .limit(top_k)
    )

    results = db.execute(statement).all()

    retrieved_chunks = []

    for chunk, document, distance_value in results:
        retrieved_chunks.append({
            "chunk_id": chunk.id,
            "document_id": chunk.document_id,
            "document_name": document.filename,
            "page_number": chunk.page_number,
            "chunk_index": chunk.chunk_index,
            "content": chunk.content,
            "similarity": round(1 - distance_value, 4)
        })

    return retrieved_chunks
