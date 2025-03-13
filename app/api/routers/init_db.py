from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.cruds import init_db as crud
from app.database import Base, engine, get_db

router = APIRouter(prefix="/db", tags=["init_db"])


@router.post("/init_db", response_model=dict)
def init_db(db: Session = Depends(get_db)) -> dict:
    """
    Initialize the database by creating all tables and populating with initial data.

    Parameters:
        db: Database session

    Returns:
        A message confirming database initialization
    """

    Base.metadata.create_all(bind=engine)
    crud.initialize_data(db)
    return {"message": "Database initialized"}


@router.delete("/reset_db", response_model=dict)
def reset_db() -> dict:
    """
    Reset the database by dropping all tables and recreating them.

    Returns:
        A message confirming database reset
    """
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    return {"message": "Database reset successfully"}
