from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.cruds import user as crud
from app.api.models.user import User
from app.api.schemas.user import UserOut
from app.database import get_db
from app.dependencies import get_current_active_superuser

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", dependencies=[Depends(get_current_active_superuser)], response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[User]:
    """
    Retrieves a list of users from the database.

    Args:
        skip : The number of users to skip. Defaults to 0.
        limit: The maximum number of users to retrieve. Defaults to 100.
        db: The database session. Defaults to the session obtained from the `get_db` dependency.

    Returns:
        A list of user objects.

    Raises:
        HTTPException: If no users are found in the database.
    """
    users = crud.get_users(db, skip, limit)
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not found")
    return users


@router.get("/{id}")
def get_user():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")


@router.post("/")
def create_user():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")


@router.put("/{id}")
def update_user():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")


@router.delete("/{id}")
def delete_user():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")
