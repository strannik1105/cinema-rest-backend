from common.repository.repository import AbstractRepository
from models.rooms.booking import Booking


class BookingRepository(AbstractRepository[Booking]):
    def __init__(self):
        super().__init__(Booking)
