from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, index=True, unique=True)
    hash_password = Column(String)
    is_active = Column(Boolean)
    is_superuser = Column(Boolean)
