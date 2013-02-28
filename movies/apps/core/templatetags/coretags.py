# -*- coding: utf-8 -*-
from django import template


register = template.Library()


@register.filter
def get_item(obj, item_selector):
    if hasattr(obj, unicode(item_selector)):
        return getattr(obj, item_selector)
    else:
        try:
            return obj[item_selector]
        except:
            return ''

@register.filter
def dotify(value):
    if isinstance(value, basestring):
        return value.replace(',', '.')
    elif isinstance(value, float):
        return ('%f' % value).replace(',', '.')
    else:
        return value