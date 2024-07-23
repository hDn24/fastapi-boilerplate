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

*Install required Python packages:*
```shell
$ pip install poetry
$ poetry install
```


### Install (for local development)

*- Make your own `.env` file from the example:*
```shell
$ cp .env.example .env
# update values
```

*- Execute below command to build `db` and init data:*
```shell
$ make db
```

*- Execute below command to run the app at local:*
```shell
$ make api
```

### API docs
*Now, you can view API docs via* http://localhost:8000/docs/

## Deployment
