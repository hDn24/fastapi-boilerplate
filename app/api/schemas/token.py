from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str = Field(example="ey...")
    token_type: str = Field(default="bearer")
