from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.schemas.category import CategoryCreate, CategoryUpdate
from core.models import Category


async def show_all(
    session: AsyncSession,
    limit: int,
    page: int,
    user_id: int,
):
    result = await session.scalars(
        select(Category)
        .where(Category.user_id == user_id)
        .limit(limit)
        .offset(page - 1 if page == 1 else (page - 1) * limit),
    )
    return result.all()


async def create(
    category_create: CategoryCreate,
    session: AsyncSession,
    user_id: int,
):
    category = Category(**category_create.model_dump())
    category.user_id = user_id
    session.add(category)
    await session.commit()
    return category


# TODO
async def put(
    category_update: CategoryUpdate,
    category: Category,
    session: AsyncSession,
):
    for key, value in category_update.model_dump().items():
        setattr(category, key, value)
    await session.commit()
    return category


async def delete(
    category: Category,
    session: AsyncSession,
):
    await session.delete(category)
    await session.commit()
