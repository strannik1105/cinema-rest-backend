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
