from sqlalchemy.orm import Session

from app.api.cruds.user import get_user_by_email
from app.api.models.user import User
from app.api.utils.security import verify_password


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
