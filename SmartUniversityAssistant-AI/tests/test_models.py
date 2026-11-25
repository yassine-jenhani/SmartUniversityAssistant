from sqlalchemy import inspect

from app.core.database import engine, Base
from app.vectorstore.models import Document, DocumentChunk


def test_create_tables():
    print("Creating database tables...")

    Base.metadata.create_all(bind=engine)

    inspector = inspect(engine)
    tables = inspector.get_table_names()

    print("\n========== DATABASE TABLES ==========")

    for table in tables:
        print("-", table)

    required_tables = {"documents", "document_chunks"}

    if required_tables.issubset(set(tables)):
        print("\nSUCCESS: Both tables exist!")
    else:
        raise Exception("Required database tables are missing!")


if __name__ == "__main__":
    test_create_tables()