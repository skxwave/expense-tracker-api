from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base
from .mixins import TableIdMixin, TransactionRelationMixin, UserRelationMixin


class Wallet(Base, TableIdMixin, TransactionRelationMixin, UserRelationMixin):
    __tablename__ = "wallets"
    _transaction_back_populates = "wallet"
    _user_back_populates = "wallets"

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    currency: Mapped[str] = mapped_column(String(50), nullable=False)
    balance: Mapped[float]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
