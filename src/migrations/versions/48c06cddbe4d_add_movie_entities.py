"""Add movie entities

Revision ID: 48c06cddbe4d
Revises: 72aa0df75b91
Create Date: 2024-05-21 23:53:31.274768

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "48c06cddbe4d"
down_revision = "72aa0df75b91"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SCHEMA movies")

    op.create_table(
        "movie",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("genre", sa.String(), nullable=False),
        sa.Column("sid", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("sid"),
        schema="movies",
        comment="Table with all users",
    )
    op.create_index(
        op.f("ix_movies_movie_sid"), "movie", ["sid"], unique=True, schema="movies"
    )

    op.create_table(
        "movie_image",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("path", sa.String(), nullable=False),
        sa.Column("select_as_title", sa.Boolean(), nullable=False),
        sa.Column("movie_sid", sa.UUID(), nullable=True),
        sa.Column("sid", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["movie_sid"],
            ["movies.movie.sid"],
        ),
        sa.PrimaryKeyConstraint("sid"),
        schema="movies",
        comment="Table with all users",
    )
    op.create_index(
        op.f("ix_movies_movie_image_sid"),
        "movie_image",
        ["sid"],
        unique=True,
        schema="movies",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_movies_movie_image_sid"), table_name="movie_image", schema="movies"
    )
    op.drop_table("movie_image", schema="movies")

    op.drop_index(op.f("ix_movies_movie_sid"), table_name="movie", schema="movies")
    op.drop_table("movie", schema="movies")

    op.execute("DROP SCHEMA movies")
    # ### end Alembic commands ###