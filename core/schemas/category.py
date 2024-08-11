from pydantic import BaseModel


class CategoryRead(BaseModel):
    name: str
    description: str


class CategoryCreate(CategoryRead):
    pass


class CategoryUpdate(CategoryRead):
    pass
