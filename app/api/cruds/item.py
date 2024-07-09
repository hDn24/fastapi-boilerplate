from typing import List

from sqlalchemy.orm import Session

from app.api.models.user import Item
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
