FROM python:3.10.4-slim

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /code

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /code/

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

ENV VIRTUAL_ENV=/code/.venv \
    PATH=/code/.venv/bin:$PATH

COPY app app

CMD ["python", "-m", "app.main"]

