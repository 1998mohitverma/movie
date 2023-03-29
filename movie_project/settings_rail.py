from movie_project.settings import *
from decouple import config
import os

SECRET_KEY = config('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['web-production-bf16.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://web-production-bf16.up.railway.app']

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"