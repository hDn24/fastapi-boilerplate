from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.cruds import user as crud
from app.api.models.user import User
from app.api.schemas.user import UserOut
from app.database import get_db
from app.dependencies import CurrentUser, get_current_active_superuser

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


@router.get("/{user_id}", response_model=UserOut | None)
def read_user_by_id(user_id: int, current_user: CurrentUser, db: Session = Depends(get_db)) -> User:
    """
    Retrieves a user from the database by ID.

    Args:
        user_id: The ID of the user to retrieve.
        current_user: The current user object.
        db: The database session. Defaults to the session obtained from the `get_db` dependency.

    Returns:
        The user object if found.

    Raises:
        HTTPException: If the user is not found or doesn't have enough privileges.
    """
    # Retrieve the user from the database
    user = crud.get_user_by_id(db, user_id)

    # Check if the user was found
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # Check if the current user has enough privileges to access the user's information
    if user != current_user and not user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="The user doesn't have enough privileges")

    # Return the user object
    return user


@router.post("/")
def create_user():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")


@router.put("/{id}")
def update_user():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")


@router.delete("/{id}")
def delete_user():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")
