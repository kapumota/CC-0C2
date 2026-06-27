from __future__ import annotations

from fastapi.testclient import TestClient

from cc0c2_mlops_rag.app import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_query_endpoint() -> None:
    response = client.post(
        "/query",
        json={
            "query": "qué es este proyecto",
            "top_k": 2,
        },
    )

    assert response.status_code == 200
    body = response.json()

    assert body["query"] == "qué es este proyecto"
    assert len(body["retrieved"]) >= 1
    assert "index_version" in body


def test_reindex_requires_token() -> None:
    response = client.post("/admin/reindex")

    assert response.status_code == 401


def test_reindex_with_token() -> None:
    response = client.post(
        "/admin/reindex",
        headers={"x-admin-token": "dev-token"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "reindexed"


def test_metrics_endpoint() -> None:
    response = client.get("/metrics")

    assert response.status_code == 200
    assert "cc0c2_mlops_rag_requests_total" in response.text
