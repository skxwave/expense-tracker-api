from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models import db, Category, User
from ..api_v1.fastapi_users_router import current_user


async def find_category(
    session: AsyncSession = Depends(db.session_getter),
    category_id: int = Path,
    user: User = Depends(current_user),
):
    stmt = select(Category).where(
        Category.id == category_id,
        Category.user_id == user.id,
    )
    category = await session.scalar(statement=stmt)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
    return category
