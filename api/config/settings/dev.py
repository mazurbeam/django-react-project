from .base import *

DEBUG = True

ALLOWED_HOSTS = ['api.localhost', '127.0.0.1']


try:
    from .local import *
except ImportError:
    pass