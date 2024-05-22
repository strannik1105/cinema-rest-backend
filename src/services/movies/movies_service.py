import uuid

from fastapi import UploadFile

import settings
from models.movies import MovieImage


class MovieService:
    def __init__(self, movie_repository, movie_image_repository):
        self._movie_repository = movie_repository
        self._movie_image_repository = movie_image_repository

    def create_movie_image(
            self,
            db_session,
            name,
            select_as_title: bool,
            movie_sid: uuid.UUID,
            image: UploadFile,
    ):
        filename = uuid.uuid4().hex
        image_type = image.filename.split(".")[-1]
        file_path = f"{settings.FILE_PATH}/{filename}"
        with open(file_path, "wb") as f:
            f.write(image.file.read())

        image = self._movie_image_repository.create(
            db_session, MovieImage(name, f"{file_path}.{image_type}", select_as_title, str(movie_sid))
        )

        return image
