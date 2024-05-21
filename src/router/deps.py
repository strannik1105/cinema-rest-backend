from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.db.session import get_pg_session
from models.users.auth_repository import AuthRepository
from models.users.user_repository import UserRepository
from services.auth.auth_service import AuthService
from services.users.user_service import UserService

PGSession = Annotated[AsyncSession, Depends(get_pg_session)]

user_repository = UserRepository()


def get_user_repository() -> UserRepository:
    return user_repository


user_service = UserService(user_repository)


auth_repository = AuthRepository()


def get_auth_repository() -> AuthRepository:
    return auth_repository


auth_service = AuthService(user_repository)


def get_user_service() -> UserService:
    return user_service


def get_auth_service() -> AuthService:
    return auth_service
