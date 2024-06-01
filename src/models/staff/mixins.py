from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column


class StaffMixin:
    bookings_count = mapped_column(Integer, nullable=False, default=0)
