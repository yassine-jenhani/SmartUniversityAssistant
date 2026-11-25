from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Integer,
    Text,
    TIMESTAMP,
    ForeignKey,
    func
)

from pgvector.sqlalchemy import Vector

from app.core.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(BigInteger, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    file_type = Column(String(20), nullable=False)
    file_hash = Column(String(64), unique=True)
    total_pages = Column(Integer)
    status = Column(String(30), default="PROCESSED")
    created_at = Column(TIMESTAMP, server_default=func.now())


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id = Column(BigInteger, primary_key=True, index=True)

    document_id = Column(
        BigInteger,
        ForeignKey("documents.id", ondelete="CASCADE"),
        nullable=False
    )

    page_number = Column(Integer)
    chunk_index = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)

    embedding = Column(Vector(1024), nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())