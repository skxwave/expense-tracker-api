from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from . import Base
from .mixins import TableIdMixin, TransactionRelationMixin


class Wallet(Base, TableIdMixin, TransactionRelationMixin):
    __tablename__ = "wallets"
    _transaction_back_populates = "wallet"

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    currency: Mapped[str] = mapped_column(String(50), nullable=False)
    balance: Mapped[int]
