from movies.settings import *

from ..utils import proj
#COMPRESS_OFFLINE = True
EMAIL_PORT = 1025
INTERNAL_IPS = tuple()

INSTALLED_APPS_MORE = ['django_extensions',]


if 'test' in sys.argv:
    DATABASES['default']['NAME'] = ':memory:'


if FORCE_NONCOMPRESS:
    COMPRESS_CSS_FILTERS = [
        'compressor.filters.template.TemplateFilter',
        'compressor.filters.css_default.CssAbsoluteFilter',
    ]

    COMPRESS_JS_FILTERS = [
        'compressor.filters.template.TemplateFilter',
    ]

if 1:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins', 'console'],
                'level': 'ERROR',
                'propagate': True,
                },
            'movies.apps': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
                },
            'django.db.backends':{
                'handlers': [],
                'level': 'DEBUG',
                'propagate': False,
            }
            }
    }


ADMINS = (
 ('me', 'mail@gmail.com'),
)

FACEBOOK_APP_ID = '236092469854622'
FACEBOOK_APP_SECRET = 'd28c32ed5fa91c94565738bbaa945b0f'
FACEBOOK_TEST_ACCESS_TOKEN = '236092469854622|eLrEbEzJc2CksC6Q150IF_wkWzY'

MANAGERS = ADMINS

IS_DEV = True

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    )

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

INTERNAL_IPS = ('127.0.0.1', '93.72.123.211')


try:
    from movies.settings.local import *
except:
    print '***movies/settings/local.py not found***'
