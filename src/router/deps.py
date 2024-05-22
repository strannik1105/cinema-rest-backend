from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.db.session import get_pg_session
from models.food.repository.food_image_repository import FoodImageRepository
from models.food.repository.food_repository import FoodRepository
from models.movies.repository.movie_image_repository import MovieImageRepository
from models.movies.repository.movie_repository import MovieRepository
from models.rooms.repository.booking_repository import BookingRepository
from models.rooms.repository.room_repository import RoomRepository
from models.users.auth_repository import AuthRepository
from models.users.user_repository import UserRepository
from services.auth.auth_service import AuthService
from services.booking_service.booking_service import BookingService
from services.crud_service.crud_service import CRUDService
from services.food.food_service import FoodService
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


food_repository = FoodRepository()
food_image_repository = FoodImageRepository()


def get_food_repository() -> FoodRepository:
    return food_repository


def get_food_image_repository() -> FoodImageRepository:
    return food_image_repository


food_service = FoodService(food_repository, food_image_repository)


def get_food_service() -> FoodService:
    return food_service


room_repository = RoomRepository()
booking_repository = BookingRepository()


def get_room_repository() -> RoomRepository:
    return room_repository


def get_booking_repository() -> BookingRepository:
    return booking_repository


booking_service = BookingService(booking_repository, room_repository)


def get_booking_service() -> BookingService:
    return booking_service
