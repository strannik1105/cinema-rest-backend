from sqlalchemy import String
from sqlalchemy.orm import mapped_column
from common.db.base_model import BaseModel

SCHEMA = "food"


class Food(BaseModel):
    __tablename__ = "food"
    __table_args__ = {
        "schema": SCHEMA,
        "comment": "Table with all users",
        "extend_existing": True,
    }

    name = mapped_column(String, nullable=False)
    description = mapped_column(String, nullable=False)
    genre = mapped_column(String, nullable=False)

    def __init__(self, name, description, genre):
        self.name = name
        self.description = description
        self.genre = genre
