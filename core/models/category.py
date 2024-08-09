from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from . import Base
from .mixins import TableIdMixin


class Category(Base, TableIdMixin):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(80))
    description: Mapped[str] = mapped_column(String(120))
