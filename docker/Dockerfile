FROM python:3.10.4-slim

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /src

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /src/

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

ENV VIRTUAL_ENV=/src/.venv \
    PATH=/src/.venv/bin:$PATH

COPY ./app /src/app

ENTRYPOINT poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
