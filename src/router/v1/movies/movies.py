from typing import List, Annotated, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Path, Query

from models.movies import Movie
from models.movies.repository.movie_repository import MovieRepository
from models.users.schemas import user
from router.deps import (
    PGSession,
    get_crud_service,
    get_movie_repository,
)
from router.v1.movies.schemas import MovieSchema, MovieUpdateSchema, MovieBaseSchema
from services.crud_service.crud_service import CRUDService

router = APIRouter()


@router.get("/", response_model=List[MovieSchema])
async def get_movies(
        db: PGSession,
        movie_repository: Annotated[MovieRepository, Depends(get_movie_repository)],
        crud_service: Annotated[CRUDService, Depends(get_crud_service)],
        year_gt: Optional[int] = Query(None),
        year_lt: Optional[int] = Query(None),
        duration_gt: Optional[int] = Query(None),
        duration_lt: Optional[int] = Query(None),
        genre: Optional[str] = Query(None)
):
    db_objs = await crud_service.get_all(db, movie_repository)
    objs = []

    for db_obj in db_objs:
        if year_gt is not None:
            if db_obj.year < year_gt:
                continue
        if year_lt is not None:
            if db_obj.year > year_lt:
                continue
        if duration_gt is not None:
            if db_obj.duration < duration_gt:
                continue
        if duration_lt is not None:
            if db_obj.duration < duration_lt:
                continue
        if genre is not None:
            if genre not in db_obj.genre:
                continue

        objs.append(db_obj)

    return objs


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
        new_movie: MovieBaseSchema,
):
    db_obj = await crud_service.create(
        db,
        movie_repository,
        Movie,
        {
            "name": new_movie.name,
            "description": new_movie.description,
            "genre": new_movie.genre,
            "year": new_movie.year,
            "duration": new_movie.duration
        },
    )
    return db_obj


@router.patch("/{sid}", response_model=MovieSchema)
async def update_user(
        db: PGSession,
        movie_repository: Annotated[MovieRepository, Depends(get_movie_repository)],
        crud_service: Annotated[CRUDService, Depends(get_crud_service)],
        updated_user: MovieUpdateSchema,
        sid: UUID = Path(description="сид пользователя"),
):
    db_obj = await crud_service.update(db, movie_repository, sid, updated_user.__dict__)
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
