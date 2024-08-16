from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy import select
from fastapi import HTTPException, status

from core.schemas.transaction import TransactionCreate, TransactionUpdate
from core.models import Transaction
from .validators import validate_wallet, validate_category


async def show_all(
    session: AsyncSession,
    transaction_type: str,
    limit: int,
    page: int,
):
    result = await session.scalars(
        select(Transaction)
        .options(
            joinedload(Transaction.category),
            joinedload(Transaction.wallet),
        )
        .where(Transaction.transaction_type == transaction_type)
        .limit(limit)
        .offset(page - 1 if page == 1 else (page - 1) * limit),
    )
    return result.all()


async def add(
    transaction_type: str,
    transaction_create: TransactionCreate,
    session: AsyncSession,
):
    wallet = await validate_wallet(
        session=session,
        wallet_id=transaction_create.wallet_id,
    )

    await validate_category(
        session=session,
        category_id=transaction_create.category_id,
    )

    if transaction_type == "expense":
        if wallet.balance < transaction_create.quantity:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Insufficient funds",
            )
        wallet.balance -= transaction_create.quantity
    else:
        wallet.balance += transaction_create.quantity

    transaction = Transaction(**transaction_create.model_dump())
    transaction.transaction_type = transaction_type
    session.add(transaction)

    await session.commit()
    return transaction


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
