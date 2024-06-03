from datetime import datetime, timedelta
from uuid import UUID

from sqlalchemy import select

from common.exceptions.exceptions import (
    AlreadyBookedError,
    HTTPNotFoundError,
    AllStaffsAreBusyError,
    TooLowTimeRangeError,
)
from common.utils import check_for_intersection
from models.rooms.booking import Booking
from models.rooms.repository.booking_repository import BookingRepository
from models.rooms.repository.room_repository import RoomRepository
from models.staff.repository.cook_repository import CookRepository
from models.staff.repository.waiter_repository import WaiterRepository
from services.booking_service.ext import get_available_cook, get_available_waiter


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
        if datetime_end - datetime_start < timedelta(hours=2):
            raise TooLowTimeRangeError

        db_room = await self._room_repository.get(db_session, room_sid)
        if db_room is None:
            raise HTTPNotFoundError

        db_bookings = await self._booking_repository.get_all(db_session)
        intersections = []

        for booking in db_bookings:
            if check_for_intersection(
                (datetime_start, datetime_end),
                (booking.datetime_start, booking.datetime_end),
            ):
                if booking.room_sid == room_sid:
                    raise AlreadyBookedError
                else:
                    intersections.append(booking)

        waiter = await get_available_waiter(
            db_session, intersections, self._waiter_repository
        )
        if waiter is None:
            raise AllStaffsAreBusyError

        cook = await get_available_cook(
            db_session, intersections, self._cook_repository
        )
        if cook is None:
            raise AllStaffsAreBusyError

        booking = await self._booking_repository.create(
            db_session,
            Booking(
                room_sid, user_sid, datetime_start, datetime_end, waiter.sid, cook.sid
            ),
            with_commit=False,
        )
        await db_session.commit()

        return booking

    async def get_bookings_by_room(self, db_session, room_sid):
        bookings = await db_session.execute(
            select(Booking).filter(Booking.room_sid == room_sid)
        )
        return list(bookings.scalars().all())
