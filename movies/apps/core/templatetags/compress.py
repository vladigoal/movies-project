# -*- coding: utf-8 -*-

from django import template
from django.core import management
from django.conf import settings

from compressor.templatetags.compress import compress as original_compress

register = template.Library()


@register.tag
def compress(parser, token):
    """Collect static before compressing. Only works with run_collecting server

    Default runserver triggers autoreload on this tag

    """
    if settings.IS_DEV:
        management.call_command('collectstatic', interactive=False, verbosity=0)
    return original_compress(parser, token)