from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^logout/$', 'core.views.logout_aux', name='logout_aux'),
    url(r'^overview/$', 'core.views.overview', name='overview'),
    url(r'^dashboard/$', 'core.views.dashboard', name='dashboard'),

    url(r'^admin/', include(admin.site.urls)),
)
