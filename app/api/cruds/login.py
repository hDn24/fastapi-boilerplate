from typing import List

from sqlalchemy.orm import Session

from app.api.models.user import User
from app.api.utils.security import verify_password


def get_user_by_email(db: Session, email: str) -> List[User]:
    return db.query(User).filter(User.email == email).first()


def authenticate(db: Session, email: str, password: str):
    db_user = get_user_by_email(db, email)

    if not db_user:
        return None
    if not verify_password(password, db_user.hash_password):
        return None
    return db_user
