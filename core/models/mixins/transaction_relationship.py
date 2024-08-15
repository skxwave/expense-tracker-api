from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship, declared_attr

if TYPE_CHECKING:
    from core.models import Transaction


class TransactionRelationMixin:
    _transaction_back_populates: str = None

    @declared_attr
    def transactions(cls) -> Mapped[List["Transaction"]]:
        return relationship(
            "Transaction",
            back_populates=cls._transaction_back_populates,
        )
