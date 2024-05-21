from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import mapped_column
from common.db.base_model import BaseModel

SCHEMA = "food"


class FoodImage(BaseModel):
    __tablename__ = "food_image"
    __table_args__ = {
        "schema": SCHEMA,
        "comment": "Table with all users",
        "extend_existing": True,
    }

    name = mapped_column(String, nullable=False)
    path = mapped_column(String, nullable=False)
    select_as_title = mapped_column(Boolean, nullable=False)

    food_sid = mapped_column(ForeignKey("food.food.sid"))

    def __init__(self, name, path, select_as_title, food_sid):
        self.name = name
        self.path = path
        self.select_as_title = select_as_title
        self.food_sid = food_sid
