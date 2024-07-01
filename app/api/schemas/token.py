from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str = Field(example="ey...")
    token_type: str = Field(default="bearer")


class TokenPayload(BaseModel):
    sub: int = Field(example=1)
