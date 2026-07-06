# DocuMind — RAG-Based PDF Q&A Assistant

Upload PDFs, ask questions, get answers grounded in your documents (not the LLM's memory).

## Architecture
```
User → React Chat UI → FastAPI Backend → pgvector (retrieval) → Claude API (generation) → Answer
                              ↑
                     PDF Ingestion Pipeline
                  (extract → chunk → embed → store)
```

## Tech Stack
| Layer       | Choice                          | Why |
|-------------|----------------------------------|-----|
| Backend     | FastAPI                          | Async, auto-docs, matches existing stack |
| Embeddings  | sentence-transformers (local)    | Free, offline, teaches the embedding step directly |
| Vector DB   | PostgreSQL + pgvector            | Production-grade, real SQL + vector search combined |
| LLM         | Claude API (Anthropic SDK)       | Answer generation grounded in retrieved context |
| Frontend    | React                            | Minimal chat interface |
| Deployment  | Docker Compose                   | Postgres + backend in one command |

## Local Setup
```bash
cp backend/.env.example backend/.env
# fill in ANTHROPIC_API_KEY in backend/.env

docker compose up -d db          # start Postgres+pgvector
cd backend
python -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
API docs: http://localhost:8000/docs

## Project Status
See `GAPS.md` for the running knowledge-gap log kept throughout the build week.
