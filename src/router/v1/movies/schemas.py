from typing import Optional

from fastapi import UploadFile
from pydantic import BaseModel


class MovieSchema(BaseModel):
    name: str
    description: Optional[str]
    genre: Optional[str]
    images: Optional[UploadFile]


class MovieUpdateSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    genre: Optional[str]
    images: Optional[UploadFile]


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
