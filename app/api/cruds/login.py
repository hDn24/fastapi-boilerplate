from typing import List

from sqlalchemy.orm import Session

from app.api.models.user import User
from app.api.utils.security import verify_password

# def get_user_by_email(db: Session, email: str) -> List[User]:
#     return db.query(User).all()


def authenticate(db: Session, email: str, password: str):
    # db_user = get_user_by_email(db, email)
    db_user = db.query(User).filter(User.email == email).first()

    print(db_user)

    if not db_user:
        return None
    if not verify_password(password, db_user.password):
        return None
    return db_user
