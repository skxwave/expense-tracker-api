from pydantic import BaseModel


class WalletRead(BaseModel):
    name: str
    currency: str
    balance: int


class WalletCreate(WalletRead):
    pass


class WalletUpdate(WalletRead):
    pass
