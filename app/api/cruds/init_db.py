from sqlalchemy.orm import Session

from app.api.cruds import user as crud
from app.api.schemas.user import UserCreate
from app.configs import settings
from app.database import Base, engine


def initialize_data(db: Session) -> None:
    """Initializes the data for the application by resetting the database and creating a superuser."""

    superuser_data = UserCreate(
        email=settings.SUPER_USER,
        password=settings.SUPER_USER_PASSWORD,
        is_superuser=True,
    )

    crud.create_user(db, superuser_data)


def reset_database() -> None:
    """
    Resets the database by dropping all tables and recreating them.

    """
    # Drop all tables from the database
    Base.metadata.drop_all(bind=engine)

    # Recreate all tables in the database
    Base.metadata.create_all(bind=engine)
