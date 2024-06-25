from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(example="hDn24")
    email: str = Field(example="hDn24@gmail")
    password: str = Field(example="2ES69y0EFiPynrhAelkcmBTgOGTTirDBJ4G0R-y9qcQ")
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)


class UseCreate(UserBase):
    pass
