from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path

from common.enums.enums import Role
from models.users.schemas import user
from router.deps import PGSession, get_user_service
from router.v1.auth.auth import TokenInfo
from services.users.user_service import UserService
from auth import utils as auth_utils

router = APIRouter()


@router.get("/", response_model=List[user.User])
async def get_users(
    db: PGSession,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    db_objs = await user_service.get_all_users(db)
    return db_objs


@router.get("/{sid}", response_model=user.User)
async def get_user(
    db: PGSession,
    user_service: Annotated[UserService, Depends(get_user_service)],
    sid: UUID = Path(description="сид пользователя"),
):
    db_obj = await user_service.get_user_by_sid(db, sid)
    return db_obj


@router.post("/", response_model=TokenInfo)
async def create_user(
    db: PGSession,
    user_service: Annotated[UserService, Depends(get_user_service)],
    new_user: user.UserCreate,
):
    db_obj = await user_service.create_user(
        db, new_user.name, new_user.email, new_user.password, Role.USER
    )
    jwt_payload = {
        "username": db_obj.name,
    }
    token = auth_utils.encode_jwt(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type="Bearer",
    )


@router.put("/{sid}", response_model=user.User)
async def update_user(
    db: PGSession,
    user_service: Annotated[UserService, Depends(get_user_service)],
    updated_user: user.UserUpdate,
    sid: UUID = Path(description="сид пользователя"),
):
    db_obj = await user_service.update_user(db, sid, updated_user.__dict__)
    return db_obj


@router.delete("/{sid}")
async def delete_user(
    db: PGSession,
    user_service: Annotated[UserService, Depends(get_user_service)],
    sid: UUID = Path(description="сид пользователя"),
):
    await user_service.remove_user(db, sid)
    return {"msg": "success"}
