from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from auth.utils import encode_jwt, decode_jwt
from router.deps import PGSession, get_auth_service
from router.v1.auth.schemas import TokenInfo
from services.auth.auth_service import AuthService
from passlib.context import CryptContext

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@router.post("/token", response_model=TokenInfo)
async def authenticate_user(
    db: PGSession,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
    username: str,
    password: str,

):
    db_obj = await auth_service.authenticate(db, username, password)

    if not db_obj:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    is_password_correct = pwd_context.verify(password, db_obj.password)

    if not is_password_correct:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    jwt_token = encode_jwt({"sub": db_obj.name})
    return {"access_token": jwt_token, "token_type": "bearer"}


class User(BaseModel):
    username: str
    password: str


def get_current_user(token: str = Depends(oauth2_scheme)):
    decoded_data = decode_jwt(token)
    if not decoded_data:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = "root"  # Получите пользователя из базы данных
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    print(user)
    return user


@router.get("/users/me")
def get_user_me(token: str = Depends(oauth2_scheme)):
    decoded_data = decode_jwt(token)
    if not decoded_data:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = "root"  # Получите пользователя из базы данных
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    print(user)
    return user

