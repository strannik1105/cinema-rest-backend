from common.db.base_model import BaseModel

# include models here
from models.users.user import User  # noqa
from models.movies.movie import Movie  # noqa
from models.movies.movie_image import MovieImage  # noqa
from models.food.food import Food  # noqa
from models.food.food_image import FoodImage  # noqa


metadata = BaseModel.metadata
