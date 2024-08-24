from pydantic import BaseModel


class WalletBase(BaseModel):
    name: str
    currency: str
    balance: float


class WalletRead(WalletBase):
    id: float


class WalletCreate(WalletBase):
    pass


class WalletUpdate(WalletBase):
    pass
