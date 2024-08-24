from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession

from crud.export import export_data
from core.models.db_helper import db_helper
from core.models import User
from ..api_v1.fastapi_users_router import current_user

router = APIRouter(
    prefix="/export",
    tags=["Export"],
)


@router.get("/csv")
async def download_csv(
    session: AsyncSession = Depends(db_helper.session_getter),
    user: User = Depends(current_user),
):
    output = await export_data(
        session=session,
        user_id=user.id,
    )

    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=transactions.csv"},
    )
