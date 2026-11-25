from app.ingestion.document_loader import extract_document
from app.ingestion.text_cleaner import clean_text
from app.ingestion.chunker import chunk_text

def process_document(file_path: str) -> dict:
    """
    Complete document ingestion pipeline:
    Extraction -> Cleaning -> Chunking
    """

    document = extract_document(file_path)

    processed_chunks = []

    for page in document["pages"]:

        cleaned_content = clean_text(page["text"])

        chunks = chunk_text(cleaned_content)

        for chunk_index, chunk in enumerate(chunks):

            processed_chunks.append({
                "document_name": document["filename"],
                "file_type": document["file_type"],
                "page_number": page["page_number"],
                "chunk_index": chunk_index,
                "content": chunk
            })

    return {
        "filename": document["filename"],
        "file_type": document["file_type"],
        "total_pages": document["total_pages"],
        "total_chunks": len(processed_chunks),
        "chunks": processed_chunks
    }
