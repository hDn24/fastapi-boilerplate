from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(example="hDn24")
    email: str = Field(example="hDn24@gmail")
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)

    class Config:
        orm_mode = True


class UseCreate(UserBase):
    password: str = Field(example="...")


class User(UserBase):
    hash_password: str = Field(examples="...")

    class Config:
        orm_mode = True


class UserOut(UserBase):
    id: int