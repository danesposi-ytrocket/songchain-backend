"""create blockchain_currency and blockchain_network tables

Revision ID: 751738a0896a
Revises: aaa0490de8be
Create Date: 2024-05-05 10:15:25.265009

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '751738a0896a'
down_revision: Union[str, None] = 'aaa0490de8be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
