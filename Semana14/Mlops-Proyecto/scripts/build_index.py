from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from cc0c2_mlops_rag.rag.index import build_index, save_index  # noqa: E402


def main() -> None:
    index = build_index()
    save_index(index)

    manifest = index["manifest"]

    print("Índice construido correctamente")
    print(f"Versión del índice: {manifest['index_version']}")
    print(f"Documentos: {manifest['documents_count']}")
    print(f"Chunks: {manifest['chunks_count']}")


if __name__ == "__main__":
    main()
