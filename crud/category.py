from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.schemas.category import CategoryCreate, CategoryUpdate
from core.models import Category


async def show_all(
    session: AsyncSession,
    limit: int,
    page: int,
):
    result = await session.scalars(
        select(Category)
        .limit(limit)
        .offset(page - 1 if page == 1 else (page - 1) * limit),
    )
    return result.all()


async def create(
    category_create: CategoryCreate,
    session: AsyncSession,
):
    category = Category(**category_create.model_dump())
    session.add(category)
    await session.commit()
    return category


# TODO
async def put(
    category_update: CategoryUpdate,
    category: Category,
    session: AsyncSession,
):
    pass


async def delete(
    category: Category,
    session: AsyncSession,
):
    await session.delete(category)
    await session.commit()
