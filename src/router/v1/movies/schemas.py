from typing import Optional
from uuid import UUID

from fastapi import UploadFile
from pydantic import BaseModel


class MovieImageSchema(BaseModel):
    name: str
    path: str
    select_as_title: bool


class MovieImageCreateSchema(BaseModel):
    name: str
    select_as_title: bool = False
    image: UploadFile


class MovieImageUpdateSchema(BaseModel):
    select_as_title: bool = False


class MovieBaseSchema(BaseModel):
    name: str
    description: Optional[str]
    genre: Optional[str]


class MovieSchema(MovieBaseSchema):
    sid: UUID


class MovieUpdateSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    genre: Optional[str]
