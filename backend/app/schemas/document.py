"""
Pydantic schemas define what goes over the wire — separate from the
SQLAlchemy models, which define what's in the database. Keeping them
separate means we control exactly what's exposed in the API (e.g. we never
want to accidentally serialize a raw embedding vector back to the client).
"""
from datetime import datetime

from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: int
    filename: str
    uploaded_at: datetime
    num_chunks: int

    # Lets Pydantic build this schema directly from a SQLAlchemy model
    # instance (model.id, model.filename, ...) instead of requiring a dict.
    model_config = {"from_attributes": True}


class UploadResponse(BaseModel):
    document: DocumentResponse
    message: str
