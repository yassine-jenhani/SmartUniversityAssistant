
from app.core.database import SessionLocal
from app.services.rag_service import answer_question


def test_rag():

    question = "How can I implement JWT authentication using Spring Boot?"

    db = SessionLocal()

    try:
        result = answer_question(
            db=db,
            question=question,
            top_k=3
        )

        print("\n========== RAG RESULTS ==========")

        print("\nQUESTION:")
        print(result["question"])

        print("\nGENERATED ANSWER:")
        print(result["answer"])

        print("\nSOURCE CITATIONS:")

        for source in result["sources"]:
            print(
                f"Document: {source['document_name']} | "
                f"Page: {source['page_number']} | "
                f"Similarity: {source['similarity']}"
            )

    finally:
        db.close()


if __name__ == "__main__":
    test_rag()
