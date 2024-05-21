from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column
from common.db.base_model import BaseModel

SCHEMA = "movies"


class MovieImage(BaseModel):
    __tablename__ = "movie"
    __table_args__ = {
        "schema": SCHEMA,
        "comment": "Table with all users",
        "extend_existing": True,
    }

    name = mapped_column(String, nullable=False)
    path = mapped_column(String, nullable=False)

    movie_sid = mapped_column(ForeignKey("movies.movie.sid"))

    def __init__(self, name, description, images):
        self.name = name
        self.description = description
        self.images = images
