from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship, declared_attr

if TYPE_CHECKING:
    from core.models import User


class UserRelationMixin:
    _user_back_populates: str = None

    @declared_attr
    def user(cls) -> Mapped[List["User"]]:
        return relationship(
            "User",
            back_populates=cls._user_back_populates,
        )
