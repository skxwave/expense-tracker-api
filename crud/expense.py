from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status

from core.schemas.expense import ExpenseCreate, ExpenseUpdate
from core.models import Transaction, Category, Wallet


async def show_all(
    session: AsyncSession,
):
    result = await session.execute(select(Transaction))
    return result.scalars().all()


async def add(
    expense_create: ExpenseCreate,
    session: AsyncSession,
):
    wallet = await session.get(Wallet, expense_create.wallet_id)
    if not wallet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wallet not found",
        )

    category = await session.get(Category, expense_create.category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    if wallet.balance < expense_create.quantity:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Insufficient funds",
        )

    expense = Transaction(**expense_create.model_dump())
    session.add(expense)

    wallet.balance -= expense_create.quantity

    await session.commit()
    return expense


async def put(
    expense_update: ExpenseUpdate,
    expense: Transaction,
    session: AsyncSession,
):
    for key, value in expense_update.model_dump().items():
        setattr(expense, key, value)
    await session.commit()
    return expense


async def delete(
    expense: Transaction,
    session: AsyncSession,
):
    await session.delete(expense)
    await session.commit()
