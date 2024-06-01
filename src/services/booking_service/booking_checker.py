from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings
from models.rooms.booking import Booking
from models.staff.cook import Cook
from models.staff.waiter import Waiter


def check_bookings():
    engine = create_engine(
        f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}",
        pool_pre_ping=True
    )
    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
        bind=engine,
    )
    session = SessionLocal()
    bookings = session.query(Booking).all()
    for booking in bookings:
        if booking.datetime_end > datetime.now():
            waiter = session.query(Waiter).filter(Waiter.sid == booking.waiter_sid).first()
            if waiter is None:
                continue

            cook = session.query(Cook).filter(Cook.sid == booking.cook_sid).first()
            if cook is None:
                continue

            waiter.bookings_count -= 1
            cook.bookings_count -= 1
            session.commit()
