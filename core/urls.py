from django.conf.urls import url

from .api import api_departamentos
from .api import api_provincias

from .views import HomeTV

urlpatterns = [
    url(r'^api/departamentos/$', api_departamentos, name='api_departamentos'),
    url(r'^api/provincias/(?P<pk>\d+)/$', api_provincias, name='api_provincias'),

    url(r'^$', HomeTV.as_view(), name='home'),
]
