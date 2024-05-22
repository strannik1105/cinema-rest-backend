from fastapi import APIRouter

from router.v1.auth import auth
from router.v1.users import user
from router.v1.movies import movies
from router.v1.movies import movie_images
from router.v1.rooms import room, booking

router = APIRouter(prefix="/v1")
router.include_router(user.router, prefix="/users", tags=["Пользователи"])
router.include_router(auth.router, prefix="/auth", tags=["Регистрация"])
router.include_router(movies.router, prefix="/movies", tags=["Фильмы"])
router.include_router(movie_images.router, prefix="/movies_images", tags=["Фильмы"])
router.include_router(room.router, prefix="/rooms", tags=["Комнаты"])
router.include_router(booking.router, prefix="/booking", tags=["Бронирование"])
