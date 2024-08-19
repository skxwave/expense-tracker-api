from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from . import Base
from .mixins import TableIdMixin, TransactionRelationMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from . import Wallet


class User(TableIdMixin, SQLAlchemyBaseUserTable[int], Base, TransactionRelationMixin):
    _transaction_back_populates = "user"

    wallets: Mapped["Wallet"] = relationship(
        "Wallet",
        back_populates="user",
    )

    @classmethod
    def get_db(
        cls,
        session: "AsyncSession",
    ):
        return SQLAlchemyUserDatabase(session, cls)
