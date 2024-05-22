from common.repository.repository import AbstractRepository
from models.rooms.room import Room


class RoomRepository(AbstractRepository[Room]):
    def __init__(self):
        super().__init__(Room)
