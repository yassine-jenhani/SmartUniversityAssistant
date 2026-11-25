from app.core.database import SessionLocal
from app.ingestion.pipeline import process_document
from app.embeddings.embedding_service import generate_embeddings
from app.vectorstore.document_repository import save_document


def test_save_document():

    # 1. Process PDF
    document_data = process_document("data/sample.pdf")

    # 2. Generate embeddings
    texts = [
        chunk["content"]
        for chunk in document_data["chunks"]
    ]

    embeddings = generate_embeddings(texts)

    # 3. Save everything in PostgreSQL
    db = SessionLocal()

    try:
        saved_document = save_document(
            db=db,
            document_data=document_data,
            embeddings=embeddings
        )

        print("\n========== DOCUMENT STORAGE ==========")
        print("Document ID:", saved_document.id)
        print("Filename:", saved_document.filename)
        print("File type:", saved_document.file_type)
        print("Total pages:", saved_document.total_pages)
        print("Status:", saved_document.status)

        print("\nDocument successfully stored!")

    finally:
        db.close()


if __name__ == "__main__":
    test_save_document()