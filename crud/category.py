from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.schemas.category import CategoryRead, CategoryCreate, CategoryUpdate
from core.models import db, Category


async def find(
    category_id: int = Path,
    session: AsyncSession = Depends(db.session_getter),
):
    stmt = select(Category).where(Category.id == category_id)
    category = await session.scalar(statement=stmt)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
    return category


async def show_all(
    session: AsyncSession,
):
    result = await session.execute(select(Category))
    return result.scalars().all()


async def create(
    category_create: CategoryCreate,
    session: AsyncSession,
):
    category = Category(**category_create.model_dump())
    session.add(category)
    await session.commit()
    return category
