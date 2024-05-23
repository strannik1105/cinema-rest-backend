import os
from dotenv import load_dotenv
from sys import platform

from pathlib import Path
from pydantic import BaseModel

load_dotenv(
    os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), ".env.local")
)

BASE_DIR = Path(__file__).resolve().parent.parent


class AuthJwt(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


def get_local_host(addr="0.0.0.0"):
    if addr in ("0.0.0.0", "localhost", "127.0.0.1"):
        match platform:
            case "linux" | "darwin":
                return "0.0.0.0"
            case "win32":
                return "localhost"
            case _:
                raise OSError("Unsupported platform")
    else:
        return addr


HOST = get_local_host(os.getenv("HOST", "0.0.0.0"))
PORT: int = int(os.getenv("PORT", 8000))

POSTGRES_DB: str = os.getenv("POSTGRES_DB", "events")
POSTGRES_USER: str = os.getenv("POSTGRES_USER", "user")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
POSTGRES_HOST: str = get_local_host(os.getenv("POSTGRES_HOST", "0.0.0.0"))
POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))
FILE_PATH: str = os.getenv("FILE_PATH", "../static")

auth_jwt = AuthJwt()
