from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from . import Base
from .mixins import TableIdMixin

if TYPE_CHECKING:
    from . import Transaction


class Category(Base, TableIdMixin):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(80))
    description: Mapped[str] = mapped_column(String(120))

    transactions: Mapped[List["Transaction"]] = relationship(
        "Transaction",
        back_populates="category",
    )
