from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str


class LoginData(UserBase):
    pass


class PyUser(UserBase):
    id: int
    permissions: list[str] = []


class Token(BaseModel):
    access_token: str
    token_type: str
