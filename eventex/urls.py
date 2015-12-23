from django.conf.urls import include, url
from django.contrib import admin

from eventex.core.views import home
from eventex.subscriptions.views import subscribe

urlpatterns = [
    url(r'^$', home),
    url(r'^inscricao/$', subscribe),
    url(r'^admin/', include(admin.site.urls)),
]
