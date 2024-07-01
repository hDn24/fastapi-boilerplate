from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from .configs import settings

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))


# Dependency
def get_db() -> Iterator[Session]:
    """
    Get a database session for executing database operations.

    Returns:
        Iterator[Session]: A context manager that provides a database session.
            The session is automatically closed when the context is exited.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
