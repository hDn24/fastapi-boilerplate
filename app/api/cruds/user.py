from sqlalchemy.orm import Session

from app.api.models.user import User
from app.api.schemas import user as schemas
from app.api.schemas.user import UseCreate
from app.api.utils.security import get_password_hash


def create_user(db: Session, user_create: UseCreate):
    user_dict = user_create.dict()
    user_dict["hash_password"] = get_password_hash(user_create.password)
    user_hashed = schemas.User(**user_dict)
    user = User(**user_hashed.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
