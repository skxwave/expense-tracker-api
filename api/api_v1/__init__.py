from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from .categories import router as category_router
from .wallets import router as wallet_router
from .expenses import router as expense_router
from .income import router as income_router
from .auth import router as auth_router
from .export import router as export_router

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix="/v1",
    dependencies=[Depends(http_bearer)],
)

router.include_router(category_router)
router.include_router(wallet_router)
router.include_router(expense_router)
router.include_router(income_router)
router.include_router(auth_router)
router.include_router(export_router)
