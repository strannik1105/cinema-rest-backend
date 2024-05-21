from common.repository.repository import AbstractRepository
from models.food.food import Food


class FoodRepository(AbstractRepository[Food]):
    def __init__(self):
        super().__init__(Food)
