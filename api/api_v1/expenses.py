from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.expense import find_expense
from crud import expense as crud
from core.schemas.expense import ExpenseCreate
from core.models import Transaction
from core.models import db

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"],
)


@router.get("/{expense_id}")
async def show_expense(
    expense: Transaction = Depends(find_expense),
):
    return expense


@router.get("/")
async def show_expenses(
    session: AsyncSession = Depends(db.session_getter),
):
    return await crud.show_all(session=session)


@router.post("/add")
async def add_expense(
    expense_create: ExpenseCreate,
    session: AsyncSession = Depends(db.session_getter),
):
    return await crud.add(
        expense_create=expense_create,
        session=session,
    )
