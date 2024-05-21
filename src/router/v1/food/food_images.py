from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path

from models.food.repository.food_image_repository import FoodImageRepository
from models.food.repository.food_repository import FoodRepository
from models.users.schemas import user
from router.deps import (
    PGSession,
    get_crud_service,
    get_food_image_repository,
    get_food_service,
    get_food_repository,
)
from router.v1.food.schemas import FoodImageCreateSchema, FoodImageUpdateSchema
from router.v1.movies.schemas import (
    MovieImageSchema,
)
from services.crud_service.crud_service import CRUDService
from services.food.food_service import FoodService

router = APIRouter()


@router.get("/{sid}", response_model=List[MovieImageSchema])
async def get_images(
    db: PGSession,
    food_image_repository: Annotated[
        FoodImageRepository, Depends(get_food_image_repository)
    ],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    sid: UUID = Path(description="сид блюда"),
):
    db_objs = await crud_service.get_all(db, food_image_repository)
    objs_to_repr = []
    for obj_ in db_objs:
        if obj_.movie_sid == sid:
            objs_to_repr.append(obj_)

    return db_objs


@router.post("/{sid}", response_model=MovieImageSchema)
async def create_image(
    db: PGSession,
    food_service: Annotated[FoodService, Depends(get_food_service)],
    new_food: FoodImageCreateSchema,
    sid: UUID = Path(description="сид блюда"),
):
    db_obj = await food_service.create_food_image(
        db, new_food.name, new_food.select_as_title, sid, new_food.image
    )
    return db_obj


@router.put("/{sid}", response_model=user.User)
async def update(
    db: PGSession,
    food_repository: Annotated[FoodRepository, Depends(get_food_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    updated_image: FoodImageUpdateSchema,
    sid: UUID = Path(description="сид"),
):
    db_obj = await crud_service.update(db, sid, food_repository, updated_image.__dict__)
    return db_obj


@router.delete("/{sid}")
async def delete(
    db: PGSession,
    food_repository: Annotated[FoodRepository, Depends(get_food_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    sid: UUID = Path(description="сид"),
):
    await crud_service.delete(db, food_repository, sid)
    return {"msg": "success"}
