from fastapi import APIRouter

from .categories import router as category_router
from .wallets import router as wallet_router
from .expenses import router as expense_router
from .income import router as income_router

router = APIRouter(prefix="/v1")

router.include_router(category_router)
router.include_router(wallet_router)
router.include_router(expense_router)
router.include_router(income_router)
