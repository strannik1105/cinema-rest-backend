from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import mapped_column, relationship
from common.db.base_model import BaseModel

SCHEMA = "rooms"


class Booking(BaseModel):
    __tablename__ = "booking"
    __table_args__ = {
        "schema": SCHEMA,
        "comment": "Table with all users",
        "extend_existing": True,
    }

    room_sid = mapped_column(ForeignKey("rooms.room.sid"), nullable=False)
    user_sid = mapped_column(ForeignKey("users.user.sid"), nullable=False)
    datetime_start = mapped_column(DateTime, nullable=False)
    datetime_end = mapped_column(DateTime, nullable=False)

    waiter_sid = mapped_column(ForeignKey("staff.waiter.sid"))
    # waiter = relationship("Waiter", backref="bookings")

    cook_sid = mapped_column(ForeignKey("staff.cook.sid"))

    def __init__(self, room_sid, user_sid, datetime_start, datetime_end):
        self.room_sid = room_sid
        self.user_sid = user_sid
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end
