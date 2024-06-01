from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path

from models.staff.cook import Cook
from router.deps import (
    PGSession,
    get_crud_service,
    get_cook_repository,
)
from router.v1.staff.schemas import CookSchema, CookBaseSchema
from services.crud_service.crud_service import CRUDService

router = APIRouter()


@router.get("/", response_model=List[CookSchema])
async def get_all(
    db: PGSession,
    repository: Annotated[CookSchema, Depends(get_cook_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
):
    db_objs = await crud_service.get_all(db, repository)
    return db_objs


@router.get("/{sid}", response_model=CookSchema)
async def get_by_sid(
    db: PGSession,
    repository: Annotated[CookSchema, Depends(get_cook_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    sid: UUID = Path(description="сид сущности"),
):
    db_obj = await crud_service.get_by_sid(db, repository, sid)
    return db_obj


@router.post("/", response_model=CookSchema)
async def create(
    db: PGSession,
    repository: Annotated[CookSchema, Depends(get_cook_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    new_obj: CookBaseSchema,
):
    db_obj = await crud_service.create(
        db,
        repository,
        Cook,
        {
            "name": new_obj.name,
            "surname": new_obj.surname,
        },
    )
    return db_obj


@router.patch("/{sid}", response_model=CookSchema)
async def update(
    db: PGSession,
    repository: Annotated[CookSchema, Depends(get_cook_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    updated_obj: CookBaseSchema,
    sid: UUID = Path(description="сид сущности"),
):
    db_obj = await crud_service.update(db, repository, sid, updated_obj.__dict__)
    return db_obj


@router.delete("/{sid}")
async def delete(
    db: PGSession,
    repository: Annotated[CookSchema, Depends(get_cook_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    sid: UUID = Path(description="сид сущности"),
):
    await crud_service.delete(db, repository, sid)
    return {"msg": "success"}
