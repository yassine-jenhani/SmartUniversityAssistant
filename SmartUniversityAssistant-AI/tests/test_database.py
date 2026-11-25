from sqlalchemy import text
from app.core.database import engine

with engine.connect() as connection:

    result = connection.execute(
        text("SELECT current_database(), version()")
    )

    database_name, version = result.fetchone()

    print("Database connection successful!")
    print("Database:", database_name)
    print("PostgreSQL:", version)

    result = connection.execute(
        text("""
            SELECT extname
            FROM pg_extension
            WHERE extname = 'vector'
        """)
    )

    print("pgvector:", result.fetchone())