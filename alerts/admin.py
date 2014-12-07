# enable django's automatic admin

from django.contrib import admin
from alerts.models import News, Subscriber

admin.site.register(News)
admin.site.register(Subscriber)
