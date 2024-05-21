from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.repository.repository import AbstractRepository
from models.users import User


class UserRepository(AbstractRepository[User]):
    def __init__(self):
        super().__init__(User)

    async def get_user_by_username(self, session: AsyncSession, username: str):
        obj = await session.execute(
            select(self._t_model).filter(self._t_model.name == username)
        )
        return obj.scalar()

