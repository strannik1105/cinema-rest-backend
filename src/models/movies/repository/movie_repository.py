from common.repository.repository import AbstractRepository
from models.movies.movie import Movie


class MovieRepository(AbstractRepository[Movie]):
    def __init__(self):
        super().__init__(Movie)
