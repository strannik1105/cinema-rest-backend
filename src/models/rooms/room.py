from sqlalchemy import String, Float
from sqlalchemy.orm import mapped_column
from common.db.base_model import BaseModel

SCHEMA = "rooms"


class Room(BaseModel):
    __tablename__ = "room"
    __table_args__ = {
        "schema": SCHEMA,
        "comment": "Table with all users",
        "extend_existing": True,
    }

    name = mapped_column(String, nullable=False)
    description = mapped_column(String, nullable=True)
    cost_per_hour = mapped_column(Float, nullable=False)
    x = mapped_column(Float, nullable=False)
    y = mapped_column(Float, nullable=False)
    width = mapped_column(Float, nullable=True)
    height = mapped_column(Float, nullable=True)

    def __init__(self, name, description, x, y, width, height):
        self.name = name
        self.description = description
        self.x = x
        self.y = y
        self.width = width
        self.height = height
