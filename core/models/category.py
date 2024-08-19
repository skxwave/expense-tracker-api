from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey

from . import Base
from .mixins import TableIdMixin, TransactionRelationMixin, UserRelationMixin


class Category(Base, TableIdMixin, TransactionRelationMixin, UserRelationMixin):
    __tablename__ = "categories"
    _transaction_back_populates = "category"
    _user_back_populates = "categories"

    name: Mapped[str] = mapped_column(String(80))
    description: Mapped[str] = mapped_column(String(120))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
