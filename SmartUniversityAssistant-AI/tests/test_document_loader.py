from app.ingestion.document_loader import extract_document

file_path = "data/sample.pdf"

result = extract_document(file_path)

print("Filename:", result["filename"])
print("Type:", result["file_type"])
print("Pages:", result["total_pages"])

for page in result["pages"]:
    print(f"\n--- Page {page['page_number']} ---")
    print(page["text"][:500])  # Print the first 500 characters of each page
