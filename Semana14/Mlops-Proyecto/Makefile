.PHONY: install lint test index eval run docker-build docker-run compose-up clean

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

lint:
	ruff check .

test:
	pytest -q

index:
	python scripts/build_index.py

eval:
	python scripts/evaluate_rag.py

run:
	PYTHONPATH=src uvicorn cc0c2_mlops_rag.app:app --host 0.0.0.0 --port 8000 --reload

docker-build:
	docker build -t cc0c2-mlops-rag:local .

docker-run:
	docker run --rm -p 8000:8000 cc0c2-mlops-rag:local

compose-up:
	docker compose up --build

clean:
	rm -rf .pytest_cache .ruff_cache
	rm -rf data/indexes/*.pkl data/indexes/*.json
