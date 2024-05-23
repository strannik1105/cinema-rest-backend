"""Add staff tables

Revision ID: e523cddb5763
Revises: d2fd7a7e7903
Create Date: 2024-05-23 23:18:51.847461

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e523cddb5763'
down_revision = 'd2fd7a7e7903'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SCHEMA staff")

    op.create_table('cook',
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('surname', sa.String(), nullable=False),
                    sa.Column('sid', sa.UUID(), nullable=False),
                    sa.PrimaryKeyConstraint('sid'),
                    schema='staff'
                    )
    op.create_index(op.f('ix_staff_cook_sid'), 'cook', ['sid'], unique=True, schema='staff')

    op.create_table('waiter',
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('surname', sa.String(), nullable=False),
                    sa.Column('sid', sa.UUID(), nullable=False),
                    sa.PrimaryKeyConstraint('sid'),
                    schema='staff'
                    )
    op.create_index(op.f('ix_staff_waiter_sid'), 'waiter', ['sid'], unique=True, schema='staff')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_staff_waiter_sid'), table_name='waiter', schema='staff')
    op.drop_table('waiter', schema='staff')

    op.drop_index(op.f('ix_staff_cook_sid'), table_name='cook', schema='staff')
    op.drop_table('cook', schema='staff')

    op.execute("DROP SCHEMA staff")
    # ### end Alembic commands ###
