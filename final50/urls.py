from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'alerts.views.signup', name='signup'),
    url(r'^receive$', 'alerts.views.receive_sms', name='receive_sms'),
    url(r'^admin/', include(admin.site.urls)),
)
