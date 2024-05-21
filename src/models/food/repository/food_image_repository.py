from common.repository.repository import AbstractRepository
from models.food.food_image import FoodImage


class FoodImageRepository(AbstractRepository[FoodImage]):
    def __init__(self):
        super().__init__(FoodImage)
