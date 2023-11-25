"""third commit

Revision ID: 5f2c6d7e6d52
Revises: 3dbdb62a5b20
Create Date: 2023-11-25 20:00:47.917249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f2c6d7e6d52'
down_revision: Union[str, None] = '3dbdb62a5b20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
