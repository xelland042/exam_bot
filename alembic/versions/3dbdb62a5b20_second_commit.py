"""second commit

Revision ID: 3dbdb62a5b20
Revises: ef7e5ea87e9a
Create Date: 2023-11-25 19:55:09.224736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3dbdb62a5b20'
down_revision: Union[str, None] = 'ef7e5ea87e9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
