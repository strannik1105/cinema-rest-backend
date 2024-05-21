"""Add food entities

Revision ID: 21dc80b46091
Revises: 48c06cddbe4d
Create Date: 2024-05-22 02:09:36.149506

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "21dc80b46091"
down_revision = "48c06cddbe4d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SCHEMA food")
    op.create_table(
        "food",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("genre", sa.String(), nullable=False),
        sa.Column("sid", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("sid"),
        schema="food",
        comment="Table with all users",
    )
    op.create_index(
        op.f("ix_food_food_sid"), "food", ["sid"], unique=True, schema="food"
    )

    op.create_table(
        "food_image",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("path", sa.String(), nullable=False),
        sa.Column("select_as_title", sa.Boolean(), nullable=False),
        sa.Column("food_sid", sa.UUID(), nullable=True),
        sa.Column("sid", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["food_sid"],
            ["food.food.sid"],
        ),
        sa.PrimaryKeyConstraint("sid"),
        schema="food",
        comment="Table with all users",
    )
    op.create_index(
        op.f("ix_food_food_image_sid"),
        "food_image",
        ["sid"],
        unique=True,
        schema="food",
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_food_food_image_sid"), table_name="food_image", schema="food"
    )
    op.drop_table("food_image", schema="food")

    op.drop_index(op.f("ix_food_food_sid"), table_name="food", schema="food")
    op.drop_table("food", schema="food")
    op.execute("DROP SCHEMA food")
    # ### end Alembic commands ###
