from common.repository.repository import AbstractRepository
from models.users import User


class UserRepository(AbstractRepository[User]):
    def __init__(self):
        super().__init__(User)
