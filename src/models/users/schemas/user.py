from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr

from common.enums.enums import Role


class UserBase(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    role: Optional[Role]


class User(UserBase):
    sid: UUID


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    old_password: Optional[str]
    new_password: Optional[str]
