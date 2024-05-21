from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.db.session import get_pg_session
from models.movies.repository.movie_image_repository import MovieImageRepository
from models.movies.repository.movie_repository import MovieRepository
from models.users.auth_repository import AuthRepository
from models.users.user_repository import UserRepository
from services.auth.auth_service import AuthService
from services.crud_service.crud_service import CRUDService
from services.movies.movies_service import MovieService
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


movie_repository = MovieRepository()
movie_image_repository = MovieImageRepository()


def get_movie_repository() -> MovieRepository:
    return movie_repository


def get_movie_image_repository() -> MovieImageRepository:
    return movie_image_repository


movie_service = MovieService(movie_repository, movie_image_repository)


def get_movie_service() -> MovieService:
    return movie_service


crud_service = CRUDService()


def get_crud_service() -> CRUDService:
    return crud_service
