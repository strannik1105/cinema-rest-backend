"""Add waiter and staff sids

Revision ID: 0bfc4f2c3a2d
Revises: 720f698b3fe8
Create Date: 2024-05-26 01:24:46.885988

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0bfc4f2c3a2d'
down_revision = '720f698b3fe8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("food", Column("recipe", sa.String, nullable=True), schema="food")

    op.add_column(
        "food",
        sa.Column(
            "waiter_sid",
            postgresql.UUID(as_uuid=True),
            nullable=True,
        ),
        schema="food",
    )
    op.create_foreign_key(
        "food_waiter_sid_fkey",
        "food",
        "waiter",
        ["waiter_sid"],
        ["sid"],
        source_schema="food",
        referent_schema="staff",
    )

    op.add_column(
        "food",
        sa.Column(
            "cook_sid",
            postgresql.UUID(as_uuid=True),
            nullable=True,
        ),
        schema="food",
    )
    op.create_foreign_key(
        "food_cook_sid_fkey",
        "food",
        "cook",
        ["cook_sid"],
        ["sid"],
        source_schema="food",
        referent_schema="staff",
    )


def downgrade() -> None:
    op.drop_constraint(
        "food_waiter_sid_fkey",
        "food",
        schema="food",
        type_="foreignkey",
    )
    op.drop_column("food", "waiter_sid", schema="food")

    op.drop_constraint(
        "food_cook_sid_fkey",
        "food",
        schema="food",
        type_="foreignkey",
    )
    op.drop_column("food", "cook_sid", schema="food")

    op.drop_column("food", "recipe", schema="food")
