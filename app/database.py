from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from .configs import settings

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{settings.db_user}:{settings.db_pass}@{settings.db_host}:{settings.db_port}/"
    f"{settings.db_name}?client_encoding=utf8"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, echo=settings.sqlalchemy_echo
)
SessionLocal = scoped_session(
    sessionmaker(bind=engine, autocommit=False, autoflush=False)
)


# Dependency
def get_db() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
