from movie_project.settings import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')