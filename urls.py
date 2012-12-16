from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_task.views.home', name='home'),
    # url(r'^test_task/', include('test_task.foo.urls')),
    url(r'^accounts/', include("registration.backends.default.urls")),
    url(r'^loyalty/',include("loyalty.urls")),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
