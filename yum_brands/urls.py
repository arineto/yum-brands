from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^logout/$', 'core.views.logout_aux', name='logout_aux'),
    url(r'^overview/$', 'core.views.overview', name='overview'),
    url(r'^overview/(?P<filter_value>.+)/$', 'core.views.overview', name='overview'),
    url(r'^dashboard/$', 'core.views.dashboard', name='dashboard'),
    url(r'^dashboard/(?P<filter_value>.+)/$', 'core.views.dashboard', name='dashboard'),

    url(r'^forgot_password/$', 'core.views.forgot_password', name='forgot_password'),  
    url(r'^change_password/$', 'core.views.change_password', name='change_password'),  

    url(r'^add_branch/$', 'core.views.add_branch', name='add_branch'),
    url(r'^edit_branch/(?P<branch_id>\d+)/$', 'core.views.edit_branch', name='edit_branch'),
    url(r'^delete_branch/(?P<branch_id>\d+)/$', 'core.views.delete_branch', name='delete_branch'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )