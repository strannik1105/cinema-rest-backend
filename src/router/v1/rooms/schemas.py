from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class RoomBaseSchema(BaseModel):
    name: str
    description: Optional[str]
    cost_per_hour: float
    x: float
    y: float
    width: Optional[float]
    height: Optional[float]


class RoomSchema(RoomBaseSchema):
    sid: UUID
