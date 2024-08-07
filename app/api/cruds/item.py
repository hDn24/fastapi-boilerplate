from typing import List

from sqlalchemy import delete, update
from sqlalchemy.orm import Session

from app.api.models.user import Item
from app.api.schemas.item import ItemCreate, ItemUpdate
from app.dependencies import CurrentUser


def get_items(db: Session, skip: int, limit: int, current_user: CurrentUser) -> List[Item]:
    """
    Retrieves a list of items from the database based on the provided skip, limit, and current user.

    Args:
        db: The database session.
        skip: The number of items to skip.
        limit: The maximum number of items to retrieve.
        current_user: The current user object.

    Returns:
        A list of Item objects retrieved from the database.
    """
    query = db.query(Item).order_by(Item.id).offset(skip).limit(limit)
    if not current_user.is_superuser:
        query = query.filter(Item.owner_id == current_user.id)

    return query.all()


def get_item_by_id(db: Session, id: int) -> Item | None:
    """
    Retrieves an item from the database based on the provided item ID and current user.

    Args:
        db: The database session.
        id: The ID of the item to retrieve.

    Returns:
        An Item object retrieved from the database.

    Raises:
        HTTPException: If the item is not found.
    """
    return db.query(Item).filter(Item.id == id).first()


def create_item(db: Session, item: ItemCreate, current_user: CurrentUser) -> Item:
    """
    Creates an item in the database.

    Args:
        db: The database session.
        item: The item data to create.
        current_user: The current user object.

    Returns:
        An Item object created in the database.
    """
    db_item = Item(**item.dict(), owner_id=current_user.id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, id: int, item_update: ItemUpdate) -> Item | None:
    """
    Updates an item in the database.

    Args:
        db: The database session.
        id: The ID of the item to update.
        item_update: The item data to update.

    Returns:
        An Item object updated in the database.
    """
    stmt = update(Item).where(Item.id == id).values(**item_update.dict()).execution_options(synchronize_session="fetch")

    db.execute(stmt)
    db.commit()

    return db.query(Item).filter(Item.id == id).first()


def delete_item_by_id(db: Session, id: int) -> None:
    """
    Deletes an item by ID.

    Args:
        db: The database session.
        id: The ID of the item to delete.
    """
    stmt = delete(Item).where(Item.id == id).execution_options(synchronize_session="fetch")
    db.execute(stmt)
    db.commit()
