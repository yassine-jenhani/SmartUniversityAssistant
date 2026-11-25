from sqlalchemy.orm import Session

from app.vectorstore.models import Document, DocumentChunk


def save_document(
    db: Session,
    document_data: dict,
    embeddings: list[list[float]]
) -> Document:

    chunks = document_data["chunks"]

    if len(chunks) != len(embeddings):
        raise ValueError(
            "The number of chunks must match the number of embeddings"
        )

    try:
        # Create document metadata
        document = Document(
            filename=document_data["filename"],
            file_type=document_data["file_type"],
            total_pages=document_data["total_pages"],
            status="PROCESSED"
        )

        db.add(document)
        db.flush()  # Generate document.id without committing

        # Create document chunks
        document_chunks = []

        for chunk, embedding in zip(chunks, embeddings):
            document_chunk = DocumentChunk(
                document_id=document.id,
                page_number=chunk["page_number"],
                chunk_index=chunk["chunk_index"],
                content=chunk["content"],
                embedding=embedding
            )

            document_chunks.append(document_chunk)

        db.add_all(document_chunks)

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()
        raise