from sqlalchemy import Enum, String
from sqlalchemy.orm import mapped_column
from common.db.base_model import BaseModel
from common.enums.enums import Role

USER_SCHEMA = "users"


class User(BaseModel):
    __tablename__ = "user"
    __table_args__ = {"schema": USER_SCHEMA, "comment": "Table with all users"}

    name = mapped_column(String, nullable=False)
    email = mapped_column(String, nullable=False)
    password = mapped_column(String, nullable=False)
    role = mapped_column(Enum(Role, name="role"))

    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
