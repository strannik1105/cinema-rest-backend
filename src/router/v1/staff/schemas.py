from uuid import UUID

from pydantic import BaseModel


class WaiterBaseSchema(BaseModel):
    name: str
    surname: str


class WaiterSchema(WaiterBaseSchema):
    sid: UUID
