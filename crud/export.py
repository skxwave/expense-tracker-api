import csv
from io import BytesIO

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy import select
import pandas as pd

from core.models import Transaction


async def export_data(
    session: AsyncSession,
    user_id: int,
):
    result = await session.scalars(
        select(Transaction)
        .options(
            joinedload(Transaction.wallet),
            joinedload(Transaction.category),
        )
        .where(Transaction.user_id == user_id)
    )

    dataframe = pd.DataFrame(
        [
            {
                "transaction_type": txn.transaction_type,
                "quantity": txn.quantity,
                "description": txn.description,
                "wallet_balance_after": txn.wallet_balance_after,
                "wallet_name": txn.wallet.name,
                "wallet_id": txn.wallet.id,
                "category_name": txn.category.name,
                "category_id": txn.category.id,
            }
            for txn in result
        ]
    )

    output = BytesIO()
    dataframe.to_csv(output, index=False)
    output.seek(0)

    return output
