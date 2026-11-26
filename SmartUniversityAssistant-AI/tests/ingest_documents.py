from pathlib import Path

from app.core.database import SessionLocal
from app.vectorstore.models import Document
from app.ingestion.pipeline import process_document
from app.embeddings.embedding_service import generate_embeddings
from app.vectorstore.document_repository import save_document


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def ingest_all_documents():

    pdf_files = sorted(DATA_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in the data folder.")
        return

    print(f"\nFound {len(pdf_files)} PDF files.")

    db = SessionLocal()

    try:
        for file_path in pdf_files:

            print("\n" + "=" * 55)
            print(f"Processing: {file_path.name}")
            print("=" * 55)

            # Avoid ingesting the same filename twice
            existing_document = (
                db.query(Document)
                .filter(Document.filename == file_path.name)
                .first()
            )

            if existing_document:
                print("Already stored in database. Skipping.")
                continue

            # 1. Extract, clean and chunk
            document_data = process_document(str(file_path))

            print(f"Pages: {document_data['total_pages']}")
            print(f"Chunks: {document_data['total_chunks']}")

            if not document_data["chunks"]:
                print("No extractable text found. Skipping.")
                continue

            # 2. Generate embeddings
            texts = [
                chunk["content"]
                for chunk in document_data["chunks"]
            ]

            embeddings = generate_embeddings(texts)

            print(f"Embeddings generated: {len(embeddings)}")

            # 3. Save document and chunks in PostgreSQL
            saved_document = save_document(
                db=db,
                document_data=document_data,
                embeddings=embeddings
            )

            print(f"Successfully stored document ID: {saved_document.id}")

        print("\n" + "=" * 55)
        print("DOCUMENT INGESTION FINISHED")
        print("=" * 55)

    finally:
        db.close()


if __name__ == "__main__":
    ingest_all_documents()
