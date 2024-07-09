from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.cruds import item as crud
from app.api.schemas.item import Item
from app.database import get_db
from app.dependencies import CurrentUser

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=List[Item])
def read_items(current_user: CurrentUser, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieves a list of items from the database based on the provided skip and limit parameters.

    Args:
        current_user: The current user object obtained from the dependency.
        skip: The number of items to skip. Defaults to 0.
        limit: The maximum number of items to retrieve. Defaults to 100.
        db: The database session obtained from the `get_db` dependency.

    Returns:
        A list of Item objects retrieved from the database.
    """
    items = crud.get_items(db, skip, limit, current_user)

    if not items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items not found")

    return items
