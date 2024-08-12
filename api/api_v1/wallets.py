from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.wallet import find_wallet
from crud import wallet as crud
from core.models import Wallet
from core.models import db
from core.schemas.wallet import WalletRead, WalletCreate, WalletUpdate

router = APIRouter(
    prefix="/wallets",
    tags=["Wallets"],
)


@router.get("{wallet_id}", response_model=WalletRead)
async def show_wallet(
    wallet: Wallet = Depends(find_wallet),
):
    return wallet


@router.get("/", response_model=List[WalletRead])
async def show_wallets(
    session: AsyncSession = Depends(db.session_getter),
):
    return await crud.show_all(session=session)


@router.post("/add")
async def create_wallet(
    wallet_create: WalletCreate,
    session: AsyncSession = Depends(db.session_getter),
):
    return await crud.create(
        wallet_create=wallet_create,
        session=session,
    )


@router.post("/update")
async def update_wallet():
    pass
