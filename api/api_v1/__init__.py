from fastapi import APIRouter

from .categories import router as category_router
from .wallets import router as wallet_router

router = APIRouter(prefix="/v1")

router.include_router(category_router)
router.include_router(wallet_router)
