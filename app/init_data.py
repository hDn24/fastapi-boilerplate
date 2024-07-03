import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))


from app.api.cruds import user as crud
from app.api.schemas.user import UseCreate
from app.configs import settings
from app.database import Base, SessionLocal, engine


def initialize_data() -> None:
    """
    Initializes the data for the application by resetting the database and creating a superuser.
    """
    session = SessionLocal()
    reset_database()

    superuser_data = UseCreate(
        username=settings.SUPER_USER,
        email=settings.SUPER_USER,
        password=settings.SUPER_USER_PASSWORD,
        is_superuser=True,
    )

    crud.create_user(session, superuser_data)


def reset_database() -> None:
    """
    Resets the database by dropping all tables and recreating them.

    """
    # Drop all tables from the database
    Base.metadata.drop_all(bind=engine)

    # Recreate all tables in the database
    Base.metadata.create_all(bind=engine)


initialize_data()
