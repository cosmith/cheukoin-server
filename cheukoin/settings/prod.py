import dj_database_url
from common import *

DEBUG = False

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ["cheukoin.herokuapp.com"]
