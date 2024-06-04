from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, Request
from fastapi.security import OAuth2PasswordBearer

import jwt
from jose import ExpiredSignatureError, JWTError

import settings
from auth.utils import encode_jwt, decode_jwt
from common.exceptions.exceptions import (
    TokenExpiredException,
    IncorrectTokenFormatException,
    UserIsNotPresentException,
    TokenAbsentException,
)
from models.users import User
from router.deps import PGSession, get_auth_service
from router.v1.auth.schemas import TokenInfo
from services.auth.auth_service import AuthService
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(
    db: PGSession,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
    token: str = Depends(get_token),
):
    try:
        payload = decode_jwt(token)

    except ExpiredSignatureError:
        raise TokenExpiredException

    except JWTError:
        raise IncorrectTokenFormatException

    user_name: str = payload.get("sub")
    if not user_name:
        raise UserIsNotPresentException
    user = await auth_service.get_by_username(db, user_name)
    if not user:
        raise UserIsNotPresentException

    return user


@router.post("/token", response_model=TokenInfo)
async def authenticate_user(
    db: PGSession,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
    username: str,
    password: str,
    response: Response,
):
    db_obj = await auth_service.authenticate(db, username, password)

    if not db_obj:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    is_password_correct = pwd_context.verify(password, db_obj.password)

    if not is_password_correct:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = encode_jwt({"sub": str(db_obj.name)})
    response.set_cookie("booking_access_token", access_token, httponly=True)

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
