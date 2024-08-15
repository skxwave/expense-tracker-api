from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.transaction import find_income
from crud import transaction as crud
from core.schemas.transaction import TransactionCreate, TransactionRead
from core.models import Transaction
from core.models import db

router = APIRouter(
    prefix="/income",
    tags=["Income"],
)


@router.get("/{income_id}", response_model=TransactionRead)
async def show_income(
    income: Transaction = Depends(find_income),
):
    return income


@router.get("/", response_model=list[TransactionRead])
async def show_incomes(
    session: AsyncSession = Depends(db.session_getter),
):
    return await crud.show_all(
        session=session,
        transaction_type="income",
    )


@router.post("/add", response_model=TransactionCreate)
async def add_income(
    transaction_create: TransactionCreate,
    session: AsyncSession = Depends(db.session_getter),
):
    return await crud.add(
        transaction_create=transaction_create,
        session=session,
    )
