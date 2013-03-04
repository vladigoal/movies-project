import sys
import urllib

from django.utils.encoding import smart_str

from .utils import proj, root


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': root('db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
}


#SESSION_ENGINE='django.contrib.sessions.backends.cache'

if 'test' in sys.argv:
    DATABASES['default']['NAME'] = ':memory:'
    IS_TESTING = True


SITE_ID = 1

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
USE_TZ = True

USE_I18N = True
USE_L10N = True

SECRET_KEY = 'df76e5)(K)fjvmIAQ)vMOe4iwasdfsfrwegrwg3g3wvg3wefgv'

ROOT_URLCONF = 'movies.urls'

WSGI_APPLICATION = 'movies.wsgi.application'

COMPRESS_ENABLED = True
COMPRESS_YUI_BINARY = 'java -jar %s' % root('dev_bins/yuicompressor-2.4.6.jar')
LESS_BIN = ''
COMPRESS_CSS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.yui.YUICSSFilter',
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
    'compressor.filters.yui.YUIJSFilter',
]

COMPRESS_OFFLINE = False


MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

#EMAIL_BACKEND = "mailer.backend.DbBackend"

ACCOUNT_OPEN_SIGNUP = False
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False

AUTHENTICATION_BACKENDS = [
    "pinax.apps.account.auth_backends.AuthenticationBackend",
]

LOGIN_URL = "/auth/login/"
SIGNUP_REDIRECT_URLNAME = "home"
LOGIN_REDIRECT_URLNAME = "home"
LOGOUT_REDIRECT_URLNAME = "home"

EMAIL_CONFIRMATION_DAYS = 2


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",

    "pinax.core.context_processors.pinax_settings",
    "pinax.apps.account.context_processors.account",
    'movies.apps.core.context_processors.site_url',
    'movies.apps.core.context_processors.menu_status',
)

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda o: "/accounts/%s/" % urllib.quote(smart_str(o.username)),
}

ENV_PATH = root('.env')

PYTHON_PATHNAME = 'python2.7'

AJAX_SELECT_BOOTSTRAP = False
AJAX_SELECT_INLINES = False

AJAX_LOOKUP_CHANNELS = {
}

# The maximum number of rows which can be added by user
# who answers a Work Questionnaire's question of type 4

AUTH_PROFILE_MODULE = "core.Profile"


LOCALE_PATHS = (root('locale'), )

COMPLETION_DELAY = 300

ADMINS = ()

MANAGERS = ADMINS

FORCE_NONCOMPRESS = False
