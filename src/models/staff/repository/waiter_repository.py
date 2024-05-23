from common.repository.repository import AbstractRepository
from models.staff.waiter import Waiter


class WaiterRepository(AbstractRepository[Waiter]):
    def __init__(self):
        super().__init__(Waiter)
