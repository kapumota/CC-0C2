from __future__ import annotations

from cc0c2_mlops_rag.rag.index import build_index, retrieve, save_index


def test_build_index_creates_chunks() -> None:
    index = build_index()

    assert index["manifest"]["documents_count"] >= 1
    assert index["manifest"]["chunks_count"] >= 1
    assert index["matrix"].shape[0] == index["manifest"]["chunks_count"]


def test_retrieve_returns_results() -> None:
    index = build_index()
    save_index(index)

    results = retrieve("métricas del sistema rag", top_k=2)

    assert len(results) >= 1
    assert results[0].score >= 0.0
    assert results[0].text
