from typing import TYPE_CHECKING, List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base
from .mixins.table_id import TableIdMixin

if TYPE_CHECKING:
    from . import Transaction


class Wallet(Base, TableIdMixin):
    __tablename__ = "wallets"

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    currency: Mapped[str] = mapped_column(String(50), nullable=False)
    balance: Mapped[int]

    transactions: Mapped[List["Transaction"]] = relationship(
        "Transaction", back_populates="wallet"
    )
