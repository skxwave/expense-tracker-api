from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.wallet import find_wallet
from crud import wallet as crud
from core.models import Wallet, User
from core.models import db
from core.schemas.wallet import WalletRead, WalletCreate, WalletUpdate
from .fastapi_users_router import current_user

router = APIRouter(
    prefix="/wallets",
    tags=["Wallets"],
)


@router.get("/{wallet_id}", response_model=WalletRead)
async def show_wallet(
    wallet: Wallet = Depends(find_wallet),
):
    return wallet


@router.get("/", response_model=List[WalletRead])
async def show_wallets(
    session: AsyncSession = Depends(db.session_getter),
    user: User = Depends(current_user),
):
    return await crud.show_all(
        session=session,
        user_id=user.id,
    )


@router.post("/add")
async def create_wallet(
    wallet_create: WalletCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(db.session_getter),
):
    return await crud.create(
        user_id=user.id,
        wallet_create=wallet_create,
        session=session,
    )


@router.put("/update/{wallet_id}")
async def update_wallet(
    wallet_update: WalletUpdate,
    wallet: Wallet = Depends(find_wallet),
    session: AsyncSession = Depends(db.session_getter),
):
    await crud.put(
        wallet_update=wallet_update,
        wallet=wallet,
        session=session,
    )
