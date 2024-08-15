from typing import TYPE_CHECKING, List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base
from .mixins import TableIdMixin

if TYPE_CHECKING:
    from . import Category
    from . import Wallet


class Transaction(Base, TableIdMixin):
    __tablename__ = "transactions"

    quantity: Mapped[int]
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallets.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    wallet: Mapped["Wallet"] = relationship(
        "Wallet",
        back_populates="transactions",
    )
    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="transactions",
    )
