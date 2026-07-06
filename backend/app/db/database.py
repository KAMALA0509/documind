"""
Database connection setup.

Why SQLAlchemy here instead of raw psycopg2: we get connection pooling for
free, an ORM layer for the metadata tables (documents, chunks), and a clean
session-per-request pattern via the `get_db` dependency below.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """
    FastAPI dependency: yields a DB session per request and guarantees it's
    closed afterwards, even if the request raises an exception.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
