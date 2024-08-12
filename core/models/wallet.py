from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from . import Base
from .mixins.table_id import TableIdMixin


class Wallet(Base, TableIdMixin):
    __tablename__ = "wallets"

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    currency: Mapped[str] = mapped_column(String(50), nullable=False)
    balance: Mapped[int]
