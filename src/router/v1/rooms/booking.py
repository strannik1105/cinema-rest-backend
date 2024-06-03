from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path

from models.rooms.repository.booking_repository import BookingRepository
from router.deps import (
    PGSession,
    get_crud_service,
    get_booking_repository,
    get_booking_service,
)
from router.v1.rooms.schemas import (
    BookingSchema,
    BookingBaseSchema,
    BookingCreateSchema,
)
from services.booking_service.booking_service import BookingService
from services.crud_service.crud_service import CRUDService

router = APIRouter()


@router.get("/", response_model=List[BookingSchema])
async def get(
    db: PGSession,
    repository: Annotated[BookingRepository, Depends(get_booking_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
):
    db_objs = await crud_service.get_all(db, repository)
    return db_objs


@router.get("/{sid}", response_model=BookingSchema)
async def get(
    db: PGSession,
    repository: Annotated[BookingRepository, Depends(get_booking_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    sid: UUID = Path(description="сид сущности"),
):
    db_obj = await crud_service.get_by_sid(db, repository, sid)
    return db_obj


@router.post("/", response_model=BookingSchema)
async def create(
    db: PGSession,
    booking_service: Annotated[BookingService, Depends(get_booking_service)],
    new_obj: BookingCreateSchema,
):
    db_obj = await booking_service.create_booking(
        db,
        new_obj.room_sid,
        new_obj.user_sid,
        new_obj.datetime_start,
        new_obj.datetime_end,
    )
    return db_obj


@router.delete("/{sid}")
async def delete(
    db: PGSession,
    repository: Annotated[BookingRepository, Depends(get_booking_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    sid: UUID = Path(description="сид сущности"),
):
    await crud_service.delete(db, repository, sid)
    return {"msg": "success"}


@router.get("/{sid}/bookings")
async def get_bookings_by_sid(
    db: PGSession,
    service: Annotated[BookingService, Depends(get_booking_service)],
    sid: UUID = Path(description="сид комнаты"),
):
    bookings = await service.get_bookings_by_room(db, sid)
    return bookings
