from typing import List

from fastapi import APIRouter, Depends, HTTPException, status  # type: ignore
from sqlalchemy.orm import Session

from app.api.cruds import item as crud
from app.api.schemas.item import ItemCreate, ItemOut
from app.database import get_db
from app.dependencies import CurrentUser

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=List[ItemOut])
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


@router.get("/{item_id}", response_model=ItemOut | None)
def read_item_by_id(item_id: int, current_user: CurrentUser, db: Session = Depends(get_db)):
    """
    Retrieves an item from the database based on the provided item ID and current user.

    Args:
        item_id: The ID of the item to retrieve.
        current_user: The current user object obtained from the dependency.
        db: The database session obtained from the `get_db` dependency.

    Returns:
        An Item object retrieved from the database.

    Raises:
        HTTPException: If the item is not found.
    """
    item = crud.get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    if not current_user.is_superuser and item.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")

    return item


@router.post("/", response_model=ItemOut)
def create_item(item: ItemCreate, current_user: CurrentUser, db: Session = Depends(get_db)):
    """
    Creates an item in the database.

    Args:
        item: The item data to create.
        db: The database session obtained from the `get_db` dependency.
        current_user: The current user object obtained from the dependency.

    Returns:
        An Item object created in the database.
    """
    return crud.create_item(db=db, item=item, current_user=current_user)
