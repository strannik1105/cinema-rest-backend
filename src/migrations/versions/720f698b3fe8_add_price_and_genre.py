"""Add price and genre

Revision ID: 720f698b3fe8
Revises: e523cddb5763
Create Date: 2024-05-23 23:52:03.246512

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '720f698b3fe8'
down_revision = 'e523cddb5763'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("food", sa.Column("price", sa.Float, nullable=False), schema="food")
    op.add_column("movie", sa.Column("genre", sa.String), schema="movies")


def downgrade() -> None:
    op.drop_column("movie", "genre", schema="movies")
    op.drop_column("food", "price", schema="food")
