from common import *

DEBUG = True
SECRET_KEY = "woigh084hg02gn-39jg-2931n-9n-3ibg0823bg203igm[owmqf[ofmapifn083h"

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
