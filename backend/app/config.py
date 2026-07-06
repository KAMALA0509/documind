"""
Centralized application settings, loaded from environment variables.

Why this pattern: hardcoding config (DB URLs, API keys, chunk sizes) scattered
across files makes it impossible to know what needs to change between dev/
staging/prod. pydantic-settings gives us validation (fails fast if a required
var is missing) plus a single source of truth.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    anthropic_api_key: str
    database_url: str
    embedding_model: str = "all-MiniLM-L6-v2"
    chunk_size: int = 500
    chunk_overlap: int = 50
    top_k_results: int = 4

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# Instantiated once, imported everywhere else. If a required env var is
# missing, this line raises immediately on startup instead of failing later
# mid-request.
settings = Settings()
