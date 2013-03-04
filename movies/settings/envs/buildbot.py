from movies.settings import *

from ..utils import proj
#COMPRESS_OFFLINE = True
EMAIL_PORT = 1025
INTERNAL_IPS = tuple()


ENV_PATH = root('.env')


PYTHON_PATHNAME = 'python2.7'

try:
    from movies.settings.local import *
except:
    print '***movies/settings/local.py not found***'