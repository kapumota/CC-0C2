from __future__ import annotations

import os
import time
from typing import Annotated

from fastapi import FastAPI, Header, HTTPException, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
from pydantic import BaseModel, Field

from cc0c2_mlops_rag.rag.index import build_index, read_manifest, retrieve, save_index

REQUESTS_TOTAL = Counter(
    "cc0c2_mlops_rag_requests_total",
    "Cantidad total de requests recibidos",
    ["endpoint"],
)

ERRORS_TOTAL = Counter(
    "cc0c2_mlops_rag_errors_total",
    "Cantidad total de errores",
    ["endpoint"],
)

QUERY_LATENCY = Histogram(
    "cc0c2_mlops_rag_query_latency_seconds",
    "Latencia de consultas RAG",
)

RETRIEVED_CHUNKS = Histogram(
    "cc0c2_mlops_rag_retrieved_chunks",
    "Cantidad de chunks recuperados por consulta",
)

app = FastAPI(
    title="CC0C2 MLOps RAG",
    description="Proyecto educativo de LLMOps/MLOps para operar un sistema RAG pequeño.",
    version="0.1.0",
)


class QueryRequest(BaseModel):
    query: str = Field(min_length=1)
    top_k: int = Field(default=3, ge=1, le=10)


class QueryResponse(BaseModel):
    query: str
    answer: str
    retrieved: list[dict]
    index_version: str


@app.get("/health")
def health() -> dict:
    REQUESTS_TOTAL.labels(endpoint="/health").inc()
    manifest = read_manifest()

    return {
        "status": "ok",
        "service": "cc0c2-mlops-rag",
        "index_version": manifest["index_version"],
        "chunks_count": manifest["chunks_count"],
    }


@app.post("/query", response_model=QueryResponse)
def query_rag(payload: QueryRequest) -> QueryResponse:
    REQUESTS_TOTAL.labels(endpoint="/query").inc()
    start = time.perf_counter()

    try:
        retrieved = retrieve(payload.query, top_k=payload.top_k)
        manifest = read_manifest()
        context = "\n\n".join(chunk.text for chunk in retrieved)

        answer = (
            "Respuesta basada en los documentos recuperados:\n\n"
            f"{context[:900]}\n\n"
            "Nota: este ejemplo usa respuesta extractiva para enfocarse en MLOps/RAG."
        )

        RETRIEVED_CHUNKS.observe(len(retrieved))

        return QueryResponse(
            query=payload.query,
            answer=answer,
            retrieved=[
                {
                    "doc_id": chunk.doc_id,
                    "chunk_id": chunk.chunk_id,
                    "score": chunk.score,
                    "text": chunk.text[:300],
                }
                for chunk in retrieved
            ],
            index_version=manifest["index_version"],
        )

    except Exception as exc:
        ERRORS_TOTAL.labels(endpoint="/query").inc()
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    finally:
        QUERY_LATENCY.observe(time.perf_counter() - start)


@app.post("/admin/reindex")
def reindex(
    x_admin_token: Annotated[str | None, Header()] = None,
) -> dict:
    REQUESTS_TOTAL.labels(endpoint="/admin/reindex").inc()
    expected_token = os.getenv("ADMIN_TOKEN", "dev-token")

    if x_admin_token != expected_token:
        ERRORS_TOTAL.labels(endpoint="/admin/reindex").inc()
        raise HTTPException(status_code=401, detail="Token de administración inválido")

    index = build_index()
    save_index(index)

    return {
        "status": "reindexed",
        "manifest": index["manifest"],
    }


@app.get("/metrics")
def metrics() -> Response:
    REQUESTS_TOTAL.labels(endpoint="/metrics").inc()
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
