from typing import Optional
from uuid import UUID

from fastapi import UploadFile, File
from pydantic import BaseModel


class FoodImageSchema(BaseModel):
    name: str
    path: str
    select_as_title: bool


class FoodImageCreateSchema(BaseModel):
    name: str
    select_as_title: bool = False
    image: UploadFile = File(...)


class FoodImageUpdateSchema(BaseModel):
    select_as_title: bool = False


class FoodBaseSchema(BaseModel):
    name: str
    description: Optional[str]
    price: Optional[float]


class FoodSchema(FoodBaseSchema):
    sid: UUID


class FoodUpdateSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
