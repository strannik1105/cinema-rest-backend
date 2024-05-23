"""Add superuser

Revision ID: d2fd7a7e7903
Revises: cb16afca1290
Create Date: 2024-05-23 01:34:49.379965

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd2fd7a7e7903'
down_revision = 'cb16afca1290'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        "INSERT INTO users.user (sid, name, email, password, role) VALUES ('cc859d7c-3fbf-4d89-ad81-1a31bbeebd42', 'root', 'root@root.com', '$2b$12$.PzoY1uUccOxI/A.CB1wteutIjF853LXRDPkR89Y.WPa0jDc4/1OC', 'ADMIN'::role) ON CONFLICT DO NOTHING"
    )


def downgrade() -> None:
    pass
