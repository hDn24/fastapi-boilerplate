from sqlalchemy.orm import Session

from app.api.models.user import User
from app.api.schemas.user import UseCreate


def create_user(db: Session, user_create: UseCreate):
    user = User(**user_create.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
