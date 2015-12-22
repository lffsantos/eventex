from django.conf.urls import include, url
from django.contrib import admin

from eventex.core.views import home

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', include(admin.site.urls)),
]
