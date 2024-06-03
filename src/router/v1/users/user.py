from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from starlette import status

from common.enums.enums import Role
from models.users.schemas import user
from router.deps import PGSession, get_user_service
from router.v1.auth.auth import TokenInfo
from services.users.user_service import UserService
from auth import utils as auth_utils

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


async def get_current_user(
        token: str = Depends(oauth2_scheme)
):
    decoded_data = auth_utils.decode_jwt(token)
    if not decoded_data:
        raise HTTPException(status_code=400, detail="Invalid token")
    #user = await user_service.get_user_by_sid(db, sid)
    print(token)
    print('aaaaa')
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    return user


class PermissionChecker:

    def __init__(self, required_permissions: list[str]) -> None:
        self.required_permissions = required_permissions

    def __call__(self, user) -> bool:
        print('aaaa')
        for r_perm in self.required_permissions:
            if r_perm not in user.permissions:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Permissions'
                )
        return True


class User(BaseModel):
    username: str
    password: str


@router.get("/me")
async def get_user_me(current_user: User = Depends(get_current_user)):
    return current_user


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
        db,
        new_user.name,
        new_user.email,
        auth_utils.hash_password(new_user.password).decode("utf-8"),
        Role.USER,
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


@router.get('/users')
def users(
        token: str = Depends(oauth2_scheme)
):
    print('aaaa')
    return 'users'
