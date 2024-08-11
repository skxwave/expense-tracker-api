from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from crud import category as crud
from core.schemas.category import CategoryCreate
from core.models import Category, db


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.get("/{category_id}")
async def show_category(
    category: Category = Depends(crud.find),
):
    return category


@router.get("/")
async def show_categories(session: AsyncSession = Depends(db.session_getter)):
    return await crud.show_all(
        session=session,
    )


@router.post("/create")
async def create_category(
    category_create: CategoryCreate,
    session: AsyncSession = Depends(db.session_getter),
):
    return await crud.create(
        category_create=category_create,
        session=session,
    )
