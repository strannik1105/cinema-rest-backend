from common.repository.repository import AbstractRepository
from models.staff.repository.mixins import StaffRepository
from models.staff.waiter import Waiter


class WaiterRepository(AbstractRepository[Waiter], StaffRepository):
    def __init__(self):
        super().__init__(Waiter)
