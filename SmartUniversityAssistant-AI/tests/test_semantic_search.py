from app.core.database import SessionLocal
from app.retrieval.semantic_search import search_similar_chunks


def test_semantic_search():

    query = "Comment lancer des instances EC2 avec un Auto Scaling Group ?"

    db = SessionLocal()

    try:
        results = search_similar_chunks(
            db=db,
            query=query,
            top_k=3
        )

        print("\n========== SEMANTIC SEARCH RESULTS ==========")
        print("Question:", query)
        print("Number of results:", len(results))

        for index, result in enumerate(results, start=1):

            print(f"\n----- Result {index} -----")
            print("Document ID:", result["document_id"])
            print("Page:", result["page_number"])
            print("Chunk:", result["chunk_index"])
            print("Similarity:", result["similarity"])
            print("Content:", result["content"])

    finally:
        db.close()


if __name__ == "__main__":
    test_semantic_search()