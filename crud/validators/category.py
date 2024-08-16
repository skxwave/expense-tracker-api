from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from core.models import Category


async def validate_category(
    category_id: int,
    session: AsyncSession,
):
    category = await session.get(Category, category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
    return category
