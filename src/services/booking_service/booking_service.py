from datetime import datetime
from uuid import UUID

from common.exceptions.exceptions import AlreadyBookedError, HTTPNotFoundError
from common.utils import time_in_range
from models.rooms.booking import Booking
from models.rooms.repository.booking_repository import BookingRepository
from models.rooms.repository.room_repository import RoomRepository


class BookingService:
    def __init__(self, booking_repository: BookingRepository, room_repository: RoomRepository):
        self._booking_repository = booking_repository
        self._room_repository = room_repository

    async def create_booking(self, db_session, room_sid: UUID, user_sid: UUID, datetime_start: datetime,
                             datetime_end: datetime):
        db_room = await self._room_repository.get(db_session, room_sid)
        if db_room is None:
            raise HTTPNotFoundError

        db_bookings = await self._booking_repository.get_all(db_session)

        for booking in db_bookings:
            if booking.room_sid == room_sid:
                if time_in_range(booking.datetime_start, booking.datetime_end, datetime_start) and time_in_range(
                        booking.datetime_start, booking.datetime_end, datetime_end):
                    raise AlreadyBookedError

        booking = await self._booking_repository.create(db_session,
                                                        Booking(room_sid, user_sid, datetime_start, datetime_end))
        return booking
