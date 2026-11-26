from app.core.database import SessionLocal
from app.retrieval.semantic_search import search_similar_chunks


def test_semantic_search():

    question = "Explain the Transformer architecture in deep learning."

    db = SessionLocal()

    try:
        results = search_similar_chunks(
        db=db,
        query=question,
        top_k=3,
        min_similarity=0.55

)

        print("\n========== SEMANTIC SEARCH RESULTS ==========")
        print(f"Question: {question}")
        print(f"Number of results: {len(results)}")

        for index, result in enumerate(results, start=1):

            print(f"\n----- Result {index} -----")
            print(f"Document: {result['document_name']}")
            print(f"Document ID: {result['document_id']}")
            print(f"Page: {result['page_number']}")
            print(f"Chunk: {result['chunk_index']}")
            print(f"Similarity: {result['similarity']}")
            print(f"Content: {result['content']}")

    finally:
        db.close()


if __name__ == "__main__":
    test_semantic_search()
