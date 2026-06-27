from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from cc0c2_mlops_rag.evaluation.metrics import (  # noqa: E402
    precision_at_k,
    recall_at_k,
    reciprocal_rank,
)
from cc0c2_mlops_rag.rag.index import retrieve  # noqa: E402

EVAL_PATH = PROJECT_ROOT / "data" / "eval" / "eval_rag.jsonl"
TOP_K = 3
MIN_RECALL_AT_K = 0.5


def load_eval_cases() -> list[dict[str, Any]]:
    if not EVAL_PATH.exists():
        raise FileNotFoundError(f"No existe el archivo de evaluación: {EVAL_PATH}")

    cases: list[dict[str, Any]] = []

    for line_number, line in enumerate(EVAL_PATH.read_text(encoding="utf-8").splitlines(), start=1):
        line = line.strip()

        if not line:
            continue

        try:
            case = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"JSON inválido en línea {line_number}: {line}") from exc

        if "query" not in case:
            raise ValueError(f"Falta el campo 'query' en línea {line_number}")

        if "relevant_doc_ids" not in case:
            raise ValueError(f"Falta el campo 'relevant_doc_ids' en línea {line_number}")

        if not isinstance(case["relevant_doc_ids"], list):
            raise ValueError(f"'relevant_doc_ids' debe ser una lista en línea {line_number}")

        cases.append(case)

    if not cases:
        raise ValueError("El dataset de evaluación está vacío")

    return cases


def unique_in_order(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def mean(values: list[float]) -> float:
    if not values:
        return 0.0

    return sum(values) / len(values)


def main() -> None:
    cases = load_eval_cases()

    p_at_k_values: list[float] = []
    r_at_k_values: list[float] = []
    mrr_values: list[float] = []
    case_reports: list[dict[str, Any]] = []

    for case in cases:
        query = str(case["query"])
        relevant = set(str(doc_id) for doc_id in case["relevant_doc_ids"])

        results = retrieve(query, top_k=TOP_K)
        retrieved_doc_ids = unique_in_order([result.doc_id for result in results])

        p_at_k = precision_at_k(retrieved_doc_ids, relevant, TOP_K)
        r_at_k = recall_at_k(retrieved_doc_ids, relevant, TOP_K)
        mrr = reciprocal_rank(retrieved_doc_ids, relevant)

        p_at_k_values.append(p_at_k)
        r_at_k_values.append(r_at_k)
        mrr_values.append(mrr)

        case_reports.append(
            {
                "query": query,
                "relevant_doc_ids": sorted(relevant),
                "retrieved_doc_ids": retrieved_doc_ids,
                f"precision_at_{TOP_K}": round(p_at_k, 4),
                f"recall_at_{TOP_K}": round(r_at_k, 4),
                "mrr": round(mrr, 4),
            }
        )

    report = {
        "cases": len(cases),
        f"precision_at_{TOP_K}": round(mean(p_at_k_values), 4),
        f"recall_at_{TOP_K}": round(mean(r_at_k_values), 4),
        "mrr": round(mean(mrr_values), 4),
        "details": case_reports,
    }

    print(json.dumps(report, indent=2, ensure_ascii=False))

    if (
        report[f"precision_at_{TOP_K}"] == 1.0
        and report[f"recall_at_{TOP_K}"] == 1.0
        and report["mrr"] == 1.0
    ):
        print(
            "\nAdvertencia: la evaluación salió perfecta. "
            "Esto puede indicar que el dataset es demasiado pequeño, directo o sin distractores."
        )

    if report[f"recall_at_{TOP_K}"] < MIN_RECALL_AT_K:
        raise SystemExit("La evaluación RAG no alcanzó el recall mínimo esperado")


if __name__ == "__main__":
    main()