from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from . import Base
from .mixins import TableIdMixin, TransactionRelationMixin


class Category(Base, TableIdMixin, TransactionRelationMixin):
    __tablename__ = "categories"
    _transaction_back_populates = "category"

    name: Mapped[str] = mapped_column(String(80))
    description: Mapped[str] = mapped_column(String(120))
