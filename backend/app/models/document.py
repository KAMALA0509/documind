"""
Two tables:
  - documents: one row per uploaded PDF
  - chunks: one row per text chunk, with its embedding vector attached

Why two tables instead of one: a document's metadata (filename, upload time)
shouldn't be duplicated across every chunk row. Standard 1-to-many
normalization — one document has many chunks.
"""
from datetime import datetime, timezone

from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base

# all-MiniLM-L6-v2 outputs 384-dimensional vectors. This MUST match the
# actual output size of the embedding model in embedding_service.py, or
# pgvector will reject inserts with a dimension mismatch error.
EMBEDDING_DIM = 384


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    uploaded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    num_chunks = Column(Integer, default=0)

    # cascade="all, delete-orphan": deleting a Document also deletes its
    # Chunks. Without this, deleting a document would leave orphaned chunk
    # rows pointing at a document_id that no longer exists.
    chunks = relationship("Chunk", back_populates="document", cascade="all, delete-orphan")


class Chunk(Base):
    __tablename__ = "chunks"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    chunk_index = Column(Integer, nullable=False)  # position within the document
    content = Column(Text, nullable=False)
    embedding = Column(Vector(EMBEDDING_DIM), nullable=False)

    document = relationship("Document", back_populates="chunks")
