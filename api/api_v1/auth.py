from fastapi import APIRouter

from .fastapi_users_router import fastapi_users
from ..dependencies.auth.backend import auth_backend
from core.schemas.user import UserCreate, UserRead

router = APIRouter(prefix="/auth")

router.include_router(fastapi_users.get_auth_router(auth_backend))
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
