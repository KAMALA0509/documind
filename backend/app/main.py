"""
FastAPI application entrypoint.

Day 1 scope: app boots, connects to Postgres, enables the pgvector
extension, and exposes a health check. Routers for ingestion and chat
get wired in on Day 2/3 as those services are built.
"""
import logging

from fastapi import FastAPI
from sqlalchemy import text

from app.config import settings
from app.db.database import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("documind")

app = FastAPI(
    title="DocuMind API",
    description="RAG-based PDF Q&A backend",
    version="0.1.0",
)


@app.on_event("startup")
def on_startup() -> None:
    """
    Enable the pgvector extension on startup. This is idempotent (CREATE
    EXTENSION IF NOT EXISTS) so it's safe to run on every boot rather than
    requiring a separate manual migration step for this one-time setup.
    """
    try:
        with engine.connect() as conn:
            conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
            conn.commit()
        logger.info("pgvector extension ready")
    except Exception as exc:
        # Fail loudly rather than silently continuing without vector search
        logger.error("Failed to enable pgvector extension: %s", exc)
        raise


@app.get("/health")
def health_check():
    """Basic liveness check, also confirms config loaded correctly."""
    return {
        "status": "ok",
        "embedding_model": settings.embedding_model,
    }
