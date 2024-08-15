from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models import db, Transaction


async def find_expense(
    session: AsyncSession = Depends(db.session_getter),
    expense_id: int = Path,
):
    stmt = select(Transaction).where(Transaction.id == expense_id)
    expense = await session.scalar(statement=stmt)
    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found",
        )
    return expense
