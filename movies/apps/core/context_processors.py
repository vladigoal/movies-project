# -*- coding: utf-8 -*-
from collections import OrderedDict
from django.contrib.sites.models import Site
from django.core.urlresolvers import resolve
from django.utils.translation import ugettext_lazy as _


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


def menu_status(request):
    menu_dict = OrderedDict([
        ('dashboard',
         {'url_names': ['home'], 'title': _(' My dashboard'), 'classes': ['mainmenu-item'],}
        ),
        ('movies',
         {'url_names': [], 'title': _('Movies'), 'classes': ['mainmenu-item'],}
        ),
        ('tv',
         {'url_names': [], 'title': _('TV'), 'classes': ['mainmenu-item'],}
        ),
        ('trailers',
         {'url_names': [], 'title': _('Trailers'), 'classes': ['mainmenu-item'],}
        ),
        ('photos',
         {'url_names': [], 'title': _('Photos'), 'classes': ['mainmenu-item'],}
        ),
    ])
    dashboard_submenu = OrderedDict([
        ('my-dashboard', {'url_names': ['home'], 'title': _('Dashboard'), 'classes': ['submenu-item'], 'updates': 35}),
        ('my-films', {'url_names': [], 'title': _('My films'), 'classes': ['submenu-item'], 'updates': 248}),
        ('my-likes', {'url_names': [], 'title': _('My likes'), 'classes': ['submenu-item'], 'updates': 18}),
        ('my-follows', {'url_names': [], 'title': _('My followings'), 'classes': ['submenu-item'], 'updates': 0}),
    ])
    movies_submenu = OrderedDict([
        ('top', {'url_names': [], 'title': _('Top TV shows'), 'classes': ['submenu-item']}),
        ('updates', {'url_names': [], 'title': _('Last updates'), 'classes': ['submenu-item']}),
        ('articles', {'url_names': [], 'title': _('Articles'), 'classes': ['submenu-item']}),
        ('news', {'url_names': [], 'title': _('News'), 'classes': ['submenu-item']}),
    ])
    tv_submenu = OrderedDict([
        ('top', {'url_names': [], 'title': _('Top movies'), 'classes': ['submenu-item']}),
        ('updates', {'url_names': [], 'title': _('Last updates'), 'classes': ['submenu-item']}),
        ('articles', {'url_names': [], 'title': _('Articles'), 'classes': ['submenu-item']}),
        ('news', {'url_names': [], 'title': _('News'), 'classes': ['submenu-item']}),
    ])
    menu_dict['dashboard']['submenu'] = dashboard_submenu
    menu_dict['movies']['submenu'] = movies_submenu
    menu_dict['tv']['submenu'] = tv_submenu
    try:
        resolved = resolve(request.path)
        url_name = resolved.url_name
    except Exception:
        url_name = None

    def mark_active(menu_description):
        for key in menu_description:
            item_description = menu_description['key']
            if url_name in item_description['url_names']:
                item_description['classes'].append('active')
            if 'submenu' in item_description:
                mark_active(item_description['submenu'])
    return {'menu_description': menu_dict}
