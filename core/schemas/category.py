from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    description: str


class CategoryRead(CategoryBase):
    pass


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass
