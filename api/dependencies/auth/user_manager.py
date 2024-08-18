from typing import TYPE_CHECKING

from fastapi import Depends

from core.authentication import UserManager
from .users import get_user_db

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


async def get_user_manager(
    user_db: "SQLAlchemyUserDatabase" = Depends(get_user_db),
):
    yield UserManager(user_db)
