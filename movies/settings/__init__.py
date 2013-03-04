import logging
import os
from distutils.util import strtobool

from default import *
from static import *
from media import *
from middleware import *
from template import *
from apps import *
from debug_toolbar_settings import *
from log_settings import *
from tests import *

IS_TESTING = strtobool(os.environ.get("TESTING", "no"))
IS_DEV = strtobool(os.environ.get("IS_DEV", "no"))
IS_FAST_TESTING= strtobool(os.environ.get("FAST_TESTING", "no"))

if IS_FAST_TESTING:
    COMPRESS_ENABLED = False
    COMPRESS_CSS_FILTERS = []

    COMPRESS_JS_FILTERS = []

try:
    from local import *
except:
    print '***movies/settings/local.py not found***'

COMPRESS_TEMPLATE_FILTER_CONTEX = {
    'STATIC_URL': STATIC_URL,
    'MEDIA_URL': MEDIA_URL,
}

if DEBUG:
    COMPRESS_DEBUG_TOGGLE = 'debug'


if not IS_FAST_TESTING:
    LESS_INCLUDES = '%s/lib/%s/site-packages/pinax_theme_bootstrap/static/bootstrap/less/' % (ENV_PATH, PYTHON_PATHNAME)
    if not LESS_BIN:
        LESS_BIN = root('dev_bins/less/bin/lessc')

    COMPRESS_PRECOMPILERS = (
        ('text/less', '%s --include-path=%s {infile} {outfile}' % (LESS_BIN, LESS_INCLUDES)),
    )

if INSTALLED_APPS_MORE:
    INSTALLED_APPS += INSTALLED_APPS_MORE

if 'south' in INSTALLED_APPS and not IS_TESTING:
    import south_fields
