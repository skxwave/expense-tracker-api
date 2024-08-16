from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.transaction import find_expense
from api.dependencies.pagination import pagination_params
from crud import transaction as crud
from core.schemas.transaction import TransactionCreate, TransactionRead
from core.schemas.pagination import Pagination
from core.models import Transaction
from core.models import db

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"],
)


@router.get("/{expense_id}", response_model=TransactionRead)
async def show_expense(
    expense: Transaction = Depends(find_expense),
):
    return expense


@router.get("/", response_model=list[TransactionRead])
async def show_expenses(
    pagination: Pagination = Depends(pagination_params),
    session: AsyncSession = Depends(db.session_getter),
):
    return await crud.show_all(
        session=session,
        transaction_type="expense",
        limit=pagination.per_page,
        page=pagination.page,
    )


@router.post("/add", response_model=TransactionCreate)
async def add_expense(
    transaction_create: TransactionCreate,
    session: AsyncSession = Depends(db.session_getter),
):
    return await crud.add(
        transaction_type="expense",
        transaction_create=transaction_create,
        session=session,
    )
