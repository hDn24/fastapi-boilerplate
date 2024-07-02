from typing import List

from sqlalchemy.orm import Session

from app.api.models.user import User
from app.api.schemas.user import UseCreate
from app.api.utils.security import get_password_hash


def create_user(db: Session, user_data: UseCreate) -> User:
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


def get_users(skip: int, limit: int, db: Session) -> List[User]:
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
