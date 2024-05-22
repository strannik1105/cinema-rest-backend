"""Add room and booking entities

Revision ID: cb16afca1290
Revises: 21dc80b46091
Create Date: 2024-05-22 21:41:47.365549

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cb16afca1290'
down_revision = '21dc80b46091'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SCHEMA rooms")
    
    op.create_table('room',
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('description', sa.String(), nullable=True),
                    sa.Column('cost_per_hour', sa.Float(), nullable=False),
                    sa.Column('x', sa.Float(), nullable=False),
                    sa.Column('y', sa.Float(), nullable=False),
                    sa.Column('width', sa.Float(), nullable=True),
                    sa.Column('height', sa.Float(), nullable=True),
                    sa.Column('sid', sa.UUID(), nullable=False),
                    sa.PrimaryKeyConstraint('sid'),
                    schema='rooms',
                    comment='Table with all users'
                    )
    op.create_index(op.f('ix_rooms_room_sid'), 'room', ['sid'], unique=True, schema='rooms')

    op.create_table('booking',
                    sa.Column('room_sid', sa.UUID(), nullable=False),
                    sa.Column('user_sid', sa.UUID(), nullable=False),
                    sa.Column('datetime_start', sa.DateTime(), nullable=False),
                    sa.Column('datetime_end', sa.DateTime(), nullable=False),
                    sa.Column('sid', sa.UUID(), nullable=False),
                    sa.ForeignKeyConstraint(['room_sid'], ['rooms.room.sid'], ),
                    sa.ForeignKeyConstraint(['user_sid'], ['users.user.sid'], ),
                    sa.PrimaryKeyConstraint('sid'),
                    schema='rooms',
                    comment='Table with all users'
                    )
    op.create_index(op.f('ix_rooms_booking_sid'), 'booking', ['sid'], unique=True, schema='rooms')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_rooms_booking_sid'), table_name='booking', schema='rooms')
    op.drop_table('booking', schema='rooms')

    op.drop_index(op.f('ix_rooms_room_sid'), table_name='room', schema='rooms')
    op.drop_table('room', schema='rooms')

    op.execute("DROP SCHEMA rooms")
    # ### end Alembic commands ###
