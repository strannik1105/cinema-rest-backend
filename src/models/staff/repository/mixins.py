from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class StaffRepository:
    async def get_available_staff(self, session: AsyncSession):
        obj = await session.execute(
            select(self._t_model).filter(self._t_model.bookings_count < 2)
        )
        return obj.scalar()
