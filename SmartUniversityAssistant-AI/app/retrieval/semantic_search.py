
import logging

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.vectorstore.models import Document, DocumentChunk
from app.embeddings.embedding_service import generate_embedding

logger = logging.getLogger(__name__)


def search_similar_chunks(
    db: Session,
    query: str,
    top_k: int = 5,
    min_similarity=0.55
) -> list[dict]:

    if not query or not query.strip():
        raise ValueError("Search query cannot be empty")

    if top_k <= 0:
        raise ValueError("top_k must be positive")

    if min_similarity is not None and not 0 <= min_similarity <= 1:
        raise ValueError("min_similarity must be between 0 and 1")

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

        similarity = round(1 - distance_value, 4)

        if (
            min_similarity is not None
            and similarity < min_similarity
        ):
            continue

        retrieved_chunks.append({
            "chunk_id": chunk.id,
            "document_id": chunk.document_id,
            "document_name": document.filename,
            "page_number": chunk.page_number,
            "chunk_index": chunk.chunk_index,
            "content": chunk.content,
            "similarity": similarity
        })

    # Debugging: display retrieved documents
    logger.warning("Retrieved chunks: %d", len(retrieved_chunks))

    for chunk in retrieved_chunks:
        logger.warning(
            "Document: %s | Page: %s | Similarity: %.4f",
            chunk["document_name"],
            chunk["page_number"],
            chunk["similarity"]
        )

    return retrieved_chunks
