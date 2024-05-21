import bcrypt

from common.exceptions.exceptions import UnauthorizedError


class AuthService:

    def __init__(self, auth_repository):
        self._auth_repository = auth_repository

    async def authenticate(self, db_session, username: str, password: str):
        user = await self._auth_repository.get_user_by_username(db_session, username)

        if not user:
            raise UnauthorizedError

        if not bcrypt.checkpw(password.encode(), user.password.encode()):
            raise UnauthorizedError

        return user
