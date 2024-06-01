from datetime import datetime
from uuid import UUID

from common.exceptions.exceptions import (
    AlreadyBookedError,
    HTTPNotFoundError,
    AllStaffsAreBusyError,
)
from common.utils import time_in_range
from models.rooms.booking import Booking
from models.rooms.repository.booking_repository import BookingRepository
from models.rooms.repository.room_repository import RoomRepository
from models.staff.repository.cook_repository import CookRepository
from models.staff.repository.waiter_repository import WaiterRepository
from services.booking_service.ext import get_available_staff


class BookingService:
    def __init__(
            self,
            booking_repository: BookingRepository,
            room_repository: RoomRepository,
            cook_repository: CookRepository,
            waiter_repository: WaiterRepository,
    ):
        self._booking_repository = booking_repository
        self._room_repository = room_repository
        self._cook_repository = cook_repository
        self._waiter_repository = waiter_repository

    async def create_booking(
            self,
            db_session,
            room_sid: UUID,
            user_sid: UUID,
            datetime_start: datetime,
            datetime_end: datetime,
    ):
        db_room = await self._room_repository.get(db_session, room_sid)
        if db_room is None:
            raise HTTPNotFoundError

        db_bookings = await self._booking_repository.get_all(db_session)

        for booking in db_bookings:
            if booking.room_sid == room_sid:
                if time_in_range(
                        booking.datetime_start, booking.datetime_end, datetime_start
                ) and time_in_range(
                    booking.datetime_start, booking.datetime_end, datetime_end
                ):
                    raise AlreadyBookedError

        waiter = await get_available_staff(db_session, self._waiter_repository)
        if waiter is None:
            raise AllStaffsAreBusyError

        cook = await get_available_staff(db_session, self._cook_repository)
        if cook is None:
            raise AllStaffsAreBusyError

        booking = await self._booking_repository.create(
            db_session,
            Booking(
                room_sid, user_sid, datetime_start, datetime_end, waiter.sid, cook.sid
            ),
            with_commit=False,
        )
        waiter.bookings_count += 1
        cook.bookings_count += 1
        await db_session.commit()

        return booking
