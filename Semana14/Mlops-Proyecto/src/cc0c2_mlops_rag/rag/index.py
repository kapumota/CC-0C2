from __future__ import annotations

import hashlib
import json
import pickle
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DOCS_DIR = PROJECT_ROOT / "data" / "docs"
INDEX_DIR = PROJECT_ROOT / "data" / "indexes"
INDEX_PATH = INDEX_DIR / "rag_index.pkl"
MANIFEST_PATH = INDEX_DIR / "index_manifest.json"


@dataclass(frozen=True)
class RetrievedChunk:
    doc_id: str
    chunk_id: int
    score: float
    text: str


def read_documents(docs_dir: Path = DOCS_DIR) -> list[dict[str, str]]:
    documents: list[dict[str, str]] = []

    for path in sorted(docs_dir.glob("**/*")):
        if path.suffix.lower() not in {".md", ".txt"}:
            continue

        text = path.read_text(encoding="utf-8").strip()
        if not text:
            continue

        documents.append({"doc_id": path.relative_to(docs_dir).as_posix(), "text": text})

    if not documents:
        raise RuntimeError(f"No se encontraron documentos en {docs_dir}")

    return documents


def chunk_text(text: str, chunk_size: int = 700, overlap: int = 100) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size debe ser mayor que cero")

    if overlap >= chunk_size:
        raise ValueError("overlap debe ser menor que chunk_size")

    chunks: list[str] = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break

        start = end - overlap

    return chunks


def build_index(chunk_size: int = 700, overlap: int = 100) -> dict:
    documents = read_documents()
    chunks: list[dict[str, object]] = []

    for document in documents:
        for chunk_id, chunk in enumerate(chunk_text(document["text"], chunk_size, overlap)):
            chunks.append(
                {
                    "doc_id": document["doc_id"],
                    "chunk_id": chunk_id,
                    "text": chunk,
                }
            )

    texts = [str(chunk["text"]) for chunk in chunks]

    vectorizer = TfidfVectorizer(
        lowercase=True,
        strip_accents="unicode",
        ngram_range=(1, 2),
        min_df=1,
    )
    matrix = vectorizer.fit_transform(texts)

    doc_hash = hashlib.sha256("\n".join(texts).encode("utf-8")).hexdigest()

    manifest = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "index_version": doc_hash[:12],
        "documents_count": len(documents),
        "chunks_count": len(chunks),
        "chunk_size": chunk_size,
        "overlap": overlap,
        "vectorizer": "TfidfVectorizer",
        "doc_hash_sha256": doc_hash,
    }

    return {
        "chunks": chunks,
        "vectorizer": vectorizer,
        "matrix": matrix,
        "manifest": manifest,
    }


def save_index(index: dict) -> None:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)

    with INDEX_PATH.open("wb") as file:
        pickle.dump(index, file)

    MANIFEST_PATH.write_text(
        json.dumps(index["manifest"], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def load_index() -> dict:
    if not INDEX_PATH.exists():
        index = build_index()
        save_index(index)
        return index

    with INDEX_PATH.open("rb") as file:
        return pickle.load(file)


def retrieve(query: str, top_k: int = 3) -> list[RetrievedChunk]:
    if not query.strip():
        raise ValueError("La consulta no puede estar vacía")

    if top_k <= 0:
        raise ValueError("top_k debe ser mayor que cero")

    index = load_index()
    query_vector = index["vectorizer"].transform([query])
    scores = cosine_similarity(query_vector, index["matrix"])[0]

    limit = min(top_k, len(index["chunks"]))
    top_indices = np.argsort(scores)[::-1][:limit]

    results: list[RetrievedChunk] = []

    for idx in top_indices:
        chunk = index["chunks"][int(idx)]
        results.append(
            RetrievedChunk(
                doc_id=str(chunk["doc_id"]),
                chunk_id=int(chunk["chunk_id"]),
                score=float(scores[int(idx)]),
                text=str(chunk["text"]),
            )
        )

    return results


def read_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        index = build_index()
        save_index(index)

    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
