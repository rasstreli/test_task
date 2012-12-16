__author__ = 'pavelmeshkoy'
from django.conf.urls.defaults import patterns, include, url
from loyalty.views import index
urlpatterns = patterns('',
    url(r'^$',index),
    )
