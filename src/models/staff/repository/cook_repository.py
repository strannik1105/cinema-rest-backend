from common.repository.repository import AbstractRepository
from models.staff.cook import Cook
from models.staff.repository.mixins import StaffRepository


class CookRepository(AbstractRepository[Cook], StaffRepository):
    def __init__(self):
        super().__init__(Cook)
