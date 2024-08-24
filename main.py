from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from api import router
from core.models import db
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db.dispose()


main_app = FastAPI(
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

main_app.include_router(router=router)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
