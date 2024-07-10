from pydantic import BaseModel, Extra, Field


class ItemBase(BaseModel):
    title: str = Field(examples=["Foo"])
    description: str | None = Field(examples=["A very nice Item"])

    class Config:
        extra = Extra.forbid


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int = Field(examples=[1])
    owner_id: int = Field(examples=[1])

    class Config:
        from_attributes = True
        extra = Extra.forbid
