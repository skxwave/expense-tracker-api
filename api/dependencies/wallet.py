from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models import db, Wallet, User
from ..api_v1.fastapi_users_router import current_user


async def find_wallet(
    session: AsyncSession = Depends(db.session_getter),
    wallet_id: int = Path,
    user: User = Depends(current_user),
):
    stmt = select(Wallet).where(
        Wallet.id == wallet_id,
        Wallet.user_id == user.id,
    )
    wallet = await session.scalar(statement=stmt)
    if not wallet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wallet not found",
        )
    return wallet
