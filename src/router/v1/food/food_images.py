import base64
from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path, UploadFile

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
from router.v1.food.schemas import FoodImageUpdateSchema, FoodImageSchema
from router.v1.movies.schemas import (
    MovieImageSchema,
)
from services.crud_service.crud_service import CRUDService
from services.food.food_service import FoodService

router = APIRouter()


@router.get("/{sid}")
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
        if obj_.food_sid == sid:
            obj_.file = "data:image/png;base64,"
            with open(obj_.path, "rb") as image_file:
                obj_.file += base64.b64encode(image_file.read()).decode('utf-8')
            objs_to_repr.append(obj_)

    return objs_to_repr


@router.post("/{sid}")
async def create_image(
        db: PGSession,
        food_service: Annotated[FoodService, Depends(get_food_service)],
        new_food_image: UploadFile,
        sid: UUID = Path(description="сид блюда"),
):
    db_obj = await food_service.create_food_image(
        db, True, sid, new_food_image
    )
    return db_obj


@router.patch("/{sid}", response_model=user.User)
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
