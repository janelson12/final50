from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'alerts.views.signup', name='signup'),
    url(r'^success$', TemplateView.as_view(template_name='alerts/success.html'), name='success'),
    url(r'^receive$', 'alerts.views.receive_sms', name='receive_sms'),
    url(r'^admin/', include(admin.site.urls)),
)
