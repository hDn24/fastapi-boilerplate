from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str | None = Field(examples=["hDn24"], default=None)
    email: str | None = Field(examples=["hDn24@gmail.com"])
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str = Field(examples=["..."])


class User(UserBase):
    hash_password: str = Field(examples=["..."])

    class Config:
        from_attributes = True


class UserUpdate(UserBase):
    email: str | None = Field(default=None)
    password: str = Field()


class UserUpdateMe(BaseModel):
    email: str | None = Field(default=None)
    username: str | None = Field(default=None)


class UserOut(UserBase):
    id: int
