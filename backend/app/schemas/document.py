"""
Defines request and response schemas for the API.
Separating Pydantic schemas from SQLAlchemy models keeps the API contract
independent of the database model and prevents internal fields (e.g.,
embedding vectors) from being exposed to clients.
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
