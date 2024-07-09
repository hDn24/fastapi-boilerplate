from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, index=True, unique=True)
    hash_password = Column(String)
    is_active = Column(Boolean)
    is_superuser = Column(Boolean)
    items = relationship("Item", uselist=True, order_by="Item.id", backref="users")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
