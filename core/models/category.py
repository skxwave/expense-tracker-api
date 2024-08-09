from sqlalchemy.orm import Mapped, mapped_column

from . import Base
from .mixins import TableIdMixin


class Category(TableIdMixin, Base):
    name: Mapped[str]
    description: Mapped[str]
