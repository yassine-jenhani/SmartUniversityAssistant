
from app.ingestion.pipeline import process_document
from app.embeddings.embedding_service import generate_embeddings


# Step 1: Process the PDF
document = process_document("data/sample.pdf")

chunks = document["chunks"]

# Step 2: Extract text from all chunks
texts = [
    chunk["content"]
    for chunk in chunks
]

# Step 3: Generate embeddings
embeddings = generate_embeddings(texts)

# Step 4: Display results
print("\n========== EMBEDDING RESULTS ==========")

print("Document:", document["filename"])
print("Number of chunks:", len(chunks))
print("Number of embeddings:", len(embeddings))

for index, embedding in enumerate(embeddings):

    print("\n-----------------------------")
    print("Chunk:", index)
    print("Page:", chunks[index]["page_number"])
    print("Vector dimensions:", len(embedding))
    print("First 5 values:", embedding[:5])
