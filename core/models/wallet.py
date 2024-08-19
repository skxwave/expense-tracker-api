from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base
from .mixins import TableIdMixin, TransactionRelationMixin

if TYPE_CHECKING:
    from . import User


class Wallet(Base, TableIdMixin, TransactionRelationMixin):
    __tablename__ = "wallets"
    _transaction_back_populates = "wallet"

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    currency: Mapped[str] = mapped_column(String(50), nullable=False)
    balance: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="wallets",
    )
