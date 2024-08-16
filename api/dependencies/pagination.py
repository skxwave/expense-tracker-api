from fastapi import Query

from core.schemas.pagination import Pagination


async def pagination_params(
    page: int = Query(ge=1, default=1),
    per_page: int = Query(ge=1, le=100, default=10),
):
    return Pagination(
        page=page,
        per_page=per_page,
    )
