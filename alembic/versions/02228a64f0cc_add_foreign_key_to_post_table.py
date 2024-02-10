"""add foreign key to post table

Revision ID: 02228a64f0cc
Revises: c4c018eec9c1
Create Date: 2024-02-01 15:30:48.210943

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02228a64f0cc'
down_revision: Union[str, None] = 'c4c018eec9c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk',
                          source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', 'posts')
    op.drop_column('posts', 'owner_id')
    pass
