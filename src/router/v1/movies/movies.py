from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path

from models.movies import Movie
from models.movies.repository.movie_repository import MovieRepository
from models.users.schemas import user
from router.deps import (
    PGSession,
    get_crud_service,
    get_movie_repository,
)
from router.v1.movies.schemas import MovieSchema, MovieUpdateSchema
from services.crud_service.crud_service import CRUDService

router = APIRouter()


@router.get("/", response_model=List[MovieSchema])
async def get_movies(
    db: PGSession,
    movie_repository: Annotated[MovieRepository, Depends(get_movie_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
):
    db_objs = await crud_service.get_all(db, movie_repository)
    return db_objs


@router.get("/{sid}", response_model=MovieSchema)
async def get_movie(
    db: PGSession,
    movie_repository: Annotated[MovieRepository, Depends(get_movie_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    sid: UUID = Path(description="сид пользователя"),
):
    db_obj = await crud_service.get_by_sid(db, movie_repository, sid)
    return db_obj


@router.post("/", response_model=MovieSchema)
async def create_movie(
    db: PGSession,
    movie_repository: Annotated[MovieRepository, Depends(get_movie_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    new_movie: MovieUpdateSchema,
):
    db_obj = await crud_service.create(
        db,
        movie_repository,
        Movie,
        {
            "name": new_movie.name,
            "description": new_movie.description,
            "genre": new_movie.genre,
        },
    )
    return db_obj


@router.put("/{sid}", response_model=user.User)
async def update_user(
    db: PGSession,
    movie_repository: Annotated[MovieRepository, Depends(get_movie_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    updated_user: user.UserUpdate,
    sid: UUID = Path(description="сид пользователя"),
):
    db_obj = await crud_service.update(db, sid, movie_repository, updated_user.__dict__)
    return db_obj


@router.delete("/{sid}")
async def delete(
    db: PGSession,
    movie_repository: Annotated[MovieRepository, Depends(get_movie_repository)],
    crud_service: Annotated[CRUDService, Depends(get_crud_service)],
    sid: UUID = Path(description="сид пользователя"),
):
    await crud_service.delete(db, movie_repository, sid)
    return {"msg": "success"}
