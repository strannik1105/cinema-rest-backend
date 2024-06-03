from datetime import timedelta, datetime

import bcrypt
import jwt

import settings

EXPIRATION_TIME = timedelta(minutes=30)


def encode_jwt(
        payload: dict,
        private_key: str = settings.auth_jwt.private_key_path.read_text(),
        algorithm: str = settings.auth_jwt.algorithm,
) -> str:
    expiration = datetime.utcnow() + EXPIRATION_TIME
    payload.update({"exp": expiration})
    token = jwt.encode(payload, private_key, algorithm=algorithm)
    return token


def decode_jwt(
        token: str | bytes,
        public_key: str = settings.auth_jwt.public_key_path.read_text(),
        algorithm: str = settings.auth_jwt.algorithm,
) -> dict:
    try:
        decoded_data = jwt.decode(token, public_key, algorithms=[algorithm])
        return decoded_data
    except jwt.PyJWTError:
        return None


def hash_password(
        password: str,
) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(
        password: str,
        hashed_password: bytes,
) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password,
    )
