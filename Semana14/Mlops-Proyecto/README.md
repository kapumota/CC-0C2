# Proyecto MLOps / LLMOps - CC0C2

Este proyecto implementa un sistema RAG pequeño, observable y reproducible para mostrar
cómo un experimento de lenguaje puede convertirse en un servicio operable.

El objetivo no es entrenar un LLM desde cero. El objetivo es mostrar el ciclo mínimo de
MLOps/LLMOps:

```text
documentos -> construcción de índice -> API -> evaluación -> métricas -> Docker -> CI
```

## Qué implementa

- API con FastAPI.
- Recuperación RAG local basada en TF-IDF.
- Construcción reproducible de índice.
- Manifiesto de índice con versión, cantidad de documentos, chunks y hash.
- Endpoint `/query` para consultas.
- Endpoint `/health` para estado del servicio.
- Endpoint `/metrics` compatible con Prometheus.
- Endpoint `/admin/reindex` protegido por token simple.
- Evaluación básica de retrieval.
- Pruebas automatizadas.
- Lint con Ruff.
- Dockerfile.
- Docker Compose.
- Workflow de GitHub Actions ejecutado desde una subcarpeta del repositorio.

## Arquitectura

```text
data/docs/
   |
   v
scripts/build_index.py
   |
   v
data/indexes/rag_index.pkl
data/indexes/index_manifest.json
   |
   v
FastAPI
   |
   +--> /health
   +--> /query
   +--> /metrics
   +--> /admin/reindex
   |
   v
scripts/evaluate_rag.py
```

## Estructura

```text
Mlops-Proyecto/
  README.md
  Makefile
  requirements.txt
  pyproject.toml
  Dockerfile
  docker-compose.yml
  .env.example

  data/
    docs/
      curso.md
    eval/
      eval_rag.jsonl
    indexes/
      .gitkeep

  src/
    cc0c2_mlops_rag/
      __init__.py
      app.py
      rag/
        __init__.py
        index.py
      evaluation/
        __init__.py
        metrics.py

  scripts/
    build_index.py
    evaluate_rag.py

  tests/
    test_api.py
    test_rag.py
```

## Instalación local

Desde la raíz del repositorio `CC-0C2`:

```bash
cd Semana15/Mlops-Proyecto
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows Git Bash:

```bash
cd Semana15/Mlops-Proyecto
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

## Comandos principales

```bash
make lint
make index
make test
make eval
make run
```

## Ejecutar API

```bash
make run
```

Luego abrir:

```text
http://localhost:8000/docs
```

## Consultar el sistema

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "qué componentes tiene el proyecto MLOps", "top_k": 3}'
```

## Reindexar

```bash
curl -X POST http://localhost:8000/admin/reindex \
  -H "x-admin-token: dev-token"
```

## Ver métricas

```bash
curl http://localhost:8000/metrics
```

## Evaluación

```bash
make eval
```

La evaluación calcula:

- `precision@3`
- `recall@3`
- `MRR`

## Docker

```bash
make docker-build
make docker-run
```

Con Docker Compose:

```bash
make compose-up
```

## Qué evidencia de MLOps contiene

Este proyecto contiene evidencia mínima de operación de sistemas ML/LLM:

- Reproducibilidad de índice.
- Manifiesto de índice.
- API de inferencia.
- Endpoint de salud.
- Métricas operativas.
- Evaluación automática.
- Pruebas automatizadas.
- Lint.
- Contenedor Docker.
- CI por subcarpeta.

## Limitaciones

- Usa TF-IDF, no embeddings densos.
- No usa un LLM externo para generación.
- La respuesta es extractiva para reducir dependencias.
- No tiene model registry.
- No tiene despliegue cloud.
- No tiene monitoreo de drift.
- La autenticación de reindexado es mínima y solo sirve para clase.

## Mejoras sugeridas

- Reemplazar TF-IDF por embeddings densos.
- Agregar evaluación de grounded generation.
- Agregar trazas con OpenTelemetry.
- Agregar Prometheus + Grafana.
- Versionar datasets e índices con manifiestos más completos.
- Agregar CD hacia staging.
- Agregar rollback de índice.
