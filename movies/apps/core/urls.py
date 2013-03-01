from django.conf.urls import patterns, url


urlpatterns = patterns('movies.apps.core.views',
    url(r'^(?P<app_label>\w+)/(?P<model_name>\w+)s/?$', "dummy_list", name="dummy_list"),
    url(r'^(?P<app_label>\w+)/(?P<model_name>\w+)/(?P<slug>[-\w\d]+)/?$', "dummy_details", name="dummy_details"),
)
