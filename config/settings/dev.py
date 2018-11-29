from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9yp3cmh^2xo47i%$-jp_xaakqc4)8c_5x0s_dq=-==9z^f(lzt'


ALLOWED_HOSTS = ['*']



try:
    from .local import *
except ImportError:
    pass
