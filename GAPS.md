# Knowledge Gap Log — DocuMind Week

## Day 1
- **Gap:** Didn't know FastAPI returns 404 for undefined routes by default (no automatic "welcome" root page)
- **Where:** Testing http://127.0.0.1:8000/ in browser after first run
- **Resolution:** Learned every route must be explicitly defined; checked /health instead, and discovered /docs gives free interactive API testing UI

## Day 2

## Day 3

## Day 4

## Day 5

---

## Pre-identified gaps (before starting, based on stack for this project)
- **Gap:** How vector similarity search actually works under the hood (cosine similarity vs L2 distance vs inner product)
- **Where:** Will hit this in Day 2 (pgvector setup)
- **Resolution:** _(pending)_

- **Gap:** Chunking strategy for documents (fixed-size vs semantic chunking) and why chunk size affects retrieval quality
- **Where:** Day 2 ingestion pipeline
- **Resolution:** _(pending)_

- **Gap:** How to structure a prompt so the LLM answers *only* from retrieved context (prompt grounding / anti-hallucination technique)
- **Where:** Day 3 LLM service
- **Resolution:** _(pending)_
