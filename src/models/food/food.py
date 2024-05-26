from sqlalchemy import String, Float, ForeignKey
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
    price = mapped_column(Float, nullable=False)
    recipe = mapped_column(String, nullable=True)

    def __init__(self, name, description, price, recipe):
        self.name = name
        self.description = description
        self.price = price
        self.recipe = recipe
