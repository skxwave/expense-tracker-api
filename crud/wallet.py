from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.schemas.wallet import WalletCreate, WalletUpdate
from core.models import Wallet


async def show_all(
    session: AsyncSession,
    user_id: int,
):
    result = await session.scalars(select(Wallet).where(Wallet.user_id == user_id))
    return result.all()


async def create(
    user_id: int,
    wallet_create: WalletCreate,
    session: AsyncSession,
):
    wallet = Wallet(**wallet_create.model_dump())
    wallet.user_id = user_id
    session.add(wallet)
    await session.commit()
    return wallet


async def put(
    wallet_update: WalletUpdate,
    wallet: Wallet,
    session: AsyncSession,
):
    for key, value in wallet_update.model_dump().items():
        setattr(wallet, key, value)
    await session.commit()
    return wallet


async def delete(
    wallet: Wallet,
    session: AsyncSession,
):
    await session.delete(wallet)
    await session.commit()
