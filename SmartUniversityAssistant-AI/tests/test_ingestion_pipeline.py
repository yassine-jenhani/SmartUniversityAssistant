from app.ingestion.pipeline import process_document

file_path = "data/sample.pdf"

result = process_document(file_path)

print("\n========== DOCUMENT INFORMATION ==========")

print("Filename:", result["filename"])
print("File type:", result["file_type"])
print("Total pages:", result["total_pages"])
print("Total chunks:", result["total_chunks"])

print("\n========== EXTRACTED CHUNKS ==========")

for chunk in result["chunks"]:

    print("\n-----------------------------------")
    print("Page:", chunk["page_number"])
    print("Chunk:", chunk["chunk_index"])
    print("Content:")
    print(chunk["content"])
