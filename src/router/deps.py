from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.db.session import get_pg_session
from models.users.user_repository import UserRepository
from services.users.user_service import UserService

PGSession = Annotated[AsyncSession, Depends(get_pg_session)]

user_repository = UserRepository()


def get_user_repository() -> UserRepository:
    return user_repository


user_service = UserService(user_repository)


def get_user_service() -> UserService:
    return user_service
