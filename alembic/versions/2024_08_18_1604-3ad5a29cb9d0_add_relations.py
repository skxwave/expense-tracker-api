"""add relations

Revision ID: 3ad5a29cb9d0
Revises: 595dd09200aa
Create Date: 2024-08-18 16:04:22.382822

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3ad5a29cb9d0"
down_revision: Union[str, None] = "595dd09200aa"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, "transactions", "user", ["user_id"], ["id"])
    op.add_column(
        "wallets", sa.Column("user_id", sa.Integer(), nullable=False)
    )
    op.create_foreign_key(None, "wallets", "user", ["user_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "wallets", type_="foreignkey")
    op.drop_column("wallets", "user_id")
    op.drop_constraint(None, "transactions", type_="foreignkey")
    # ### end Alembic commands ###
