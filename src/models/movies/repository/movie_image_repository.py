from common.repository.repository import AbstractRepository
from models.movies.movie_image import MovieImage


class MovieImageRepository(AbstractRepository[MovieImage]):
    def __init__(self):
        super().__init__(MovieImage)
