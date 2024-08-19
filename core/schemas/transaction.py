from pydantic import BaseModel

from .category import CategoryRead
from .wallet import WalletRead


class TransactionBase(BaseModel):
    quantity: int
    description: str | None


class TransactionRead(TransactionBase):
    id: int
    transaction_type: str
    wallet: WalletRead
    category: CategoryRead


class TransactionCreate(TransactionBase):
    wallet_id: int
    category_id: int


class TransactionUpdate(TransactionCreate):
    pass
