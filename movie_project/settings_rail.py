from movie_project.settings import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['web-production-bf16.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://web-production-bf16.up.railway.app']