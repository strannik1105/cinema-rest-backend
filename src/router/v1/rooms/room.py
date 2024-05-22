from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path

from models.rooms.repository.room_repository import RoomRepository
from models.rooms.room import Room
from router.deps import (
    PGSession,
    get_crud_service,
    get_room_repository,
)
from router.v1.rooms.schemas import RoomBaseSchema, RoomSchema
from services.crud_service.crud_service import CRUDService

router = APIRouter()


@router.get("/", response_model=List[RoomSchema])
async def get(
        db: PGSession,
        repository: Annotated[RoomRepository, Depends(get_room_repository)],
        crud_service: Annotated[CRUDService, Depends(get_crud_service)],
):
    db_objs = await crud_service.get_all(db, repository)
    return db_objs


@router.get("/{sid}", response_model=RoomSchema)
async def get(
        db: PGSession,
        repository: Annotated[RoomRepository, Depends(get_room_repository)],
        crud_service: Annotated[CRUDService, Depends(get_crud_service)],
        sid: UUID = Path(description="сид сущности"),
):
    db_obj = await crud_service.get_by_sid(db, repository, sid)
    return db_obj


@router.post("/", response_model=RoomSchema)
async def create(
        db: PGSession,
        repository: Annotated[RoomRepository, Depends(get_room_repository)],
        crud_service: Annotated[CRUDService, Depends(get_crud_service)],
        new_obj: RoomBaseSchema,
):
    db_obj = await crud_service.create(
        db,
        repository,
        Room,
        {
            "name": new_obj.name,
            "description": new_obj.description,
            "cost_per_hour": new_obj.cost_per_hour,
            "x": new_obj.x,
            "y": new_obj.y,
            "width": new_obj.width,
            "height": new_obj.height
        },
    )
    return db_obj


@router.patch("/{sid}", response_model=RoomSchema)
async def update(
        db: PGSession,
        repository: Annotated[RoomRepository, Depends(get_room_repository)],
        crud_service: Annotated[CRUDService, Depends(get_crud_service)],
        updated_obj: RoomBaseSchema,
        sid: UUID = Path(description="сид сущности"),
):
    db_obj = await crud_service.update(db, repository, sid, updated_obj.__dict__)
    return db_obj


@router.delete("/{sid}")
async def delete(
        db: PGSession,
        repository: Annotated[RoomRepository, Depends(get_room_repository)],
        crud_service: Annotated[CRUDService, Depends(get_crud_service)],
        sid: UUID = Path(description="сид сущности"),
):
    await crud_service.delete(db, repository, sid)
    return {"msg": "success"}
