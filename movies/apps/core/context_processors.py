# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.core.urlresolvers import resolve


def site_url(request):
    current_site = Site.objects.get_current()
    domain = current_site.domain
    if request.is_secure():
        protocol = 'https'
    else:
        protocol = 'http'
    if domain.find(':') < 0:
        port = request.META['SERVER_PORT']
    else:
        port = None
    site_url = '%s://%s' % (protocol, domain)
    non_standart_port = not (
     (port == '80' and protocol == 'http') or
     (port == '443' and protocol == 'https')
    )
    if non_standart_port and port:
        site_url = '%s:%s' % (site_url, port)
    return {'SITE_URL': site_url}


def active_menuitems(request):
    try:
        resolved = resolve(request.path)
    except Exception:
        return {'home_active': 'active'}
    url_name = resolved.url_name
    if url_name == 'home':
        return {'home_active': 'active'}
    if url_name == 'advicemap':
        return {'advicemap_active': 'active'}
    if url_name == 'activity':
        return {'activity_active': 'active'}
    if url_name == 'my_places':
        return {'myplaces_active': 'active'}
    return {}
