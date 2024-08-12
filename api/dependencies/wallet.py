from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models import db, Wallet


async def find_wallet(
    session: AsyncSession = Depends(db.session_getter),
    wallet_id: int = Path,
):
    stmt = select(Wallet).where(Wallet.id == wallet_id)
    category = await session.scalar(statement=stmt)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wallet not found",
        )
    return category
