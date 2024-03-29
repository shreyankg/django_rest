from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'^$', index, name="index"),
    url(r'^(?P<soap_id>\d+)/$', show, name="show"),
    url(r'^(?P<soap_id>\d+)/$', show, name="create"),
    url(r'^(?P<soap_id>\d+)/$', show, name="delete"),
    url(r'^new/$', new, name="new"),
    url(r'^(?P<soap_id>\d+)/edit/$', edit, name="edit"),
)

