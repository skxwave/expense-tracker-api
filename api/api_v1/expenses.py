from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from ..api_v1.fastapi_users_router import current_user
from api.dependencies.transaction import find_expense
from api.dependencies.pagination import pagination_params
from crud import transaction as crud
from core.schemas import (
    TransactionCreate,
    TransactionRead,
    TransactionUpdate,
    Pagination,
)
from core.models import Transaction, db, User

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"],
)


@router.get("/{expense_id}", response_model=TransactionRead)
async def show_expense(
    expense: Transaction = Depends(find_expense),
):
    return expense


@router.get("/", response_model=list[TransactionRead])
async def show_expenses(
    pagination: Pagination = Depends(pagination_params),
    session: AsyncSession = Depends(db.session_getter),
    user: User = Depends(current_user),
):
    return await crud.show_all(
        session=session,
        transaction_type="expense",
        limit=pagination.per_page,
        page=pagination.page,
        user_id=user.id,
    )


@router.post("/add", response_model=TransactionCreate)
async def add_expense(
    transaction_create: TransactionCreate,
    session: AsyncSession = Depends(db.session_getter),
    user: User = Depends(current_user),
):
    return await crud.add(
        transaction_type="expense",
        transaction_create=transaction_create,
        session=session,
        user_id=user.id,
    )


# @router.put("/update/{transaction_id}")
# async def update_expense(
#     transaction_update: TransactionUpdate,
#     transaction: Transaction = Depends(find_expense),
#     session: AsyncSession = Depends(db.session_getter),
# ):
#     result = await crud.put(
#         transaction=transaction,
#         transaction_update=transaction_update,
#         session=session,
#     )
#     return result


@router.delete("/delete/{transaction_id}")
async def delete_expense(
    transaction: Transaction = Depends(find_expense),
    session: AsyncSession = Depends(db.session_getter),
):
    await crud.delete(
        transaction=transaction,
        session=session,
    )
    return transaction
