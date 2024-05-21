import bcrypt
from fastapi import HTTPException
from starlette import status


class AuthService:

    def __init__(self, auth_repository):
        self._auth_repository = auth_repository

    async def authenticate(self, db_session, username: str, password: str):
        unauthed_exc = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid username or password",
        )
        user = await self._auth_repository.get_user_by_username(db_session, username)

        if not user:
            raise unauthed_exc

        if not bcrypt.checkpw(password.encode(), user.password.encode()):
            raise unauthed_exc

        return user
