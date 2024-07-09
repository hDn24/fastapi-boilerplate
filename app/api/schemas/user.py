from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str | None = Field(example="hDn24", default=None)
    email: str = Field(example="hDn24@gmail.com")
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str = Field(example="...")


class User(UserBase):
    hash_password: str = Field(examples="...")

    class Config:
        from_attributes = True


class UserUpdate(UserBase):
    email: str | None = Field(example="hDn24@gmail.com", default=None)
    password: str = Field(example="...")


class UserOut(UserBase):
    id: int
