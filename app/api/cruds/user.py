from typing import List

from sqlalchemy import update
from sqlalchemy.orm import Session

from app.api.models.user import User
from app.api.schemas.user import UserCreate, UserUpdate
from app.api.utils.security import get_password_hash


def create_user(db: Session, user_data: UserCreate) -> User:
    """
    Create a new user in the database.

    Args:
        db: The database session.
        user_data: The data of the user to be created.

    Returns:
        User: The created user object.
    """
    # Generate the hashed password from the provided password
    hashed_password = get_password_hash(user_data.password)
    # Create the user object and add it to the database in one step
    user = User(**user_data.dict(exclude={"password"}), hash_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session, skip: int, limit: int) -> List[User]:
    """
    Retrieves a list of users from the database.

    Args:
        skip: The number of users to skip.
        limit: The maximum number of users to retrieve.
        db: The database session.

    Returns:
        A list of user objects.
    """
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, id: int) -> User | None:
    """
    Retrieves a user from the database by their ID.

    Args:
        db: The database session.
        id: The ID of the user.

    Returns:
        The user object if found, otherwise None.
    """
    return db.query(User).filter(User.id == id).first()


def get_user_by_email(db: Session, email: str) -> User | None:
    """
    Retrieves a user from the database based on their email.

    Args:
        db: The database session.
        email: The email of the user.

    Returns:
        The user object if found, otherwise None.
    """
    return db.query(User).filter(User.email == email).first()


def update_user(db: Session, user: User, user_update: UserUpdate, hashed_password: str):
    """
    Updates a user in the database.

    Args:
        db: The database session.
        user: The user object to update.
        user_update: The updated user data.
        hashed_password: The hashed password of the user.
    """
    stmt = (
        update(User)
        .where(User.id == user.id)
        .values(**user_update.dict(exclude={"password"}), hash_password=hashed_password)
        .execution_options(synchronize_session="fetch")
    )

    db.execute(stmt)
    db.commit()
