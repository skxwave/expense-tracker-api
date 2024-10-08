"""add transaction_type column

Revision ID: 8f09588da7c0
Revises: 264e99d7d481
Create Date: 2024-08-15 18:44:36.294664

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8f09588da7c0"
down_revision: Union[str, None] = "264e99d7d481"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "transactions",
        sa.Column("transaction_type", sa.String(length=10), nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("transactions", "transaction_type")
    # ### end Alembic commands ###
