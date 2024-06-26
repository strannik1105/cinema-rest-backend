import uuid

from fastapi import UploadFile

import settings
from models.food.food_image import FoodImage


class FoodService:
    def __init__(self, food_repository, food_image_repository):
        self._food_repository = food_repository
        self._food_image_repository = food_image_repository

    def create_food_image(
        self,
        db_session,
        select_as_title: bool,
        movie_sid: uuid.UUID,
        image: UploadFile,
    ):
        filename = image.filename
        file_path = f"{settings.FILE_PATH}/{filename}"

        with open(file_path, "wb") as f:
            f.write(image.file.read())

        image = self._food_image_repository.create(
            db_session, FoodImage(filename, file_path, select_as_title, str(movie_sid))
        )

        return image
