from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy import select
from fastapi import HTTPException, status

from core.schemas.transaction import TransactionCreate, TransactionUpdate
from core.models import Transaction, Category, Wallet


async def show_all(
    session: AsyncSession,
    transaction_type: str,
):
    result = await session.execute(
        select(Transaction)
        .options(
            joinedload(Transaction.category),
            joinedload(Transaction.wallet),
        )
        .where(Transaction.transaction_type == transaction_type),
    )
    return result.scalars().all()


# TODO: default transaction_type, depends on endpoint (income, expense)
async def add(
    transaction_create: TransactionCreate,
    session: AsyncSession,
):
    if transaction_create.transaction_type not in ["expense", "income"]:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Invalid transaction type",
        )

    wallet = await session.get(Wallet, transaction_create.wallet_id)
    if not wallet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wallet not found",
        )

    category = await session.get(Category, transaction_create.category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    if wallet.balance < transaction_create.quantity:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Insufficient funds",
        )

    expense = Transaction(**transaction_create.model_dump())
    session.add(expense)

    if transaction_create.transaction_type == "expense":
        wallet.balance -= transaction_create.quantity
    else:
        wallet.balance += transaction_create.quantity

    await session.commit()
    return expense


async def put(
    transaction_update: TransactionUpdate,
    transaction: Transaction,
    session: AsyncSession,
):
    for key, value in transaction_update.model_dump().items():
        setattr(transaction, key, value)
    await session.commit()
    return transaction


async def delete(
    transaction: Transaction,
    session: AsyncSession,
):
    await session.delete(transaction)
    await session.commit()
