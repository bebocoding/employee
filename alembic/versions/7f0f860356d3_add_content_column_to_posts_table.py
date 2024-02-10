"""add content column to posts table

Revision ID: 7f0f860356d3
Revises: 673ee8845c83
Create Date: 2024-02-01 15:08:26.268791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f0f860356d3'
down_revision: Union[str, None] = '673ee8845c83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
