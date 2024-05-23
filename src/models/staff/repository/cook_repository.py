from common.repository.repository import AbstractRepository
from models.staff.cook import Cook


class CookRepository(AbstractRepository[Cook]):
    def __init__(self):
        super().__init__(Cook)
