from sqlalchemy import String
from sqlalchemy.orm import mapped_column

from common.db.base_model import BaseModel

SCHEMA = "staff"


class Waiter(BaseModel):
    __tablename__ = "waiter"
    __table_args__ = {
        "schema": SCHEMA,
        "extend_existing": True,
    }

    name = mapped_column(String, nullable=False)
    surname = mapped_column(String, nullable=False)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
