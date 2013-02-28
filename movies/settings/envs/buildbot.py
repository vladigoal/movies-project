from movies.settings import *

from ..utils import proj
#COMPRESS_OFFLINE = True
EMAIL_PORT = 1025
INTERNAL_IPS = tuple()


ENV_PATH = proj('.env')


PYTHON_PATHNAME = 'python2.6'

try:
    from movies.settings.local import *
except:
    print '***movies/settings/local.py not found***'