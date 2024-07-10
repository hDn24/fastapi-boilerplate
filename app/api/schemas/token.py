from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str = Field(examples=["ey..."])
    token_type: str = Field(default="bearer")


class TokenPayload(BaseModel):
    sub: int = Field(examples=[1])
