from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path, UploadFile

from models.movies.repository.movie_image_repository import MovieImageRepository
from models.movies.repository.movie_repository import MovieRepository
from models.users.schemas import user
from router.deps import (
    PGSession,
    get_crud_service,
    get_movie_repository,
    get_movie_image_repository,
    get_movie_service,
)
from router.v1.movies.schemas import (
    MovieImageSchema,
    MovieImageCreateSchema,
    MovieImageUpdateSchema,
)
from services.crud_service.crud_service import CRUDService
from services.movies.movies_service import MovieService

router = APIRouter()


@router.get("/{sid}", response_model=List[MovieImageSchema])
async def get_images(
    db: PGSession,
    movie_image_repository: Annotated[
        MovieImageRepository, Depends(get_movie_image_repository)
    ],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    sid: UUID = Path(description="сид пользователя"),
):
    db_objs = await crud_service.get_all(db, movie_image_repository)
    objs_to_repr = []
    for obj_ in db_objs:
        if obj_.movie_sid == sid:
            objs_to_repr.append(obj_)

    return db_objs


@router.post("/{sid}")
async def create_image(
    db: PGSession,
    movie_service: Annotated[MovieService, Depends(get_movie_service)],
    new_movie: UploadFile,
    sid: UUID = Path(description="сид фильма"),
):
    db_obj = await movie_service.create_movie_image(
        db, True, sid, new_movie
    )
    return db_obj


@router.put("/{sid}", response_model=user.User)
async def update(
    db: PGSession,
    movie_repository: Annotated[MovieRepository, Depends(get_movie_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    updated_image: MovieImageUpdateSchema,
    sid: UUID = Path(description="сид"),
):
    db_obj = await crud_service.update(
        db, sid, movie_repository, updated_image.__dict__
    )
    return db_obj


@router.delete("/{sid}")
async def delete(
    db: PGSession,
    movie_repository: Annotated[MovieRepository, Depends(get_movie_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    sid: UUID = Path(description="сид"),
):
    await crud_service.delete(db, movie_repository, sid)
    return {"msg": "success"}
