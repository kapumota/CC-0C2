FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8891

ARG INSTALL_opcional=true

WORKDIR /workspace

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    wget \
    tini \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-base.txt requirements-opcional.txt ./

RUN python -m pip install --upgrade pip setuptools wheel && \
    pip install -r requirements-base.txt && \
    if [ "$INSTALL_opcional" = "true" ]; then \
        pip install -r requirements-opcional.txt; \
    fi

RUN python -m nltk.downloader punkt stopwords wordnet omw-1.4 averaged_perceptron_tagger && \
    python -m spacy download es_core_news_sm

EXPOSE 8891

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD sh -c "jupyter lab \
  --ip=0.0.0.0 \
  --port=${PORT} \
  --no-browser \
  --allow-root \
  --ServerApp.root_dir=/workspace"
