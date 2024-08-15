from pydantic import BaseModel


class WalletBase(BaseModel):
    name: str
    currency: str
    balance: int


class WalletRead(WalletBase):
    pass


class WalletCreate(WalletBase):
    pass


class WalletUpdate(WalletBase):
    pass
