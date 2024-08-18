import asyncio
import contextlib

from core.config import settings
from core.models import User
from core.models.db_helper import db_helper
from core.schemas.user import UserCreate
from core.authentication.user_manager import UserManager
from api.dependencies.auth.users import get_user_db
from api.dependencies.auth.user_manager import get_user_manager

# get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> User:
    return await user_manager.create(
        user_create=user_create,
        safe=False,
    )


async def create_superuser(
    email: str = settings.superuser.email,
    password: str = settings.superuser.password,
    is_active: bool = settings.superuser.is_active,
    is_superuser: bool = settings.superuser.is_superuser,
    is_verified: bool = settings.superuser.is_verified,
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )
    async with db_helper.session_factory() as session:
        async with get_user_db_context(session) as users_db:
            async with get_user_manager_context(users_db) as user_manager:
                return await create_user(
                    user_manager=user_manager,
                    user_create=user_create,
                )


if __name__ == "__main__":
    asyncio.run(create_superuser())
