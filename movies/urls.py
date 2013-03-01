from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from ajax_select import urls as ajax_select_urls


admin.autodiscover()


urlpatterns = patterns('',

    url(r'^$', "movies.apps.core.views.home", name="home"),
    url(r'^core/', include('movies.apps.core.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # translation
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog',
        {'packages': ('movies', ), }),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
