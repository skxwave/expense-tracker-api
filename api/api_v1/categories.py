from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from crud import category as crud
from api.dependencies.category import find_category
from api.dependencies.pagination import pagination_params
from core.schemas.category import CategoryCreate, CategoryRead
from core.schemas.pagination import Pagination
from core.models import Category, db


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.get("/{category_id}", response_model=CategoryRead)
async def show_category(
    category: Category = Depends(find_category),
):
    return category


@router.get("/", response_model=List[CategoryRead])
async def show_categories(
    session: AsyncSession = Depends(db.session_getter),
    pagination: Pagination = Depends(pagination_params),
):
    return await crud.show_all(
        session=session,
        limit=pagination.per_page,
        page=pagination.page,
    )


@router.post("/create", response_model=CategoryCreate)
async def create_category(
    category_create: CategoryCreate,
    session: AsyncSession = Depends(db.session_getter),
):
    return await crud.create(
        category_create=category_create,
        session=session,
    )


@router.delete("/{category_id}")
async def delete_category(
    category: Category = Depends(find_category),
    session: AsyncSession = Depends(db.session_getter),
):
    await crud.delete(category, session)
    return category
