# fastapi-boilerplate

## Based
- python `3.10.4`
- pip `22.x`

## Technology Stack
- ⚡ [FastAPI](https://fastapi.tiangolo.com) for the Python backend API.
    - 🧰 [SQLAlchemy](https://www.sqlalchemy.org/) for the Python SQL database interactions (ORM).
    - 🔍 [Pydantic](https://docs.pydantic.dev), used by FastAPI, for the data validation and settings management.
    - 💾 [PostgreSQL](https://www.postgresql.org) as the SQL database.
- 🐋 [Docker Compose](https://www.docker.com) for development and production.
- 🚢 Deployment instructions using Docker Compose.
- 🏭 CI (continuous integration) and CD (continuous deployment) based on GitHub Actions.

## Development

### Coding

**Tools:**

- Editor: `Visual Code`<br>*Please install required extensions*
- Package management tools: `Poetry`
- Local runtime: `Docker-compose`

### Environment

#### Setup python version with pyenv

    pyenv install 3.10.4
    pyenv local 3.10.4

#### Setup venv with poetry

*Install required Python packages:*
```shell
$ pip install poetry
$ poetry config virtualenvs.in-project true
$ poetry run pip install --upgrade pip
$ poetry install
```

*`.venv` directory is created in this project directory, and Python and packages are installed.*

#### Enter venv environment

    source .venv/bin/activate

or

    poetry shell


### Install (for local development)
*- Execute the below command to run the app at locally:*
```shell
$ make local
$ make start-local
```

### API docs
*Now, you can view API docs via* http://localhost:8000/docs/

## Deployment
- TBU
