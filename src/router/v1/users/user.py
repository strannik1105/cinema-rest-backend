from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path

from models.users import User
from models.users.schemas import user
from models.users.user_repository import UserRepository
from router.deps import PGSession, get_user_repository

router = APIRouter()


@router.get("/", response_model=List[user.User])
async def get_users(
    db: PGSession,
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
):
    db_objs = await user_repository.get_all(db)
    return db_objs


@router.get("/{sid}", response_model=user.User)
async def get_user(
    db: PGSession,
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    sid: UUID = Path(description="сид пользователя"),
):
    db_obj = await user_repository.get(db, sid)
    return db_obj


@router.post("/", response_model=user.User)
async def create_user(
    db: PGSession,
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    new_user: user.UserCreate,
):
    obj = User(**new_user.__dict__)
    db_obj = await user_repository.create(db, obj, with_commit=True)
    return db_obj


@router.put("/{sid}", response_model=user.User)
async def update_user(
    db: PGSession,
    updated_user: user.UserUpdate,
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    sid: UUID = Path(description="сид пользователя"),
):
    db_obj = await user_repository.get(db, sid)
    db_obj = await user_repository.update(db, db_obj, updated_user.__dict__)
    return db_obj


@router.delete("/{sid}")
async def delete_user(
    db: PGSession,
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    sid: UUID = Path(description="сид пользователя"),
):
    db_obj = await user_repository.get(db, sid)
    await user_repository.remove(db, db_obj)
    return {"msg": "success"}
