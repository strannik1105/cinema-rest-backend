from fastapi import APIRouter

from router.v1.users import user
from router.v1.auth import auth


router = APIRouter(prefix="/v1")
router.include_router(user.router, prefix="/users", tags=["Пользователи"])
router.include_router(auth.router, prefix="/auth", tags=["Регистрация"])
