from pydantic import BaseModel


class WalletBase(BaseModel):
    name: str
    currency: str
    balance: int


class WalletRead(WalletBase):
    id: int


class WalletCreate(WalletBase):
    pass


class WalletUpdate(WalletBase):
    pass
