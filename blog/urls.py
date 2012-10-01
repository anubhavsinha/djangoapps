from django.conf.urls.defaults import patterns, include, url
from views import archive

urlpatterns = patterns('',
                       url(r'^$',archive),
                       )