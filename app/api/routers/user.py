from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.api.cruds import user as crud
from app.api.models.user import User
from app.api.schemas.user import UserCreate, UserOut, UserUpdate
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


@router.post("/", dependencies=[Depends(get_current_active_superuser)], response_model=UserOut)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)) -> User:
    """
    Create a new user.

    Args:
        user_data: The data of the user to be created.
        db: The database session. Defaults to the session obtained from the `get_db` dependency.

    Returns:
        User
    """
    user = crud.get_user_by_email(db, email=user_data.email)

    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    return crud.create_user(db, user_data)


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


@router.patch("/{user_id}", dependencies=[Depends(get_current_active_superuser)], response_model=UserOut)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    """
    Updates a user in the database with the given user ID and user update data.

    Args:
        user_id: The ID of the user to update.
        user_update: The updated user data.
        db: The database session. Defaults to the session obtained from the `get_db` dependency.

    Returns:
        UserOut: The updated user object.

    Raises:
        HTTPException: If the user is not found, if the email is already registered, or if there is an error updating the user.
    """
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if user_update.email:
        existing_user = crud.get_user_by_email(db, email=user_update.email)
        if existing_user and existing_user.id != user_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    try:
        crud.update_user(db, user, user_update)
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.errors())
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Update failed")

    return crud.get_user_by_id(db, user_id)


@router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int, current_user: CurrentUser, db: Session = Depends(get_db)):
    """
    Deletes a user by ID.

    Args:
        user_id: The ID of the user to delete.
        current_user: The current user object.
        db: The database session. Defaults to the session obtained from the `get_db` dependency.

    Returns:
        A message indicating the success of the deletion.

    Raises:
        HTTPException: If the user is not found or if there are permission issues.
    """
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    elif user != current_user and not user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="The user doesn't have enough privileges")
    elif user == current_user and user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Superuser cannot delete themselves")

    crud.delete_user(db, user)
    return {"message": "User deleted successfully"}
