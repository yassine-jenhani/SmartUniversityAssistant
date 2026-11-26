from app.core.database import SessionLocal
from app.services.rag_service import answer_question


def test_rag():

    question = "What are the steps to create an EC2 instance?"

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

        print("\nSOURCES:")

        for source in result["sources"]:
            print(
                f"Document ID: {source['document_id']} | "
                f"Page: {source['page_number']} | "
                f"Similarity: {source['similarity']}"
            )

    finally:
        db.close()


if __name__ == "__main__":
    test_rag()