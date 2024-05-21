from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import mapped_column
from common.db.base_model import BaseModel

SCHEMA = "movies"


class MovieImage(BaseModel):
    __tablename__ = "movie_image"
    __table_args__ = {
        "schema": SCHEMA,
        "comment": "Table with all users",
        "extend_existing": True,
    }

    name = mapped_column(String, nullable=False)
    path = mapped_column(String, nullable=False)
    select_as_title = mapped_column(Boolean, nullable=False)

    movie_sid = mapped_column(ForeignKey("movies.movie.sid"))

    def __init__(self, name, path, movie_sid):
        self.name = name
        self.path = path
        self.movie_sid = movie_sid
