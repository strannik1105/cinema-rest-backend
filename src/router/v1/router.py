from fastapi import APIRouter

from router.v1.auth import auth
from router.v1.users import user
from router.v1.movies import movies
from router.v1.movies import movie_images

router = APIRouter(prefix="/v1")
router.include_router(user.router, prefix="/users", tags=["Пользователи"])
router.include_router(auth.router, prefix="/auth", tags=["Регистрация"])
router.include_router(movies.router, prefix="/movies", tags=["Фильмы"])
router.include_router(movie_images.router, prefix="/movies_images", tags=["Фильмы"])
