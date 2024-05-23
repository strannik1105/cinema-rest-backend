from uuid import UUID

from pydantic import BaseModel


class WaiterBaseSchema(BaseModel):
    name: str
    surname: str


class WaiterSchema(WaiterBaseSchema):
    sid: UUID


class CookBaseSchema(BaseModel):
    name: str
    surname: str


class CookSchema(WaiterBaseSchema):
    sid: UUID
