from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models import db, Category


async def find_category(
    session: AsyncSession = Depends(db.session_getter),
    category_id: int = Path,
):
    stmt = select(Category).where(Category.id == category_id)
    category = await session.scalar(statement=stmt)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
    return category
