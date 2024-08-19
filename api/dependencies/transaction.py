from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy import select

from core.models import db, Transaction, User
from ..api_v1.fastapi_users_router import current_user


async def find_transaction(
    transaction_type: str,
    session: AsyncSession,
    transaction_id: int,
    user_id: int,
):
    stmt = (
        select(Transaction)
        .options(
            joinedload(Transaction.category),
            joinedload(Transaction.wallet),
        )
        .where(Transaction.transaction_type == transaction_type)
        .where(Transaction.id == transaction_id)
        .where(Transaction.user_id == user_id)
    )
    transaction = await session.scalar(statement=stmt)
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{transaction_type.capitalize()} not found",
        )
    return transaction


async def find_expense(
    session: AsyncSession = Depends(db.session_getter),
    transaction_id: int = Path,
    user: User = Depends(current_user),
):
    return await find_transaction(
        user_id=user.id,
        transaction_type="expense",
        session=session,
        transaction_id=transaction_id,
    )


async def find_income(
    session: AsyncSession = Depends(db.session_getter),
    transaction_id: int = Path,
    user: User = Depends(current_user),
):
    return await find_transaction(
        user_id=user.id,
        transaction_type="income",
        session=session,
        transaction_id=transaction_id,
    )
