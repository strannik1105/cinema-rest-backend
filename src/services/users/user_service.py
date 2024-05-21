from uuid import UUID

from common.exceptions.exceptions import HTTPNotFoundError
from models.users import User
from auth import utils as auth_utils


class UserService:

    def __init__(self, user_repository):
        self._user_repository = user_repository

    async def get_all_users(self, db_session):
        return await self._user_repository.get_all(db_session)

    async def get_user_by_sid(self, db_session, sid: UUID):
        user = await self._user_repository.get(db_session, sid)
        if user is None:
            raise HTTPNotFoundError
        return user

    async def create_user(self, db_session, name, email, password, role):
        hashed_password = auth_utils.hash_password(password).decode('utf-8')
        return await self._user_repository.create(
            db_session, User(name=name, email=email, password=hashed_password, role=role)
        )

    async def update_user(self, db_session, user_sid, changes: dict):
        db_obj = await self._user_repository.get(db_session, user_sid)
        db_obj = await self._user_repository.update(db_session, db_obj, changes)
        return db_obj

    async def remove_user(self, db_session, user_id):
        user_obj = await self._user_repository.get(db_session, user_id)
        if user_obj is None:
            raise HTTPNotFoundError
