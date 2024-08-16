from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from core.models import Wallet


async def validate_wallet(
    wallet_id: int,
    session: AsyncSession,
):
    wallet = await session.get(Wallet, wallet_id)
    if not wallet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wallet not found",
        )
    return wallet
