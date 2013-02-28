# -*- coding: utf-8 -*-
from movies.settings import *

from ..utils import proj

if FORCE_NONCOMPRESS:
    COMPRESS_CSS_FILTERS = [
        'compressor.filters.template.TemplateFilter',
        'compressor.filters.css_default.CssAbsoluteFilter',
    ]

    COMPRESS_JS_FILTERS = [
        'compressor.filters.template.TemplateFilter',
    ]

ADMINS = (
# ('me', 'mail@gmail.com'),
)

#FACEBOOK_APP_ID = '236092469854622'
#FACEBOOK_APP_SECRET = 'd28c32ed5fa91c94565738bbaa945b0f'

MANAGERS = ADMINS


try:
    from movies.settings.local import *
except:
    print '***movies/settings/local.py not found***'