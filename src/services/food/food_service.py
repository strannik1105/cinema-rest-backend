import uuid

from fastapi import UploadFile

from models.food.food_image import FoodImage


class FoodService:
    def __init__(self, food_repository, food_image_repository):
        self._food_repository = food_repository
        self._food_image_repository = food_image_repository

    def create_food_image(
        self,
        db_session,
        name: str,
        select_as_title: bool,
        movie_sid: uuid.UUID,
        image: UploadFile,
    ):
        filename = uuid.uuid4().hex
        file_path = f"static/{filename}"
        with open(file_path, "wb") as f:
            f.write(image.file.read())

        image = self._food_image_repository.create(
            db_session, FoodImage(name, file_path, select_as_title, str(movie_sid))
        )

        return image
