from sqlalchemy.orm import Session

from app.api.models.user import User
from app.api.utils.security import verify_password


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


def authenticate(db: Session, email: str, password: str) -> User | None:
    """
    Authenticates a user based on their email and password.

    Args:
        db: The database session.
        email: The email of the user.
        password: The user's password.

    Returns:
        The authenticated user object if successful, otherwise None.
    """
    user = get_user_by_email(db, email)

    if user and verify_password(password, user.hash_password):
        return user

    return None
