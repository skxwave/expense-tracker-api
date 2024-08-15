from pydantic import BaseModel


class ExpenseRead(BaseModel):
    quantity: int
    description: str


class ExpenseCreate(ExpenseRead):
    wallet_id: int
    category_id: int


class ExpenseUpdate(ExpenseRead):
    pass
