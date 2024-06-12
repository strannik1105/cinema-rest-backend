from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column
from common.db.base_model import BaseModel

SCHEMA = "movies"


class Movie(BaseModel):
    __tablename__ = "movie"
    __table_args__ = {
        "schema": SCHEMA,
        "comment": "Table with all users",
        "extend_existing": True,
    }

    name = mapped_column(String, nullable=False)
    description = mapped_column(String, nullable=False)
    genre = mapped_column(String)
    year = mapped_column(Integer)
    duration = mapped_column(Integer)

    def __init__(self, name, description, genre, year, duration):
        self.name = name
        self.description = description
        self.genre = genre
        self.year = year
        self.duration = duration
