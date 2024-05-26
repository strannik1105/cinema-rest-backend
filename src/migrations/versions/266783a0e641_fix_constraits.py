"""fix constraits

Revision ID: 266783a0e641
Revises: 0bfc4f2c3a2d
Create Date: 2024-05-26 23:28:31.123882

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '266783a0e641'
down_revision = '0bfc4f2c3a2d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column("food", "genre", schema="food")
    op.drop_column("movie", "price", schema="movies")


def downgrade() -> None:
    op.add_column("movie", sa.Column("price", sa.Float()), schema="movies")
    op.add_column("food", sa.Column("genre", sa.String(), nullable=True), schema="food")
