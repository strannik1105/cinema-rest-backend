from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path

from models.food.food import Food
from models.food.repository.food_repository import FoodRepository
from router.deps import (
    PGSession,
    get_crud_service,
    get_food_repository,
)
from router.v1.food.schemas import FoodSchema, FoodUpdateSchema, FoodBaseSchema
from services.crud_service.crud_service import CRUDService

router = APIRouter()


@router.get("/", response_model=List[FoodSchema])
async def get_foods(
    db: PGSession,
    food_repository: Annotated[FoodRepository, Depends(get_food_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
):
    db_objs = await crud_service.get_all(db, food_repository)
    return db_objs


@router.get("/{sid}", response_model=FoodSchema)
async def get_food(
    db: PGSession,
    food_repository: Annotated[FoodRepository, Depends(get_food_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    sid: UUID = Path(description="сид ,k.lf"),
):
    db_obj = await crud_service.get_by_sid(db, food_repository, sid)
    return db_obj


@router.post("/", response_model=FoodSchema)
async def create_food(
    db: PGSession,
    food_repository: Annotated[FoodRepository, Depends(get_food_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    new_food: FoodBaseSchema,
):
    db_obj = await crud_service.create(
        db,
        food_repository,
        Food,
        {
            "name": new_food.name,
            "description": new_food.description,
            "genre": new_food.genre,
        },
    )
    return db_obj


@router.put("/{sid}", response_model=FoodSchema)
async def update_food(
    db: PGSession,
    food_repository: Annotated[FoodRepository, Depends(get_food_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    updated_user: FoodUpdateSchema,
    sid: UUID = Path(description="сид пользователя"),
):
    db_obj = await crud_service.update(db, sid, food_repository, updated_user.__dict__)
    return db_obj


@router.delete("/{sid}")
async def delete(
    db: PGSession,
    food_repository: Annotated[FoodRepository, Depends(get_food_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    sid: UUID = Path(description="сид пользователя"),
):
    await crud_service.delete(db, food_repository, sid)
    return {"msg": "success"}